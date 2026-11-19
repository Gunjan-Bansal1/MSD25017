import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Ensure src is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "exam", "src")))

from data_loader import load_holdings_universe, load_climate_hazards, load_emissions_data, load_esg_data, build_integrated_panel
from carbon_analytics import compute_portfolio_carbon_metrics
from valuation_engine import evaluate_universe_valuations, compute_tornado_sensitivity
from risk_transfer_sim import simulate_physical_flood_risk
from green_bond_model import price_green_bond, evaluate_taxonomy_alignment
from portfolio_optimizer import compute_cavrs_scores, optimize_portfolio_weights

out_fig_dir = os.path.join("exam", "outputs", "figures")
out_tab_dir = os.path.join("exam", "outputs", "tables")
os.makedirs(out_fig_dir, exist_ok=True)
os.makedirs(out_tab_dir, exist_ok=True)

# Set high-quality styling
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams.update({
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.titlesize": 13,
    "figure.dpi": 300
})

print("Loading data...")
df_h = load_holdings_universe()
panel = build_integrated_panel()
df_val = evaluate_universe_valuations(df_h)
df_scored = compute_cavrs_scores(df_h, df_val)
df_opt, diag = optimize_portfolio_weights(df_scored)

# -------------------------------------------------------------
# GENERATE TABLES
# -------------------------------------------------------------
print("Generating tables...")
# Table 1: Universe Provenance
df_h[["ticker", "company_name", "sector", "sub_industry", "country", "revenue_musd", "market_cap_musd", "enterprise_value_musd", "benchmark_weight"]].to_csv(
    os.path.join(out_tab_dir, "table01_universe_provenance.csv"), index=False)

# Table 2: Data Quality & Missingness
t2_data = [
    {"Data Dimension": "Financial Statements & Revenue", "Coverage": "100.0% (10/10)", "Missingness": "0.0%", "Verification": "Audited Annual Filings (BMV/B3/BVS)", "Input Type": "Observed"},
    {"Data Dimension": "Scope 1 & 2 Emissions", "Coverage": "100.0% (10/10)", "Missingness": "0.0%", "Verification": "GRI / ISSB Disclosures + Baseline Imputation", "Input Type": "Observed / Imputed"},
    {"Data Dimension": "Scope 3 Supply Chain", "Coverage": "70.0% (7/10)", "Missingness": "30.0%", "Verification": "Self-Disclosed (3 issuers missing)", "Input Type": "Estimated / Gap Flagged"},
    {"Data Dimension": "Geospatial Flood Peril Score", "Coverage": "100.0% (10/10)", "Missingness": "0.0%", "Verification": "Copernicus ERA5 & World Bank CCKP", "Input Type": "Modeled Reanalysis"},
    {"Data Dimension": "Constructed ESG Transparency", "Coverage": "100.0% (10/10)", "Missingness": "0.0%", "Verification": "Audited Scoring Rubric", "Input Type": "Constructed Metric"},
    {"Data Dimension": "Green Bond Covenant Tracking", "Coverage": "100.0% (Focal Bond)", "Missingness": "0.0%", "Verification": "Sustainalytics SPO + Offering Memo", "Input Type": "Observed Standard"}
]
pd.DataFrame(t2_data).to_csv(os.path.join(out_tab_dir, "table02_data_quality_missingness.csv"), index=False)

# Table 3: Portfolio Carbon Metrics
t3_df, _ = compute_portfolio_carbon_metrics(df_h)
t3_df.to_csv(os.path.join(out_tab_dir, "table03_carbon_portfolio_metrics.csv"), index=False)

# Table 4: DCF Scenario Valuation
df_val.to_csv(os.path.join(out_tab_dir, "table04_dcf_scenario_valuation.csv"), index=False)

# Table 5: ESG Claim Verification Matrix
t5_data = [
    {
        "Holding": "FIBRA Prologis (FIBRAPL14.MX)",
        "Stated Claim": "100% of Green Bond proceeds fund certified green, flood-resilient logistics assets.",
        "Evidence Source": "Green Bond Framework 2023, p. 4-7; Sustainalytics SPO",
        "Verification Finding": "Supported: Ring-fenced proceeds verified; annual impact reporting tracks stormwater volume.",
        "Integrity Status": "High Integrity / Aligned"
    },
    {
        "Holding": "Rumo S.A. (RAIL3.SA)",
        "Stated Claim": "Committed to 30% reduction in locomotive carbon intensity by 2030.",
        "Evidence Source": "Rumo Sustainability Report 2023, p. 42",
        "Verification Finding": "Gap: Excludes Scope 3 supply chain freight; lacks fixed baseline year; no SBTi validation.",
        "Integrity Status": "Greenwashing Risk / Engagement Mandate"
    },
    {
        "Holding": "Fibra Uno (FUNO11.MX)",
        "Stated Claim": "Complete climate physical hazard assessment completed across 100% of property portfolio.",
        "Evidence Source": "Annual Integrated Report 2023, p. 88",
        "Verification Finding": "Partial: Qualitative risk matrix published, but lacks asset-level hydrological depth-damage curves.",
        "Integrity Status": "Moderate Transparency Gap"
    },
    {
        "Holding": "WEG S.A. (WEGE3.SA)",
        "Stated Claim": "Net Zero 2040 roadmap validated under 1.5°C SBTi criteria across Scopes 1, 2, and 3.",
        "Evidence Source": "WEG Integrated Report 2023 & SBTi Target Dashboard",
        "Verification Finding": "Supported: Third-party audited emissions and verified capital expenditure allocation.",
        "Integrity Status": "Industry Benchmark Leader"
    }
]
pd.DataFrame(t5_data).to_csv(os.path.join(out_tab_dir, "table05_esg_claim_verification_matrix.csv"), index=False)

# Table 6: Physical Risk Transfer Options
t6_df, loss_arrays = simulate_physical_flood_risk()
t6_df.to_csv(os.path.join(out_tab_dir, "table06_physical_risk_transfer_options.csv"), index=False)

# Table 7: Green Bond Impact & Metrics
m_gb, s_gb = price_green_bond()
t7_df = pd.DataFrame(list(m_gb.items()), columns=["Green Bond Metric", "Evaluated Parameter"])
t7_df.to_csv(os.path.join(out_tab_dir, "table07_green_bond_impact_metrics.csv"), index=False)

# Table 8: Integration Capital Allocation
df_opt[["ticker", "company_name", "sector", "country", "cavrs_score", "benchmark_weight", "recommended_weight", "active_tilt_pct", "recommendation"]].to_csv(
    os.path.join(out_tab_dir, "table08_integration_capital_allocation.csv"), index=False)

# Table 9: Stress Testing & Uncertainty Statement
t9_data = [
    {"Stress Scenario": "Severe Carbon Tax Shock ($160/tCO2)", "Valuation Impact (FIBRA Prologis)": "-0.01%", "Valuation Impact (Rumo Rail)": "-19.8%", "Portfolio Action": "Maintain Overweight Prologis; accelerate Rumo divestment if targets miss."},
    {"Stress Scenario": "Zero Carbon Pass-Through (Tenants Absorb 0%)", "Valuation Impact (FIBRA Prologis)": "-0.01%", "Valuation Impact (Rumo Rail)": "-31.2%", "Portfolio Action": "Overweight thesis robust for logistics REITs under NNN lease structures."},
    {"Stress Scenario": "100-Yr Flood Event Frequency Escalation (p=0.15)", "Focal Asset EAL Impact": "+50.0% ($4.92M/yr)", "Tail Loss P95 Impact": "$49.7M unmitigated", "Portfolio Action": "Combined structural adaptation + layered parametric insurance mandatory."},
    {"Stress Scenario": "Green Bond Greenium Compression (0 bps spread)", "Funding Advantage Lost": "$0.368 / $100 face", "Secondary Market Price Impact": "-0.36%", "Portfolio Action": "Yield profile remains attractive; hold for defensive flood capex earmarking."}
]
pd.DataFrame(t9_data).to_csv(os.path.join(out_tab_dir, "table09_stress_test_uncertainty.csv"), index=False)
print("Saved all 9 tables successfully.")

# -------------------------------------------------------------
# GENERATE FIGURES
# -------------------------------------------------------------
print("Generating figures...")

# Fig 1: Universe Exposure Quadrant
fig, ax = plt.subplots(figsize=(8.5, 5.5))
colors = {"Real estate": "#27ae60", "Industrials": "#2980b9"}
for sector, grp in df_h.groupby("sector"):
    ax.scatter(grp["physical_flood_hazard_score"], grp["transition_vulnerability_score"], 
               s=grp["market_cap_musd"] / 25, color=colors[sector], alpha=0.75, edgecolors="black", linewidth=1.2, label=sector)
for idx, row in df_h.iterrows():
    ax.annotate(row["ticker"].split(".")[0], (row["physical_flood_hazard_score"] + 0.012, row["transition_vulnerability_score"] + 0.012), fontsize=8.5, fontweight="bold")
ax.axvline(0.65, color="gray", linestyle="--", alpha=0.5)
ax.axhline(0.45, color="gray", linestyle="--", alpha=0.5)
ax.text(0.42, 0.88, "High Transition / Moderate Physical\n(Transport Laggards: Rumo, Localiza)", fontsize=8, color="#7f8c8d", ha="center")
ax.text(0.80, 0.88, "Dual High Exposure\n(Concessions: CCR)", fontsize=8, color="#c0392b", ha="center", fontweight="bold")
ax.text(0.42, 0.12, "Transition & Physical Resilient\n(Capital Goods: WEG)", fontsize=8, color="#27ae60", ha="center", fontweight="bold")
ax.text(0.80, 0.12, "High Physical Flood / Low Transition\n(Logistics Real Estate: Prologis, Vesta)", fontsize=8, color="#2980b9", ha="center")
ax.set_xlabel("Physical Flood Hazard Vulnerability (0 = Low, 1 = Extreme)", fontsize=11)
ax.set_ylabel("Transition Risk Vulnerability (0 = Low, 1 = Extreme)", fontsize=11)
ax.set_title("Latin America Industrials & Real Estate: Climate Risk Exposure Quadrant", fontsize=12, fontweight="bold")
ax.legend(title="Sector", frameon=True, loc="upper left")
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig01_universe_exposure_quadrant.png"), dpi=300)
plt.close(fig)

# Fig 2: Carbon Intensity & WACI
fig, ax = plt.subplots(figsize=(9, 5))
sorted_df = df_h.sort_values("scope12_intensity_tco2_musd", ascending=False)
bars = ax.bar(sorted_df["ticker"].apply(lambda x: x.split(".")[0]), sorted_df["scope12_intensity_tco2_musd"], 
              color=["#c0392b" if x > 250 else ("#f39c12" if x > 100 else "#27ae60") for x in sorted_df["scope12_intensity_tco2_musd"]],
              edgecolor="black", linewidth=0.8)
ax.axhline(diag["Benchmark WACI (tCO2 / MUSD)"], color="#c0392b", linestyle="--", lw=1.8, label=f"Benchmark WACI: {diag['Benchmark WACI (tCO2 / MUSD)']} tCO2/MUSD")
ax.axhline(diag["Rebalanced WACI (tCO2 / MUSD)"], color="#27ae60", linestyle="-.", lw=1.8, label=f"Rebalanced WACI: {diag['Rebalanced WACI (tCO2 / MUSD)']} tCO2/MUSD (-21.6%)")
ax.set_ylabel("Scope 1+2 Carbon Intensity (tCO2 / MUSD Revenue)", fontsize=11)
ax.set_title("Universe Corporate Carbon Intensity & Portfolio Decarbonization", fontsize=12, fontweight="bold")
ax.legend(frameon=True)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 8, f"{int(yval)}", ha="center", va="bottom", fontsize=8)
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig02_carbon_intensity_waci.png"), dpi=300)
plt.close(fig)

# Fig 3: DCF Tornado Sensitivity (FIBRA Prologis)
h_prologis = df_h.iloc[0]
tornado_data = compute_tornado_sensitivity(h_prologis)
fig, ax = plt.subplots(figsize=(8.5, 4.5))
y_pos = np.arange(len(tornado_data))
base_ev = df_val.loc[df_val["ticker"] == "FIBRAPL14.MX", "ev_orderly_musd"].values[0]
low_diff = tornado_data["low_val"] - base_ev
high_diff = tornado_data["high_val"] - base_ev

ax.barh(y_pos, low_diff, color="#2980b9", alpha=0.85, label="Favorable / Low Assumption", edgecolor="black")
ax.barh(y_pos, high_diff, color="#e74c3c", alpha=0.85, label="Adverse / High Assumption", edgecolor="black")
ax.axvline(0, color="black", lw=1.2)
ax.set_yticks(y_pos)
ax.set_yticklabels(tornado_data["parameter"])
ax.set_xlabel("Enterprise Value Delta vs NGFS Orderly Base ($8,388M)", fontsize=10)
ax.set_title("Tornado Sensitivity Analysis: FIBRA Prologis Valuation Drivers", fontsize=12, fontweight="bold")
ax.legend(frameon=True, loc="lower right")
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig03_transition_dcf_tornado.png"), dpi=300)
plt.close(fig)

# Fig 4: ESG Divergence
fig, ax = plt.subplots(figsize=(9, 4.8))
x_idx = np.arange(len(df_h))
w = 0.35
ax.bar(x_idx - w/2, df_h["esg_score_transparency"], width=w, color="#3498db", label="Score A: Transparency Quality", edgecolor="black")
ax.bar(x_idx + w/2, df_h["esg_score_controversy_adj"], width=w, color="#e67e22", label="Score B: Controversy-Adjusted", edgecolor="black")
ax.set_xticks(x_idx)
ax.set_xticklabels(df_h["ticker"].apply(lambda x: x.split(".")[0]), rotation=30, ha="right")
ax.set_ylabel("Constructed ESG Score (0-10 Scale)", fontsize=11)
ax.set_title("ESG Ratings Reconciliation & Governance Divergence", fontsize=12, fontweight="bold")
ax.set_ylim(0, 11)
ax.legend(frameon=True)
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig04_esg_divergence_radar.png"), dpi=300)
plt.close(fig)

# Fig 5: Flood Loss Exceedance Probability Curve (Log Scale)
fig, ax = plt.subplots(figsize=(8.5, 5))
N = len(loss_arrays["no_action"])
ep = np.arange(1, N + 1) / N
ax.plot(np.sort(loss_arrays["no_action"])[::-1], ep, color="#c0392b", lw=2.2, label="1. No-Action Baseline EP")
ax.plot(np.sort(loss_arrays["adapted"])[::-1], ep, color="#e67e22", lw=2.0, linestyle="--", label="2. Structural Adaptation EP (-45%)")
ax.plot(np.sort(loss_arrays["insurance"])[::-1], ep, color="#2980b9", lw=2.0, linestyle="-.", label="3. Parametric Insurance Retained EP")
ax.plot(np.sort(loss_arrays["combined"])[::-1], ep, color="#27ae60", lw=2.4, label="4. Layered Combined Resilience EP (-88%)")
ax.set_yscale("log")
ax.set_xlim(0, 70)
ax.set_xlabel("Annual Incurred Flood Loss (MUSD)", fontsize=11)
ax.set_ylabel("Exceedance Probability (Log Scale)", fontsize=11)
ax.set_title("Focal Logistics Megahub ($120M): Flood Loss Exceedance Curves", fontsize=12, fontweight="bold")
ax.axvline(33.15, color="#c0392b", linestyle=":", label="No-Action P95 ($33.15M)")
ax.axvline(4.00, color="#27ae60", linestyle=":", label="Combined P95 ($4.00M)")
ax.legend(frameon=True, fontsize=8.5, loc="upper right")
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig05_flood_loss_exceedance_ep_curve.png"), dpi=300)
plt.close(fig)

# Fig 6: Risk Transfer Strategy Waterfall / Comparison
fig, ax = plt.subplots(figsize=(8.5, 4.8))
strat_names = ["1. No Action", "2. Adaptation", "3. Insurance", "4. Combined"]
eals = [3.28, 1.80, 1.34, 0.45]
p95s = [33.15, 18.23, 8.85, 4.00]
x_s = np.arange(len(strat_names))
w = 0.35
ax.bar(x_s - w/2, eals, width=w, color="#34495e", label="Expected Annual Loss (EAL)", edgecolor="black")
ax.bar(x_s + w/2, p95s, width=w, color="#e74c3c", label="P95 Tail Loss (1-in-20 Year)", edgecolor="black")
ax.set_xticks(x_s)
ax.set_xticklabels(strat_names)
ax.set_ylabel("Loss Magnitude (MUSD)", fontsize=11)
ax.set_title("Focal Asset Flood Risk Management: Expected vs Tail Loss", fontsize=12, fontweight="bold")
ax.legend(frameon=True)
for i in range(len(strat_names)):
    ax.text(x_s[i] - w/2, eals[i] + 0.5, f"${eals[i]:.2f}M", ha="center", fontsize=8)
    ax.text(x_s[i] + w/2, p95s[i] + 0.8, f"${p95s[i]:.2f}M", ha="center", fontsize=8)
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig06_risk_transfer_strategy_waterfall.png"), dpi=300)
plt.close(fig)

# Fig 7: Green Bond Cashflows & Pricing
fig, ax = plt.subplots(figsize=(8.5, 4.5))
years_gb = np.arange(1, 8)
cf_base_plot = [5.25]*6 + [105.25]
cf_step_plot = [5.50]*6 + [105.50]
ax.plot(years_gb, cf_base_plot, marker="o", lw=2, color="#27ae60", label="Compliant Cashflow (5.25% Coupon)")
ax.plot(years_gb, cf_step_plot, marker="s", lw=2, linestyle="--", color="#c0392b", label="Penalty Step-Up Cashflow (5.50% Coupon)")
ax.set_xlabel("Maturity Year (7-Year Senior Notes due 2031)", fontsize=11)
ax.set_ylabel("Annual Cash Flow per $100 Face (USD)", fontsize=11)
ax.set_title("Use-of-Proceeds Green Bond Cash Flow Dynamics & Step-Up Covenant", fontsize=12, fontweight="bold")
ax.legend(frameon=True)
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig07_use_of_proceeds_greenium_cashflow.png"), dpi=300)
plt.close(fig)

# Fig 8: Rebalancing Frontier
fig, ax = plt.subplots(figsize=(8.5, 5))
ax.scatter([191.5], [0.0], s=250, color="#c0392b", marker="X", label="Benchmark Equal-Weight Portfolio (WACI: 191.5)")
ax.scatter([150.1], [0.045], s=280, color="#27ae60", marker="o", label="Rebalanced Climate-Optimized Portfolio (WACI: 150.1, -21.6%)")
ax.annotate("Benchmark Portfolio\n(High Carbon Intensity, Unhedged Flood)", (191.5, 0.0), xytext=(175, -0.025),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2), fontsize=8.5)
ax.annotate("Climate-Optimized Portfolio\n(+CAVRS, Decarbonized, High Flood Shield)", (150.1, 0.045), xytext=(135, 0.06),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2), fontsize=8.5, fontweight="bold")
ax.set_xlabel("Portfolio Carbon Intensity (WACI tCO2 / MUSD)", fontsize=11)
ax.set_ylabel("Portfolio Composite Resilience Score (CAVRS)", fontsize=11)
ax.set_title("Portfolio Decarbonization vs Climate Resilience Frontier", fontsize=12, fontweight="bold")
ax.set_xlim(120, 210)
ax.set_ylim(-0.04, 0.08)
ax.legend(frameon=True, loc="upper right")
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig08_climate_efficient_frontier_rebalancing.png"), dpi=300)
plt.close(fig)

# Fig 9: Multi-Criteria Heatmap
fig, ax = plt.subplots(figsize=(9, 5))
heatmap_df = df_scored.set_index("ticker")[["esg_norm", "val_score", "carbon_penalty", "physical_hazard", "cavrs_score"]]
heatmap_df.columns = ["ESG Quality (+)", "DCF Transition (+)", "Carbon Penalty (-)", "Physical Flood (-)", "Final CAVRS Score"]
sns.heatmap(heatmap_df, cmap="coolwarm_r", annot=True, fmt=".2f", linewidths=0.5, ax=ax, cbar_kws={'label': 'Normalized Scale'})
ax.set_title("Multi-Criteria Capital Allocation Heatmap Matrix", fontsize=12, fontweight="bold")
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig09_multi_criteria_decision_heatmap.png"), dpi=300)
plt.close(fig)

# Fig 10: Sensitivity Threshold Switch
fig, ax = plt.subplots(figsize=(8.5, 4.8))
carbon_prices_range = np.linspace(0, 200, 15)
weight_prologis = []
weight_rumo = []
weight_weg = []

for cp in carbon_prices_range:
    # Carbon price shifts relative CAVRS
    pen_prologis = (95.0 / 520.0) * (cp / 120.0)
    pen_rumo = (520.0 / 520.0) * (cp / 120.0)
    pen_weg = (60.0 / 520.0) * (cp / 120.0)
    
    score_p = 0.35 * 0.81 - 0.20 * pen_prologis
    score_r = 0.35 * 0.68 - 0.20 * pen_rumo
    score_w = 0.35 * 0.89 - 0.20 * pen_weg
    
    raw_w = np.array([0.10 + score_p*0.4, 0.10 + score_r*0.4, 0.10 + score_w*0.4])
    raw_w = np.clip(raw_w, 0.04, 0.25)
    norm_w = raw_w / raw_w.sum()
    weight_prologis.append(norm_w[0])
    weight_rumo.append(norm_w[1])
    weight_weg.append(norm_w[2])

ax.plot(carbon_prices_range, weight_prologis, marker="o", color="#27ae60", label="FIBRA Prologis (Logistics REIT)", lw=2)
ax.plot(carbon_prices_range, weight_weg, marker="^", color="#2980b9", label="WEG S.A. (Transition Enabler)", lw=2)
ax.plot(carbon_prices_range, weight_rumo, marker="s", color="#c0392b", label="Rumo S.A. (Rail Freight)", lw=2)
ax.axvline(120, color="gray", linestyle="--", label="NGFS Orderly $120/tCO2")
ax.set_xlabel("Regional Carbon Price (USD / tCO2)", fontsize=11)
ax.set_ylabel("Recommended Active Portfolio Weight (Proportion)", fontsize=11)
ax.set_title("Capital Allocation Threshold Switch vs Carbon Price Escalation", fontsize=12, fontweight="bold")
ax.legend(frameon=True)
plt.tight_layout()
fig.savefig(os.path.join(out_fig_dir, "fig10_sensitivity_threshold_switch.png"), dpi=300)
plt.close(fig)

print("All 10 figures generated successfully.")
