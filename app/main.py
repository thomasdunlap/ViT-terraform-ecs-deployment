from fastapi import FastAPI, Query, File, UploadFile
from transformers import ViTForImageClassification, ViTFeatureExtractor
import torch
import joblib
from io import BytesIO
import base64
from PIL import Image


app = FastAPI()
model = joblib.load("app/models/sota_model.joblib")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
vit = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
vit.to(device)

@app.get("/")
def read_root():
    return {"API status": "If you can see this, it's working!"}

@app.post("/predict/")
def predict_price(
    location: str = Query(..., description="Location", min_length=1),
    size: float = Query(..., description="Size (in meters squared)", ge=10.0),
    bedrooms: int = Query(2, description="Number of bedrooms", ge=0, le=50)
    ):
    
    example = [location, size, bedrooms]
    price = model.predict([example])[0]
    return {"prediction": int(price)}

@app.post("/image/")
def classify_image(
        image_bytes: bytes = File(..., description="Image file as bytes")
    ):
    image = Image.open(BytesIO(image_bytes))
    encoding = feature_extractor(images=image, return_tensors="pt")
    pixel_values = encoding['pixel_values'].to(device)
    outputs = vit(pixel_values)
    logits = outputs.logits
    prediction = logits.argmax(-1)
    return {"Predicted class:": vit.config.id2label[prediction.item()]}





