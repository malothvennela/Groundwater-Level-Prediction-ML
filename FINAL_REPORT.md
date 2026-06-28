# Groundwater Level Prediction Using Machine Learning

## Project Title

Groundwater Level Prediction Using Machine Learning

## Objective

The objective of this project is to predict groundwater level using rainfall and temperature data. The project uses rainfall and temperature data from IMD and groundwater level information from a Telangana Ground Water Department report.

## Tools And Libraries

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- XGBoost
- pdfplumber
- imdlib
- Streamlit

## Dataset Sources

### Rainfall And Temperature Data

Rainfall, maximum temperature, and minimum temperature data were downloaded using `imdlib` for the years 2015 to 2024.

The downloaded IMD gridded data was converted into Telangana district-wise data using approximate district headquarters coordinates.

Generated file:

```text
data/processed/telangana_imd_rainfall_temperature.csv
```

### Groundwater Level Data

Groundwater level data was extracted from:

```text
data/raw/groundwater_level.pdf
```

The useful groundwater table was found on PDF page 42:

```text
ANNEXURE-III
DEPTH TO WATER LEVEL IN MARCH-2026
```

Generated file:

```text
data/processed/groundwater_march_2026_clean.csv
```

## Data Preprocessing

The preprocessing steps included:

- Inspecting raw files
- Extracting PDF tables
- Cleaning groundwater table rows
- Standardizing district names
- Converting IMD gridded rainfall and temperature into district-wise values
- Merging groundwater, rainfall, and temperature data
- Handling district name mismatches using aliases

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

## Exploratory Data Analysis

The following visualizations were generated:

- Rainfall trends
- Temperature trends
- Groundwater level trends
- Correlation heatmap
- District-wise groundwater level analysis

Plots are saved in:

```text
outputs
```

## Feature Engineering

The model uses:

- Rainfall
- Temperature
- District
- Year
- Month
- Season

The target variable is:

```text
groundwater_level
```

## Models Trained

Three regression models were trained and compared:

1. Random Forest Regressor
2. Gradient Boosting Regressor
3. XGBoost Regressor

## Model Evaluation

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

## Prediction Example

Command:

```powershell
py -3.10 src/predict.py --rainfall 50 --temperature 30 --district Hyderabad --date 2026-03-01
```

Output:

```text
Predicted groundwater level: 9.581
```

## Streamlit App

A Streamlit app was created for interactive prediction:

```text
app.py
```

Run using:

```powershell
streamlit run app.py
```

## Limitations

- The current groundwater dataset has only 33 district-level rows for March 2026.
- IMD rainfall and temperature data was downloaded up to 2024, so March 2024 weather values were used as a temporary fallback for March 2026 groundwater data.
- For a stronger scientific model, groundwater data should be collected for multiple months and years.

## Conclusion

The project successfully demonstrates an end-to-end machine learning workflow for groundwater level prediction. It includes data download, PDF extraction, preprocessing, EDA, model training, evaluation, prediction, and an interactive app.
