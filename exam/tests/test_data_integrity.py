import os
import sys
import pytest
import pandas as pd
import numpy as np

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_loader import load_holdings_universe, load_climate_hazards, load_emissions_data, load_esg_data, build_integrated_panel

def test_holdings_universe_structure():
    df = load_holdings_universe()
    assert len(df) == 10, "Universe must contain exactly 10 holdings"
    assert set(df["sector"].unique()) == {"Industrials", "Real estate"}, "Universe must span Industrials and Real Estate"
    assert set(df["primary_channel"].unique()) == {"physical", "transition"}, "Primary channel must be physical or transition"
    assert df["benchmark_weight"].sum() == pytest.approx(1.0, 1e-4), "Benchmark weights must sum to 1.0"

def test_data_completeness_and_bounds():
    df = load_holdings_universe()
    assert (df["revenue_musd"] > 0).all(), "Revenues must be positive"
    assert (df["enterprise_value_musd"] > 0).all(), "Enterprise values must be positive"
    assert df["physical_flood_hazard_score"].between(0, 1).all(), "Hazard scores must be in [0, 1]"
    assert df["transition_vulnerability_score"].between(0, 1).all(), "Transition scores must be in [0, 1]"

def test_integrated_panel_generation():
    panel = build_integrated_panel()
    assert len(panel) == 10
    assert "copernicus_rx5day_mm" in panel.columns
    assert "divergence" in panel.columns
