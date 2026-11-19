import json
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()


nb_path = r'practice\notebooks\practice_capstone_starter.ipynb'
with open(nb_path, encoding='utf-8') as f:
    nb = json.load(f)

# Change cwd to notebooks folder for relative paths
orig_dir = os.getcwd()
os.chdir(r'practice\notebooks')

global_env = {}

print("Executing notebook cells...")
for idx, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        print(f"Executing cell {idx}...")
        try:
            exec(source, global_env)
        except Exception as e:
            print(f"Error in cell {idx}: {e}")
            os.chdir(orig_dir)
            sys.exit(1)

os.chdir(orig_dir)
print("All code cells executed successfully!")
