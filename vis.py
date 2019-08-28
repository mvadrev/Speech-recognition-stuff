import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
import torch.utils.data as datax
import numpy as np


TRANSFORM_IMG = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225] )
    ])   

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.fc1 = nn.Linear(432*288,1)
        
    def forward(self,x):
        x = x.view(-1,432*288)
        x = F.relu(self.fc1(x))
        return x
    
model = Net()
criterion = torch.nn.CrossEntropyLoss()
optimizers = torch.optim.SGD(model.parameters(), lr=0.01) 
n_epoch = 20 


TRAIN_DATA_PATH = '..\librosa\images'
train_data = torchvision.datasets.ImageFolder(root=TRAIN_DATA_PATH, transform=TRANSFORM_IMG)
train_loader = datax.DataLoader(train_data, batch_size=1, shuffle=True,  num_workers=1)

import matplotlib.pyplot as plt
dataiter = iter(train_loader)
images, labels = dataiter.next()
img = images[0].numpy()
plt.imshow(np.transpose(images[0].numpy(), (1, 2, 0)))



 