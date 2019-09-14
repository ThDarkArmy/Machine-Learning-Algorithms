import numpy as np 
import math

def GradientDescent(x,y):
    m_curr=b_curr=0
    iterations=2000-1
    n=len(x)
    learning_rate = 0.084
    for i in range(iterations):
#     i=1
#     while(True):
        y_predicted = m_curr*x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {} , cost {}, iteration {}".format(m_curr,b_curr,cost, i))
        i=i+1
        # if math.isclose(m_curr,b_curr,rel_tol = 1e-09, abs_tol = 0.009):
        #         break
        

if __name__ == "__main__":
        x = np.array([1,2,3,4,5])
        y = np.array([5,7,9,11,13])
        GradientDescent(x,y)





