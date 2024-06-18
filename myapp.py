from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import pandas as pd

app = FastAPI()

class features(BaseModel):
    
    Gender : int
    Height : float
    Weight : float
    
with open("Weight Predection lgr_model.pkl", "rb") as f:
    model = pickle.load(f)    
    
@app.get('/')
def hello():
    return {"message": "Hello from post or postman, FastAPI!"}

@app.post('/predict/')
def score(item:features):
    df = pd.DataFrame([item.dict().values()],columns = item.dict().keys())
    prediction = model.predict(df)
    return {"prediction":int(prediction[0])}
    # return item