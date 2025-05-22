from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Aurora API is online"}

@app.get("/forecast")
def forecast():
    # Nessun modello Aurora qui
    return {
        "forecast_shape": "(dummy, test)",
        "message": "Modello non caricato per limiti RAM su Render Free"
    }
