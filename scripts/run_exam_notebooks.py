import json
import os
import sys

nb_dir = os.path.join("exam", "notebooks")
notebooks = [
    "01_frame_foundations.ipynb",
    "02_data_carbon_analytics.ipynb",
    "03_valuation_transition.ipynb",
    "04_esg_stewardship.ipynb",
    "05_physical_risk_transfer.ipynb",
    "06_instruments_policy.ipynb",
    "07_integration_decision.ipynb"
]

orig_dir = os.getcwd()
os.chdir(nb_dir)

for nb_file in notebooks:
    print(f"Executing {nb_file}...")
    with open(nb_file, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    global_env = {"__file__": os.path.abspath(nb_file)}
    
    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            try:
                exec(source, global_env)
            except Exception as e:
                print(f"Error in {nb_file} cell {idx}: {e}")
                os.chdir(orig_dir)
                sys.exit(1)

os.chdir(orig_dir)
print("All 7 exam notebooks executed successfully!")
