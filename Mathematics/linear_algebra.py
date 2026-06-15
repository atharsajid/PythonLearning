import matplotlib.pyplot as plt
import seaborn as sns


# y=−x+3

no_of_points = 5
y = []
x = []

for i in range(no_of_points+1):
    x.append(i)
    value = -(i) + 3
    y.append(value)



plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")

