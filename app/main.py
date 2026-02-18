from fastapi import FastAPI, HTTPException
import pandas as pd
from app.schemas import GameFeatures
from app.model_loader import load_models

app = FastAPI(title="NBA ML Pregame API")

# Load models once at startup
model_spread, model_total, model_ml = load_models()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: GameFeatures):
    try:
        df = pd.DataFrame([features.model_dump()])

        predicted_spread = model_spread.predict(df)[0]
        predicted_total  = model_total.predict(df)[0]
        home_win_prob    = model_ml.predict_proba(df)[0][1]

        return {
            "predicted_spread": float(predicted_spread),
            "predicted_total": float(predicted_total),
            "home_win_probability": float(home_win_prob)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
