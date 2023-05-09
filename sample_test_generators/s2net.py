import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.autograd import Variable

from GA_test_generator import GATestGenerator

class Net(nn.Module):
    def __init__(self, individual):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, individual[0])
        self.fc2 = nn.Linear(individual[0], individual[1])
        self.fc3 = nn.Linear(individual[1], 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

ga_object = GATestGenerator()
bestindivi = ga_object.start()
best_individual =bestindivi # GA best one

model = Net(best_individual)

# 设置损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# training model
for epoch in range(10000):
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data
        inputs, labels = Variable(inputs), Variable(labels)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    if epoch % 1000 == 999:
        print('Epoch [%d/%d], Loss: %.4f' % (epoch+1, 10000, loss.data))

# 评估模型
correct = 0
total = 0
for data in test_loader:
    inputs, labels = data
    inputs, labels = Variable(inputs), Variable(labels)
    outputs = model(inputs)
    predicted = (outputs.data > 0.5).float()
    total += labels.size(0)
    correct += (predicted == labels).sum()

print('Accuracy of the network on the 100 test data: %d %%' % (100 * correct / total))
