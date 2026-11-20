import os
import pandas as pd
import numpy as np

def run_transition_dcf(holding_row, carbon_price, wacc=0.09, g=0.02, pass_through=0.50, tax_rate=0.25, horizon_years=10):
    """
    10-year discounted cash flow model adjusting for carbon pricing under NGFS pathways.
    """
    rev_base = holding_row["revenue_musd"]
    ebitda_margin = holding_row["ebitda_margin"]
    intensity = holding_row["scope12_intensity_tco2_musd"]
    
    # Annual revenue growth rate (2.5% p.a.)
    years = np.arange(1, horizon_years + 1)
    rev_t = rev_base * ((1.025) ** years)
    ebit_t = rev_t * (ebitda_margin - 0.06) # Depr & Amort approx 6% of revenue
    
    # Scope 1+2 emissions volume in ktCO2
    annual_emissions_t = (intensity * rev_t) / 1e3
    
    # Gross carbon cost liability
    gross_carbon_cost_musd = (annual_emissions_t * carbon_price) / 1e3
    # Net carbon cost after tenant/customer pass-through
    net_carbon_cost_musd = gross_carbon_cost_musd * (1.0 - pass_through)
    
    # CapEx & Working Capital reinvestment (approx 5% of rev)
    reinvestment_t = rev_t * 0.05
    
    # Free Cash Flow to Firm (FCFF)
    nopat_t = (ebit_t - net_carbon_cost_musd) * (1.0 - tax_rate)
    fcff_t = nopat_t - reinvestment_t
    
    # Discount factors
    discount_factors = (1.0 + wacc) ** years
    pv_cashflows = np.sum(fcff_t / discount_factors)
    
    # Terminal Value
    terminal_fcf = fcff_t[-1] * (1.0 + g)
    terminal_value = terminal_fcf / (wacc - g)
    pv_terminal_value = terminal_value / discount_factors[-1]
    
    enterprise_value = pv_cashflows + pv_terminal_value
    return float(enterprise_value)

def evaluate_universe_valuations(df_holdings):
    results = []
    scenarios = {
        "baseline_5usd": 5.0,
        "delayed_75usd": 75.0,
        "orderly_120usd": 120.0,
        "severe_160usd": 160.0
    }
    for idx, row in df_holdings.iterrows():
        ev_base = run_transition_dcf(row, scenarios["baseline_5usd"], pass_through=0.50)
        ev_delayed = run_transition_dcf(row, scenarios["delayed_75usd"], pass_through=0.50)
        ev_orderly = run_transition_dcf(row, scenarios["orderly_120usd"], pass_through=0.50)
        ev_severe = run_transition_dcf(row, scenarios["severe_160usd"], pass_through=0.50)
        
        impact_orderly_pct = ((ev_orderly / ev_base) - 1.0) * 100.0
        impact_severe_pct = ((ev_severe / ev_base) - 1.0) * 100.0
        
        # Zero pass-through stress test
        ev_zero_pt = run_transition_dcf(row, scenarios["orderly_120usd"], pass_through=0.0)
        impact_zero_pt_pct = ((ev_zero_pt / ev_base) - 1.0) * 100.0

        results.append({
            "ticker": row["ticker"],
            "company_name": row["company_name"],
            "sector": row["sector"],
            "ev_baseline_musd": round(ev_base, 2),
            "ev_delayed_musd": round(ev_delayed, 2),
            "ev_orderly_musd": round(ev_orderly, 2),
            "ev_severe_musd": round(ev_severe, 2),
            "impact_orderly_pct": round(impact_orderly_pct, 2),
            "impact_severe_pct": round(impact_severe_pct, 2),
            "impact_zero_passthrough_pct": round(impact_zero_pt_pct, 2)
        })
    df_val = pd.DataFrame(results)
    return df_val

def compute_tornado_sensitivity(holding_row):
    """
    Computes sensitivity swings for holding under variations of key parameters.
    """
    base_val = run_transition_dcf(holding_row, 120.0, wacc=0.09, g=0.02, pass_through=0.50)
    
    # 1. Carbon Price ($5 vs $160)
    low_cp = run_transition_dcf(holding_row, 5.0, wacc=0.09, g=0.02, pass_through=0.50)
    high_cp = run_transition_dcf(holding_row, 160.0, wacc=0.09, g=0.02, pass_through=0.50)
    
    # 2. Pass-through (100% vs 0%)
    high_pt = run_transition_dcf(holding_row, 120.0, wacc=0.09, g=0.02, pass_through=1.00)
    low_pt = run_transition_dcf(holding_row, 120.0, wacc=0.09, g=0.02, pass_through=0.00)
    
    # 3. WACC (7.5% vs 10.5%)
    low_wacc = run_transition_dcf(holding_row, 120.0, wacc=0.075, g=0.02, pass_through=0.50)
    high_wacc = run_transition_dcf(holding_row, 120.0, wacc=0.105, g=0.02, pass_through=0.50)
    
    # 4. Terminal Growth Rate (1.5% vs 2.5%)
    low_g = run_transition_dcf(holding_row, 120.0, wacc=0.09, g=0.015, pass_through=0.50)
    high_g = run_transition_dcf(holding_row, 120.0, wacc=0.09, g=0.025, pass_through=0.50)

    tornado_df = pd.DataFrame([
        {"parameter": "Carbon Price ($5 vs $160/t)", "low_val": low_cp, "high_val": high_cp, "swing": abs(high_cp - low_cp)},
        {"parameter": "Pass-Through Rate (100% vs 0%)", "low_val": high_pt, "high_val": low_pt, "swing": abs(high_pt - low_pt)},
        {"parameter": "WACC (7.5% vs 10.5%)", "low_val": high_wacc, "high_val": low_wacc, "swing": abs(high_wacc - low_wacc)},
        {"parameter": "Terminal Growth (1.5% vs 2.5%)", "low_val": low_g, "high_val": high_g, "swing": abs(high_g - low_g)},
    ]).sort_values("swing", ascending=False)
    
    return tornado_df

if __name__ == "__main__":
    from data_loader import load_holdings_universe
    df = load_holdings_universe()
    val_df = evaluate_universe_valuations(df)
    print(val_df[["ticker", "ev_baseline_musd", "ev_orderly_musd", "impact_orderly_pct", "impact_zero_passthrough_pct"]].to_string(index=False))

