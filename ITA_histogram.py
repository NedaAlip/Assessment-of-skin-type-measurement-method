# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:16:43 2024

@author: D21124371
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the number of bins for the histogram
num_bins = 40  # Adjust the number of bins as needed for your dataset


p4='path'
# Load your Excel sheet into a DataFrame
df = pd.read_excel(p4)

# Assuming the columns are named 'Computer_Classification' and 'Human_Classification'
image_numbers = df['Image']
ground_truth_labels = df['Ground Truth']
predicted_labels = df['Skin Type']


# Manually picked colors from the Fitzpatrick skin types using Roman numerals
skin_colors = {
    'I': '#f1c27d',  # Lightest color
    'II': '#e0ac69',
    'III': '#c68642',
    'IV': '#8d5524',
    'V': '#654321',  # Intermediate color
    'VI': '#473b2f'   # Darkest color
}

# Create the histogram
plt.figure(figsize=(10, 6))

# Initialize a list to hold the histogram data for each skin type
hist_data = []
labels = []  # List to hold the legend labels for the histogram

# Plot a histogram for each skin type
for skin_type in sorted(skin_colors.keys()):
    # Select ITA values for the current skin type (map Roman numeral back to integer if needed)
    ita_values = df[df['Ground Truth'] == list(skin_colors.keys()).index(skin_type) + 1]['ITA']
    # Collect the data for the histogram
    hist_data.append(ita_values)
    # Append the label for the legend
    labels.append(f'Skin Type {skin_type}')

# Plot the stacked histogram
n, bins, patches = plt.hist(hist_data, bins=num_bins, stacked=True,
                            color=[skin_colors[x] for x in sorted(skin_colors.keys())], label=labels)

# Adding labels and title
plt.xlabel('ITA Values', fontsize=22)
plt.ylabel('Number of Images', fontsize=22)

# Adding legend
plt.legend(title='Fitzpatrick Skin Type', fontsize=18, title_fontsize='15')

# Show the plot
plt.tight_layout()
plt.show()