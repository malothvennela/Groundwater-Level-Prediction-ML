# Groundwater Level Prediction Using Machine Learning

BTech CSE internship project for predicting groundwater levels using rainfall and temperature data.

## Project Structure

```text
Groundwater_Level_Prediction/
├── data/
│   ├── raw/          # Place original groundwater, rainfall, temperature files here
│   └── processed/    # Cleaned and merged datasets
├── notebooks/        # Jupyter notebook with explanations
├── src/              # Python scripts
├── models/           # Trained models
└── outputs/          # Plots, metrics, reports
```

## How To Use

1. Put all dataset files in `data/raw`.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Inspect datasets:

```bash
python src/inspect_data.py
```

4. Run the full pipeline:

```bash
python src/run_pipeline.py
```

5. Make an example prediction:

```bash
python src/predict.py --rainfall 120 --temperature 28
```

6. Run the Streamlit app:

```bash
streamlit run app.py
```

## Current Results

Best model:

```text
XGBoost Regressor
```

Metrics:

```text
R2 Score: 0.591762
MAE: 1.384762
RMSE: 1.604212
```

Final report:

```text
FINAL_REPORT.md
```

## Expected Final Dataset

The pipeline tries to create:

```text
Date, District, Rainfall, Temperature, Groundwater_Level
```

If your original column names are different, update the aliases in `src/config.py`.
