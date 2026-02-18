import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models")

def load_models():
    model_spread = joblib.load(os.path.join(MODEL_PATH, "nba_model_spread_v6.pkl"))
    model_total  = joblib.load(os.path.join(MODEL_PATH, "nba_model_total_v6.pkl"))
    model_ml     = joblib.load(os.path.join(MODEL_PATH, "nba_model_ml_v6.pkl"))

    return model_spread, model_total, model_ml
