import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = Path("models/best_groundwater_model.joblib")
DATA_PATH = Path("data/processed/final_groundwater_imd_march_2026.csv")
METRICS_PATH = Path("outputs/model_comparison.csv")
FEATURE_IMPORTANCE_PATH = Path("outputs/feature_importance.json")
OUTPUTS_DIR = Path("outputs")

DISTRICTS = [
    "Adilabad",
    "Bhadradri Kothagudem",
    "Hanumakonda",
    "Hyderabad",
    "Jayashankar",
    "Jagtial",
    "Jogulamba Gadwal",
    "Kamareddy",
    "Karimnagar",
    "Khammam",
    "Kumuram Bheem",
    "Mahabubabad",
    "Mahabubnagar",
    "Mancherial",
    "Medak",
    "Medchal-Malkajgiri",
    "Mulugu",
    "Nagarkurnool",
    "Nalgonda",
    "Narayanpet",
    "Nirmal",
    "Nizamabad",
    "Peddapalli",
    "Rajanna Sircilla",
    "Rangareddy",
    "Sangareddy",
    "Siddipet",
    "Suryapet",
    "Vikarabad",
    "Wanaparthy",
    "Warangal",
    "Yadadri Bhuvanagiri",
]


def season_from_month(month: int) -> str:
    if month in [12, 1, 2]:
        return "winter"
    if month in [3, 4, 5]:
        return "summer"
    if month in [6, 7, 8, 9]:
        return "monsoon"
    return "post_monsoon"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_dataset() -> pd.DataFrame:
    if not DATA_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(DATA_PATH, parse_dates=["date"])


@st.cache_data
def load_metrics() -> pd.DataFrame:
    if not METRICS_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(METRICS_PATH)


@st.cache_data
def load_feature_importance() -> pd.DataFrame:
    if not FEATURE_IMPORTANCE_PATH.exists():
        return pd.DataFrame()
    with FEATURE_IMPORTANCE_PATH.open("r", encoding="utf-8") as file:
        values = json.load(file)
    rows = [
        {
            "feature": name.replace("num__", "").replace("cat__", ""),
            "importance": score,
        }
        for name, score in values.items()
    ]
    return pd.DataFrame(rows).head(12)


def prediction_row(rainfall: float, temperature: float, district: str, prediction_date) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "rainfall": rainfall,
                "temperature": temperature,
                "year": prediction_date.year,
                "month": prediction_date.month,
                "district": district,
                "season": season_from_month(prediction_date.month),
            }
        ]
    )


st.set_page_config(page_title="Groundwater Level Prediction", layout="wide")

st.title("Groundwater Level Prediction")
st.caption("Machine learning app for district-wise groundwater level prediction using rainfall and temperature.")

try:
    model = load_model()
except FileNotFoundError:
    st.error("Trained model not found. Run `py -3.10 src/train_models.py` first.")
    st.stop()

dataset = load_dataset()
metrics = load_metrics()
feature_importance = load_feature_importance()

tab_predict, tab_metrics, tab_graphs, tab_district, tab_features, tab_info = st.tabs(
    [
        "Prediction",
        "Model Accuracy",
        "Graphs",
        "District Analysis",
        "Feature Importance",
        "Project Info",
    ]
)

with tab_predict:
    left, right = st.columns([1.1, 0.9])
    with left:
        district = st.selectbox("District", DISTRICTS, index=DISTRICTS.index("Hyderabad"))
        prediction_date = st.date_input("Prediction date", value=pd.Timestamp("2026-03-01"))
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, value=50.0, step=1.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=30.0, step=0.5)

        if st.button("Predict groundwater level", type="primary"):
            row = prediction_row(rainfall, temperature, district, prediction_date)
            prediction = float(model.predict(row)[0])
            st.metric("Predicted groundwater level", f"{prediction:.3f} m bgl")
            st.info("m bgl means meters below ground level. Higher values indicate deeper groundwater.")

    with right:
        st.subheader("How To Use")
        st.write(
            "Select a district, choose the date, enter rainfall and temperature values, "
            "then click the prediction button. The model returns groundwater depth in m bgl."
        )
        st.write("Example input:")
        st.code(
            "District: Hyderabad\nDate: 2026-03-01\nRainfall: 50 mm\nTemperature: 30 °C",
            language="text",
        )

with tab_metrics:
    st.subheader("Model Accuracy")
    if metrics.empty:
        st.warning("Model metrics file not found. Run `py -3.10 src/train_models.py`.")
    else:
        best = metrics.iloc[0]
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Best Model", str(best["model"]))
        col2.metric("R² Score", f"{best['r2_score']:.4f}")
        col3.metric("MAE", f"{best['mae']:.4f}")
        col4.metric("RMSE", f"{best['rmse']:.4f}")
        st.dataframe(metrics, use_container_width=True)
        st.write(
            "R² shows model fit, MAE shows average absolute error, and RMSE gives larger penalty "
            "to bigger prediction errors."
        )

with tab_graphs:
    st.subheader("EDA Graph Outputs")
    graph_files = [
        ("District-wise Groundwater Ranking", OUTPUTS_DIR / "strong_district_groundwater_ranking.png"),
        ("Rainfall vs Groundwater Level", OUTPUTS_DIR / "strong_rainfall_vs_groundwater.png"),
        ("Temperature vs Groundwater Level", OUTPUTS_DIR / "strong_temperature_vs_groundwater.png"),
        ("Correlation Heatmap", OUTPUTS_DIR / "strong_correlation_heatmap.png"),
        ("Model Comparison", OUTPUTS_DIR / "strong_model_comparison.png"),
        ("Feature Importance", OUTPUTS_DIR / "strong_feature_importance.png"),
        ("Actual vs Predicted Groundwater Level", OUTPUTS_DIR / "strong_actual_vs_predicted.png"),
    ]

    for title, path in graph_files:
        if path.exists():
            st.markdown(f"### {title}")
            st.image(str(path), use_container_width=True)
        else:
            st.warning(f"Missing graph: {path}. Run `py -3.10 src/create_strong_graphs.py`.")

with tab_district:
    st.subheader("District-wise Analysis")
    if dataset.empty:
        st.warning("Final dataset not found.")
    else:
        selected = st.selectbox("Select district for analysis", sorted(dataset["district"].dropna().unique()))
        district_df = dataset[dataset["district"] == selected]
        if district_df.empty:
            st.warning("No records found for selected district.")
        else:
            row = district_df.iloc[0]
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Groundwater Level", f"{row['groundwater_level']:.2f} m bgl")
            col2.metric("Rainfall", f"{row['rainfall']:.2f} mm")
            col3.metric("Temperature", f"{row['temperature']:.2f} °C")
            col4.metric("No. of Wells", f"{row['number_of_wells']:.0f}")
            st.dataframe(district_df, use_container_width=True)

        chart_df = dataset.sort_values("groundwater_level")[["district", "groundwater_level"]].set_index("district")
        st.bar_chart(chart_df)

with tab_features:
    st.subheader("Feature Importance")
    if feature_importance.empty:
        st.warning("Feature importance file not found. Run `py -3.10 src/train_models.py`.")
    else:
        st.write("This shows which input features influenced the trained model most.")
        st.bar_chart(feature_importance.set_index("feature"))
        st.dataframe(feature_importance, use_container_width=True)

with tab_info:
    st.subheader("Project Information")
    st.markdown(
        """
        **Objective:** Predict groundwater level using rainfall and temperature data.

        **Dataset:**
        - IMD rainfall data
        - IMD maximum and minimum temperature data
        - Telangana Ground Water Department groundwater report

        **Methodology:**
        1. Download rainfall and temperature data.
        2. Convert IMD gridded data into district-wise data.
        3. Extract groundwater level table from PDF.
        4. Clean and merge datasets.
        5. Perform EDA.
        6. Train Random Forest, Gradient Boosting, and XGBoost models.
        7. Save the best model and build this app.

        **Current Best Model:** XGBoost Regressor

        **Limitation:** This is a prototype because groundwater data currently has only March 2026
        district-level observations. More historical groundwater data will improve accuracy.
        """
    )
