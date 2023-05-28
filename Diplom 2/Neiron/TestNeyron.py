import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt

# определение класса нейронной сети
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=16)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=32)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=1, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu2(x)
        x = self.conv3(x)
        return x

# определение класса датасета
class RliDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        x = self.data[index]
        y = x + np.random.normal(loc=0, scale=0.1, size=x.shape)
        x = torch.from_numpy(x).float().unsqueeze(0)
        y = torch.from_numpy(y).float().unsqueeze(0)
        return x, y

    def __len__(self):
        return len(self.data)

# определение функции обучения
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = nn.MSELoss()(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

# загрузка и предобработка данных
data = np.load('rli_data.npy')
data = (data - data.min()) / (data.max() - data.min())

# создание датасета и загрузчика данных
dataset = RliDataset(data)
train_loader = DataLoader(dataset, batch_size=64, shuffle=True)

# создание экземпляра нейронной сети
model = Net()

# определение устройства
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# определение функции оптимизации
optimizer = optim.Adam(model.parameters(), lr=0.001)
# обучение модели
for epoch in range(1, 21):
    train(model, device, train_loader, optimizer, epoch)
# тестирование модели
test_data = dataset[0][0].unsqueeze(0).to(device)
output = model(test_data)
output = output.squeeze().cpu().detach().numpy()
# визуализация результатов
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(data[0], cmap='gray')
plt.title('Input')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray')
plt.title('Output')
plt.axis('off')
plt.show()