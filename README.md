# Deepfake-Image-Identification
Deepfake images are manipulated media created using advanced AI techniques. These images can be highly convincing, making it difficult to distinguish them from real ones. To counter this, deepfake image identification systems have emerged as a crucial tool.

In this Project We Try to identify the Deepfake Image in Python
# libraries Used
1. **Gradio:** A Python library for creating user-friendly machine learning interfaces.
Used to build web-based applications that can be easily shared and used, even by people without technical expertise.
In this context, it's likely used to create a web interface for users to upload images and get real-time deepfake detection results

2. **Torch:** The fundamental Python library for machine learning, providing tensor computations and automatic differentiation.

3. **facenet_pytorch:** A PyTorch library specifically designed for face recognition and analysis.

   **MTCNN:** A state-of-the-art face detection model that can accurately locate faces in images, even in challenging conditions.

   **InceptionResnetV1:** A powerful pre-trained face recognition model that extracts high-quality facial features.

4. **NumPy:** A library for numerical computations in Python.
Used for efficient array manipulation and mathematical operations, which are essential for processing image data and performing calculations.

5. **PIL (Pillow):** The Python Imaging Library (PIL) provides image processing capabilities.
Used for loading, manipulating, and saving images in various formats.

6. **OpenCV (cv2):** A popular computer vision library.
Used for tasks like image and video processing, object detection, and face recognition.

7. **PyTorch-Grad-CAM:** A library for visualizing the decision-making process of neural networks.

  **GradCAM:** A technique that generates class-specific heatmaps to highlight the regions of the image that the model focuses on when making a prediction.

  **ClassifierOutputTarget:** A target class for GradCAM, used to visualize the model's attention to specific classes (e.g., real or fake).

  **show_cam_on_image:** A function to overlay the heatmap on the original image, providing a visual explanation of the model's decision.

#Images
**Interface Look**

![2 (2)](https://github.com/user-attachments/assets/999788ff-6927-478b-8ba1-e42ef471c6d8)

**Output:**


![2 (3)](https://github.com/user-attachments/assets/d20d2b5f-029e-4211-b17c-6b2ce2f442b9)




