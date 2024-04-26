import matplotlib.pyplot as plt

x_values = list(range(1, 1000 + 1))
y_values = [i ** 2 for i in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.plot(x_values, y_values,  linewidth=3)

# Назначение загаловка диограммы и меток сетей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта и делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапозона для каждой оси
ax.axis = ([0, 1100, 0, 1100000])

plt.show()