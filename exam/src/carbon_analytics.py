import os
import pandas as pd
import numpy as np

def compute_portfolio_carbon_metrics(df_holdings):
    """
    Computes WACI, emissions coverage, financed emissions proxy, and concentration.
    Follows PCAF (Partnership for Carbon Accounting Financials) & TCFD guidance.
    """
    n = len(df_holdings)
    weights = df_holdings["benchmark_weight"].values
    intensities = df_holdings["scope12_intensity_tco2_musd"].values
    revenues = df_holdings["revenue_musd"].values
    ev = df_holdings["enterprise_value_musd"].values

    # Coverage
    coverage_scope12 = df_holdings["scope12_intensity_tco2_musd"].notna().mean()
    coverage_scope3 = df_holdings["scope3_disclosed"].mean()

    # WACI (tCO2 / MUSD) = Sum (Weight_i * CarbonIntensity_i)
    waci_portfolio = float(np.sum(weights * intensities))

    # Total Universe Gross Emissions (Scope 1 + Scope 2 in ktCO2)
    total_scope1_kt = df_holdings["scope1_emis_kt"].sum()
    total_scope2_kt = df_holdings["scope2_emis_kt"].sum()
    total_emissions_kt = total_scope1_kt + total_scope2_kt

    # Financed Emissions Proxy (assuming an equal 10% equity investment in each firm)
    # Financed Emissions = Sum (Investment_i / EV_i * TotalEmissions_i)
    fund_size_musd = 250.0 # $250M AUM Fund
    investment_per_holding = fund_size_musd * weights
    ownership_share = investment_per_holding / ev
    financed_emissions_kt = np.sum(ownership_share * (df_holdings["scope1_emis_kt"] + df_holdings["scope2_emis_kt"]))

    # Sector Breakdown
    ind_mask = df_holdings["sector"] == "Industrials"
    re_mask = df_holdings["sector"] == "Real estate"

    waci_industrials = float(np.sum(weights[ind_mask] * intensities[ind_mask]) / weights[ind_mask].sum())
    waci_real_estate = float(np.sum(weights[re_mask] * intensities[re_mask]) / weights[re_mask].sum())

    # Concentration: Top 2 emitter share of total universe emissions
    emitter_shares = (df_holdings["scope1_emis_kt"] + df_holdings["scope2_emis_kt"]) / total_emissions_kt
    top2_concentration = float(emitter_shares.nlargest(2).sum())
    hhi_emissions = float(np.sum((emitter_shares * 100) ** 2))

    summary = {
        "Metric": [
            "Scope 1 & 2 Disclosure Coverage",
            "Scope 3 Value Chain Coverage",
            "Portfolio WACI (Financed Intensity)",
            "Industrials Sector Average Intensity",
            "Real Estate Sector Average Intensity",
            "Total Universe Gross Emissions",
            "Scope 1 Gross Emissions",
            "Scope 2 Gross Emissions",
            "Financed Emissions Proxy ($250M AUM)",
            "Top-2 Emitters Share of Emissions (Rumo + CCR)",
            "Emissions Herfindahl-Hirschman Index (HHI)"
        ],
        "Value": [
            f"{coverage_scope12:.1%}",
            f"{coverage_scope3:.1%}",
            f"{waci_portfolio:.1f} tCO2 / MUSD",
            f"{waci_industrials:.1f} tCO2 / MUSD",
            f"{waci_real_estate:.1f} tCO2 / MUSD",
            f"{total_emissions_kt:,.1f} ktCO2e",
            f"{total_scope1_kt:,.1f} ktCO2e",
            f"{total_scope2_kt:,.1f} ktCO2e",
            f"{financed_emissions_kt:,.2f} ktCO2e",
            f"{top2_concentration:.1%}",
            f"{hhi_emissions:,.0f} pts"
        ]
    }
    df_summary = pd.DataFrame(summary)
    return df_summary, waci_portfolio

if __name__ == "__main__":
    from data_loader import load_holdings_universe
    df = load_holdings_universe()
    summary_df, waci = compute_portfolio_carbon_metrics(df)
    print(f"Computed WACI: {waci:.1f} tCO2/MUSD")
    print(summary_df.to_string(index=False))

