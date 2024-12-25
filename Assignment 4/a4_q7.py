import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
import torch.optim as optim
from torchvision import datasets, models
from matplotlib import pyplot as plt
import numpy as np

#Adding noise to the test set
def add_noise(images, std_dev=0.2):
    #Make sure noise is 0 mean and 0.2 std_dev
    noise = torch.randn(images.shape) * std_dev
    #Add noise to imagages
    noisy_images = images + noise
    return noisy_images

#Visualize images
#Got from notebook
def imshow(img, title=None):
    img = img / 2 + 0.5  # Unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    if title:
        plt.title(title)
    plt.show()

#Define the CNN
#Got from notebook
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3,32,5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 32, 5)
        self.fc1 = nn.Linear(32 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == '__main__':
    #Load the CIFAR-10 dataset with normalization
    #Basically got all from notebook
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    batch_size = 32

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                              shuffle=True, num_workers=4)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                             shuffle=False, num_workers=4)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    #Initialize and train the network
    net = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    #Train the network
    for epoch in range(20):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data
            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            
            if i % 400 == 399:    # print every 400 mini-batches
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    dataiter = iter(testloader)
    images, labels = next(dataiter)
    noisy_images = add_noise(images)

    #Show original and noisy images
    imshow(torchvision.utils.make_grid(images), title="Original Images")
    imshow(torchvision.utils.make_grid(noisy_images), title="Noisy Images")


    #Find accuracy of clean test data
    correct = 0
    total = 0
    with torch.no_grad():
        net.eval()
        for images, labels in testloader:
            outputs = net(images)
            predicted = torch.max(outputs.data, 1)[1]
            correct += (predicted == labels).sum().item()
    print(f'Accuracy on clean test images: {100 * correct / len(testloader.dataset):.2f}%')
    
    #Find accuaracy on noisy test data
    correct = 0
    total = 0
    with torch.no_grad():
        net.eval()
        for images, labels in testloader:
            noisy_images = add_noise(images)
            outputs = net(noisy_images)
            predicted = torch.max(outputs.data, 1)[1]
            correct += (predicted == labels).sum().item()

    print(f'Accuracy on noisy test images: {100 * correct / len(testloader.dataset):.2f}%')
