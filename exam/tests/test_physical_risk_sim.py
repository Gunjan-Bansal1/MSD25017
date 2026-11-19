import os
import sys
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from risk_transfer_sim import simulate_physical_flood_risk

def test_physical_flood_sim():
    tab, arrs = simulate_physical_flood_risk(n_sims=5000)
    
    # EAL comparisons
    eal_no_action = arrs["no_action"].mean()
    eal_adapted = arrs["adapted"].mean()
    eal_combined = arrs["combined"].mean()
    
    assert eal_adapted < eal_no_action, "Adaptation must reduce expected annual loss"
    assert eal_combined < eal_no_action, "Combined strategy must substantially reduce loss"
    
    # P95 Tail Loss
    p95_no_action = np.percentile(arrs["no_action"], 95)
    p95_combined = np.percentile(arrs["combined"], 95)
    assert p95_combined < p95_no_action, "P95 tail loss must be compressed"
