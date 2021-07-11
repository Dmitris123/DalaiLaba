import numpy as np
import matplotlib.pyplot as plt

def getInitialState(N): # задаём случайным образом начальное состояние системы 
    state0 = np.array([2*(np.round(np.random.rand(N))) - 1 for i in range(N)])
    return state0

def flipEnrg(state,i,j): # считаем изменение энергии при перевороте спиновой ячейки
    N = state.shape[0]
    
    if (j-1 < 0):
        jleft = N-1
    else:
        jleft = j-1
        
    if (j+1 > N-1):
        jright = 0
    else:
        jright = j+1
        
    if (i-1 < 0):
        iup = N-1
    else:
        iup = i-1
        
    if (i+1 > N-1):
        idown = 0
    else:
        idown = i+1
        
    dE = 2*state[i,j]*(state[i,jleft] + state[iup,j] + state[i,jright] + state[idown,j])
    return dE
   
def makeFlip(T, state): # функция для преворота спина
    newstate = state
    N = newstate.shape[0]
    arri = np.random.randint(0,N,N**2)
    arrj = np.random.randint(0,N,N**2) 
    for k in range(N**2):
        if (flipEnrg(newstate,arri[k],arrj[k]) < 0):
            newstate[arri[k],arrj[k]] = (-1)*newstate[arri[k],arrj[k]]
        else:
            probab = np.exp(-flipEnrg(newstate,arri[k],arrj[k]) / T)
            random = np.random.rand()
            if random < probab:
                newstate[arri[k],arrj[k]] = (-1)*newstate[arri[k],arrj[k]]
    return newstate

def getEnergy(state): # функция, считающая энергию состояния системы
    N = state.shape[0]
    E = 0 # Е - энергия
    for i in range(N):
        for j in range(N):
            
            if (j-1 < 0):
                jleft = N-1
            else:
                jleft = j-1
        
            if (j+1 > N-1):
                jright = 0
            else:
                jright = j+1
                
            if (i-1 < 0):
                iup = N-1
            else:
                iup = i-1
        
            if (i+1 > N-1):
                idown = 0
            else:
                idown = i+1
        
        E += -state[i,j]*(state[i,jleft] + state[iup,j] + state[i,jright] + state[idown,j])
        
    return E
        
def getMagnetization(state):   
    N = state.shape[0]
    M = 0
    for i in range(N):
        for j in range(N):
            M += state[i, j]
    return M


N = 64
state = getInitialState(N)
temp = state

    
plt.figure(figsize=(4,4))
plt.xlim((-1, 64))
plt.ylim((-1, 64))
plt.plot(np.nonzero(state - 1)[1], np.nonzero(state - 1)[0], '.', color = 'green')
plt.plot(np.nonzero(state + 1)[1], np.nonzero(state + 1)[0], '.', color = 'red')
plt.grid(False)
plt.title('Начальное состояние')
plt.axis('off')
plt.show()

for i in range(64):
    makeFlip(0.5, state);

plt.figure(figsize=(4,4))
plt.xlim((-1, 64))
plt.ylim((-1, 64))
plt.plot(np.nonzero(state - 1)[1], np.nonzero(state - 1)[0], '.', color = 'green')
plt.plot(np.nonzero(state + 1)[1], np.nonzero(state + 1)[0], '.', color = 'red')
plt.grid(False)
plt.title('Низкотемператерный переворот')
plt.axis('off')
plt.show()

state = temp

for i in range(64):
    makeFlip(100, state);

plt.figure(figsize=(4,4))
plt.xlim((-1, 64))
plt.ylim((-1, 64))
plt.plot(np.nonzero(state - 1)[1], np.nonzero(state - 1)[0], '.', color = 'green')
plt.plot(np.nonzero(state + 1)[1], np.nonzero(state + 1)[0], '.', color = 'red')
plt.grid(False)
plt.title('Высокотемпературный переворот')
plt.axis('off')
plt.show()  