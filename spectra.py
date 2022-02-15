import matplotlib.pyplot as plt
import pandas as pd
import os

n = 411 
spectras = []
path = 'data'

files = os.listdir(path)
for filename in files:
    result = []
    file_properies = 'data\%s\properties.csv' % filename
    file_absorbtion = 'data\%s\\absorbtion.csv' % filename
    properties = pd.read_csv(file_properies, delimiter = ';')
    absorbtion = pd.read_csv(file_absorbtion, delimiter = ';')
    result = pd.concat([properties, absorbtion], ignore_index=True)
    spectras.append(result)
    plt.subplot(n)
    plt.plot(result['nm'], result.loc[:, '7':], label = result.columns[6:])
    plt.legend()
    title = result.loc[[0], 'spectrum_type':'surf_conc']
    plt.title(title.to_string(), fontsize=10, x=0.5, y=0.7)
    plt.ylabel('Интенсивность, у.е.')
    n += 1

print(spectras)
plt.xlabel('длина волны, нм')
plt.show()
