import gradio as gr
import torch
import torch.nn.functional as F
from facenet_pytorch import MTCNN, InceptionResnetV1
import numpy as np
from PIL import Image
import cv2
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image
import warnings
warnings.filterwarnings("ignore")

DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'

mtcnn = MTCNN(
    select_largest=False,
    post_process=False,
    device=DEVICE
).to(DEVICE).eval()

model = InceptionResnetV1(
    pretrained="vggface2",
    classify=True,
    num_classes=1,
    device=DEVICE
)

checkpoint_path = r"D:\deepfake detection\Image_deepfake_detection\resnetinceptionv1_epoch_32.pth"
checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))

model.load_state_dict(checkpoint['model_state_dict'])
model.to(DEVICE)
model.eval()

def predict(input_image:Image.Image):
    face = mtcnn(input_image)
    if face is None:
        raise Exception('No face detected')
    face = face.unsqueeze(0) 
    face = F.interpolate(face, size=(256, 256), mode='bilinear', align_corners=False)
    
    prev_face = face.squeeze(0).permute(1, 2, 0).cpu().detach().int().numpy()
    prev_face = prev_face.astype('uint8')

    face = face.to(DEVICE)
    face = face.to(torch.float32)
    face = face / 255.0
    face_image_to_plot = face.squeeze(0).permute(1, 2, 0).cpu().detach().int().numpy()

    target_layers=[model.block8.branch1[-1]]
    cam = GradCAM(model=model, target_layers=target_layers)
    targets = [ClassifierOutputTarget(0)]

    grayscale_cam = cam(input_tensor=face, targets=targets, eigen_smooth=True)
    grayscale_cam = grayscale_cam[0, :]
    visualization = show_cam_on_image(face_image_to_plot, grayscale_cam, use_rgb=True)
    face_with_mask = cv2.addWeighted(prev_face, 1, visualization, 0.5, 0)
    with torch.no_grad():
        output = torch.sigmoid(model(face).squeeze(0))
        prediction = "real" if output.item() < 0.5 else "fake"
        
        real_prediction = 1 - output.item()
        fake_prediction = output.item()
        
        confidences = {
            'real': real_prediction,
            'fake': fake_prediction
        }
    return confidences, face_with_mask
interface = gr.Interface(
  fn=predict,
  inputs=gr.Image(label="Input Image", type="pil"),  
  outputs=[
    gr.Label(label="Class"),
    gr.Image(label="Face with Explainability", type="pil")
  ],
).launch()



