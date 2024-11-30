# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:19:47 2024

@author: D21124371
"""

import cv2
import numpy as np
import os

def calculate_overall_mean_a_b(dataset_path):
    total_a_sum = 0
    total_b_sum = 0
    total_pixel_count = 0

    for image_file in os.listdir(dataset_path):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(dataset_path, image_file)
            image = cv2.imread(image_path)

            # تبدیل BGR به Lab
            lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

            # استخراج کانال‌های a* و b*
            a_channel = lab_image[:, :, 1].astype(float) - 128  # تنظیم به بازه [-128, 127]
            b_channel = lab_image[:, :, 2].astype(float) - 128  # تنظیم به بازه [-128, 127]

            # محاسبه مجموع مقادیر a* و b*
            total_a_sum += np.sum(a_channel)
            total_b_sum += np.sum(b_channel)

            # محاسبه تعداد کل پیکسل‌ها
            total_pixel_count += a_channel.size

    # محاسبه میانگین کلی a* و b*
    overall_mean_a = total_a_sum / total_pixel_count if total_pixel_count > 0 else 0
    overall_mean_b = total_b_sum / total_pixel_count if total_pixel_count > 0 else 0
    return overall_mean_a, overall_mean_b

# # مسیر دیتاست
# dataset_path = "path_to_your_dataset"
overall_mean_a, overall_mean_b = calculate_overall_mean_a_b(dataset_path)

print(f"Overall Mean a*: {overall_mean_a}")
print(f"Overall Mean b*: {overall_mean_b}")

