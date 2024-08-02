import matplotlib.pyplot as plt

animal = "urogallo"
años = [2021, 2022, 2023]
ejemplares = [190, 193, 201]
stdev = [5.5, 6.3, 7.1]

plt.bar(años, ejemplares, yerr=stdev)
plt.ylim(185, 205)
plt.xticks(años)
plt.show()
