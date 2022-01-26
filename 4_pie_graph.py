import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()

vals = [23, 16, 21, 18, 22]
x = 'category: '
labels = [f'{x}food', f'{x}transport', f'{x}entertainment', f'{x}medicine', f'{x}other']
exp = (0.1, 0.1, 0.1, 0.1, 0.1)
ax.pie(vals, labels=labels, autopct='%.2f', explode=exp, shadow=True)
ax.grid()

plt.show()