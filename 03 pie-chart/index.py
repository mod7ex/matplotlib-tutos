from matplotlib import pyplot as plt

plt.style.use('Solarize_Light2')

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(
    slices, 
    labels=None, 
    shadow=True,
    explode=explode,
    startangle=90,
    autopct='%1.1f%%',
    wedgeprops={'edgecolor': 'black'}
)

plt.title('Chart title here')
plt.legend(labels)
# plt.tight_layout()
plt.show()

