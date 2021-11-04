import matplotlib.pyplot as plt, matplotlib.colors as mccolours
import numpy as np
import seaborn

linestyles = ["-", "--", "-.", ":"]

# x = np.linspace(-10, 10, 100)
# for i, ls in enumerate(linestyles):
#     y = 3.5 - 2.3 * (x + i) + 0.5 * (x + i) ** 2
#     matplotlib.pyplot.plot(x, y, linestyle=ls, label=ls)
    

# plot the data
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

cp = seaborn.color_palette('colorblind', 6)
for i in range(6):
    c = "C{}".format(i)
    plt.axvline(i, color=c, label=c)

plt.xlim([-1, 6])
plt.legend(loc="upper right")
plt.show()
