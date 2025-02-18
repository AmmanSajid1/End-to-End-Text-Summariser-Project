from fastapi import FastAPI, HTTPException
import uvicorn 
import sys 
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummariser.pipeline.prediction_pipeline import PredictionPipeline
from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successfull!")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Occurred: {str(e)}")
    
@app.post("/predict")
async def predict_route(input_text: TextInput):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(input_text.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

