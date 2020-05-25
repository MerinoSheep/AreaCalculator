import tkinter as tk
import scipy.integrate
import numpy as np


class IntegralWindow:
    def __init__(self, master,startrange,endrange,n,fx):
        self.master = master
        master.title("window")
        master.geometry("200x180")
        self.startrange = startrange
        self.endrange = endrange
        self.n = n
        self.fx = fx
        self.integrate_label = tk.Label(text="Integral:")
        self.integrate_answer = tk.Label()
        self.integrate_label.grid(row=0, column=0)
        self.integrate_answer.grid(row=0, column=1)
        self.width = (endrange - startrange)/n
        # left riemann sum
        self.lr_sum_label = tk.Label(text="Left Riemann Sum:")
        self.lr_sum = tk.Label()
        self.lr_sum.grid(row=1, column=1)
        self.lr_sum_label.grid(row=1, column=0)

        #right riemann sum
        self.rr_sum = tk.Label()
        self.rr_sum_label = tk.Label(text="Right Riemann Sum")
        self.rr_sum.grid(row=1, column=0)
        self.rr_sum_label.grid(row=2, column=0)
        self.rr_sum.grid(row=2, column=1)

        #middle riemann sum
        self.mr_sum_label = tk.Label(text="Middle Riemann Sum")
        self.mr_sum = tk.Label()
        self.mr_sum_label.grid(row=3, column=0)
        self.mr_sum.grid(row=3, column=1)

        #Trapezoid sum
        self.trpz_sum_label = tk.Label(text="Trapezoidal Sum")
        self.trpz_sum = tk.Label(text =trapezoid(self,self.fx))
        self.trpz_sum_label.grid(row=4,column=0)
        self.trpz_sum.grid(row=4,column=1)
        ######
        self.integrate(startrange, endrange,n,fx)
    def integrate(self, startrange, endrange, N, fx):

        self.function = eval("lambda x:{}".format(fx))
        self.i = scipy.integrate.quad(self.function, self.startrange, self.endrange)
        self.integrate_answer['text'] = str(self.i[0])
        # left riemann sum
        self.lr_sum['text'] =riemann(self,self.startrange, self.endrange, self.n, self.fx, self.width)
        # right riemann sum
        self.rr_sum['text']=riemann(self,
            endrange, startrange, N, fx, self.width)
        # middle riemann sum
        self.mr_sum['text']=riemann(self,
            startrange+self.width/2, (endrange+self.width/2), N, fx, self.width)
        # Trapezoid Sum



def riemann(self,startrange, endrange, N, fx, width):
    points = np.linspace(startrange, endrange, num=N, endpoint=False)
    func_points = []
    for i in points:
        func_points.append(f(self,i, fx))
    func_points = np.asarray(func_points)
    indv_area = func_points*width
    return np.sum(indv_area)


def trapezoid(self,fx):
    #print(self.width)
    points = np.arange(self.startrange, self.endrange, self.width)
    points = np.append(points, self.endrange)
    print(points)
    func_points = []
    for i in points:
        func_points.append(f(self, i, fx))
    #print(func_points)
    ans = np.trapz(func_points, dx=self.width)
    return ans

def f(self,x, fx):
    x = x
    return eval(fx)


root = tk.Tk()
integral_window = IntegralWindow(root, 0, 5, 10,'2*x')
#integral_window.integrate(0, 5, 10, '2*x')
root.mainloop()


if __name__ == "__main__":
    pass
