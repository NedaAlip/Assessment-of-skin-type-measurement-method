# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:19:01 2024

@author: D21124371
"""

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# مسیر فولدر شامل تصاویر
image_folder = dataset_path  # Replace with your folder path

# لیست برای ذخیره مقادیر L* (بر حسب پیکسل و بر حسب تصاویر)
l_values_pixels = []
l_values_images = []

# خواندن تصاویر از فولدر
for image_file in os.listdir(image_folder):
    # بررسی فرمت تصویر
    if image_file.endswith(('.jpg', '.png', '.jpeg')):
        # خواندن تصویر
        img_path = os.path.join(image_folder, image_file)
        img = cv2.imread(img_path)

        # تبدیل تصویر به فضای رنگی Lab
        lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

        # استخراج کانال L* (روشنایی)
        l_channel = lab_img[:, :, 0] * (100 / 255)  # L* channel

        # ذخیره مقادیر L* برای هیستوگرام بر حسب پیکسل
        l_values_pixels.extend(l_channel.flatten())

        # محاسبه میانگین L* برای هر تصویر
        mean_l = np.mean(l_channel)
        l_values_images.append(mean_l)

# # هیستوگرام بر حسب پیکسل
plt.figure(figsize=(10, 6))
plt.hist(l_values_pixels, bins=50, color='#f1c27d', edgecolor='black', alpha=0.7)
plt.xlabel(r"$L^*$ (lightness)", fontsize=14)
plt.ylabel("Frequency (Pixel Count)", fontsize=14)
#plt.title(r"Histogram of $L^*$ Values (Pixel-Level)", fontsize=16)
plt.tight_layout()
plt.show()

