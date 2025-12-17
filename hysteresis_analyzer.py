# A script i developed to get energy descipation per cycle.
# A one click process for no matter how many cycles you have to process
# WhatsApp: Https://wa.me/+923440907874 or +923440907874

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz

# Load the Excel file
file_name = "GlobalResponse_FDCurve.xlsx"
df = pd.read_excel(file_name, sheet_name=0)  # Read first sheet

displacement = df.iloc[:, 0]  # First column (Displacement)
force = df.iloc[:, 1]  # Second column (Force)

# Identify full cycles based on displacement reversals and crossings
cycle_indices = []
start_idx = 0

for i in range(1, len(displacement) - 1):
    # Detect when the displacement returns to a similar value after a full excursion
    if i > start_idx and np.sign(displacement[i]) != np.sign(displacement[i - 1]):
        if start_idx != 0 and np.sign(displacement[i]) == np.sign(displacement[start_idx]):
            cycle_indices.append((start_idx, i))
            start_idx = i  # Start new cycle
        elif start_idx == 0:
            start_idx = i  # Initialize first cycle start

# Create output directories
output_dir = "Splitted Cycles"
plot_dir = "Splitted Cycles/Plots"
area_dir = "Splitted Cycles/Areas"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(plot_dir, exist_ok=True)
os.makedirs(area_dir, exist_ok=True)

# Save each cycle separately
for i, (start, end) in enumerate(cycle_indices):
    cycle_df = df.iloc[start:end + 1]
    cycle_df.to_csv(f"{output_dir}/cycle_{i+1}.csv", index=False)
    
    # Calculate the area enclosed by the cycle (Energy Dissipation)
    area = abs(trapz(cycle_df.iloc[:, 1], cycle_df.iloc[:, 0]))
    with open(f"{area_dir}/cycle_{i+1}_area.txt", "w") as f:
        f.write(f"Energy Dissipation (Area) for Cycle {i+1}: {area:.2f} kN.mm\n")
    
    # Plot and save
    plt.figure()
    plt.plot(cycle_df.iloc[:, 0], cycle_df.iloc[:, 1], linestyle='-')
    
    # Connect start and end points
    plt.plot([cycle_df.iloc[0, 0], cycle_df.iloc[-1, 0]],
             [cycle_df.iloc[0, 1], cycle_df.iloc[-1, 1]],
             linestyle='--', color='red', label='Start-End Connection')
    
    # Add area text annotation
    plt.text(np.mean(cycle_df.iloc[:, 0]), np.mean(cycle_df.iloc[:, 1]),
             f"Area: {area:.2f} kN.mm", fontsize=12, color='blue',
             bbox=dict(facecolor='white', alpha=0.6))
    
    plt.xlabel("Displacement (mm)")
    plt.ylabel("Force (kN)")
    plt.title(f"Control Model - Cycle {i+1}")
    plt.grid()
    plt.legend()
    plt.savefig(f"{plot_dir}/cycle_{i+1}.png")
    plt.close()

print(f"{len(cycle_indices)} full cycles have been saved in '{output_dir}' folder along with their plots in '{plot_dir}'.")
print(f"Energy dissipation values are stored in '{area_dir}'.")
