import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from data_loader import load_holdings_universe
from valuation_engine import evaluate_universe_valuations, compute_tornado_sensitivity

def test_valuation_sensitivities():
    df = load_holdings_universe()
    val_df = evaluate_universe_valuations(df)
    
    # Baseline enterprise value must exceed orderly transition value
    assert (val_df["ev_baseline_musd"] >= val_df["ev_orderly_musd"]).all()
    # Severe transition impact must be more negative than orderly
    assert (val_df["impact_severe_pct"] <= val_df["impact_orderly_pct"]).all()

def test_tornado_ranking():
    df = load_holdings_universe()
    prologis_row = df.iloc[0]
    tornado_df = compute_tornado_sensitivity(prologis_row)
    assert len(tornado_df) == 4
    assert (tornado_df["swing"] >= 0).all()

