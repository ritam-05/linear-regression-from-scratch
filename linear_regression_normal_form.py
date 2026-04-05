import numpy as np
def linear_regression(x_train,y_train,x):
    x_sum=x_train.sum()
    y_sum=y_train.sum()
    x_mean=x_sum/len(x_train)
    y_mean=y_sum/len(y_train)
    n=len(y_train)

    sum_x2=0
    for i in x_train:
        sum_x2+=i**2

    xy_sum = 0
    for i, j in zip(x_train, y_train):
        xy_sum += i * j

    w= (((n*xy_sum)-(x_sum*y_sum)) / ((n*sum_x2)-(x_sum**2)))

    b= y_mean - (w*x_mean)

    print(float(w*x + b)) 
    
    return w,b

# testing
x_train = np.array([1, 2, 3, 4, 5])
y_train = np.array([2, 4, 5, 6, 7])

print((linear_regression(x_train,y_train,10)))



    