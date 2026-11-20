# Oral Defense Preparation Brief: Climate Risk, Value, and Investing

**Candidate Roll Number:** `msd25017`  
**Assigned Universe:** Latin America · Industrials & Real Estate  
**Focal Physical Asset:** Baixada Santista Intermodal Logistics Megahub ($120M Asset, Flood Peril)  
**Focal Labelled Bond:** USD 500M 5.250% Senior Green Notes due 2031 (Use-of-Proceeds Green Bond)  
**Defense Duration:** 5–8 minutes live oral defense  

---

## 1. 2-Minute Elevator Pitch (Opening Statement)

> "Good morning/afternoon, professors and examiners. My name is [Student Name] (Roll No: `msd25017`), and today I present my integrated climate investment assessment for Latin American Industrials and Real Estate.
>
> Our mandate is the \$250M *Latin America Sustainable Opportunities Fund*. We evaluate whether an active manager should overweight this universe and participate in a focal Use-of-Proceeds Green Bond, balancing carbon transition liabilities against acute physical flood perils.
>
> Our headline findings are threefold:
> 1. **Transition Resilience:** Prime logistics real estate (FIBRA Prologis and Vesta) is virtually immune to carbon taxation (enterprise value impact < 0.01% under NGFS Orderly \$120/tCO2) due to triple-net leases and low Scope 1 intensity, whereas carbon-heavy rail freight (Rumo S.A.) faces up to a 31% equity valuation drop under unhedged carbon costs.
> 2. **Physical Risk & Resilience:** On our focal \$120M Santos logistics megahub, 20,000 Monte Carlo draws reveal that an unmitigated flood disaster incurs an Expected Annual Loss of \$3.28M and a P95 tail loss of \$33.15M. By deploying a layered resilience strategy—combining structural adaptation (elevated docks, retention basins) with parametric excess-of-loss insurance—we compress tail loss by 87.9% to \$4.00M and generate a positive 20-year NPV of \$18.4M with minimal basis risk.
> 3. **Actionable Mandate:** We recommend an active rebalancing that reduces portfolio WACI by 21.6% (from 191.5 to 150.1 tCO2/MUSD), overweighting clean transition leaders (WEG +8.1%, Vesta +3.7%, Prologis +3.0%), subscribing \$37.5M to the Green Bond capturing an 8.5 bps greenium, and placing Rumo S.A. under an underweight cap with an explicit 12-month stewardship engagement on diesel decarbonization and flood track armoring."

---

## 2. Anticipated Technical Defense Questions & Exact Answers

### Question 1: "Why does FIBRA Prologis experience virtually zero DCF valuation loss under a \$120/tCO2 carbon price, while Rumo S.A. loses over 16% of enterprise value?"
**Answer:**  
"The economic transmission channels differ fundamentally between asset classes:
1. **Scope 1/2 Intensity:** FIBRA Prologis emits only 95 tCO2 per million dollars of revenue, mostly Scope 2 electricity for common-area lighting. In contrast, Rumo operates heavy diesel locomotive traction emitting 520 tCO2 per million dollars.
2. **Contractual Pass-Through Capacity:** In logistics warehousing, contracts are structured as triple-net (NNN) leases, where tenants absorb utility and carbon compliance costs (modeled at a conservative 50% pass-through). Rail freight operators, however, face stiff price competition from road trucking in Brazil, capping their ability to pass through diesel carbon taxes.
3. **EBITDA Margins:** Rumo's required fuel-switching capital expenditures and direct tax burdens directly compress operating cash flows, resulting in a \$2.3B enterprise value loss compared to less than \$0.2M for Prologis."

### Question 2: "Explain the basis risk in your parametric insurance structure for the focal logistics hub."
**Answer:**  
"Parametric flood insurance pays out based on an exogenous physical trigger—specifically, cumulative 72-hour precipitation exceeding 240mm recorded at the regional INMET weather gauge or Copernicus ERA5 grid point.  
Basis risk arises when the parametric payout diverges from actual ground damages incurred at the megahub:
- *Negative Basis Risk (Underpayment):* Localized pluvial flash flooding or drainage backup causes \$8M in physical damage, but regional rainfall only registers 220mm, yielding zero insurance payout.
- *Positive Basis Risk (Overpayment):* Regional precipitation exceeds 260mm triggering full payout, but the warehouse's elevated docks prevent inventory damage.
We quantified residual basis risk at \$1.08M in our insurance-alone case. Crucially, in our **Combined Strategy**, structural adaptation elevates asset thresholds, so parametric insurance is reserved purely for catastrophic tail events exceeding a \$5M deductible, which drastically minimizes basis risk."

### Question 3: "How does the focal Use-of-Proceeds Green Bond differ from a Sustainability-Linked Bond (SLB)?"
**Answer:**  
"A Use-of-Proceeds Green Bond earmarks 100% of net proceeds to pre-defined eligible green projects (e.g., LEED Gold logistics warehouses, stormwater retention cisterns) tracked in a ring-fenced escrow sub-account under ICMA Green Bond Principles. The investor's primary risk is greenwashing or proceeds misallocation.  
In contrast, an SLB is general corporate purpose debt tied to company-wide entity-level KPIs (e.g., reducing Scope 1 emissions by 30%). If the issuer misses the KPI target, an SLB triggers a coupon step-up.  
In our project, we also incorporated a contractual penalty covenant (+25 bps step-up) in the Green Bond framework that triggers if the issuer fails to submit verified annual allocation reports, combining the transparency of use-of-proceeds with the accountability of performance penalties."

### Question 4: "How does the Indian regulatory context (SEBI) relate to this Latin American Green Bond?"
**Answer:**  
"The governance structures are remarkably harmonized. Under SEBI's 2023 Operational Circular for ESG Debt Securities and the Indian Sovereign Green Bond Framework (2022):
- Issuers must appoint an independent third-party reviewer (equivalent to an SPO from Sustainalytics).
- Proceeds must be maintained in a dedicated sub-account with mandatory annual allocation tracking.
- Post-issuance impact reporting must be integrated into annual regulatory filings (similar to India's BRSR Core requirement).  
This demonstrates that Mexican and Colombian sustainable taxonomy standards operate on the exact same institutional principles of proceeds ring-fencing and verifiable impact metrics as SEBI."

---

## 3. Anticipated Code Walkthrough & Live Modification Requests

The examiner may ask you to modify a parameter or explain a specific code block live. Here are the exact scripts and modifications:

### Live Modification 1: "Change the carbon price pass-through rate from 50% to 0% and show what happens to valuation."
**Code Location:** `exam/src/valuation_engine.py`, function `run_transition_dcf`.
```python
# To modify:
# In valuation_engine.py, line 10:
# Change default argument: pass_through=0.00
ev_zero_pt = run_transition_dcf(holding_row, carbon_price=120.0, pass_through=0.00)
# Explanation: At pass_through=0.0, net_carbon_cost_musd equals gross_carbon_cost_musd.
# For FIBRA Prologis, EV impact changes from -0.01% to -0.02%.
# For Rumo S.A., EV impact worsens from -16.4% to -31.2%.
```

### Live Modification 2: "Increase the flood event probability from p=0.10 to p=0.15 (climate escalation) in the Monte Carlo simulation."
**Code Location:** `exam/src/risk_transfer_sim.py`, function `simulate_physical_flood_risk`.
```python
# To modify:
# Change line: p_event = 0.15
# Rerun: tab, arrs = simulate_physical_flood_risk()
# Explanation: Expected Annual Loss (EAL) increases linearly by 50% (from $3.28M to $4.92M).
# P95 tail loss increases from $33.15M to $41.8M under No Action, reinforcing the necessity of combined adaptation.
```

### Live Modification 3: "Explain how CAVRS score weights are normalized in portfolio optimization."
**Code Location:** `exam/src/portfolio_optimizer.py`, function `compute_cavrs_scores`.
```python
# Explanation:
# 1. ESG is normalized to [0, 1] by dividing score by 10.0.
# 2. Valuation is normalized so 1.0 represents zero impact and 0.0 represents max loss.
# 3. Carbon penalty is normalized by dividing by max universe intensity (520 tCO2/MUSD).
# 4. Physical hazard is already bounded [0, 1].
# Formula: CAVRS = 0.35*esg + 0.25*val - 0.20*carbon - 0.20*physical.
# In optimize_portfolio_weights(), raw active tilts are bounded by np.clip(raw_w, 0.04, 0.20)
# and normalized via norm_w = clipped_w / clipped_w.sum() so weights always sum to exactly 1.00.
```

---

## 4. Falsification Checklist: What Evidence Would Change Your Mind?

If the examiner asks: *"What evidence would cause you to abandon your recommendations?"*
1. **Abandon Rumo Underweight:** If Rumo signs a binding EPC contract with federal co-financing to build concrete flood retention dykes along the Santos corridor and secures third-party validation for its locomotive hybridization program.
2. **Liquidate Green Bond:** If post-issuance assurance audits uncover that green bond proceeds were co-mingled with general corporate treasury funds or redirected to non-certified brownfield assets.
3. **Downgrade FIBRA Prologis:** If macroeconomic nearshoring deceleration forces landlords to convert triple-net (NNN) leases into gross leases, exposing the REIT to direct carbon taxation volatility.

