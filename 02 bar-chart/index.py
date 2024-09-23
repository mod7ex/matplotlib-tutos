from matplotlib import pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')

ages_x = [x for x in range(25, 36)]
x_indexes = np.arange(len(ages_x))
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

_width = (x_indexes[1] - x_indexes[0])/5

plt.bar(
    x_indexes - _width,
    py_dev_y,
    width=_width,
    color='red',
    label="Python"
)
plt.bar(
    x_indexes,
    js_dev_y,
    width=_width,
    color='#2cff05', 
    label="JavaScript"
)
plt.bar(
    x_indexes + _width,
    dev_y,
    width=_width,
    color="b",
    label="All devs"
)

plt.xticks(ticks=x_indexes, labels=ages_x)
plt.xlabel('Age')
plt.ylabel('Median salary (USD)')
plt.title('Median salary (USD) by age')
plt.legend()
plt.show()

