#!/usr/bin/env bash
# ============================================================================
# DIGITAL FINANCE FRONTIER — Project Generator
# Run: bash setup.sh
# Creates: ./digital-finance-frontier/
# ============================================================================

set -e

ROOT="digital-finance-frontier"

echo "============================================"
echo "  DIGITAL FINANCE FRONTIER — Project Setup"
echo "============================================"
echo ""

# ─── CREATE DIRECTORY STRUCTURE ─────────────────────────────────────────────
echo "[1/5] Creating directory structure..."

mkdir -p "$ROOT"/{
  00-executive-summary,
  01-architecture,
  02-global-institutions,
  03-platforms/{payments-networks,exchanges,asset-managers,banks,infrastructure},
  04-tokenization,
  05-defi-web3,
  06-ai-finance/research,
  07-quantum-finance,
  08-cybersecurity-intelligence/tools,
  09-geopolitics,
  10-disruptive-technologies,
  11-research-labs/{universities,industry,think-tanks},
  12-timeline-projections,
  13-forensics-intelligence,
  14-strategic-analysis,
  15-appendices,
  data/{market-data,on-chain-analytics,research-datasets},
  code/{forensics,visualization,ml-models,quantum-sim,osint},
  assets/{diagrams,charts,infographics},
  .github/{workflows,ISSUE_TEMPLATE}
}

# ─── CREATE .gitkeep FILES ──────────────────────────────────────────────────
echo "[2/5] Creating .gitkeep files..."

for dir in data/market-data data/on-chain-analytics data/research-datasets \
           assets/diagrams assets/charts assets/infographics; do
  touch "$ROOT/$dir/.gitkeep"
done

# ─── INITIALIZE GIT ─────────────────────────────────────────────────────────
echo "[3/5] Initializing git repository..."

cd "$ROOT"
git init 2>/dev/null || true
git add -A 2>/dev/null || true
git commit -m "v1.0: Digital Finance Frontier — project structure" 2>/dev/null || true

# ─── CREATE VENV (OPTIONAL) ─────────────────────────────────────────────────
echo "[4/5] Python environment (optional)..."

if command -v python3 &> /dev/null; then
  echo "  Python 3 found: $(python3 --version)"
  echo "  To install dependencies:"
  echo "    cd code && pip install -r requirements.txt"
else
  echo "  Python 3 not found. Install for code tools."
fi

# ─── DONE ───────────────────────────────────────────────────────────────────
echo "[5/5] Done!"
echo ""
echo "============================================"
echo "  Project created: ./$ROOT/"
echo ""
echo "  Next steps:"
echo "    1. cd $ROOT"
echo "    2. code .          (open in VS Code)"
echo "    3. Add file content (see conversation)"
echo "    4. git add . && git commit -m 'v1.0'"
echo "    5. git remote add origin https://github.com/YOUR_USER/$ROOT.git"
echo "    6. git push -u origin main"
echo ""
echo "  Total files to populate: ~120"
echo "  Total directories: ~45"
echo "============================================"   