# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:12:07 2024

@author: D21124371
"""

##########ITA_classification_Rays#########
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd  # Import pandas to read Excel sheet
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import math


# Assuming you have your data in an Excel file named 'your_file.xlsx'
excel_file_path = p1
#excel_file_path = p22

# # # Load the data into a Pandas DataFrame
df = pd.read_excel(excel_file_path)
ita_values = df['ITA']

# Function to calculate the end point for the line given an ITA value
def calculate_endpoint(ita, origin, length=45):
    if ita == 0:
        return [origin[0], origin[1] + length]
    else:
        slope = np.tan(np.radians(ita))
        delta_b = length / np.sqrt(1 + slope**2)
        delta_L = slope * delta_b
        return [origin[0] + delta_b, origin[1] + delta_L]

fig, ax = plt.subplots(figsize=(12, 10))
ita_lines = [55, 41, 28, 10, -30]
origin = [0, 50]  # Define the origin

offset = 3  # Define an offset for the y position of the label
for ita in ita_lines:
    end_point = calculate_endpoint(ita, origin)
    if ita == 0:
        # For ita=0, draw a vertical line
        ax.plot([origin[0], origin[0]], [origin[1], end_point[1]], 'k-', linewidth=4, color='black')
    else:
        ax.plot([origin[0], end_point[0]], [origin[1], end_point[1]], 'k-', linewidth=4, color='black')

    # Check if the label is for the -30 degree line and adjust its vertical position
    if ita == -30:
        ax.text(end_point[0], end_point[1] + offset, f'{ita}°', fontsize=20, fontweight='bold',
                verticalalignment='bottom', horizontalalignment='right')
    else:
        ax.text(end_point[0], end_point[1], f'{ita}°', fontsize=20, fontweight='bold',
                verticalalignment='bottom', horizontalalignment='right')
        
ground_truth_markers = {
    'I': 'o',  # Very light skin
    'II': '^', # Light skin
    'III': 's', # Medium skin
    'IV': 'd', # Olive skin
    'V': 'x',  # Brown skin
    'VI': '*'  # Dark brown to black skin
}

##FAA08C
# # # Define a color for each Ground Truth category
ground_truth_colors = {
    'I': '#F0D9B5',  # Very light skin
    'II': '#E0AC69', # Light skin
    'III': '#C68642', # Medium skin
    'IV': '#8D5524', # Olive skin
    'V': '#613318',  # Brown skin
    'VI': '#3E1F00'  # Dark brown to black skin
}


# Plot ITA points for each Ground Truth category with the given color and label
for ground_truth in range(1, 7):  # Ground Truth categories from I to VI
    df_filtered = df[df['Ground Truth'] == ground_truth]
    b_star_values = df_filtered['b'].values
    L_star_values = df_filtered['L'].values
    roman_label = ['I', 'II', 'III', 'IV', 'V', 'VI'][ground_truth - 1]
    ax.scatter(b_star_values, L_star_values, color=ground_truth_colors[roman_label], marker=ground_truth_markers[roman_label], s=50, label=roman_label)
    #ax.scatter(b_star_values, L_star_values, color=ground_truth_colors[roman_label], s=70, label=roman_label, alpha=0.6)  # Adjust alpha as needed


# Set the labels for axes
ax.set_xlabel('b* (chrominance)', fontsize=30)
ax.set_ylabel('L* (lightness)', fontsize=30)

# Set the plot limits
ax.set_xlim(0, 50)
ax.set_ylim(20, 95)

# Set larger tick labels
ax.tick_params(axis='x', labelsize=20)  # Set x-axis tick label size
ax.tick_params(axis='y', labelsize=20)  # Set y-axis tick label size

# Optionally, increase tick width
ax.tick_params(axis='x', width=2)  # Set x-axis tick width
ax.tick_params(axis='y', width=2)  # Set y-axis tick width

# Add a legend to the plot outside of the figure to the right
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=20, markerscale=2)  # Increase fontsize to 14 and markerscale to 2

# # # Adjust the figure so the legend fits outside the plot
# plt.tight_layout()

# # Show the plot
# plt.show()

# # Add a legend to the plot outside of the figure to the right
# ax.legend(
#     loc='upper left', 
#     bbox_to_anchor=(1, 1), 
#     fontsize=20, 
#     markerscale=2, 
#     title='Fitzpatrick Skin Type'  # Add a title to the legend
# )


# Add a legend inside the plot
legend = ax.legend(
    loc='upper right',  # Place the legend inside the plot at the top-right corner
    fontsize=12, 
    markerscale=2, 
    title='DBL'  # Add a title to the legend
)

# تنظیم فونت و اندازه عنوان legend
plt.setp(legend.get_title(), fontsize=22, weight='bold')  # Set font size and weight for the legend title

# حذف tight_layout تا legend بهتر در داخل نمودار جا بگیرد
#plt.tight_layout()

# Show the plot
plt.show()

