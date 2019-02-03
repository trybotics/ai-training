import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
# print(digits.data)
# print(digits.target)
# print(len(digits.data))

clf = svm.SVC()
X,y = digits.data[:10], digits.target[:10]
clf.fit(X,y)
print(clf.predict([digits.data[-6]]))
plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()