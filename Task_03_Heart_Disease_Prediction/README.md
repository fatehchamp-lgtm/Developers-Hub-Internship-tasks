# Heart Disease Risk Prediction using Machine Learning

## 📌 Project Overview
This project focuses on building an automated binary classification model to predict whether a person is at risk of heart disease based on their health indicators and clinical data. The dataset used is the standard **Heart Disease UCI Dataset** from Kaggle, containing 920 clinical records.

---

## 🛠️ Tasks Completed & Methodology

### 1. Advanced Data Preprocessing & Cleaning
* **Handling Missing Strings:** Replaced ambiguous data tags (like `?`) with standard `NaN` values.
* **Safe Categorical Encoding:** Manually mapped key medical text features (`sex`, `cp`, `restecg`, `slope`, `thal`) into ordinal numerical ranges to completely prevent feature loss or dummy columns misalignment.
* **Robust Imputation:** Handled heavy missing counts in structural features (like `ca` and `thal`) using **Median Imputation** to make the dataset 100% compliant with standard Scikit-Learn pipelines.

### 2. Exploratory Data Analysis (EDA)
* Plotted class distribution profiles for target variables to optimize data stratification during data splitting.
* Evaluated Age-group variances against disease risk using density histograms to assess high-risk demographic clusters.

### 3. Predictive Modeling (Classification Pipeline)
The dataset was split using an 80/20 train-test ratio with mandatory target stratification. Two core classification algorithms were implemented and trained:
* **Logistic Regression:** Implemented with scaled iterations (`max_iter=3000`) for statistical baseline modeling.
* **Decision Tree Classifier:** Configured with a controlled depth (`max_depth=5`) to prevent overfitting while capturing non-linear relationships.

### 4. Advanced Evaluation Frameworks
* **Confusion Matrix (CM):** Evaluated both models on diagnostics accuracy metrics (True Positives, False Positives, False Negatives, and True Negatives).
* **ROC-AUC Diagnostics:** Plotted the trade-off curves for True Positive Rate against False Positive Rate. Both models showed exceptional performance convergence with **AUC scores up to 0.81**.

### 5. Feature Importance Analysis
* Extracted empirical feature weights directly from the trained Decision Tree estimator.
* Successfully highlighted **Chest Pain Type (`cp`)** as the primary predicting indicator, closely followed by **Cholesterol Levels (`chol`)** and **Patient Age**.

---

## 📊 Performance Analytics Summary

| Evaluation Metric | Logistic Regression Pipeline | Decision Tree Classifier |
| :--- | :---: | :---: |
| **Testing Accuracy** | 74% | **78%** |
| **Area Under ROC (AUC)** | **0.81** | 0.80 |

---

## 📂 Project Structure
```text
├── data/
│   └── heart.csv                   
├── heart_disease_prediction.ipynb   
└── README.md                       