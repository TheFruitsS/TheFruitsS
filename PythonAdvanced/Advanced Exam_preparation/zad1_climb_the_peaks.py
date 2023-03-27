import numpy as np
from numpy import dtype

def climbing(data1, data2):
    data_tops = ['Vihren',
                'Kutelo',
                'Banski Suhodol',
                'Polezhan',
                'Kamenitza']


    data1.reverse()
    data_hills = np.add(data1, data2)
    print(data_hills)

    for info in data_hills:
        print(info)

    #     if int(clim1) + int(clim2) < 80:
    #         data1.pop(-1)
    #         data2.pop(0)
    #     if int(clim1) + int(clim2) >= 80:
    #         data1.pop(-1)
    #         data2.pop(0)
    #         data_hills.append(data_tops[0])
    #
    #     elif int(clim1) + int(clim2) < 90:
    #         data1.pop()
    #         data2.pop(0)
    #     elif int(clim1) + int(clim2) >= 90:
    #         data_hills.append(data_tops[1])
    #
    #     elif int(clim1) + int(clim2) < 100:
    #         data1.pop()
    #         data2.pop(0)
    #     elif int(clim1) + int(clim2) >= 100:
    #         data_hills.append(data_tops[2])
    #
    #     elif int(clim1) + int(clim2) < 60:
    #         data1.pop()
    #         data2.pop(0)
    #     elif int(clim1) + int(clim2 >= 60:
    #         data_hills.append(data_tops[3])
    #
    #     elif int(clim1) + int(clim2) < 70:
    #         data1.pop()
    #         data2.pop(0)
    #
    #     elif int(clim1) + int(clim2) >= 70:
    #         data_hills.append(data_tops[4])
    #     elif len(data_hills) == 5:
    #         print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\n"
    #               "Conquered peaks:")
    #         for hills in data_hills:
    #             print(hills)
    #     else:
    #         print( "Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    #     print(data_hills)

data1 = input().split(',')
data2 = input().split(',')
data1 = list(map(int, data1))
data2 = list(map(int, data2))



climbing(data1, data2)

