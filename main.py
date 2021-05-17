import matplotlib.pyplot as plt
import numpy as np
import sympy


def get_fuc(x1, y1, x2, y2):
    k = sympy.Symbol('x')
    b = sympy.Symbol('y')
    a = sympy.solve([x1 * k + b - y1, x2 * k + b - y2], [k, b])
    return a


def get_fuc2(x, y):
    k_s = sympy.Symbol('x')
    a = sympy.solve(y - k_s * x, k_s)
    return float(a[0])


def fuc(k, b):
    plt.grid()
    plt.rcParams['axes.unicode_minus'] = True
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    if 10 > k > -10 and 10 > b > -10:
        x = np.arange(-10, 10, 0.1)
    elif k > 0 and 10 > b > -10:
        x = np.arange(-k * 10, k * 10, 0.1)
    elif 10 > k > -10 and b > 10:
        x = np.arange(-k * 10, 10 + b, 0.1)
    elif 10 > k > -10 > b:
        x = np.arange(-10 + b, 10, 0.1)
    else:
        x = np.arange(10 * k, -k * 10, 0.1)
    y = k * x + b
    if b > 0:
        t = "y=" + str(float(k)) + "x+" + str(float(b))
        plt.title(t)
    elif b < 0:
        t = "y=" + str(float(k)) + "x" + str(float(b))
        plt.title(t)
    else:
        t = "y=" + str(float(k)) + "x"
        plt.title(t)
    plt.plot(x, y)
    plt.show()


def main():
    while True:
        chosen = int(float(input("解正比例函数输入1，解一次函数输入2:")))
        if chosen == 1:
            x1 = float(input("输入点的x值："))
            y1 = float(input("输入点的y值："))
            a = get_fuc2(x1, y1)
            print("k=", a)
            print("已经自动画出函数图像")
            fuc(a, 0)
        if chosen == 2:
            x1 = float(input("输入第一个点的x值："))
            y1 = float(input("输入第一个点的y值："))
            x2 = float(input("输入第二个点的x值："))
            y2 = float(input("输入第二个点的y值："))
            a = get_fuc(x1, y1, x2, y2)
            t = []
            for item in a.keys():
                t.append(a[item])
            print("k=", str(float(t[0])))
            print("b=", str(float(t[1])))
            print("图像与y的交点(0,", str(float(t[0])), ")")
            print("图像与x的交点(", -(float(t[1])) / float(t[1]), ",0)")
            print("已经自动画出函数图像")
            fuc(float(t[0]), t[1])


if __name__ == '__main__':
    main()
