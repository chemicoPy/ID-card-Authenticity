import numpy as np
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


freq = array([4.040, 3.760, 3.600, 3.030, 2.560, 1.000])
voltage = array([-158.594, -120.000, -100.000, -50.000, -25.000, 0])

arrange = {"Frequency(GHz)":freq, "Voltage(V)": voltage}
data = pd.DataFrame(arrange)

print("Table of values")
print("")
print(data)

fig, ax = plt.subplots()

plt.grid()
plt.xlabel('Voltage(V)', fontsize=10)
plt.ylabel('Frequency(GHz)',fontsize=10)
plt.title('Frequency(GHz) versus Voltage(V).',fontsize=13, color = "black")
plt.yticks(color='green')
plt.xticks(color='green')

line, = ax.plot(voltage,freq, color="red")
f = np.linspace(0,10,100)

plt.scatter(voltage,freq, color ='black')


def animate_graph(digits,x,y,line):
    line.set_data(x[:digits], y[:digits])
    return line,

animation = FuncAnimation(fig, animate_graph, len(voltage), fargs=[voltage,freq,line], interval = 300, blit=True)

animation.save("Frequency vs Voltage animated graph.gif")


plt.show()





