from matplotlib import pyplot as plt

hours = [9, 10, 11, 12, 13, 14, 15, 16]
inside_temperatures = [25.2, 26.1, 27.3, 28.4, 29.6, 29.1, 30.4, 30.2]
outside_temperatures = [24.2, 25.1, 26.3, 27.4, 28.6, 28.1, 29.4, 29.2]

plt.plot(hours, inside_temperatures, label="Inside")
plt.plot(hours, outside_temperatures, label="Outside")
label_fontsize = 14
plt.xlabel("")
plt.ylabel("")

plt.show()
