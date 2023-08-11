import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot:  # class for mandelbrot set
    def __init__(self):  # initializing first complex term, and initial n value
        self.z = complex(0.0, 0.0)
        self.n = 0

    def iteration(self, c):  # function to iterate through condition for mandelbrot set and return n value
        while self.n < 256 and abs(self.z) <= 2:
            self.n += 1
            self.z = self.z ** 2 + c
        return self.n


def main():
    # asking user for resolution of mandelbrot set
    res = int(input("Enter resolution: "))
    # creating data point for real components
    x_values = np.linspace(-2.025, 0.6, res)
    # creating data points for imaginary components
    y_values = np.linspace(-1.125, 1.125, res)
    # creating array of values to store iteration number for each complex number on grid
    n_values = np.zeros((res, res))

    for i in range(res):  # loop through each complex number and find corresponding n value
        for j in range(res):
            temp = Mandelbrot()
            n_values[i, j] = temp.iteration(complex(x_values[i], y_values[j]))

    plt.imshow(np.transpose(n_values), extent=(-2.025,
               0.6, -1.125, 1.125), cmap='cividis')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()


main()
