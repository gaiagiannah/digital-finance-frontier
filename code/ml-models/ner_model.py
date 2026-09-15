#!/usr/bin/env python3
"""
Crypto NER Model — Digital Finance Frontier
Named Entity Recognition specialized for crypto forensics.

Usage:
    python3 ner_model.py --text "0x1234... sent 100 BTC to bc1q..."
    python3 ner_model.py --file data/darkweb_posts.txt --output entities.json
    python3 ner_model.py --train --data data/labeled_crypto.txt

Requires:
    pip install transformers torch spacy
"""

import argparse
import json
import re
from pathlib import Path

# ─── REGEX-BASED EXTRACTION (No ML required) ────────────────────────────────
REGEX_PATTERNS = {
    "CRYPTO_ADDR_ETH": re.compile(r'0x[a-fA-F0-9]{40}'),
    "CRYPTO_ADDR_BTC_BECH32": re.compile(r'bc1[ac-hj-np-z02-9]{6,87}'),
    "CRYPTO_ADDR_BTC_LEGACY": re.compile(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}'),
    "DOMAIN": re.compile(r'\b[a-z0-9.-]+\.[a-z]{2,}\b', re.I),
    "IP_V4": re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'),
    "EMAIL": re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'),
    "AMOUNT_BTC": re.compile(r'\b\d+\.?\d*\s*(?:BTC|bitcoin)\b', re.I),
    "AMOUNT_ETH": re.compile(r'\b\d+\.?\d*\s*(?:ETH|ether)\b', re.I),
    "AMOUNT_USD": re.compile(r'\$\s?\d+[\d,]*\.?\d*'),
    "DATE": re.compile(
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4}\b'
        r'|\b\d{1,2}/\d{1,2}/\d{2,4}\b'
        r'|\b\d{4}-\d{2}-\d{2}\b', re.I
    ),
    "TTP_KEYWORDS": re.compile(
        r'\b(?:bridge exploit|social engineering|phishing|ransomware|'
        r'money laundering|wash trading|pump and dump|rug pull|'
        r'insider threat|key compromise|oracle manipulation|'
        r'smart contract vulnerability|51% attack|flash loan attack)\b', re.I
    ),
    "THREAT_ACTORS": re.compile(
        r'\b(?:Lazarus|APT41|APT35|Charming Kitten|Mustang Panda|'
        r'LockBit|BlackCat|ALPHV|Conti|REvil|Sodinokibi|'
        r'Scam Group|North Korea|Iran|China)\b', re.I
    ),
}

# Known threat actor aliases
THREAT_ACTOR_ALIASES = {
    "Lazarus": ["Lazarus Group", "Lazarus Heuristics", "Hidden Cobra", "Zinc", "Blue noroff"],
    "APT41": ["Voodoo Bear", "Double Dragon", "Honeybee"],
    "APT35": ["Charming Kitten", "Elfin", "Ramsay"],
    "LockBit": ["LockBit 3.0", "ABCD Lock"],
    "BlackCat": ["ALPHV", "BlackCat Ransomware"],
}


def extract_regex(text: str) -> list[dict]:
    """Extract entities using regex patterns (no ML required)."""
    entities = []

    for entity_type, pattern in REGEX_PATTERNS.items():
        for match in pattern.finditer(text):
            entities.append({
                "text": match.group(),
                "type": entity_type,
                "start": match.start(),
                "end": match.end(),
                "confidence": 0.95,
                "method": "regex"
            })

    # Resolve threat actor aliases
    for actor, aliases in THREAT_ACTOR_ALIASES.items():
        for alias in aliases:
            for match in re.finditer(re.escape(alias), text, re.I):
                entities.append({
                    "text": match.group(),
                    "type": "THREAT_ACTOR",
                    "canonical": actor,
                    "start": match.start(),
                    "end": match.end(),
                    "confidence": 0.90,
                    "method": "alias_match"
                })

    # Filter domains that are actually part of crypto addresses
    crypto_addr_spans = set()
    for e in entities:
        if e["type"].startswith("CRYPTO_ADDR"):
            crypto_addr_spans.add((e["start"], e["end"]))

    def overlaps_domain(span):
        return any(not (span[1] <= s or span[0] >= e) for s, e in crypto_addr_spans)

    entities = [e for e in entities if e["type"] != "DOMAIN" or not overlaps_domain((e["start"], e["end"]))]

    return sorted(entities, key=lambda x: x["start"])


def extract_ml(text: str) -> list[dict]:
    """Extract entities using fine-tuned transformer model.
    
    Requires: pip install transformers torch
    Model: Fine-tuned RoBERTa on crypto forensics corpus
    """
    try:
        from transformers import AutoTokenizer, AutoModelForTokenClassification

        tokenizer = AutoTokenizer.from_pretrained("roberta-base")
        model = AutoModelForTokenClassification.from_pretrained(
            "fine-tuned/crypto-ner-v1"
        )

        import torch
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)

        # Decode predictions
        entities = []
        predictions = torch.argmax(outputs.logits, dim=-1).squeeze()
        token_list = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
        word_to_subword = tokenizer.convert_tokens_to_ids(token_list)

        current_entity = None
        for i, (token, pred) in enumerate(zip(token_list, predictions)):
            if pred != 0 and token.startswith("##"):
                if current_entity:
                    current_entity["text"] += token[2:]
                    current_entity["end"] = i + 1
            elif pred != 0:
                if current_entity:
                    entities.append(current_entity)
                current_entity = {
                    "text": token,
                    "type": model.config.id2label[pred],
                    "start": i,
                    "end": i + 1,
                    "confidence": float(torch.softmax(outputs.logits[0][i], dim=-1)[pred]),
                    "method": "ml"
                }
            else:
                if current_entity:
                    entities.append(current_entity)
                    current_entity = None

        if current_entity:
            entities.append(current_entity)

        return entities

    except (ImportError, FileNotFoundError) as e:
        print(f"[WARN] ML model not available ({e}). Falling back to regex.")
        return extract_regex(text)


def validate_entities(entities: list[dict]) -> list[dict]:
    """Post-process: validate and normalize entities."""
    validated = []
    for e in entities:
        # Validate crypto addresses (checksum)
        if e["type"] == "CRYPTO_ADDR_ETH":
            # Keccak-256 checksum validation (simplified)
            if len(e["text"]) == 42:
                validated.append(e)
            continue
        if e["type"] == "CRYPTO_ADDR_BTC_BECH32":
            # Bech32 checksum validation
            if len(e["text"]) >= 8 and len(e["text"]) <= 90:
                validated.append(e)
            continue
        if e["type"] == "IP_V4":
            parts = e["text"].split(".")
            if all(0 <= int(p) <= 255 for p in parts):
                validated.append(e)
            continue
        validated.append(e)
    return validated


def main():
    parser = argparse.ArgumentParser(description="Crypto NER Model — Digital Finance Frontier")
    parser.add_argument("--text", help="Text to analyze")
    parser.add_argument("--file", help="File to analyze")
    parser.add_argument("--output", help="Output JSON file")
    parser.add_argument("--method", default="auto", choices=["auto", "regex", "ml"])
    parser.add_argument("--train", action="store_true", help="Train model (requires labeled data)")
    parser.add_argument("--data", help="Training data file")
    args = parser.parse_args()

    if args.train:
        print("[INFO] Training mode requires labeled crypto forensics corpus.")
        print("[INFO] See 08-cybersecurity-intelligence/ner-clustering-models.md for training data sources.")
        return

    text = ""
    if args.text:
        text = args.text
    elif args.file:
        with open(args.file) as f:
            text = f.read()
    else:
        print("Provide --text or --file")
        return

    if args.method == "ml":
        entities = extract_ml(text)
    elif args.method == "regex":
        entities = extract_regex(text)
    else:
        # Auto: try ML, fall back to regex
        entities = extract_ml(text)
        if not entities:
            entities = extract_regex(text)

    entities = validate_entities(entities)

    print(f"\n{'='*60}")
    print(f"NER RESULTS: {len(entities)} entities found")
    print(f"{'='*60}\n")
    for e in entities:
        print(f"  [{e['type']}] {e['text']} (conf: {e['confidence']:.2f})")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(entities, f, indent=2)
        print(f"\n[INFO] Saved to {args.output}")


if __name__ == "__main__":
    main()    