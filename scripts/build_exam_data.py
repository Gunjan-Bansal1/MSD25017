import os
import numpy as np
import pandas as pd

# Fix random seed for strict reproducibility
RNG = np.random.default_rng(2026017)

# 1. 10 Holdings Universe
holdings_data = [
    {
        "ticker": "FIBRAPL14.MX",
        "company_name": "FIBRA Prologis",
        "sector": "Real estate",
        "sub_industry": "Logistics & Industrial REIT",
        "country": "Mexico",
        "revenue_musd": 3450.0,
        "ebitda_margin": 0.285,
        "market_cap_musd": 4120.0,
        "enterprise_value_musd": 5680.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 18.5,
        "scope2_emis_kt": 309.2,
        "scope12_intensity_tco2_musd": 95.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.82,
        "transition_vulnerability_score": 0.22,
        "primary_channel": "physical",
        "transmission_mechanism": "Torrential pluvial flooding inundates logistics aprons and docks, disrupting tenant inventory and triggering rent abatements; low direct transition carbon cost.",
        "esg_score_transparency": 8.8,
        "esg_score_controversy_adj": 8.1,
    },
    {
        "ticker": "RAIL3.SA",
        "company_name": "Rumo S.A.",
        "sector": "Industrials",
        "sub_industry": "Rail Freight & Intermodal Logistics",
        "country": "Brazil",
        "revenue_musd": 11200.0,
        "ebitda_margin": 0.420,
        "market_cap_musd": 8950.0,
        "enterprise_value_musd": 14200.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 5420.0,
        "scope2_emis_kt": 404.0,
        "scope12_intensity_tco2_musd": 520.0,
        "scope3_disclosed": False,
        "physical_flood_hazard_score": 0.76,
        "transition_vulnerability_score": 0.85,
        "primary_channel": "transition",
        "transmission_mechanism": "Heavy diesel locomotive fleet faces steep carbon taxation and fuel-switching capex; railbed washout risk along mountain corridors during extreme rainfall.",
        "esg_score_transparency": 4.5,
        "esg_score_controversy_adj": 6.8,
    },
    {
        "ticker": "FUNO11.MX",
        "company_name": "Fibra Uno",
        "sector": "Real estate",
        "sub_industry": "Industrial & Diversified REIT",
        "country": "Mexico",
        "revenue_musd": 4800.0,
        "ebitda_margin": 0.310,
        "market_cap_musd": 5850.0,
        "enterprise_value_musd": 9400.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 42.0,
        "scope2_emis_kt": 630.0,
        "scope12_intensity_tco2_musd": 140.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.71,
        "transition_vulnerability_score": 0.32,
        "primary_channel": "physical",
        "transmission_mechanism": "Valley basin warehouse parks face pluvial pooling; moderate Scope 2 energy efficiency retrofit costs across older vintage assets.",
        "esg_score_transparency": 7.5,
        "esg_score_controversy_adj": 6.9,
    },
    {
        "ticker": "CCRO3.SA",
        "company_name": "CCR S.A.",
        "sector": "Industrials",
        "sub_industry": "Toll Roads & Airport Concessions",
        "country": "Brazil",
        "revenue_musd": 7900.0,
        "ebitda_margin": 0.510,
        "market_cap_musd": 6200.0,
        "enterprise_value_musd": 11800.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 1280.0,
        "scope2_emis_kt": 1169.0,
        "scope12_intensity_tco2_musd": 310.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.68,
        "transition_vulnerability_score": 0.65,
        "primary_channel": "transition",
        "transmission_mechanism": "Highway landslides and airport cargo runway flash flooding impair traffic volume; concession contracts demand fleet electrification and climate adaptation capex.",
        "esg_score_transparency": 6.6,
        "esg_score_controversy_adj": 5.9,
    },
    {
        "ticker": "RENT3.SA",
        "company_name": "Localiza Fleet Logistics",
        "sector": "Industrials",
        "sub_industry": "Commercial Fleet Logistics",
        "country": "Brazil",
        "revenue_musd": 6400.0,
        "ebitda_margin": 0.330,
        "market_cap_musd": 9800.0,
        "enterprise_value_musd": 15600.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 850.0,
        "scope2_emis_kt": 942.0,
        "scope12_intensity_tco2_musd": 280.0,
        "scope3_disclosed": False,
        "physical_flood_hazard_score": 0.52,
        "transition_vulnerability_score": 0.72,
        "primary_channel": "transition",
        "transmission_mechanism": "Heavy commercial logistics vehicle fleet transition to electric/hybrid; residual physical risk from logistics hub depot inundation.",
        "esg_score_transparency": 6.2,
        "esg_score_controversy_adj": 6.5,
    },
    {
        "ticker": "VESTA.MX",
        "company_name": "Corporacion Inmobiliaria Vesta",
        "sector": "Real estate",
        "sub_industry": "Industrial Logistics Development",
        "country": "Mexico",
        "revenue_musd": 2150.0,
        "ebitda_margin": 0.340,
        "market_cap_musd": 3200.0,
        "enterprise_value_musd": 4350.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 8.2,
        "scope2_emis_kt": 163.8,
        "scope12_intensity_tco2_musd": 80.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.78,
        "transition_vulnerability_score": 0.20,
        "primary_channel": "physical",
        "transmission_mechanism": "Nearshoring logistics parks located in rapidly urbanizing northern Mexico corridors exposed to severe convective flash flooding.",
        "esg_score_transparency": 8.5,
        "esg_score_controversy_adj": 8.0,
    },
    {
        "ticker": "WEGE3.SA",
        "company_name": "WEG S.A.",
        "sector": "Industrials",
        "sub_industry": "Electrical Capital Goods",
        "country": "Brazil",
        "revenue_musd": 9300.0,
        "ebitda_margin": 0.225,
        "market_cap_musd": 24500.0,
        "enterprise_value_musd": 23900.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 145.0,
        "scope2_emis_kt": 413.0,
        "scope12_intensity_tco2_musd": 60.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.44,
        "transition_vulnerability_score": 0.15,
        "primary_channel": "transition",
        "transmission_mechanism": "Enabler of clean transition (electric motors, wind gearboxes, grid transformers); negligible carbon liability and highly resilient manufacturing plants.",
        "esg_score_transparency": 9.2,
        "esg_score_controversy_adj": 8.9,
    },
    {
        "ticker": "EMBR3.SA",
        "company_name": "Embraer S.A.",
        "sector": "Industrials",
        "sub_industry": "Aerospace & Industrial Logistics",
        "country": "Brazil",
        "revenue_musd": 5600.0,
        "ebitda_margin": 0.145,
        "market_cap_musd": 4900.0,
        "enterprise_value_musd": 6100.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 180.0,
        "scope2_emis_kt": 548.0,
        "scope12_intensity_tco2_musd": 130.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.55,
        "transition_vulnerability_score": 0.58,
        "primary_channel": "transition",
        "transmission_mechanism": "Sustainable Aviation Fuel (SAF) transition, supply chain logistical bottlenecks, and factory site flood management.",
        "esg_score_transparency": 7.8,
        "esg_score_controversy_adj": 7.2,
    },
    {
        "ticker": "PARAUCO.SN",
        "company_name": "Parque Arauco S.A.",
        "sector": "Real estate",
        "sub_industry": "Commercial & Urban Logistics REIT",
        "country": "Chile",
        "revenue_musd": 1850.0,
        "ebitda_margin": 0.320,
        "market_cap_musd": 2400.0,
        "enterprise_value_musd": 3700.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 9.5,
        "scope2_emis_kt": 194.0,
        "scope12_intensity_tco2_musd": 110.0,
        "scope3_disclosed": False,
        "physical_flood_hazard_score": 0.62,
        "transition_vulnerability_score": 0.28,
        "primary_channel": "physical",
        "transmission_mechanism": "Last-mile distribution hubs and retail logistics assets in Andean urban basins subject to winter atmospheric river flash floods.",
        "esg_score_transparency": 7.1,
        "esg_score_controversy_adj": 6.8,
    },
    {
        "ticker": "ASURB.MX",
        "company_name": "Grupo Aeroportuario del Sureste (ASUR)",
        "sector": "Industrials",
        "sub_industry": "Airport Cargo & Terminal Infrastructure",
        "country": "Mexico",
        "revenue_musd": 2600.0,
        "ebitda_margin": 0.580,
        "market_cap_musd": 5600.0,
        "enterprise_value_musd": 6250.0,
        "benchmark_weight": 0.10,
        "scope1_emis_kt": 115.0,
        "scope2_emis_kt": 380.0,
        "scope12_intensity_tco2_musd": 190.0,
        "scope3_disclosed": True,
        "physical_flood_hazard_score": 0.88,
        "transition_vulnerability_score": 0.45,
        "primary_channel": "physical",
        "transmission_mechanism": "Coastal Caribbean and Gulf air freight terminals highly exposed to tropical cyclone storm surge, sea-level rise, and torrential runway inundation.",
        "esg_score_transparency": 7.4,
        "esg_score_controversy_adj": 6.2,
    }
]

df_holdings = pd.DataFrame(holdings_data)
df_holdings.to_csv(r"exam/data/sample/latin_america_holdings_universe.csv", index=False)
print("Saved latin_america_holdings_universe.csv (10 holdings).")

# 2. Climate Hazard Flood Indicators
hazard_data = []
for h in holdings_data:
    hazard_data.append({
        "ticker": h["ticker"],
        "primary_basin": "Santos / Baixada Santista" if "Brazil" in h["country"] and "RAIL" in h["ticker"] else ("Bajío / Central Valley" if "Mexico" in h["country"] else "Regional Corridors"),
        "copernicus_rx5day_mm": round(float(RNG.uniform(180, 360)), 1),
        "return_period_100yr_precip_mm": round(float(RNG.uniform(320, 520)), 1),
        "elevation_above_sea_level_m": round(float(RNG.uniform(2.5, 750.0)), 1),
        "soil_moisture_saturation_pct": round(float(RNG.uniform(65.0, 92.0)), 1),
        "physical_flood_hazard_score": h["physical_flood_hazard_score"],
        "historical_flood_events_20yr": int(RNG.integers(2, 9)),
        "adaptation_infrastructure_rating": "High" if h["ticker"] in ["FIBRAPL14.MX", "VESTA.MX", "WEGE3.SA"] else ("Medium" if h["ticker"] in ["FUNO11.MX", "EMBR3.SA", "PARAUCO.SN"] else "Low / Vulnerable")
    })
df_hazard = pd.DataFrame(hazard_data)
df_hazard.to_csv(r"exam/data/sample/climate_hazard_flood_indicators.csv", index=False)
print("Saved climate_hazard_flood_indicators.csv.")

# 3. GHG Emissions & Targets Data
emissions_data = []
for h in holdings_data:
    emissions_data.append({
        "ticker": h["ticker"],
        "reporting_year": 2023,
        "scope1_ktco2": h["scope1_emis_kt"],
        "scope2_ktco2": h["scope2_emis_kt"],
        "scope3_ktco2": round(float(h["scope1_emis_kt"] * RNG.uniform(2.5, 8.0)), 1) if h["scope3_disclosed"] else np.nan,
        "scope12_intensity": h["scope12_intensity_tco2_musd"],
        "assurance_level": "Limited Third-Party (EY/KPMG)" if h["scope3_disclosed"] else "Self-Disclosed / Unverified",
        "net_zero_target_year": 2040 if h["ticker"] in ["WEGE3.SA", "FIBRAPL14.MX", "VESTA.MX"] else (2050 if h["ticker"] in ["FUNO11.MX", "CCRO3.SA", "ASURB.MX"] else np.nan),
        "sbti_status": "Validated 1.5C Target" if h["ticker"] in ["WEGE3.SA", "FIBRAPL14.MX"] else ("Committed" if h["ticker"] in ["VESTA.MX", "CCRO3.SA", "FUNO11.MX"] else "No Commitment")
    })
df_emissions = pd.DataFrame(emissions_data)
df_emissions.to_csv(r"exam/data/sample/ghg_emissions_and_targets.csv", index=False)
print("Saved ghg_emissions_and_targets.csv.")

# 4. ESG Scores & Audit Table
esg_data = []
for h in holdings_data:
    esg_data.append({
        "ticker": h["ticker"],
        "esg_score_transparency": h["esg_score_transparency"],
        "esg_score_controversy_adj": h["esg_score_controversy_adj"],
        "divergence": round(abs(h["esg_score_transparency"] - h["esg_score_controversy_adj"]), 2),
        "greenwashing_risk_flag": "High" if abs(h["esg_score_transparency"] - h["esg_score_controversy_adj"]) > 1.8 else ("Moderate" if abs(h["esg_score_transparency"] - h["esg_score_controversy_adj"]) > 0.8 else "Low"),
        "governance_board_oversight": "Board Sustainability Committee" if h["esg_score_transparency"] >= 7.0 else "Management Level Only",
        "executive_comp_linked": True if h["ticker"] in ["WEGE3.SA", "FIBRAPL14.MX", "VESTA.MX"] else False
    })
df_esg = pd.DataFrame(esg_data)
df_esg.to_csv(r"exam/data/sample/esg_constructed_and_reported.csv", index=False)
print("Saved esg_constructed_and_reported.csv.")

# 5. Monte Carlo Flood Loss Simulations for Focal Megahub ($120M Asset)
N_SIMS = 20000
ASSET_VAL_EXAM = 120.0 # MUSD
p_flood_annual = 0.10  # 10-year flood event probability
sev_mean, sev_sigma = 0.28, 0.14

flood_event = (RNG.random(N_SIMS) < p_flood_annual)
gross_severity = np.clip(RNG.normal(sev_mean, sev_sigma, N_SIMS), 0.03, 0.96)
loss_no_action = gross_severity * flood_event * ASSET_VAL_EXAM

ADAPT_ATTEN = 0.45       # Structural engineering reduces damage by 45%
ATTACH_PT = 5.0          # Insurance attachment (deductible)
POLICY_LIMIT = 30.0      # Insurance coverage limit
PREMIUM_ANNUAL = 2.20    # Annual insurance premium

loss_adapted = loss_no_action * (1.0 - ADAPT_ATTEN)
ins_payout_raw = np.clip(loss_no_action - ATTACH_PT, 0, POLICY_LIMIT)
loss_retained_ins = loss_no_action - ins_payout_raw

comb_payout = np.clip(loss_adapted - ATTACH_PT, 0, POLICY_LIMIT)
loss_retained_comb = loss_adapted - comb_payout

df_mc_sample = pd.DataFrame({
    "iteration": np.arange(1, 101),
    "flood_event": flood_event[:100].astype(int),
    "loss_no_action_musd": loss_no_action[:100].round(3),
    "loss_adapted_musd": loss_adapted[:100].round(3),
    "loss_retained_insurance_musd": loss_retained_ins[:100].round(3),
    "loss_retained_combined_musd": loss_retained_comb[:100].round(3),
})
df_mc_sample.to_csv(r"exam/data/sample/focal_logistics_flood_monte_carlo.csv", index=False)
print("Saved focal_logistics_flood_monte_carlo.csv.")

# 6. Green Bond Cashflows & Pricing
FACE_GB, COUPON_GB, YTM_GB, MAT_GB = 100.0, 0.0525, 0.0485, 7
STEP_GB = 0.0025 # 25 bps penalty step-up
GREENIUM_BPS = 8.5 # 8.5 bps pricing advantage

gb_cashflows = []
for t in range(1, MAT_GB + 1):
    c_base = COUPON_GB
    c_step = COUPON_GB + STEP_GB
    cf_base = FACE_GB * c_base if t < MAT_GB else FACE_GB * (1 + c_base)
    cf_step = FACE_GB * c_step if t < MAT_GB else FACE_GB * (1 + c_step)
    df_pv = 1 / ((1 + YTM_GB) ** t)
    gb_cashflows.append({
        "year": t,
        "base_cashflow_usd": cf_base,
        "stepup_cashflow_usd": cf_step,
        "discount_factor": round(df_pv, 4),
        "pv_base_usd": round(cf_base * df_pv, 3),
        "pv_stepup_usd": round(cf_step * df_pv, 3),
        "greenium_savings_usd": round((FACE_GB * (GREENIUM_BPS / 10000.0)) * df_pv, 4)
    })
df_gb = pd.DataFrame(gb_cashflows)
df_gb.to_csv(r"exam/data/sample/green_bond_framework_cashflows.csv", index=False)
print("Saved green_bond_framework_cashflows.csv.")
