from fastapi import FastAPI, File, UploadFile
import shutil
import os
import joblib  # Assuming model is saved as a joblib file
from datetime import datetime
import sqlite3  # Simple SQLite logging

app = FastAPI()

# Load your trained model (update the path as necessary)
model = joblib.load("path/to/your/model.joblib")

# Initialize SQLite logging database
conn = sqlite3.connect('logs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS log (timestamp TEXT, filename TEXT, prediction TEXT, confidence REAL)''')
conn.commit()

def ela_preprocessing(image_path):
    # Implement ELA preprocessing logic here
    pass

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file:
        return {"error": "No file uploaded"}
    
    # Save the file locally
    img_path = f"uploads/{file.filename}"
    with open(img_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ELA Preprocessing
    processed_img = ela_preprocessing(img_path)

    # Make prediction
    prediction, confidence = model.predict(processed_img)  # Adjust as necessary to call your model

    # Log to database
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO log (timestamp, filename, prediction, confidence) VALUES (?, ?, ?, ?)", 
              (timestamp, file.filename, prediction, confidence))
    conn.commit()
    
    return {
        "filename": file.filename,
        "prediction": prediction,
        "confidence": confidence
    }