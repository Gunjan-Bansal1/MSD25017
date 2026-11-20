import os
import sys
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from data_loader import load_holdings_universe
from carbon_analytics import compute_portfolio_carbon_metrics

def test_carbon_waci_and_coverage():
    df = load_holdings_universe()
    summary_df, waci = compute_portfolio_carbon_metrics(df)
    
    assert waci > 0.0, "Portfolio WACI must be strictly positive"
    assert 100.0 < waci < 300.0, f"Portfolio WACI {waci} outside expected range [100, 300]"
    
    # Check that summary dataframe contains all required metrics
    metrics_list = summary_df["Metric"].tolist()
    assert "Portfolio WACI (Financed Intensity)" in metrics_list
    assert "Scope 1 & 2 Disclosure Coverage" in metrics_list
    assert "Top-2 Emitters Share of Emissions (Rumo + CCR)" in metrics_list

def test_sector_emissions_bifurcation():
    df = load_holdings_universe()
    ind_intensity = df[df["sector"] == "Industrials"]["scope12_intensity_tco2_musd"].mean()
    re_intensity = df[df["sector"] == "Real estate"]["scope12_intensity_tco2_musd"].mean()
    assert ind_intensity > re_intensity, "Industrials should exhibit higher average carbon intensity than Real Estate"

