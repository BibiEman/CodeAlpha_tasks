# Real-time Object Detection and Tracking

This project implements real-time object detection and tracking using YOLOv8 and OpenCV. It can detect and track multiple objects in a video stream from your camera.

## Features

- Real-time object detection using YOLOv8
- Object tracking with unique IDs
- Bounding box visualization
- Class labels and confidence scores
- Support for webcam input

## Requirements

- Python 3.8 or higher
- Webcam or video input device
- CUDA-capable GPU (recommended for better performance)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd object-detection-tracking
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```bash
python object_detection_tracking.py
```

2. The program will:
   - Open your default camera
   - Start detecting and tracking objects in real-time
   - Display the video feed with bounding boxes and labels
   - Press 'q' to quit the application

## Customization

- You can modify the confidence threshold in the `process_frame` method (default is 0.5)
- To use a different YOLO model, change the `model_path` parameter in the `ObjectDetectorTracker` initialization
- Available YOLO models: yolov8n.pt (nano), yolov8s.pt (small), yolov8m.pt (medium), yolov8l.pt (large), yolov8x.pt (xlarge)

## Notes

- The first time you run the script, it will download the YOLO model weights automatically
- For better performance, use a CUDA-capable GPU
- The tracking is currently based on frame-by-frame detection. For more robust tracking, consider implementing a tracking algorithm like SORT or DeepSORT 