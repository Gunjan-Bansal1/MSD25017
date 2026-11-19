# Exam Capstone Coverage Map — Roll Number: msd25017

**Course:** Climate Risk, Value, and Investing  
**Student Roll Number:** `msd25017`  
**Assigned Universe:** Latin America · Industrials & Real estate · Focal Asset: Baixada Santista Logistics Megahub (Flood) · Focal Bond: Use-of-Proceeds Green Bond  
**As-of Date:** November 2026  

This coverage map explicitly documents where each of the six course blocks is evidenced in the independent exam capstone submission. Every block is evidenced across reproducible code, saved figures, structured tables, and the decision memo.

| Block | Covered? | Where (notebook section / figure / table) | One-line what you did |
|---|---|---|---|
| **A Foundations & transmission** | Yes | `01_frame_foundations.ipynb` §Framing; `fig01_universe_exposure_quadrant.png`; `table01_universe_provenance.csv`; Memo §2 | Classified 10 Latin American Industrials & Real Estate holdings into physical vs transition channels; mapped transmission to revenues, opex, and asset value. |
| **B Climate data & portfolio carbon** | Yes | `02_data_carbon_analytics.ipynb`; `fig02_carbon_intensity_waci.png`; `table02_data_quality_missingness.csv`; `table03_carbon_portfolio_metrics.csv` | Assembled documented climate + emissions panel (100% Scope 1/2 coverage, 70% Scope 3); computed benchmark WACI (191.5 tCO2/MUSD) and financed emissions. |
| **A–B Valuation under transition** | Yes | `03_valuation_transition.ipynb`; `fig03_transition_dcf_tornado.png`; `table04_dcf_scenario_valuation.csv`; Memo §3 | Built 10-year transition DCF model under 4 NGFS carbon price pathways ($5 to $160/tCO2); evaluated pass-through elasticity and generated tornado sensitivity rankings. |
| **C ESG, stewardship, ratings** | Yes | `04_esg_stewardship.ipynb`; `fig04_esg_divergence_radar.png`; `table05_esg_claim_verification_matrix.csv`; Memo §4 | Reconciled disclosure quality (Score A) vs controversy-adjusted reality (Score B); audited green claims (SPO audit); designed 12-month shareholder engagement plan for Rumo S.A. |
| **D Risk management & transfer** | Yes | `05_physical_risk_transfer.ipynb`; `fig05_flood_loss_exceedance_ep_curve.png`; `fig06_risk_transfer_strategy_waterfall.png`; `table06_physical_risk_transfer_options.csv` | Simulated 20,000 Monte Carlo flood loss iterations on $120M Santos megahub; evaluated No Action vs Adaptation vs Parametric Insurance vs Combined, quantifying EAL, P95 tail ($33.2M → $4.0M), 20-yr NPV, and basis risk. |
| **E Instruments, markets & policy** | Yes | `06_instruments_policy.ipynb`; `fig07_use_of_proceeds_greenium_cashflow.png`; `table07_green_bond_impact_metrics.csv`; Memo §6 | Modelled USD 500M 5.250% 7-year Use-of-Proceeds Green Bond; quantified 8.5 bps greenium ($0.50/face NPV benefit) and +25 bps penalty step-up coupon; benchmarked Mexican/Colombian taxonomies against SEBI & Indian Sovereign Green Bond framework. |
| **F Integration & decision** | Yes | `07_integration_decision.ipynb`; `fig08_climate_efficient_frontier_rebalancing.png`; `fig09_multi_criteria_decision_heatmap.png`; `fig10_sensitivity_threshold_switch.png`; `table08_integration_capital_allocation.csv`; `decision_memo.pdf` | Synthesized multi-criteria signals into Composite Climate-Adjusted Value & Resilience Score (CAVRS); rebalanced portfolio reducing WACI by 21.6% (150.1 tCO2/MUSD); defined actionable investment mandate with explicit falsification conditions. |

### Summary Verification
- **All six blocks evidenced:** Yes (asserted in `exam/tests/` and runnable notebooks).
- **All ten deliverables present:** Yes (Scope card, Coverage map, Code, Provenance, Validation, Model card, Decision memo, Dashboard, Presentation, Oral defense brief).
- **Execution runtime:** Top-to-bottom pipeline executes in < 15 seconds on committed sample datasets with fixed seeds.
