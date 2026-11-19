# Practice Capstone: Climate Risk, Value, and Investing (MSD25017)

**Component:** Practice Capstone (10% of course grade, 20 marks)  
**Student Roll Number:** `msd25017`  
**Academic Year:** 2026  
**As-of Date:** November 2026  

---

## 1. Executive Summary & Assigned Universe

This practice capstone executes an integrated, end-to-end climate-finance investment assessment across all six course blocks for the assigned student universe:

- **Roll Number:** `msd25017`
- **Region Focus:** Latin America (Mexico & Brazil)
- **Sector Pair:** Industrials & Real Estate
- **Focal Physical Asset:** Coastal Logistics & Warehouse Megahub (Santos / Baixada Santista logistics corridor, Brazil) exposed to acute **flood hazard** (10-year baseline recurrence, riverine and pluvial inundation)
- **Focal Labelled Bond:** USD 375M 5-year **Use-of-Proceeds Green Bond** (FIBRA Prologis Green Logistics Framework / ICMA GBP aligned)

### Headline Findings
1. **Emissions & Financed Carbon (Block B):** Disclosed reporting coverage is **75%** with a portfolio Weighted Average Carbon Intensity (WACI) of **136.2 tCO2 / MUSD revenue**, heavily concentrated in rail logistics diesel traction.
2. **Transition Valuation Impact (Block A–B):** Under an NGFS Orderly Transition carbon price increase to \$120/tCO2, enterprise value for prime green logistics real estate (`017-01-FIBRAPL`) decreases by **<0.1%** due to low Scope 1/2 intensity and strong tenant cost pass-through capacity, compared to severe enterprise value compression for carbon-intensive transport.
3. **Physical Resilience & Tail-Loss Transfer (Block D):** Unmitigated flood expected annual loss (EAL) of **\$1.372M** and P95 tail loss of **\$13.845M** are reduced by **85.5%** to an EAL of **\$0.199M** and P95 of **\$2.000M** under a combined structural adaptation (elevated docks, detention basins) and parametric excess-of-loss insurance structure. Residual basis risk is quantified at \$0.458M.
4. **Labelled Bond Pricing & Policy (Block E):** The Use-of-Proceeds Green Bond commands an **8.0 bps greenium**, delivering \$0.351 NPV savings per \$100 face value. Covenants comply with ICMA Green Bond Principles, Mexican Sustainable Taxonomy, Colombian Green Taxonomy, and SEBI's regulatory guidelines for ESG Debt Securities in India.
5. **Actionable Decision (Block F):** Overweight `017-01-FIBRAPL` (+8.0% active) and allocate 15% debt sleeve to the Use-of-Proceeds Green Bond; underweight `017-02-RAIL3` (-8.0% active) accompanied by a 12-month formal stewardship mandate on diesel fleet decarbonization and flood track armoring.

---

## 2. Repository Layout & Artifacts

```
practice/
├── README.md                      # This 2-minute overview & AI-use statement
├── requirements.txt               # Python package dependencies
├── environment.yml                # Conda environment definition
├── coverage_map.md                # Mapping the 6 blocks -> notebook sections & exhibits
├── decision_memo.pdf              # 3-page executive investment decision memo
├── notebooks/
│   └── practice_capstone_starter.ipynb   # Fully executed starter notebook with unit checks
├── data/
│   ├── download_manifest.json     # Data provenance, retrieval dates, checksums
│   ├── data_dictionary.csv        # Comprehensive data dictionary
│   └── sample/                    # Committed reproducible datasets
│       ├── practice_universe_holdings.csv
│       ├── focal_flood_loss_simulations.csv
│       └── green_bond_cashflows.csv
├── outputs/
│   ├── figures/
│   │   ├── fig1_carbon_sensitivity.png    # DCF EV vs carbon price ($0-$150/tCO2)
│   │   └── fig2_loss_exceedance.png       # Monte Carlo flood exceedance probability curve
│   └── tables/
│       ├── table1_holdings_frame.csv      # Holdings classification & WACI data
│       ├── table2_claim_verification.csv  # ESG claim verification audit
│       ├── table3_risk_transfer_cases.csv # EAL and P95/P99 tail loss under 4 cases
│       └── table4_capital_allocation.csv  # Composite CAVRS scores and weights
└── tests/
    └── test_practice_pipeline.py  # Pytest test suite asserting all block outputs
```

---

## 3. How to Reproduce

### Setup & Run
1. Activate your Python environment with dependencies installed:
   ```bash
   pip install -r practice/requirements.txt
   ```
2. Run the unit test suite:
   ```bash
   pytest practice/tests/test_practice_pipeline.py
   ```
3. To rerun the full starter notebook:
   - Open `practice/notebooks/practice_capstone_starter.ipynb` in JupyterLab or run via command line.
   - Execute `Kernel -> Restart & Run All`. All assertions and coverage checks pass in under 15 seconds.

---

## 4. Academic Integrity & AI-Use Statement

- **Tools & Purpose:** Claude / Google DeepMind Agent was utilized as an interactive workflow accelerator to generate boilerplate code scaffolding (vectorized Monte Carlo simulation, DCF cash flow schedules), assist in markdown table formatting, and cross-reference regulatory policy texts.
- **Material Prompts:** Prompts focused strictly on technical implementation: calibrating flood exceedance distributions for Latin American logistics real estate, verifying ICMA Green Bond Principle alignment against SEBI operational circulars, and formatting PyMuPDF report scripts.
- **AI-Generated Content:** Initial drafts of code templates and markdown scaffolding.
- **Independent Verification:** The student verified every formula and calculation from first principles (DCF algebra, WACI weighted summation, 20,000-draw Monte Carlo exceedance logic, bond cash-flow discounting). Unit tests with strict assertions guarantee that no simulated numbers were presented as audited disclosures.
- **Errors Identified & Corrected:** Initial boilerplate code utilized non-interactive matplotlib blocking calls during automated testing; corrected to configure headless Agg rendering. Bond pricing formulas were reconciled to account for both coupon step-ups and greenium yield discounts.
- **Claim Boundary:** This project was prepared for academic credit in *Climate Risk, Value, and Investing (Academic Year 2026)*. It is an educational analytical model, not official investment advice, and does not claim certified emissions reduction credits or production asset management deployment.
