import torch
import torchvision
from torch import nn
from PIL import Image
resnet = torchvision.models.resnet50()
resnet.fc = nn.Linear(2048, 102)
resnet.load_state_dict(torch.load("resnet50_0.497.pkl"))
# tensor_trans = torchvision.transforms.ToTensor()
tensor_trans = torchvision.transforms.Compose([
    torchvision.transforms.Resize((224, 224)),
    torchvision.transforms.ToTensor()
]
)

def recognize(image_name):
    image = Image.open("./static/images"+image_name).convert("RGB")
    image = tensor_trans(image)
    image = torch.reshape(image, (1, 3, 224, 224))
    resnet.eval()
    with torch.no_grad():
        result = resnet(image)
    softmax = nn.Softmax(dim=1)
    result = softmax(result)
    torch.set_printoptions(sci_mode=False)
    print(result)
    idx = result.argmax(1).item()
    classes = []
    with open("classes.txt", "r") as f:
        temp = f.readlines()
        classes = [" ".join(k) for k in [i.split()[1:] for i in temp]]
        print(classes)
        print(len(classes))

    out = classes[idx]

    print("识别结果为：{}".format(out))