
# **Assessment of Skin Type Measurement Method**

This repository contains scripts for analyzing and classifying skin patch image datasets based on ITA (Individual Typology Angle) and Fitzpatrick skin types. The following sections provide an overview of the purpose, execution order, and functionality of the scripts included in this project.

---

## **Contents**
1. [Overview](#overview)
2. [Execution Order](#execution-order)
3. [File Descriptions](#file-descriptions)
4. [Example Usage](#example-usage)
5. [Notes](#notes)

---

## **Overview**
This project evaluates the use of ITA for skin type classification by analyzing luminance and chrominance properties of skin patch datasets. The scripts in this repository provide tools for:
- Classifying skin types based on ITA values.
- Analyzing luminance (`L*`) and chrominance (`a*`, `b*`) distributions.
- Generating histograms, data distribution plots, and confusion matrices for performance evaluation.

---

## **Execution Order**
1. **Preprocessing:**
   - Run `L_distribution.py` and `chrominance_distribution.py` to analyze luminance and chrominance distributions.
2. **Classification:**
   - Use `ITA_classification.py` to classify the dataset and generate an output `.xlsx` file.
3. **Analysis:**
   - Use the `.xlsx` file with `ITA_classification_Rays.py`, `ITA_histogram.py`, and `Confusion_matrix.py` for detailed analysis.
4. **Data Distribution:**
   - Run `Data_distribution.py` to visualize dataset distribution across skin types.

---

## **File Descriptions**
| **Script**                     | **Purpose**                                                                                          | **Input**                                | **Output**                              |
|--------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|
| `L_distribution.py`            | Analyzes the distribution of luminance (`L*`) values.                                                | Dataset path                             | Luminance distribution results           |
| `chrominance_distribution.py`  | Analyzes the distribution of chrominance (`a*`, `b*`) values.                                        | Dataset path                             | Chrominance distribution results         |
| `ITA_classification.py`        | Classifies skin patches into Fitzpatrick skin types based on ITA values.                            | Dataset path                             | `.xlsx` file with classification results |
| `ITA_classification_Rays.py`   | Processes the `.xlsx` file to analyze classification using ITA rays.                                | `.xlsx` file from `ITA_classification.py`| Processed classification results         |
| `ITA_histogram.py`             | Generates histograms to visualize ITA distribution.                                                 | `.xlsx` file from `ITA_classification.py`| ITA histograms                           |
| `Data_distribution.py`         | Visualizes dataset distribution across Fitzpatrick skin types.                                      | Dataset path                             | Data distribution plots                  |
| `Confusion_matrix.py`          | Generates confusion matrix to evaluate classification performance.                                  | `.xlsx` file from `ITA_classification.py`| Confusion matrix plots                   |

---

## **Example Usage**
### **1. Preprocessing**
```bash
python L_distribution.py --dataset_path "path_to_dataset"
python chrominance_distribution.py --dataset_path "path_to_dataset"
```

### **2. Classification**
```bash
python ITA_classification.py --dataset_path "path_to_dataset"
```

### **3. Analysis**
```bash
python ITA_classification_Rays.py --input_file "output_classification.xlsx"
python ITA_histogram.py --input_file "output_classification.xlsx"
python Confusion_matrix.py --input_file "output_classification.xlsx"
```

### **4. Data Distribution**
```bash
python Data_distribution.py --dataset_path "path_to_dataset"
```

---

## **Notes**
- **Dataset Requirements:** Ensure the dataset contains skin patch images in `.png`, `.jpg`, or `.jpeg` format.
- **File Outputs:** All generated files will be saved in the same directory unless specified otherwise.
- **Dependencies:** This project uses Python libraries such as `NumPy`, `Pandas`, `Matplotlib`, and `OpenCV`. Install them using:
  ```bash
  pip install numpy pandas matplotlib opencv-python
  ```
- **Reproducibility:** Make sure to use the specified order of execution for accurate results.
- **License:** [MIT License](LICENSE)

---
