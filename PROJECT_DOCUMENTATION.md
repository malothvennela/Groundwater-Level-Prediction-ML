# Groundwater Level Prediction Using Machine Learning

## 1. Project Overview

This project predicts groundwater levels using machine learning. The main input features are rainfall and temperature, and the output is groundwater level measured in meters below ground level.

Project title:

```text
Groundwater Level Prediction Using Machine Learning
```

The project was developed as a BTech CSE internship-style machine learning project.

## 2. Objective

The main objectives are:

- Collect rainfall, temperature, and groundwater level data.
- Convert raw data into structured CSV format.
- Merge groundwater, rainfall, and temperature datasets.
- Perform exploratory data analysis.
- Train and compare machine learning regression models.
- Save the best model.
- Build a prediction workflow and Streamlit web app.

## 3. Dataset Description

### 3.1 Rainfall And Temperature Data

Rainfall, maximum temperature, and minimum temperature data were downloaded using the IMD library.

Downloaded variables:

- Rainfall
- Maximum temperature
- Minimum temperature

The data was downloaded for:

```text
2015 to 2024
```

The gridded IMD data was converted to district-wise Telangana data using approximate district headquarters latitude and longitude points.

Processed file:

```text
data/processed/telangana_imd_rainfall_temperature.csv
```

### 3.2 Groundwater Level Data

Groundwater level data was extracted from the Telangana groundwater report PDF.

Raw file:

```text
data/raw/groundwater_level.pdf
```

The useful table was found in:

```text
ANNEXURE-III
DEPTH TO WATER LEVEL IN MARCH-2026
PDF page 42
```

Processed file:

```text
data/processed/groundwater_march_2026_clean.csv
```

## 4. Project Structure

```text
Groundwater_Level_Prediction/
├── app.py
├── FINAL_REPORT.md
├── PROJECT_DOCUMENTATION.md
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

## 5. Data Preprocessing

Preprocessing included:

- Inspecting raw CSV, Excel, and PDF files.
- Extracting groundwater tables from PDF.
- Cleaning extracted groundwater rows.
- Standardizing district names.
- Converting daily IMD gridded data to district-level data.
- Aggregating rainfall and temperature values.
- Merging groundwater with rainfall and temperature.

Final merged dataset:

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

## 6. Exploratory Data Analysis

The following plots were generated:

- Rainfall trends
- Temperature trends
- Groundwater level trends
- Correlation heatmap
- District-wise groundwater analysis

Output folder:

```text
outputs
```

## 7. Feature Engineering

Features used for model training:

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

## 8. Machine Learning Models

The following models were trained:

1. Random Forest Regressor
2. Gradient Boosting Regressor
3. XGBoost Regressor

## 9. Model Evaluation

Evaluation metrics:

- R2 Score
- MAE
- RMSE

Model comparison:

| Model | R2 Score | MAE | RMSE |
|---|---:|---:|---:|
| XGBoost Regressor | 0.591762 | 1.384762 | 1.604212 |
| Gradient Boosting Regressor | 0.443384 | 1.642218 | 1.873195 |
| Random Forest Regressor | 0.441125 | 1.710036 | 1.876991 |

Best model:

```text
XGBoost Regressor
```

Saved model:

```text
models/best_groundwater_model.joblib
```

## 10. Prediction Workflow

Prediction command:

```powershell
py -3.10 src/predict.py --rainfall 50 --temperature 30 --district Hyderabad --date 2026-03-01
```

Example output:

```text
Predicted groundwater level: 9.581
```

## 11. Streamlit App

The Streamlit app allows users to enter:

- District
- Date
- Rainfall
- Temperature

Then the app predicts groundwater level.

Run command:

```powershell
py -3.10 -m streamlit run app.py
```

Local URL:

```text
http://localhost:8501
```

## 12. Limitations

- Groundwater data currently contains 33 district-level rows for March 2026.
- IMD rainfall and temperature data was downloaded up to 2024.
- March 2024 weather values were used as fallback for March 2026 groundwater data.
- A stronger model needs groundwater data for multiple months and years.

## 13. Future Scope

Future improvements:

- Collect groundwater data for multiple years.
- Download matching 2026 rainfall and temperature data.
- Add more features such as soil type, elevation, land use, and irrigation.
- Improve district-level spatial matching using GIS shapefiles.
- Deploy the Streamlit app online.

## 14. Conclusion

The project successfully demonstrates an end-to-end machine learning workflow for groundwater level prediction. It includes data collection, PDF extraction, preprocessing, EDA, machine learning model training, evaluation, prediction, and a working web app.
