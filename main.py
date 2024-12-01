import matplotlib.pyplot as plt
from R_x_y_functions.functions import *

noise = numpy.random.normal(0, 0.5, 501)

y = [i for i in range(len(noise))]
d = numpy.var(noise)
m = numpy.mean(noise)

plt.plot(y, noise, color='red', label="Белый шум")
plt.legend()
plt.grid()
plt.show()

print("Дисперсия: 0.25")
print("Дисперсия фактически: ", float(d))
print("Погрешность составила: ", abs(float(d) - 0.25))
print("Мат. ожидание: 0")
print("Мат. ожидание фактически: ", float(m))
print("Погрешность составила: ", float(m))

plt.plot(y[:16], Rxx(noise))

corr_noise = [0 for i in range(0, len(noise))]
corr_noise[0] = d

plt.plot(y[:16], corr_noise[:16])
plt.legend(["Корреляционная ф. Rxx", "Корреляционная ф. белого шума"])
plt.grid()
plt.show()

function = [0 for i in range(501)]
function[0] = noise[0]

# y(k)=0.8y(k-1)+x(k)k = 0,500

y[0] = 0
for i in range(1, len(noise)):
    y[i] = (y[i - 1] * 0.8 + noise[i])

d = numpy.var(y)
m = numpy.mean(y)

print("Дисперсия: ", 0.25 / 0.36)
print("Дисперсия фактически: ", float(d))
print("Погрешность составила: ", abs(float(d) - 0.25 / 0.36))
print("Мат. ожидание: 0")
print("Мат. ожидание фактически: ", float(m))
print("Погрешность составила: ", float(m))

x = [i for i in range(len(noise))]

plt.plot(x, y)
plt.legend(["y(k)=0.8y(k-1)+x(k)k = 0,500"])
plt.grid()
plt.show()

plt.plot(x[:16], Rxx(y))
plt.plot(x[:16], Rxx(noise))
plt.legend(["Корреляционная ф. Rxx", "Корреляционная ф. Ryy"])
plt.grid()
plt.show()

plt.plot(x[:16], Rxy(noise, y))
plt.legend(["Корреляционная ф. Rxy"])
plt.grid()
plt.show()
