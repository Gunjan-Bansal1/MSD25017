# Climate Risk, Value, and Investing — Capstone Repository

**Student Roll Number:** `msd25017`  
**GitHub Organization Repository:** [ClimateRiskLucknow001/msd25017](https://github.com/ClimateRiskLucknow001/msd25017)  
**Course Code:** V003 · **Academic Year:** 2026  
**As-of Date:** November 2026  

---

## 1. Overview & Assigned Universe

This repository houses the complete, independent submissions for **both course capstones** in *Climate Risk, Value, and Investing*:

- **Practice Capstone (`practice/`):** Guided end-to-end full-course pass (10% of course grade, 20 marks).
- **Exam Capstone (`exam/`):** Full-depth, independent integrated capstone (40% of course grade, 100 marks).

Each capstone carries the student's assigned investment universe through **all six course blocks** (Foundations, Carbon Data, ESG, Physical Risk Transfer, Instruments & Policy, and Integration) to a single defensible capital-allocation decision.

### Assigned Universe Parameters (Roll No: `msd25017`):
- **Region Focus:** Latin America (Mexico, Brazil, Chile, Colombia, Peru)
- **Sector Pair:** Industrials & Real Estate
- **Focal Physical Asset:** Baixada Santista Intermodal Logistics & Cold Storage Megahub ($120M Asset Value, Santos / Cubatão Basin, Brazil)
- **Focal Physical Hazard:** Acute Pluvial & Riverine Flood Peril (10-year baseline recurrence, convective storms)
- **Focal Labelled Bond:** USD 500M 5.250% Senior Green Notes due 2031 (Use-of-Proceeds Green Bond, ICMA GBP Aligned)

---

## 2. Directory Structure & Quick Links

```
msd25017/
├── README.md                      # This 2-minute overview & global AI-use statement
├── .gitignore                     # Git ignore rules for Python, Jupyter & temp caches
├── run_all.py                     # Master execution & validation runner script
│
├── practice/                      # GUIDED PRACTICE CAPSTONE (10% GRADE, 20 MARKS)
│   ├── README.md                  # Practice overview, results & instructions
│   ├── coverage_map.md            # Six-block evidence mapping table
│   ├── requirements.txt           # Python package dependencies
│   ├── environment.yml            # Conda environment file
│   ├── decision_memo.pdf          # 3-Page Executive Investment Decision Memorandum
│   ├── notebooks/
│   │   └── practice_capstone_starter.ipynb # Fully executed starter notebook (msd25017)
│   ├── data/
│   │   ├── download_manifest.json # Data provenance, URLs, checksums
│   │   ├── data_dictionary.csv    # Field definitions and derivation formulas
│   │   └── sample/                # Committed reproducible CSV datasets
│   ├── outputs/
│   │   ├── figures/               # Saved high-resolution PNG figures (Fig 1 - 2)
│   │   └── tables/                # Saved CSV result tables (Table 1 - 4)
│   └── tests/
│       └── test_practice_pipeline.py # Pytest test suite asserting all 6 block outputs
│
└── exam/                          # INDEPENDENT EXAM CAPSTONE (40% GRADE, 100 MARKS)
    ├── README.md                  # Comprehensive exam overview, hours log (~42h)
    ├── scope_card.pdf             # Approved 1-Page Pre-Modelling Scope Card
    ├── coverage_map.md            # Required mapping of 6 blocks -> code/tables/figures
    ├── model_card.md              # Technical Model Card (Intended use, assumptions, limits)
    ├── decision_memo.pdf          # 2,500–3,500 Word Institutional Decision Memo (6 Pages)
    ├── presentation.pptx          # 12-Slide High-Impact Presentation Deck
    ├── oral_defense_brief.md      # 5–8 Min Defense Guide with Q&A and Code Walkthrough
    ├── requirements.txt           # Python dependencies
    ├── environment.yml            # Conda environment definition
    ├── data/
    │   ├── download_manifest.json # Complete data provenance & SHA-256 checksums
    │   ├── data_dictionary.csv    # Full variable dictionary
    │   ├── sample/                # Raw reproducible datasets (10 holdings, climate, flood)
    │   └── processed/             # Clean integrated climate-financial panel
    ├── src/                       # Production Python Analytics Engine
    │   ├── data_loader.py         # Panel builder and data ingestion
    │   ├── carbon_analytics.py    # PCAF WACI and financed emissions proxy
    │   ├── valuation_engine.py    # 10-year transition DCF under NGFS pathways
    │   ├── risk_transfer_sim.py   # 20,000-draw Monte Carlo flood loss & basis risk sim
    │   ├── green_bond_model.py    # Greenium pricing & step-up penalty coupon model
    │   └── portfolio_optimizer.py # Multi-criteria CAVRS optimization engine
    ├── notebooks/                 # Runnable end-to-end Jupyter Notebooks (Stages 01–07)
    │   ├── 01_frame_foundations.ipynb
    │   ├── 02_data_carbon_analytics.ipynb
    │   ├── 03_valuation_transition.ipynb
    │   ├── 04_esg_stewardship.ipynb
    │   ├── 05_physical_risk_transfer.ipynb
    │   ├── 06_instruments_policy.ipynb
    │   └── 07_integration_decision.ipynb
    ├── outputs/
    │   ├── figures/               # 10 Publication-Quality Charts (fig01 to fig10)
    │   ├── tables/                # 9 Structured Result CSV Tables (table01 to table09)
    │   └── dashboard/
    │       └── index.html         # Interactive Responsive Executive Dashboard
    └── tests/                     # Comprehensive Pytest Suite (11 Unit Tests)
```

---

## 3. Headline Findings & Actionable Mandate

1. **Portfolio Carbon & Decarbonization:** Rebalancing reduces portfolio Weighted Average Carbon Intensity (WACI) by **21.6%** (from 191.5 to **150.1 tCO2 / MUSD revenue**), exceeding the fund's 20% decarbonization requirement.
2. **Transition Valuation Impact:** Prime logistics real estate (FIBRA Prologis and Vesta) is virtually immune to carbon taxation under an NGFS Orderly \$120/tCO2 transition (**<0.01% enterprise value impact**) due to triple-net (NNN) contract structures and low Scope 1 intensity, while diesel rail freight (Rumo S.A.) faces an equity contraction of up to **31.2%** under unhedged compliance costs.
3. **Physical Flood Risk Transfer:** 20,000 Monte Carlo draws on the \$120M Santos megahub show an unmitigated Expected Annual Loss of **\$3.28M** and a P95 tail loss of **\$33.15M**. A layered resilience strategy (structural adaptation + parametric excess-of-loss insurance) collapses P95 tail loss by **87.9% to \$4.00M**, delivering a positive 20-year NPV of **+\$18.4M** with minimized basis risk.
4. **Use-of-Proceeds Green Bond:** The USD 500M 5.250% Senior Green Notes due 2031 command an **8.5 bps greenium discount**, providing \$0.500 NPV savings per \$100 face value. Covenants include a +25 bps penalty step-up coupon for reporting breaches. Aligns with Mexican and Colombian Green Taxonomies and directly mirrors **SEBI's Regulatory Framework for ESG Debt Securities in India (SEBI Operational Circular 2023)** and the Indian Sovereign Green Bond Framework (2022).
5. **Actionable Mandate:** Overweight top climate-resilient leaders (WEG +8.1%, Vesta +3.7%, FIBRA Prologis +3.0%), allocate 15% debt sleeve (\$37.5M) to the Green Bond, and underweight transition-laggard transport operators (Rumo -6.1%, Embraer -6.1%, CCR -3.2%) with an active 12-month stewardship engagement plan.

---

## 4. Master Reproduction Instructions (< 30 Seconds)

To verify and reproduce all outputs, run the master script from the repository root:

```bash
# 1. Install dependencies
pip install -r exam/requirements.txt

# 2. Run master test suite & pipeline verification
python run_all.py
```

*Expected output: All 20 unit tests across Practice and Exam pass with 100% compliance in ~3 seconds.*

---

## 5. Global AI-Use Statement & Academic Integrity

- **Tools & Purpose:** Google DeepMind Agent was employed as an interactive pair-programmer and workflow accelerator for code scaffolding, vector algebra verification, PyMuPDF PDF formatting, and cross-border regulatory comparisons.
- **Verification:** Every formula (DCF discounting, PCAF WACI weighted summation, Monte Carlo exceedance curves, bond pricing cashflows) was independently checked and validated from first principles. Unit tests with strict assertions guarantee that no simulated numbers were presented as audited disclosures.
- **Claim Boundary:** Prepared strictly for academic evaluation in *Climate Risk, Value, and Investing (Academic Year 2026)*. Does not constitute official investment advice, credit rating certification, or commercial fund promotion.

