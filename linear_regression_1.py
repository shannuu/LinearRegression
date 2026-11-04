import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("studydata.csv") 

def loss_function(m, b, data): # not neccessary to use this function (just to show the error)
    loss = 0
    for i in range(len(data)):
        x = data["Study_Hours"].iloc[i]
        y = data['Exam_Score'].iloc[i]
        loss += (y - (m * x + b)) ** 2
    loss /= len(data)
    return loss

def gradient_descent(m_now, b_now, L, data):
    gradient_m = 0
    gradient_b = 0
    n = len(data)
    for i in range(n):
        x = data["Study_Hours"].iloc[i]
        y = data['Exam_Score'].iloc[i]
        error = y - (m_now * x) - b_now
        gradient_m += (-2/n)*(error * x)
        gradient_b += (-2/n)*error
    
    m = m_now - L * gradient_m
    b = b_now - L * gradient_b
    return m,b

m = 0
b = 0
L = 0.001
epoch = 10000

for i in range(epoch):
    m,b = gradient_descent(m,b,L,data)
    if i % 1000 == 0:
        print(f"Epoch: {i}")

plt.scatter(data.Study_Hours,data.Exam_Score)
plt.plot(list(range(1,11)), [m * x + b for x in range(1,11)], color='red')
plt.show()