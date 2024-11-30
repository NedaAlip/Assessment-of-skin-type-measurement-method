# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:01:33 2024

@author: D21124371
"""

################ITA classification#############
import os
from skimage import io, color
import numpy as np
from sklearn.cluster import KMeans
import math
import pandas as pd

def find_dominant_color(image_path):
    # Load the RGB image
    rgb_image = io.imread(image_path)
    
    # Convert the RGB image to Lab color space
    lab_image = color.rgb2lab(rgb_image)
    
    # Flatten the image to get array of Lab color values
    lab_pixels = lab_image.reshape(-1, 3)
    
    # Calculate mean Lab color
    mean_Lab = np.mean(lab_pixels, axis=0)
    L_1, a_1, b_1 = mean_Lab
    
    # Use absolute value of b
    # abs_b_1 = abs(b_1)
    
    # Calculate ITA angle using the absolute value of b
    ita_1 = np.arctan((L_1 - 50) / b_1) * (180 / math.pi)

    # Map ITA angle to Fitzpatrick skin types
    if ita_1 > 55:
        skin_type = "1"
    elif 41 < ita_1 <= 55:
        skin_type = "2"
    elif 28 < ita_1 <= 41:
        skin_type = "3"
    elif 10 < ita_1 <= 28:
        skin_type = "4"
    elif -30 < ita_1 <= 10:
        skin_type = "5"
    elif ita_1 <= -30:
        skin_type = "6"
    else:
        skin_type = "Unknown"

    return skin_type, ita_1, L_1, b_1

# Provide the path to the directory containing your images
image_directory = 'path_path'

# Get a list of image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# # Create an empty DataFrame to store the results
result_df = pd.DataFrame(columns=['Image', 'Skin Type', 'ITA', 'L', 'b'])

# List to store 'abs(b_1)' values
abs_b_values = []

# Loop through each image file
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(image_directory, image_file)

    # Find the dominant color and skin type for the current image
    skin_type, ita, L, b_1 = find_dominant_color(image_path)

    # Append the results to the DataFrame
    result_df = result_df.append({'Image': image_file, 'Skin Type': skin_type, 'ITA': ita, 'L*': L, 'b*': b_1}, ignore_index=True)
    
    # Append 'abs(b_1)' value to the list
    abs_b_values.append(b_1)

# Save the DataFrame to an Excel file
excel_file_path = 'C:/Users/d21124371/OneDrive - Technological University Dublin/Documents/Review_paper/ITA_my/similar_samples/ita_paper_result/Jun_2024_neda_10.xlsx'
result_df.to_excel(excel_file_path, index=False)

