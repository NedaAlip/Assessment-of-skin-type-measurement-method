# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:44:12 2024

@author: D21124371
"""

import pandas as pd
import matplotlib.pyplot as plt





file_path = p1  # path_excel
df = pd.read_excel(file_path)

# اطمینان از وجود ستون‌های ITA و Skin Type
if 'ITA' not in df.columns or 'Skin Type' not in df.columns:
    raise ValueError("The Excel file must contain 'ITA' and 'Skin Type' columns.")

skin_type = 6  #determine the skin type
filtered_df = df[df['Ground Truth'] == skin_type]

# استخراج مقادیر ITA برای نوع پوست انتخاب‌شده
ita_values = filtered_df['ITA'].dropna()

# skin_colors = {
#     'I': '#f1c27d',  # Lightest color
#     'II': '#e0ac69',
#     'III': '#c68642',
#     'IV': '#8d5524',
#     'V': '#654321',  # Intermediate color
#     'VI': '#473b2f'   # Darkest color
# }

# رسم هیستوگرام برای Skin Type = 1
plt.figure(figsize=(8, 6))
plt.hist(ita_values, bins=30, color='#473b2f', edgecolor='black', alpha=0.7)  # determine the color for the skin type
plt.xlabel('ITA Values', fontsize=20)
plt.ylabel('Number of Images', fontsize=20)
#plt.title(f'Skin Type {skin_type}', fontsize=14)

# تنظیم بازه محور افقی
plt.xlim([-70, 100])

# plt.tight_layout()
# plt.show()

plt.ylim([0, 40])
# plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

plt.tick_params(axis='both', which='major', labelsize=14)  # اندازه بزرگ‌تر برای اعداد

plt.tight_layout()
plt.show()