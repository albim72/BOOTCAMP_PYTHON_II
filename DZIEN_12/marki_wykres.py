import matplotlib.pyplot as plt

fig,ax = plt.subplots()

marki = ['audi','toyota','mercedes','honda','kia','jeep','seat']
sprzed = [12.7,28.9,9.8,16.8,23.5,7.8,28.3]

bar_labels = ['audi','toyota','mercedes','honda','kia','jeep','seat']
bar_colors = ['tab:red','tab:green','tab:red','tab:blue','tab:orange','tab:red','tab:green']

ax.bar(marki,sprzed,label=bar_labels,color=bar_colors)
ax.set_xlabel('sprzedaż wybranych marek')
ax.set_ylabel('marki samochodów')

ax.legend(title='marki')
plt.show()ck']
