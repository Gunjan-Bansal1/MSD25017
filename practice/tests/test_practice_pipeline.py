import os
import json
import pytest
import numpy as np
import pandas as pd

@pytest.fixture(scope="module")
def practice_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    t1_path = os.path.join(base_dir, "outputs", "tables", "table1_holdings_frame.csv")
    t2_path = os.path.join(base_dir, "outputs", "tables", "table2_claim_verification.csv")
    t3_path = os.path.join(base_dir, "outputs", "tables", "table3_risk_transfer_cases.csv")
    t4_path = os.path.join(base_dir, "outputs", "tables", "table4_capital_allocation.csv")
    nb_path = os.path.join(base_dir, "notebooks", "practice_capstone_starter.ipynb")

    return {
        "t1": pd.read_csv(t1_path),
        "t2": pd.read_csv(t2_path),
        "t3": pd.read_csv(t3_path),
        "t4": pd.read_csv(t4_path),
        "nb_path": nb_path
    }

def test_universe_assignment(practice_data):
    with open(practice_data["nb_path"], "r", encoding="utf-8") as f:
        nb = json.load(f)
    # Verify roll number in code cells
    c2_code = "".join(nb["cells"][2]["source"])
    assert 'ROLL = "msd25017"' in c2_code
    assert 'Latin America' in c2_code
    assert 'Logistics hub' in c2_code

def test_block_a_foundations(practice_data):
    df = practice_data["t1"]
    assert len(df) == 4
    assert set(df["primary_channel"]).issubset({"physical", "transition"})
    assert df["physical_exposure"].between(0, 1).all()
    assert df["transition_exposure"].between(0, 1).all()

def test_block_b_carbon_waci(practice_data):
    df = practice_data["t1"]
    coverage = df["emis_intensity_tco2_per_musd"].notna().mean()
    waci = float(np.nansum(df["weight"] * df["emis_intensity_tco2_per_musd"]))
    assert 0.0 < coverage <= 1.0
    assert waci > 0.0

def test_block_c_esg(practice_data):
    df = practice_data["t2"]
    assert len(df) >= 3
    assert "claim" in df.columns
    assert "verification_status" in df.columns

def test_block_d_physical_risk(practice_data):
    df = practice_data["t3"].set_index("case")
    assert df.loc["adaptation", "eal"] < df.loc["no_action", "eal"]
    assert df.loc["combined", "p95"] < df.loc["no_action", "p95"]

def test_block_e_bond(practice_data):
    with open(practice_data["nb_path"], "r", encoding="utf-8") as f:
        nb = json.load(f)
    c19_code = "".join(nb["cells"][19]["source"])
    assert "price_target_met" in c19_code
    assert "greenium_bps" in c19_code

def test_block_f_integration(practice_data):
    df = practice_data["t4"]
    assert len(df) == 4
    assert "score" in df.columns
    assert "recommended_weight" in df.columns
    assert np.isclose(df["recommended_weight"].sum(), 1.0, atol=0.02)

def test_outputs_exist():
    assert os.path.exists(r"practice/outputs/figures/fig1_carbon_sensitivity.png")
    assert os.path.exists(r"practice/outputs/figures/fig2_loss_exceedance.png")
    assert os.path.exists(r"practice/decision_memo.pdf")
