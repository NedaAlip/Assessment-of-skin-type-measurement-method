# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:15:16 2024

@author: D21124371
"""


import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, accuracy_score

p4 = 'C:/Users/d21124371/OneDrive - Technological University Dublin/Documents/Review_paper/ITA_my/similar_samples/ita_paper_result/results_20240422_patch7_mean_neda_7.xlsx'

# Load your Excel sheet into a DataFrame
df = pd.read_excel(p4)

# Assuming the columns are named 'Computer_Classification' and 'Human_Classification'
image_numbers = df['Image']
ground_truth_labels = df['Ground Truth']
predicted_labels = df['Skin Type']

# Create a confusion matrix
conf_matrix = confusion_matrix(ground_truth_labels, predicted_labels)

# Calculate accuracy
accuracy = accuracy_score(ground_truth_labels, predicted_labels)

# Print confusion matrix and accuracy
print("Confusion Matrix:")
print(conf_matrix)
print("\nAccuracy:", accuracy)

# Define a mapping from integers to Roman numerals
roman_labels = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI'}

# Replace the integer labels with Roman numerals
roman_xticks = [roman_labels[i] for i in range(1, 7)]
roman_yticks = [roman_labels[i] for i in range(1, 7)]

# Display confusion matrix using a heatmap
sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', xticklabels=roman_xticks, yticklabels=roman_yticks)
plt.xlabel('ITA-based Classification')
plt.ylabel('Dermatologist-based Classification')
plt.tight_layout()
plt.show()