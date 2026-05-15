# Virtual Try-On AI (Minimal Prototype)

An open-source AI app that lets users "try on" clothes virtually using mock data.

## Features
- **Mock Pose Estimation**: Simulates keypoints detection (e.g., nose, eyes).
- **Mock Segmentation**: Simulates clothing segmentation.
- **FastAPI Backend**: Lightweight server for serving predictions.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Femirins/virtual-tryon-ai.git
   cd virtual-tryon-ai
   ```

2. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # OR
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
- **GET `/`**: Root endpoint.
  ```json
  {"message": "Virtual Try-On AI Prototype"}
  ```

- **POST `/pose`**: Mock pose estimation.
  ```json
  {
    "keypoints": [
      {"x": 0.5, "y": 0.3, "score": 0.95, "name": "nose"},
      {"x": 0.5, "y": 0.4, "score": 0.93, "name": "left_eye"}
    ]
  }
  ```

- **POST `/segment`**: Mock clothing segmentation.
  ```json
  {
    "mask": "base64_encoded_mock_mask",
    "confidence": 0.92
  }
  ```

## Technical Architecture
- **Backend**: FastAPI (Python)
- **Mock Data**: Simulates pose estimation and segmentation.
- **Dependencies**: `fastapi`, `uvicorn`, `pillow`, `python-multipart`.

## License
MIT