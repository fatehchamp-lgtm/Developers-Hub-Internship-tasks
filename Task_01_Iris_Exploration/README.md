# Task 01: Iris Dataset Exploratory Data Analysis (EDA)

## 1. Task Objective
The objective of this task is to perform an Exploratory Data Analysis (EDA) on the Iris dataset to understand structural distributions, feature relationships, and spot anomalies before applying Machine Learning classification algorithms.

## 2. Dataset Used
* **Dataset Name:** Fisher's Iris Dataset
* **Total Instances:** 150 samples (50 Setosa, 50 Versicolor, 50 Virginica)
* **Features:** `sepal_length`, `sepal_width`, `petal_length`, `petal_width`
* **Target Label:** `species`

## 3. Models Applied
* **Phase 1 (Current):** Statistical Data Profiling & Visual Analytics using `matplotlib` and `seaborn`. No machine learning models applied yet (as per Task 1 EDA requirements).

## 4. Key Results and Findings
* **Linear Separability:** The *Petal Length vs Width* scatter plot highlights that `setosa` forms a highly concentrated, isolated cluster completely separate from the other species, making it linearly separable.
* **Feature Overlap Challenge:** The *Sepal Length vs Width* plot reveals a high density cloud where `versicolor` and `virginica` overlap heavily, indicating that sepal dimensions are weaker predictor features on their own.
* **Anomalies & Outliers:** The *Sepal Width Box Plot* successfully flags distinct statistical outliers within the data.