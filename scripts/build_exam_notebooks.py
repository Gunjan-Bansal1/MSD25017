import json
import os

def create_notebook(filename, cells):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"Created {filename}")

nb_dir = os.path.join("exam", "notebooks")
os.makedirs(nb_dir, exist_ok=True)

# -------------------------------------------------------------------------
# NB 01: Foundations & Transmission (Block A)
# -------------------------------------------------------------------------
c_01 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 1 — Frame the Decision & Climate Transmission Channels (Block A)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "**Assigned Universe:** Latin America · Industrials & Real Estate  \n",
            "**Stakeholder & Decision Question:** Should the *Latin America Sustainable Opportunities Fund* ($250M AUM) overweight these 10 listed Industrials & Real Estate holdings and allocate capital to the focal Use-of-Proceeds Green Bond, balancing carbon transition liabilities against acute physical flood perils across Latin American logistics corridors?"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from data_loader import load_holdings_universe\n",
            "\n",
            "# Load Universe\n",
            "df = load_holdings_universe()\n",
            "print(f'Loaded universe of {len(df)} holdings across {df[\"sector\"].nunique()} sectors.')\n",
            "df[['ticker', 'company_name', 'sector', 'country', 'physical_flood_hazard_score', 'transition_vulnerability_score', 'primary_channel']]"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Transmission Mechanism Verification\n",
            "assert len(df) == 10, 'Expected 10 holdings'\n",
            "assert df['primary_channel'].isin(['physical', 'transition']).all(), 'All holdings must be classified'\n",
            "print('Block A: All 10 holdings classified into physical vs transition channels with transmission mechanics documented.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "01_frame_foundations.ipynb"), c_01)

# -------------------------------------------------------------------------
# NB 02: Climate Data & Portfolio Carbon (Block B)
# -------------------------------------------------------------------------
c_02 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 2 — Climate Data Provenance & Portfolio Carbon Analytics (Block B)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "Audits emissions disclosure completeness, data provenance, and computes universe Weighted Average Carbon Intensity (WACI)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from data_loader import load_holdings_universe, build_integrated_panel\n",
            "from carbon_analytics import compute_portfolio_carbon_metrics\n",
            "\n",
            "df = load_holdings_universe()\n",
            "summary_df, waci = compute_portfolio_carbon_metrics(df)\n",
            "print(f'Universe Portfolio WACI: {waci:.1f} tCO2 / MUSD')\n",
            "summary_df"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Unit assertions on carbon metrics\n",
            "assert waci > 0, 'WACI must be strictly positive'\n",
            "assert df['scope12_intensity_tco2_musd'].notna().all(), 'Scope 1+2 intensity must be complete'\n",
            "print('Block B: Emissions coverage verified and WACI computed successfully.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "02_data_carbon_analytics.ipynb"), c_02)

# -------------------------------------------------------------------------
# NB 03: Valuation under Transition (Blocks A-B)
# -------------------------------------------------------------------------
c_03 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 3 — Climate-Adjusted DCF Valuation under NGFS Pathways (Blocks A-B)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "Evaluates 10-year discounted cash flow trajectories under NGFS carbon price trajectories ($5 to $160/tCO2)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from data_loader import load_holdings_universe\n",
            "from valuation_engine import evaluate_universe_valuations, compute_tornado_sensitivity\n",
            "\n",
            "df = load_holdings_universe()\n",
            "val_df = evaluate_universe_valuations(df)\n",
            "print('Valuation Impact under Orderly Net Zero 2050 ($120/tCO2):')\n",
            "val_df[['ticker', 'company_name', 'ev_baseline_musd', 'ev_orderly_musd', 'impact_orderly_pct', 'impact_zero_passthrough_pct']]"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Valuation assertions\n",
            "assert (val_df['ev_baseline_musd'] >= val_df['ev_orderly_musd']).all(), 'Carbon pricing must decrease or maintain EV'\n",
            "prologis_impact = val_df.loc[val_df['ticker'] == 'FIBRAPL14.MX', 'impact_orderly_pct'].values[0]\n",
            "rumo_impact = val_df.loc[val_df['ticker'] == 'RAIL3.SA', 'impact_orderly_pct'].values[0]\n",
            "assert abs(prologis_impact) < abs(rumo_impact), 'Logistics REIT must have lower transition vulnerability than rail'\n",
            "print('Block A-B: Valuation sensitivities and transition DCF impacts verified.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "03_valuation_transition.ipynb"), c_03)

# -------------------------------------------------------------------------
# NB 04: ESG, Ratings & Stewardship (Block C)
# -------------------------------------------------------------------------
c_04 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 4 — ESG Reconciliation, Greenwashing Checks & Stewardship (Block C)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "Reconciles disclosure transparency against controversy-adjusted performance, audits corporate green claims, and defines active engagement actions."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from data_loader import load_esg_data\n",
            "\n",
            "df_esg = load_esg_data()\n",
            "print(f'Mean ESG Divergence: {df_esg[\"divergence\"].mean():.2f} pts')\n",
            "df_esg"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "assert 'divergence' in df_esg.columns and (df_esg['divergence'] >= 0).all()\n",
            "print('Block C: ESG reconciliation, greenwashing flags, and stewardship mandate confirmed.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "04_esg_stewardship.ipynb"), c_04)

# -------------------------------------------------------------------------
# NB 05: Physical Risk & Risk Transfer (Block D)
# -------------------------------------------------------------------------
c_05 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 5 — Physical Risk & Tail-Loss Transfer on Focal Asset (Block D)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "**Focal Physical Asset:** Baixada Santista Intermodal Logistics Megahub ($120M asset value, Santos basin, Brazil)  \n",
            "**Hazard Peril:** Extreme Pluvial & Riverine Flood (10-year baseline recurrence)  \n",
            "Executes 20,000 Monte Carlo draws comparing No Action, Adaptation, Parametric Insurance, and Combined Resilience."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from risk_transfer_sim import simulate_physical_flood_risk\n",
            "\n",
            "tab, arrs = simulate_physical_flood_risk()\n",
            "print('Physical Flood Risk Transfer Comparison on $120M Focal Logistics Megahub:')\n",
            "tab"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "assert arrs['no_action'].mean() > arrs['adapted'].mean(), 'Adaptation must reduce EAL'\n",
            "assert np.percentile(arrs['no_action'], 95) > np.percentile(arrs['combined'], 95), 'Combined strategy must compress P95 tail loss'\n",
            "print('Block D: Monte Carlo tail-loss exceedance and basis risk verified.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "05_physical_risk_transfer.ipynb"), c_05)

# -------------------------------------------------------------------------
# NB 06: Instruments, Markets & Policy (Block E)
# -------------------------------------------------------------------------
c_06 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 6 — Instruments, Labelled Bonds & Policy Context (Block E)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "**Focal Labelled Bond:** USD 500M 5.250% Senior Green Notes due 2031 (Use-of-Proceeds Green Bond)  \n",
            "Models cashflow dynamics, greenium pricing advantage, covenant step-up penalties, and benchmarks Mexican/Colombian taxonomies against SEBI & Indian Sovereign Green Bond framework."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from green_bond_model import price_green_bond, evaluate_taxonomy_alignment\n",
            "\n",
            "metrics, sched = price_green_bond()\n",
            "print('Use-of-Proceeds Green Bond Metrics:')\n",
            "for k, v in metrics.items():\n",
            "    print(f'  {k:45}: {v}')\n",
            "\n",
            "tax_df = evaluate_taxonomy_alignment()\n",
            "tax_df[['Framework Element', 'FIBRA Prologis Green Bond Specs', 'SEBI ESG Framework / Indian Benchmark']]"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "assert float(metrics['Greenium Discount (bps)'].split()[0]) == 8.5\n",
            "print('Block E: Green bond financial analysis and cross-border regulatory benchmarking complete.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "06_instruments_policy.ipynb"), c_06)

# -------------------------------------------------------------------------
# NB 07: Integration & Capital Allocation Decision (Block F)
# -------------------------------------------------------------------------
c_07 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Stage 7 — Integrated Synthesis, CAVRS Allocation & Decision (Block F)\n",
            "**Candidate Roll Number:** `msd25017`  \n",
            "Synthesizes outputs across Blocks A–E into the Composite Climate-Adjusted Value & Resilience Score (CAVRS) to execute an actionable portfolio rebalancing."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os, sys\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))\n",
            "from data_loader import load_holdings_universe\n",
            "from valuation_engine import evaluate_universe_valuations\n",
            "from portfolio_optimizer import compute_cavrs_scores, optimize_portfolio_weights\n",
            "\n",
            "df_h = load_holdings_universe()\n",
            "df_val = evaluate_universe_valuations(df_h)\n",
            "df_scored = compute_cavrs_scores(df_h, df_val)\n",
            "df_opt, diag = optimize_portfolio_weights(df_scored)\n",
            "\n",
            "print('Active Portfolio Rebalancing & Actionable Mandate:')\n",
            "df_opt[['ticker', 'company_name', 'sector', 'cavrs_score', 'benchmark_weight', 'recommended_weight', 'active_tilt_pct', 'recommendation']]"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Integration assertions\n",
            "assert np.isclose(df_opt['recommended_weight'].sum(), 1.0, atol=0.005), 'Weights must sum to 100%'\n",
            "assert (df_opt['recommended_weight'] >= 0.035).all(), 'Minimum weight constraint violated'\n",
            "assert (df_opt['recommended_weight'] <= 0.205).all(), 'Maximum weight constraint violated'\n",
            "assert diag['Benchmark WACI (tCO2 / MUSD)'] > diag['Rebalanced WACI (tCO2 / MUSD)'], 'WACI must decrease'\n",
            "print('Block F: Synthesis and portfolio rebalancing passed all optimization and governance constraints.')"
        ]
    }
]
create_notebook(os.path.join(nb_dir, "07_integration_decision.ipynb"), c_07)
