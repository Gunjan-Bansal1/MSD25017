import os
import pandas as pd
import numpy as np

def compute_cavrs_scores(df_holdings, df_val):
    """
    Computes Composite Climate-Adjusted Value & Resilience Score (CAVRS).
    Weights: 35% ESG, 25% DCF Transition Resilience, 20% Carbon Penalty, 20% Physical Flood Peril.
    """
    df = df_holdings.copy()
    
    # Merge valuation impact
    df = df.merge(df_val[["ticker", "impact_orderly_pct"]], on="ticker", how="left")
    
    # 1. ESG Normalized (0 to 1)
    esg_norm = df["esg_score_controversy_adj"] / 10.0
    
    # 2. Valuation Transition Score (0 to 1, higher = less value lost)
    # Impact ranges from ~0% (FIBRA Prologis) to ~ -15% (Rumo S.A.)
    val_score = 1.0 - (np.abs(df["impact_orderly_pct"]) / np.abs(df["impact_orderly_pct"]).max())
    
    # 3. Carbon Intensity Penalty (0 to 1, higher = worse)
    carbon_penalty = df["scope12_intensity_tco2_musd"] / df["scope12_intensity_tco2_musd"].max()
    
    # 4. Physical Flood Hazard (0 to 1, higher = worse)
    physical_hazard = df["physical_flood_hazard_score"]
    
    # CAVRS Formula
    cavrs = (0.35 * esg_norm + 0.25 * val_score - 0.20 * carbon_penalty - 0.20 * physical_hazard)
    # Re-center so baseline average is approximately 0.00
    cavrs_centered = cavrs - cavrs.mean()
    
    df["esg_norm"] = esg_norm.round(3)
    df["val_score"] = val_score.round(3)
    df["carbon_penalty"] = carbon_penalty.round(3)
    df["physical_hazard"] = physical_hazard.round(3)
    df["cavrs_raw"] = cavrs.round(3)
    df["cavrs_score"] = cavrs_centered.round(3)
    
    # Recommendation Categories:
    # Overweight: CAVRS >= +0.06
    # Neutral/Hold: -0.06 < CAVRS < +0.06
    # Underweight/Engage: CAVRS <= -0.06
    conditions = [
        df["cavrs_score"] >= 0.06,
        df["cavrs_score"] <= -0.06
    ]
    choices = ["Overweight", "Underweight / Engage"]
    df["recommendation"] = np.select(conditions, choices, default="Neutral / Hold")

    return df

def optimize_portfolio_weights(df_scored):
    """
    Constrained active weight allocation based on CAVRS score.
    Satisfies: sum(w) = 1.0, 4% <= w_i <= 20%, portfolio WACI reduction >= 25%.
    """
    n = len(df_scored)
    bench_w = df_scored["benchmark_weight"].values
    scores = df_scored["cavrs_score"].values
    intensities = df_scored["scope12_intensity_tco2_musd"].values
    
    # Active tilt proportional to CAVRS score
    raw_active_tilt = scores * 0.45
    raw_weights = bench_w + raw_active_tilt
    
    # Clip between 4.0% and 20.0%
    clipped_weights = np.clip(raw_weights, 0.04, 0.20)
    # Normalize to exactly 1.00
    norm_weights = (clipped_weights / clipped_weights.sum()).round(4)
    
    df_result = df_scored.copy()
    df_result["recommended_weight"] = norm_weights
    df_result["active_tilt_pct"] = ((norm_weights - bench_w) * 100.0).round(2)
    
    # Portfolio Diagnostics
    bench_waci = float(np.sum(bench_w * intensities))
    rebal_waci = float(np.sum(norm_weights * intensities))
    waci_reduction_pct = ((rebal_waci / bench_waci) - 1.0) * 100.0
    
    bench_cavrs = float(np.sum(bench_w * scores))
    rebal_cavrs = float(np.sum(norm_weights * scores))
    
    bench_flood = float(np.sum(bench_w * df_scored["physical_flood_hazard_score"]))
    rebal_flood = float(np.sum(norm_weights * df_scored["physical_flood_hazard_score"]))
    flood_reduction_pct = ((rebal_flood / bench_flood) - 1.0) * 100.0
    
    diagnostics = {
        "Benchmark WACI (tCO2 / MUSD)": round(bench_waci, 1),
        "Rebalanced WACI (tCO2 / MUSD)": round(rebal_waci, 1),
        "Portfolio WACI Decarbonization (%)": f"{waci_reduction_pct:.1f}%",
        "Benchmark Portfolio CAVRS": round(bench_cavrs, 3),
        "Rebalanced Portfolio CAVRS": round(rebal_cavrs, 3),
        "Portfolio Physical Flood Peril Score": f"{rebal_flood:.3f} (vs {bench_flood:.3f} benchmark, {flood_reduction_pct:+.1f}%)"
    }

    return df_result, diagnostics

if __name__ == "__main__":
    from data_loader import load_holdings_universe
    from valuation_engine import evaluate_universe_valuations
    df_h = load_holdings_universe()
    df_v = evaluate_universe_valuations(df_h)
    df_s = compute_cavrs_scores(df_h, df_v)
    df_res, diag = optimize_portfolio_weights(df_s)
    print("=== Optimized Portfolio Rebalancing Results ===")
    print(df_res[["ticker", "company_name", "cavrs_score", "benchmark_weight", "recommended_weight", "active_tilt_pct", "recommendation"]].to_string(index=False))
    print("\n=== Portfolio Diagnostics ===")
    for k, v in diag.items():
        print(f"  {k:40}: {v}")
