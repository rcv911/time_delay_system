from numpy import *

##-----------------------iteration--------------------------------##
def xy_iteration(tau1, tau2, epsx, epsy, lam1, lam2, step, x0, y0, n, coef):
    #parameters---------------
    mas_x = zeros(n)
    mas_y = zeros(n)
    mas_x[0] = x0
    mas_y[0] = y0
    cut = 1000 # how many dots do you want to show
    dlina = n - cut
    
    #x_system----------------
    for i in range(1,tau1):
        mas_x[i] = mas_x[i-1] 

    for i in range(tau1,n):
        mas_x[i] = (step/epsx)*(-mas_x[i-1] + (lam1 - (mas_x[i-tau1-1]*mas_x[i-tau1-1]))) + mas_x[i-1] 
    
    # #y_system----------------
    for i in range(1,tau2):
        mas_y[i] = mas_y[i-1] 

    for i in range(tau2,n):
        mas_y[i] = (step/epsy)*(-mas_y[i-1] + (coef * mas_x[i-1]) + ((1 - coef)*(lam2 - (mas_y[i-tau2-1]*mas_y[i-tau2-1])))) + mas_y[i-1] 
        
        # mas_y[i] = (step/eps)*(-mas_y[i-1] + (coef * (mas_x[i-1]-mas_y[i-1])) + (lam2 - (mas_y[i-tau2-1]*mas_y[i-tau2-1]))) + mas_y[i-1]

    #result------------------
    return mas_x[dlina:], mas_y[dlina:]
    # return mas_x, mas_y

##-------------------------body code-----------------------------##
#parameters
N = 1000000
delay_1 = 100 # time delay
delay_2 = 110 # time delay
epsilon_x = 10 # inertia parameter
epsilon_y = 9 # inertia parameter 
lambda1 = 1.6 # nonlinearity parameter
lambda2 = 1.7 # nonlinearity parameter
dt = 1
x0 = 0.05
y0 = 0.00

k = 0.10 # 

#generation   <-----------------------------------------------
x, y = xy_iteration(delay_1, delay_2, epsilon_x, epsilon_y, lambda1, lambda2, dt, x0, y0, N, k)

###draw
import matplotlib.pyplot as plt
plt.xlabel('t')
plt.ylabel('data')
plt.grid()
plt.plot(x, 'r', label = 'x -> tau = '+str(delay_1)+', lam = '+str(lambda1)+', eps = ' +str(epsilon_x), lw = 2)
plt.plot(y, 'b', label = 'y -> tau = '+str(delay_2)+', lam = '+str(lambda2)+', eps = ' +str(epsilon_y), lw = 2)
plt.legend(loc='best')
plt.show()
print('done')
