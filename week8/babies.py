from random import randint, random
import matplotlib.pyplot as plt
import numpy as np

def create_babies(quantity):
    babies = []

    for baby in range(quantity):
        
        age=randint(0,12)

        if(age<=5):
            heigth = randint(45,60)
            weigth = randint(2500,5000)

        if(age>5 and age<=10):
            heigth = randint(60,75)
            weigth = randint(5000,8000)

        if(age>10):
            heigth = randint(80,100)
            weigth = randint(8000,12000)

        babies.append((age,heigth,weigth))

    return babies




data_3d = create_babies(3000);

babies = np.array(data_3d)

print(babies)

x, y, z = babies[:,0], babies[:,1], babies[:,2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, linewidth=0.2)

plt.show()
