from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

app = FastAPI()

# Mock data for pose estimation
MOCK_POSE = {
    "keypoints": [
        {"x": 0.5, "y": 0.3, "score": 0.95, "name": "nose"},
        {"x": 0.5, "y": 0.4, "score": 0.93, "name": "left_eye"},
    ]
}

# Mock data for segmentation
MOCK_SEGMENTATION = {
    "mask": "base64_encoded_mock_mask",
    "confidence": 0.92
}

@app.post("/pose")
async def estimate_pose(file: UploadFile = File(...)):
    # Simulate pose estimation
    return JSONResponse(content=MOCK_POSE)

@app.post("/segment")
async def segment_clothing(file: UploadFile = File(...)):
    # Simulate segmentation
    return JSONResponse(content=MOCK_SEGMENTATION)

@app.get("/")
async def root():
    return {"message": "Virtual Try-On AI Prototype"}