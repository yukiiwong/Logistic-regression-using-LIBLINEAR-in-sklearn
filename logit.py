import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import matplotlib.pyplot as plt

def print_line(title):
    print("*" * 30 + " {} ".format(title) + "*" * 30)


# 数据集地址：https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin

print_line("数据集")
df = pd.read_excel("RP数据.xlsx")
print(df.info())
df.dropna(inplace=True)

y = df.iloc[:, [1]]#目标值
print_line("y")
print(y.info())

x = df.iloc[:, range(2,17)]#特征值
print_line("x")
print(x.info())

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.3)#划分数据集为训练集与测试集

#数据标准化
std = StandardScaler()
x_train = std.fit_transform(x_train) #fit：根据训练数据集获取均值和方差，scikit-learn中返回一个Scalar对象
x_test = std.transform(x_test) #集体归一化

#逻辑回归
lg = LogisticRegression(penalty= 'l1',solver = 'liblinear',C=1.0, max_iter = 500000)
lg.fit(x_train, y_train.values.flatten())
print_line("逻辑回归建模")
print("回归系数：{}".format(lg.coef_))
print_line("真实值")
print(y_test[:].values.flatten())
print_line("预测值")
y_predict = lg.predict(x_test)
print(y_predict[:])

#召回率
print_line("召回率")
report = classification_report(y_test, y_predict, labels=[0, 1], target_names=["汽车", "轨道"])
print(report)
print (u'准确率',accuracy_score(y_test,y_predict))
print (u'混淆矩阵',confusion_matrix(y_test,y_predict))
print (u'分类报告',classification_report(y_test,y_predict))
confusion_matrix = confusion_matrix(y_test,y_predict)
plt.matshow(confusion_matrix)
plt.title(u'confusion matrix')
plt.colorbar()
plt.ylabel(u'Actual type')
plt.xlabel(u'Forecast type')
plt.show()
