from fastapi import FastAPI
from aurora import AuroraSmall

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Aurora API is online"}

@app.get("/forecast")
def get_forecast():
    model = AuroraSmall()
    model.load_checkpoint("microsoft/aurora", "aurora-0.25-small-pretrained.ckpt")
    input_tensor = model.example_inputs()
    output = model(input_tensor)
    return {"forecast_shape": str(output.shape)}
