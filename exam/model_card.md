# Model Card: Climate-Integrated Valuation & Portfolio Allocation Model (CIVPAM-LatAm)

**Model Version:** 1.0.0 (V003 Academic Standard)  
**Candidate Roll Number:** `msd25017`  
**As-of Date:** November 2026  
**License:** MIT Open Source (Educational Assessment)  

---

## 1. Intended Use & Stakeholder

- **Intended Use:** Evaluates corporate transition risks and physical flood vulnerabilities across listed Latin American Industrials and Real Estate entities to inform active capital allocation, green bond participation, and shareholder stewardship.
- **Decision Stakeholder:** Investment Committee and Mandate Portfolio Managers of the *Latin America Sustainable Opportunities Equity & Debt Fund* ($250M AUM).
- **Prohibited Uses:** Strictly prohibited for commercial investment advice, client wealth management promotions, regulatory capital solvency filings, or claiming verified carbon offset generation under the Kyoto/Paris Article 6 mechanisms.

---

## 2. Model Architecture & Method Summary

CIVPAM-LatAm operates as a multi-stage quantitative pipeline integrating six core modules:
1. **Financial Transmission Classifier (Block A):** Classifies holdings into primary physical vs transition exposure channels based on revenue-to-hazard proximity and fossil-fuel reliance.
2. **Portfolio Carbon Engine (Block B):** Implements PCAF-aligned Weighted Average Carbon Intensity (WACI) and financed-emissions proxy calculations based on Scope 1 and Scope 2 disclosures.
3. **Transition DCF Valuation Engine (Block A–B):** A 10-year discounted cash flow model pricing gross and net carbon tax liabilities under NGFS Orderly Net Zero 2050 ($120/tCO2), Delayed Transition ($75/tCO2), and Current Policies ($5/tCO2) pathways, incorporating tenant pass-through elasticity.
4. **ESG & Greenwashing Audit Studio (Block C):** Reconciles quantitative disclosure completeness against controversy-adjusted governance scores, flagging greenwashing risks via Second-Party Opinion (SPO) verification audits.
5. **Physical Risk Monte Carlo Simulator (Block D):** Generates 20,000 stochastic annual flood loss draws on focal logistics infrastructure, modeling structural attenuation (-45% damage), parametric insurance attachment/limits, exceedance probability (EP) curves, and residual basis risk.
6. **Green Bond Valuation & Policy Engine (Block E):** Schedules Use-of-Proceeds debt cash flows, models secondary market greenium discounts (8.5 bps), computes penalty step-up coupon triggers (+25 bps), and audits alignment with ICMA GBP, Mexico Sustainable Taxonomy, Colombia Green Taxonomy, and SEBI ESG Debt circulars.
7. **Composite Allocation Engine (Block F):** Computes the Composite Climate-Adjusted Value & Resilience Score (CAVRS) to optimize portfolio weights under strict diversification constraints (4% min, 20% max).

$$\text{CAVRS}_i = 0.35 \times \text{ESG}_i + 0.25 \times \text{ValuationTransition}_i - 0.20 \times \text{CarbonPenalty}_i - 0.20 \times \text{PhysicalFloodPeril}_i$$

---

## 3. Inputs & Data Provenance

| Dimension | Primary Sources | Verification Level | Input Nature |
|---|---|---|---|
| **Corporate Financials** | BMV, B3, Bolsa de Santiago Audited Regulatory Filings (FY2023/FY2024) | Audited Public Disclosures | Observed |
| **GHG Emissions** | Corporate GRI/ISSB Sustainability Disclosures; Our World in Data CO2 Database | Third-Party Limited Assurance (EY/KPMG) / Baseline Imputation | Observed / Imputed |
| **Climate Hazards** | Copernicus Climate Data Store (ERA5 Reanalysis Rx5day); World Bank CCKP | Peer-Reviewed Reanalysis | Modeled / Reanalysis |
| **Transition Pathways**| NGFS Scenarios Portal (Phase IV GCAM / MESSAGEix-GLOBIOM) | Central Bank Consortium Standard | Scenario Assumptions |
| **Labelled Bond Specs** | Offering Circulars; ICMA Database; Sustainalytics Second-Party Opinions | Legal Offering Documents | Observed |

---

## 4. Key Assumptions & Parameterization

- **Discount Rates & Growth:** Baseline Weighted Average Cost of Capital (WACC) = 9.0%; perpetual terminal growth rate (g) = 2.0%; corporate income tax rate = 25.0%.
- **Carbon Cost Pass-Through:** Base case assumes 50.0% pass-through of carbon price increases to tenants and industrial freight customers under prevailing Latin American commercial contracts.
- **Physical Flood Risk:** Baseline 10-year return period flood event probability $p = 0.10$; lognormal damage severity distribution ($\mu = 0.28, \sigma = 0.14$); replacement asset value = \$120.0M.
- **Structural Engineering:** Flood barriers, elevated docks (+2.0m), and detention basins achieve a constant 45.0% damage attenuation factor with upfront CapEx of \$14.5M.
- **Greenium Spread:** 8.5 basis points persistent pricing concession for certified Use-of-Proceeds Green Bonds relative to equivalent conventional senior debt curves.

---

## 5. Validation Performed & Stress Testing

- **Unit Assertions & Automated Testing:** 11 comprehensive unit tests implemented via `pytest` passing in < 2 seconds, verifying mathematical non-negativity, boundary conditions, and portfolio weight budget equality.
- **Closed-Form Equivalence:** DCF cash flows were reconciled against analytical Gordon Growth formulations with zero tracking error.
- **Parameter Sensitivity:** Valuation sensitivity tested across carbon prices (\$0 to \$200/tCO2), WACC (+/-150 bps), pass-through rates (0% to 100%), and flood frequencies ($p=0.05$ to $p=0.20$).
- **Dominant Uncertainty Identified:** Geospatial flood frequency parameterization ($p=0.10$) dominates transition scenario divergence. In the absence of hyper-local hydro-meteorological gauge observations, physical flood tail loss models carry wider epistemic confidence intervals than corporate carbon tax scenarios.

---

## 6. Prohibited Uses & Mandatory Governance Statements

> **MANDATORY DISCLAIMER:**  
> This analytical model was developed solely for academic credit in *Climate Risk, Value, and Investing (Academic Year 2026)*. All ESG scores, vulnerability indices, and composite allocation weights are transparently constructed academic proxies and do not reflect proprietary ratings from MSCI, S&P, or Sustainalytics. The model output does not constitute an offer, solicitation, or recommendation to purchase or sell any security.

