import torch
import os
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
import torch.utils.data as data
import numpy

BATCH_SIZE = 10

TRANSFORM_IMG = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225] )
    ])
    
    

TRAIN_DATA_PATH = '..\librosa\images'
train_data = torchvision.datasets.ImageFolder(root=TRAIN_DATA_PATH, transform=TRANSFORM_IMG)
train_loader = data.DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True,  num_workers=4)

dataiter = iter(train_data_loader)
images, labels = dataiter.next()

for idx in np.arange(2):
    ax = fig.add_subplot(2,20/2,idx+1, xticks=[],yticks=[])
    ax.imshow(np.squeeze(images[idx]))