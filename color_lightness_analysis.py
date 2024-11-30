# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:21:00 2024

@author: D21124371
"""

import pandas as pd
import matplotlib.pyplot as plt

# Data from the provided table
data = {
    "Type": ["I", "II", "III", "IV", "V", "VI"],
    "Mean H": [26.03, 19.73, 23.89, 20.16, 12.30, 13.48],
    "Mean V": [186.37, 185.11, 172.18, 176.28, 178.07, 127.68],
    "Mean Y": [159.64, 162.33, 150.92, 161.99, 156.46, 101.29],
    "Mean Cb": [146.95, 144.14, 143.02, 138.12, 143.42, 146.85],
    "Mean Cr": [111.10, 114.74, 115.07, 117.67, 115.17, 108.92],
    "Mean L": [65.469, 66.342, 62.055, 66.420, 64.176, 42.813],
    "Mean a": [10.132, 8.826, 8.11, 4.495, 8.419, 9.920],
    "Mean b": [16.838, 13.053, 2.894, 10.293, 12.782, 20.674]
}

# # Create a DataFrame
df = pd.DataFrame(data)


# فرض بر این است که DataFrame شما به نام df تعریف شده است
# ابتدا نام ستون‌ها را تغییر می‌دهیم
df.rename(columns={
    'Mean L': 'Mean L*',
    'Mean a': 'Mean a*',
    'Mean b': 'Mean b*'
}, inplace=True)

# Plot 1: Showing Mean V, Mean Y, and Mean L* with custom colors
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x='Type', y=['Mean V', 'Mean Y', 'Mean L*'], kind='bar', ax=ax, color=['#f1c27d', '#8d5524', '#654321'])

# Add labels and title for the first plot with larger font sizes
ax.set_xlabel('Fitzpatrick Skin Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Mean Lightness Values', fontsize=14, fontweight='bold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0, ha='right', fontsize=12)

# Increase font size of y-axis labels
ax.tick_params(axis='y', labelsize=12)

# Show plot
plt.tight_layout()
plt.show()

# Plot 2: Showing Mean H, Mean Cb, Mean Cr, Mean a*, Mean b* with custom colors
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x='Type', y=['Mean H', 'Mean Cb', 'Mean Cr', 'Mean a*', 'Mean b*'], kind='bar', ax=ax, color=['#e0ac69', '#c68642', '#8d5524', '#f1c27d', '#473b2f'])

# Add labels and title for the second plot with larger font sizes
ax.set_xlabel('Fitzpatrick Skin Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Mean Color Values', fontsize=14, fontweight='bold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0, ha='right', fontsize=12)

# Increase font size of y-axis labels
ax.tick_params(axis='y', labelsize=12)

# Show plot
plt.tight_layout()
plt.show()