import numpy as np
import matplotlib.pyplot as plt

""""
19.02.2021: 
There will be two Python classes. One for matrix (or generations) another for cells (or individuals)
Class Gen is meant to be for matrices. At the same will generate every individual.

22.02.2021
Two classes are unnecessary. I think I am going for a class that generates the generation background (new matrix).
And this class call for a function, that ensures that the new background already have the correct values for each of the squares.

I will not use classes anymore. It was resulting the a not subscriptable object and I do not know to deal with it.
I think I am going to create an "archive" for the last 1000 gen, in order to keep a record and to print in real-time.
"""

"""Initial variables. In the future they could be asked to the user"""
sizew = 64
sizeh = 64
memory = 50
ngen = auxp = k = i = 0
archiveGen = np.ones((memory, sizew, sizeh), dtype=np.int8)

"""Generating a new matrix"""
def Gen(sizew, sizeh, bgo):
   bg = np.empty((1, sizew,sizeh), dtype=np.int8)
   bg = fillGen(bg, bgo, sizew, sizeh)
   return bg

"""Show the generations"""
def PrintGen(bg, auxp):
    plt.imshow(bg, cmap='gray')
    plt.axis(False)
    plt.title("Generation:" + str(auxp))
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()
    """I have to think in a nice way of plotting each of the generations"""

"""Calculation of the new generation"""
def fillGen(bg, bgo, sizew, sizeh):
    """
    My old background is oldM. -> Use it to calculate nextM.
    First step:
    1. Sum the neighbors of each element on oldM.
    2. Pass the result through the rules
    3. Modified the element on nextM, accordingly
    """
    sumNeighbors = np.zeros((sizew, sizeh), dtype=np.int8)
    x = y = 0
    while x < sizew:
        while y < sizeh:
            """Step.1"""
            if (x > 0 and y > 0):
                sumNeighbors[x:x+1,y:y+1] = np.sum(bgo[0,x-1:x+2,y-1:y+2], dtype=np.int8)
            elif (x > 0 and y == 0):
               sumNeighbors[x:x+1,y:y+1] = np.sum(bgo[0,x-1:x+2,y:y+2], dtype=np.int8)
            elif (x == 0 and y > 0):
               sumNeighbors[x:x+1,y:y+1] = np.sum(bgo[0,x:x+2,y-1:y+2], dtype=np.int8)
            elif (x == 0 and y == 0):
                sumNeighbors[x:x+1,y:y+1] = np.sum(bgo[0,x:x+2,y:y+2], dtype=np.int8)
            
            if (sumNeighbors[x,y] != 0):
                sumNeighbors[x:x+1,y:y+1] -= np.sum(bgo[0,x:x+1,y:y+1], dtype=np.int8)
            
            """Step.2 and .3"""
            if (sumNeighbors[x,y] == 3 and bgo[0,x,y] == 0):
                bg[0,x:x+1,y:y+1] = 1
            elif (sumNeighbors[x,y] < 2 or sumNeighbors[x,y] > 3):
                bg[0,x:x+1,y:y+1] = 0
            elif (sumNeighbors[x,y] >= 2 or sumNeighbors[x,y] <= 3):
                bg[0,x:x+1,y:y+1] = bgo[0,x:x+1,y:y+1]
            else:
                bg[0,x:x+1,y:y+1] = bgo[0,x:x+1,y:y+1]

            y += 1
        y = 0
        x += 1
    return bg

"""Building a first random matrix"""
initM = oldM = np.random.randint(0,2, size=(1, sizew,sizeh), dtype=np.int8)
archiveGen = np.insert(archiveGen, ngen, oldM, axis=0)

"""
Eventually a while or for loop will start in here:
A condition for a while loop could be "while np.sum(nextM) != 0"
"""

while True:
    """Generating the  first matrix using the rules"""
    nextM = Gen(sizew, sizeh, oldM)
    #archiveGen = np.insert(archiveGen, ngen, nextM, axis=0)
    archiveGen[ngen] = nextM
    print(archiveGen[ngen-3])

    """When every individual of a generation dies..."""
    if np.sum(oldM) == 0:
        k += ngen
        print("The initial configuration was abel to survive ", str(k), "generations!")
        print("Initial configuration:")
        print(initM)
        break

    """In case of infinite loop of generations"""
    if (np.array_equal(archiveGen[ngen-2], archiveGen[ngen]) and np.array_equal(archiveGen[ngen-3], archiveGen[ngen-1])):
        k += ngen
        print("The initial configuration is capable of survive for infinite generations. Alternates between this two configurations after ", str(k), " generations:")
        print("Initial Configuration")
        print(initM)
        print("Final Configurations")
        print(archiveGen[ngen], "\n " ,archiveGen[ngen-1])
        break

    if (np.array_equal(archiveGen[ngen-3], archiveGen[ngen]) and np.array_equal(archiveGen[ngen-4], archiveGen[ngen-1]) and np.array_equal(archiveGen[ngen-5], archiveGen[ngen-2])):
        k += ngen
        print("The initial configuration is capable of survive for infinite generations. Alternates between this three configurations after ", str(k), " generations:")
        print("Initial Configuration")
        print(initM)
        print("Final Configurations")
        print(archiveGen[ngen], "\n " ,archiveGen[ngen-1], "\n " ,archiveGen[ngen-2])
        break

    if (np.array_equal(archiveGen[ngen-2], archiveGen[ngen]) and np.array_equal(archiveGen[ngen-1], archiveGen[ngen])):
        k += ngen
        print("The initial configuration is capable of survive for infinite generations. This 'infinite generation' was reached after ", str(k), " generations:")
        print("Initial Configuration")
        print(initM)
        print("Final Configuration")
        print(archiveGen[ngen])
        break

    ngen += 1
    oldM = nextM

    """Printing"""
    auxp += 1
    PrintGen(archiveGen[i], auxp)
    i += 1

    """Limits the archiveGen to have stored only 50 generations"""
    if i >= memory:
        k += ngen
        ngen = 0
        i = 0



