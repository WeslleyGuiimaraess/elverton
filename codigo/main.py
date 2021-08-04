from timsort import timSort
import math
import matplotlib.pyplot as plt
import timeit as ti
import datetime as dt
import numpy as np

rand_seeds = [ 10, 24, 48, 76, 104 ]

array_sizes = [ 10**3, 10**4, 10**5, 10**6, 10**7]

extime = []
if __name__ == "__main__":

    for size_sizes in array_sizes:
        for seeds in rand_seeds:

            arr = np.loadtxt(f"../dados/entrada_{size_sizes}_{seeds}.dat", delimiter=",")
            arr.sort()
            begin_time = dt.datetime.now()
            timSort(arr)
            extime.append(dt.datetime.now() - begin_time)
           # np.savetxt( f'resultado_{size_sizes}_{seeds}.dat', arr, 
            #            delimiter=',', newline='\n')
    times = []

    sum = 0
    for i in range(5):

        sum = np.mean([e.total_seconds() for e in extime[i*5:(i+1)*5]])
        times.append(sum)
    
    print(times)
    plt.plot(array_sizes, times, label="timsort")

    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for i in range(10**3, 10**7, 10**3):
        x1.append(i)
        y1.append((i*math.log(i))/10**6)
        x2.append(i)
        y2.append((i/10**6))
    
    plt.plot(x1,y1, label = "O(n Log n)")
    plt.plot(x2, y2, label = "O(n)")
    plt.legend()

    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Tempo de Execução(segundos)")
    plt.show()
