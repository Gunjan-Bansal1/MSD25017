import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from green_bond_model import price_green_bond, evaluate_taxonomy_alignment

def test_green_bond_pricing_properties():
    metrics, sched = price_green_bond()
    
    clean_base = float(metrics["Clean Price (Covenants Met)"].replace("$", ""))
    clean_step = float(metrics["Clean Price (Step-Up Penalty Triggered)"].replace("$", ""))
    greenium = float(metrics["Greenium Discount (bps)"].split()[0])
    
    assert clean_step > clean_base, "Penalty step-up coupon must increase bond price at constant yield"
    assert greenium == 8.5, "Greenium discount must match 8.5 bps"

def test_taxonomy_alignment_elements():
    audit_df = evaluate_taxonomy_alignment()
    assert len(audit_df) == 4, "Must cover all 4 ICMA GBP core pillars"
    assert "SEBI ESG Framework / Indian Benchmark" in audit_df.columns

