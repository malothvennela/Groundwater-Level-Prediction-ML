# Groundwater Level Prediction Using Machine Learning

## Title

**Groundwater Level Prediction Using Machine Learning**

## Abstract

Groundwater is an important natural resource used for drinking water, agriculture, and daily needs. Groundwater levels vary due to rainfall, temperature, seasonal changes, and environmental conditions. This project develops a machine learning-based groundwater level prediction system using rainfall and temperature data.

Rainfall and temperature data were collected from IMD using `imdlib`, and groundwater level data was extracted from a Telangana Ground Water Department PDF report. The data was cleaned, processed, merged, and used to train machine learning regression models. Random Forest, Gradient Boosting, and XGBoost models were trained and compared. XGBoost Regressor achieved the best performance. A Streamlit web application was also developed for interactive groundwater level prediction.

## 1. Introduction

Groundwater is one of the major sources of water for domestic, agricultural, and industrial use. In many regions, groundwater availability depends on rainfall, temperature, seasonal patterns, and human usage. Monitoring and predicting groundwater levels can help in better water resource management and planning.

In this project, rainfall and temperature are used as main input features to predict groundwater level. The project follows a complete machine learning workflow from data collection to model deployment using a Streamlit web application.

## 2. Problem Statement

Groundwater levels are changing due to rainfall variation, temperature changes, seasonal conditions, and increasing water demand. Groundwater data is often available in reports, but it is not always directly usable for machine learning.

The problem is to develop a system that can process rainfall, temperature, and groundwater data and predict groundwater level using machine learning techniques.

## 3. Objectives

The main objectives of this project are:

- To collect rainfall, temperature, and groundwater level data.
- To extract groundwater data from PDF reports.
- To clean and preprocess the datasets.
- To merge rainfall, temperature, and groundwater data district-wise.
- To perform exploratory data analysis.
- To train and compare machine learning regression models.
- To evaluate models using R2 Score, MAE, and RMSE.
- To build a Streamlit web application for groundwater level prediction.

## 4. Dataset Description

### 4.1 Rainfall Data

Rainfall data was downloaded from IMD using `imdlib`.

- Source: IMD
- Duration: 2015 to 2024
- Feature used: Rainfall in mm

### 4.2 Temperature Data

Temperature data was also downloaded from IMD using `imdlib`.

- Source: IMD
- Duration: 2015 to 2024
- Features used: Maximum temperature, minimum temperature, and average temperature

### 4.3 Groundwater Level Data

Groundwater data was extracted from a Telangana Ground Water Department PDF report.

- Source: Telangana Ground Water Department report
- Section used: Annexure-III
- Table used: Depth to Water Level in March 2026
- Unit: m bgl, meters below ground level

## 5. Project Structure

```text
Groundwater_Level_Prediction/
├── app.py
├── FINAL_PROJECT_DOCUMENTATION.md
├── FINAL_REPORT.md
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── outputs/
└── src/
```

## 6. Methodology

The methodology followed in this project is:

```text
Dataset Collection
       ↓
Data Extraction
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Machine Learning Model Training
       ↓
Model Evaluation
       ↓
Streamlit Web Application
       ↓
Groundwater Prediction
```

## 7. Data Preprocessing

The preprocessing steps include:

- Inspecting dataset formats.
- Extracting PDF tables using Python.
- Cleaning groundwater table values.
- Standardizing district names.
- Converting IMD gridded data into Telangana district-wise values.
- Merging rainfall, temperature, and groundwater data.

Final dataset:

```text
data/processed/final_groundwater_imd_march_2026.csv
```

Final dataset columns:

```text
date
district
rainfall
temperature
tmax
tmin
groundwater_level
number_of_wells
minimum_depth_m_bgl
maximum_depth_m_bgl
```

## 8. Exploratory Data Analysis

EDA was performed to understand rainfall, temperature, and groundwater relationships.

### 8.1 District-wise Groundwater Level

This graph compares groundwater depth across districts.

Image:

```text
outputs/strong_district_groundwater_ranking.png
```

### 8.2 Rainfall vs Groundwater Level

This graph shows the relationship between rainfall and groundwater level.

Image:

```text
outputs/strong_rainfall_vs_groundwater.png
```

### 8.3 Temperature vs Groundwater Level

This graph shows the relationship between temperature and groundwater level.

Image:

```text
outputs/strong_temperature_vs_groundwater.png
```

### 8.4 Correlation Heatmap

The correlation heatmap shows the relationship between numerical features.

Image:

```text
outputs/strong_correlation_heatmap.png
```

## 9. Feature Engineering

The model uses the following input features:

- Rainfall
- Temperature
- District
- Year
- Month
- Season

Target variable:

```text
groundwater_level
```

## 10. Models Used

The following regression models were trained:

1. Random Forest Regressor
2. Gradient Boosting Regressor
3. XGBoost Regressor

Regression models were used because groundwater level is a continuous numerical value.

## 11. Model Evaluation

The models were evaluated using:

- R2 Score
- MAE
- RMSE

### Model Comparison

| Model | R2 Score | MAE | RMSE |
|---|---:|---:|---:|
| XGBoost Regressor | 0.5918 | 1.3848 | 1.6042 |
| Gradient Boosting Regressor | 0.4434 | 1.6422 | 1.8732 |
| Random Forest Regressor | 0.4411 | 1.7100 | 1.8770 |

Best model:

```text
XGBoost Regressor
```

Saved model:

```text
models/best_groundwater_model.joblib
```

## 12. Feature Importance

Feature importance was generated from the best model to understand which input features influenced the prediction.

Image:

```text
outputs/strong_feature_importance.png
```

## 13. Actual vs Predicted Output

An actual vs predicted graph was generated to compare model predictions with actual groundwater level values.

Image:

```text
outputs/strong_actual_vs_predicted.png
```

## 14. Prediction Example

Example command:

```powershell
py -3.10 src/predict.py --rainfall 50 --temperature 30 --district Hyderabad --date 2026-03-01
```

Output:

```text
Predicted groundwater level: 9.581
```

Meaning:

```text
The predicted groundwater level is 9.581 meters below ground level.
```

## 15. Streamlit Web Application

A Streamlit web application was developed for user-friendly prediction.

The user can enter:

- District
- Prediction date
- Rainfall
- Temperature

The app displays:

- Predicted groundwater level
- Model accuracy
- EDA graphs
- District-wise analysis
- Feature importance
- Project information

Run command:

```powershell
py -3.10 -m streamlit run app.py
```

Local URL:

```text
http://localhost:8501
```

## 16. Limitations

- Groundwater data currently contains only March 2026 district-level values.
- The dataset has 33 district-level groundwater rows.
- IMD rainfall and temperature data was downloaded up to 2024.
- March 2024 weather values were used as a fallback for March 2026 groundwater data.
- The current system is a working prototype, not a final scientific production model.

## 17. Future Scope

Future improvements include:

- Collecting groundwater data for multiple months and years.
- Using matching rainfall and temperature data for the same time period.
- Adding soil type, elevation, land use, irrigation, and pumping volume.
- Improving spatial accuracy using GIS data.
- Deploying the Streamlit app online.

## 18. Conclusion

This project successfully demonstrates a complete machine learning workflow for groundwater level prediction. Rainfall, temperature, and groundwater data were collected, processed, merged, and analyzed. Multiple regression models were trained and compared, and XGBoost Regressor performed best.

The project also includes a working Streamlit web application, making it easy for users to predict groundwater level interactively. With more historical groundwater data, this prototype can be improved into a stronger groundwater prediction system.

## 19. Mentor Explanation

I developed a web-based groundwater level prediction system using Python and machine learning. The application allows users to enter rainfall, temperature, district, and date information. Based on these inputs, the trained XGBoost model predicts groundwater level in meters below ground level. The system also shows model accuracy, EDA graphs, district-wise analysis, feature importance, and project methodology.

## 20. References

- India Meteorological Department data accessed using `imdlib`
- Telangana Ground Water Department groundwater report
- Python documentation
- pandas documentation
- scikit-learn documentation
- XGBoost documentation
- Streamlit documentation
