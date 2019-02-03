# Let us take an example where we will take digits dataset and it will categorize the numbers for us, for example- 0 1 2 3 4 5 6 7 8 

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
 
digits= datasets.load_digits()
print(digits.data)

# It’s a long array of digits data where the data is stored.

#....................................................................................................................................

# Next, you can also try some other operations such as target, images etc.

# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn import svm
 
# digits= datasets.load_digits()
# print(digits.target)
# print(digits.images[0])