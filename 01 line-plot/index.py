from matplotlib import pyplot as plt

# print(plt.style.available)

plt.style.use('Solarize_Light2')
# plt.xkcd() # comec, for fun

ages_x = [x for x in range(25, 36)]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# Ages 18 to 55
ages_x = [x for x in range(18, 56)]
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000, 78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232, 78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# plt.plot(ages_x, dev_y, 'k--',label="All devs")
# plt.plot(ages_x, py_dev_y, 'b',label="Python")

plt.plot(
    ages_x,
    py_dev_y,
    # color='#444',
    # marker=".",
    # linewidth=3,
    label="Python"
)
plt.plot(
    ages_x,
    js_dev_y,
    # color='#2cff05', 
    # marker="o",
    # linewidth=3,
    label="JavaScript"
)
plt.plot(
    ages_x,
    dev_y,
    color="k", # for color check docs
    linestyle='--',
    label="All devs"
)

plt.xlabel('Age')
plt.ylabel('Median salary (USD)')
plt.title('Median salary (USD) by age')
# plt.grid(True)
plt.legend()
# plt.tight_layout()
# plt.savefig('plot.png')
plt.show()

