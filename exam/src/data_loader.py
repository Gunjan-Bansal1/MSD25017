import os
import pandas as pd
import numpy as np

def get_data_paths():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sample_dir = os.path.join(base_dir, "data", "sample")
    processed_dir = os.path.join(base_dir, "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    return sample_dir, processed_dir

def load_holdings_universe():
    sample_dir, _ = get_data_paths()
    fpath = os.path.join(sample_dir, "latin_america_holdings_universe.csv")
    df = pd.read_csv(fpath)
    return df

def load_climate_hazards():
    sample_dir, _ = get_data_paths()
    fpath = os.path.join(sample_dir, "climate_hazard_flood_indicators.csv")
    df = pd.read_csv(fpath)
    return df

def load_emissions_data():
    sample_dir, _ = get_data_paths()
    fpath = os.path.join(sample_dir, "ghg_emissions_and_targets.csv")
    df = pd.read_csv(fpath)
    return df

def load_esg_data():
    sample_dir, _ = get_data_paths()
    fpath = os.path.join(sample_dir, "esg_constructed_and_reported.csv")
    df = pd.read_csv(fpath)
    return df

def build_integrated_panel():
    sample_dir, processed_dir = get_data_paths()
    df_h = load_holdings_universe()
    df_haz = load_climate_hazards()[["ticker", "primary_basin", "copernicus_rx5day_mm", "elevation_above_sea_level_m", "adaptation_infrastructure_rating"]]
    df_emis = load_emissions_data()[["ticker", "scope3_ktco2", "assurance_level", "net_zero_target_year", "sbti_status"]]
    df_esg = load_esg_data()[["ticker", "divergence", "greenwashing_risk_flag", "governance_board_oversight"]]

    panel = df_h.merge(df_haz, on="ticker", how="left")
    panel = panel.merge(df_emis, on="ticker", how="left")
    panel = panel.merge(df_esg, on="ticker", how="left")

    out_path = os.path.join(processed_dir, "clean_climate_financial_panel.csv")
    panel.to_csv(out_path, index=False)
    return panel

if __name__ == "__main__":
    p = build_integrated_panel()
    print(f"Built integrated panel with {len(p)} holdings and {len(p.columns)} features.")

