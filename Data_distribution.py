# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:14:21 2024

@author: D21124371
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the number of bins for the histogram
num_bins = 40  # Adjust the number of bins if needed

# Define colors for each Fitzpatrick skin type
skin_colors = {
    'I': '#f1c27d',  # Lightest color
    'II': '#e0ac69',
    'III': '#c68642',
    'IV': '#8d5524',
    'V': '#654321',  # Intermediate color
    'VI': '#473b2f'   # Darkest color
}


histogram_data = {
    'VI': 3,
    'V': 12,
    'IV': 46,
    'III': 277,
    'II': 472,
    'I': 110
}
# Reverse the order of skin types and their corresponding data
skin_types = list(histogram_data.keys())[::-1]  # Reverse the order of Roman numerals
frequencies = list(histogram_data.values())[::-1]  # Reverse the corresponding frequencies

# Create the histogram
plt.figure(figsize=(10, 6))
bars = plt.bar(skin_types, frequencies, color=[skin_colors[st] for st in skin_types])

# Adding labels and title
plt.xlabel('Fitzpatrick Skin Type', fontsize=22)
plt.ylabel('Number of Images', fontsize=22)

# Customize ticks and axis
plt.tick_params(axis='both', which='major', labelsize=15)

# # Adding legend
#plt.legend(bars, [f"Skin Type {st}" for st in skin_types], title='Fitzpatrick Skin Type',
            # fontsize=18, title_fontsize='15')

# Reverse the x-axis direction
plt.gca().invert_xaxis()

# Show the plot
plt.tight_layout()
plt.show()