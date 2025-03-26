import requests
from PIL import Image
from torchvision import transforms
import torch
import torchvision.models as models

# Fetch AI Task (Image Classification)
response = requests.get("http://127.0.0.1:5000/get_task")
if response.status_code == 200:
    task = response.json()
    image_url = task["image_url"]
    task_id = task["task_id"]
else:
    print("No tasks available.")
    exit()

# Download Image
image = Image.open(requests.get(image_url, stream=True).raw)

# Load Pretrained MobileNet Model
model = models.mobilenet_v2(pretrained=True)
model.eval()

# Preprocess Image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

image_tensor = preprocess(image).unsqueeze(0)

# Run AI Model
with torch.no_grad():
    output = model(image_tensor)

# Get Classification Result
label = torch.argmax(output).item()

# Send Result Back
requests.post("http://127.0.0.1:5000/submit_result", json={"task_id": task_id, "result": label})
print(f"Task {task_id} completed. Classified image as label {label}.")
