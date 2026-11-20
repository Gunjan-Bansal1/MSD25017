import os
import pandas as pd
import numpy as np

def price_green_bond(face=100.0, coupon=0.0525, step_up=0.0025, maturity=7, ytm=0.0485, greenium_bps=8.5):
    """
    Evaluates Use-of-Proceeds Green Bond pricing under base compliance vs covenant step-up,
    and quantifies the issuer's greenium funding advantage.
    """
    years = np.arange(1, maturity + 1)
    
    # Base Cashflows (Covenants Met)
    cfs_base = np.repeat(face * coupon, maturity)
    cfs_base[-1] += face
    
    # Step-Up Cashflows (Covenants Missed / Reporting Breach)
    cfs_step = np.repeat(face * (coupon + step_up), maturity)
    cfs_step[-1] += face
    
    # Conventional Benchmark Yield (without greenium)
    ytm_brown = ytm + (greenium_bps / 10000.0)
    
    # Discount Factors
    df_green = 1.0 / ((1.0 + ytm) ** years)
    df_brown = 1.0 / ((1.0 + ytm_brown) ** years)
    
    # Clean Prices
    price_base = float(np.sum(cfs_base * df_green))
    price_stepup = float(np.sum(cfs_step * df_green))
    price_brown_equiv = float(np.sum(cfs_base * df_brown))
    
    # Greenium Net Present Value Benefit to Issuer per $100 Face
    npv_greenium_savings = float(price_base - price_brown_equiv)
    
    # Total Dollars Saved on $500M Offering
    total_dollar_savings = (npv_greenium_savings / 100.0) * 500e6
    
    schedule = pd.DataFrame({
        "Year": years,
        "Base_Cashflow": cfs_base,
        "StepUp_Cashflow": cfs_step,
        "PV_Green_Cashflow": (cfs_base * df_green).round(3),
        "PV_Brown_Cashflow": (cfs_base * df_brown).round(3),
    })

    metrics = {
        "Face Value ($)": face,
        "Stated Coupon Rate (%)": f"{coupon:.3%}",
        "Yield to Maturity (%)": f"{ytm:.3%}",
        "Tenor (Years)": maturity,
        "Greenium Discount (bps)": f"{greenium_bps:.1f} bps",
        "Clean Price (Covenants Met)": f"${price_base:.2f}",
        "Clean Price (Step-Up Penalty Triggered)": f"${price_stepup:.2f}",
        "NPV Greenium Savings (per $100 Face)": f"${npv_greenium_savings:.3f}",
        "Total Issuer Financing Benefit ($500M Tranche)": f"${total_dollar_savings / 1e6:,.2f} MUSD"
    }

    return metrics, schedule

def evaluate_taxonomy_alignment():
    """
    Detailed audit of Use-of-Proceeds Green Bond against ICMA GBP, LatAm Taxonomies, and SEBI / Indian Regulations.
    """
    audit = [
        {
            "Framework Element": "1. Use of Proceeds",
            "FIBRA Prologis Green Bond Specs": "100% net proceeds ring-fenced for LEED Gold/Platinum logistics warehouses and flood retention basins.",
            "ICMA GBP Alignment": "Fully Aligned (Eligible Green Buildings & Climate Adaptation)",
            "Mexico / Colombia Taxonomy": "Meets energy intensity thresholds (<45 kWh/m2) and flood stormwater retention capacity criteria.",
            "SEBI ESG Framework / Indian Benchmark": "Complies with SEBI Operational Circular 2023 Chap. IX (Clean transport & climate resilient infrastructure; equivalent to Indian Sovereign Green Bond Framework 2022)."
        },
        {
            "Framework Element": "2. Project Selection",
            "FIBRA Prologis Green Bond Specs": "Dedicated Green Financing Committee comprising Head of Sustainability, CFO, and Technical Operations.",
            "ICMA GBP Alignment": "Fully Aligned (Formal Governance Charter)",
            "Mexico / Colombia Taxonomy": "Requires mandatory environmental impact assessments (EIA) for flood basin construction.",
            "SEBI ESG Framework / Indian Benchmark": "Directly mirrors SEBI requirement for an internal screening committee with technical climate expertise."
        },
        {
            "Framework Element": "3. Management of Proceeds",
            "FIBRA Prologis Green Bond Specs": "Proceeds deposited into a segregated sub-account; quarterly reconciliation; temporary unallocated proceeds held in cash/treasuries.",
            "ICMA GBP Alignment": "Fully Aligned (Earmarked Account & Tracking)",
            "Mexico / Colombia Taxonomy": "Mandates no investment in high-carbon transitional assets.",
            "SEBI ESG Framework / Indian Benchmark": "Strictly matches SEBI & Indian MoF ring-fencing mandate; third-party auditor tracks account balance."
        },
        {
            "Framework Element": "4. Reporting & Impact MRV",
            "FIBRA Prologis Green Bond Specs": "Annual Green Bond Report disclosing allocated amounts, unallocated balance, avoided tCO2e, and cubic meters of flood water managed.",
            "ICMA GBP Alignment": "Fully Aligned (Annual Public Allocation & Impact Reporting)",
            "Mexico / Colombia Taxonomy": "Requires independent verification of operational metrics against regional taxonomy benchmarks.",
            "SEBI ESG Framework / Indian Benchmark": "Aligns with SEBI mandatory BRSR Core reporting and Indian Sovereign Green Bond post-issuance verification by external reviewers."
        }
    ]
    return pd.DataFrame(audit)

if __name__ == "__main__":
    m, s = price_green_bond()
    print("=== Green Bond Pricing & Financial Analysis ===")
    for k, v in m.items():
        print(f"  {k:45}: {v}")

