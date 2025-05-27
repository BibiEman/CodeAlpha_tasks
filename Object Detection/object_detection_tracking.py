import cv2
import numpy as np
from ultralytics import YOLO
import time

class ObjectDetectorTracker:
    def __init__(self, model_path="yolov8n.pt"):
        """
        Initialize the object detector and tracker
        Args:
            model_path: Path to the YOLO model weights
        """
        # Load YOLO model
        self.model = YOLO(model_path)
        
        # Initialize video capture
        self.cap = None
        
        # Initialize tracking variables
        self.tracked_objects = {}
        self.next_object_id = 0
        
    def start_camera(self, camera_id=0):
        """Start the camera capture"""
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise ValueError("Could not open camera")
            
    def process_frame(self, frame):
        """
        Process a single frame for object detection and tracking
        Args:
            frame: Input frame from camera
        Returns:
            Processed frame with detections and tracking information
        """
        # Run YOLO detection
        results = self.model(frame, verbose=False)[0]
        
        # Process detections
        current_objects = {}
        
        for detection in results.boxes.data:
            x1, y1, x2, y2, conf, class_id = detection
            if conf > 0.5:  # Confidence threshold
                bbox = (int(x1), int(y1), int(x2-x1), int(y2-y1))
                class_name = results.names[int(class_id)]
                
                # Assign object ID
                object_id = self.next_object_id
                self.next_object_id += 1
                current_objects[object_id] = {
                    'bbox': bbox,
                    'class': class_name,
                    'confidence': float(conf)
                }
                
                # Draw bounding box and label
                cv2.rectangle(frame, (bbox[0], bbox[1]), 
                            (bbox[0] + bbox[2], bbox[1] + bbox[3]), 
                            (0, 255, 0), 2)
                
                label = f"{class_name} {conf:.2f}"
                cv2.putText(frame, label, (bbox[0], bbox[1] - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Update tracking information
        self.tracked_objects = current_objects
        
        return frame
    
    def run(self):
        """Main loop for real-time object detection and tracking"""
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                # Process frame
                processed_frame = self.process_frame(frame)
                
                # Display FPS
                cv2.putText(processed_frame, f"Press 'q' to quit", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Show the frame
                cv2.imshow("Object Detection and Tracking", processed_frame)
                
                # Break loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

def main():
    # Create detector instance
    detector = ObjectDetectorTracker()
    
    # Start camera
    detector.start_camera()
    
    # Run detection and tracking
    detector.run()

if __name__ == "__main__":
    main() 