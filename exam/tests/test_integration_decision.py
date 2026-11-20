import os
import sys
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from data_loader import load_holdings_universe
from valuation_engine import evaluate_universe_valuations
from portfolio_optimizer import compute_cavrs_scores, optimize_portfolio_weights

def test_integration_and_portfolio_rebalance():
    df_h = load_holdings_universe()
    df_val = evaluate_universe_valuations(df_h)
    df_scored = compute_cavrs_scores(df_h, df_val)
    df_opt, diag = optimize_portfolio_weights(df_scored)
    
    # Portfolio constraints
    assert np.isclose(df_opt["recommended_weight"].sum(), 1.0, atol=0.005), "Weights must sum to 100%"
    assert (df_opt["recommended_weight"] >= 0.035).all(), "Min weight constraint (4%)"
    assert (df_opt["recommended_weight"] <= 0.205).all(), "Max weight constraint (20%)"
    
    # Decarbonization assertion
    bench_waci = diag["Benchmark WACI (tCO2 / MUSD)"]
    rebal_waci = diag["Rebalanced WACI (tCO2 / MUSD)"]
    assert rebal_waci < bench_waci, "Portfolio WACI must be reduced"
    
    # Top overweight holding check
    top_overweight = df_opt.sort_values("active_tilt_pct", ascending=False).iloc[0]
    assert top_overweight["recommendation"] == "Overweight"
    assert top_overweight["active_tilt_pct"] > 0

