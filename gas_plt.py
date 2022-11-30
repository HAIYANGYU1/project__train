import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gas_data = pd.read_csv('gas_prices.csv')

fig,axes = plt.subplots(2,2)
fig.set_facecolor('yellow')
axes[0][1].plot(gas_data.Year,gas_data.Germany)
axes[0][0].bar(gas_data.Year,gas_data.Canada)
axes[1][0].hist(gas_data.Year,gas_data.France,bins=1,rwidth=1,edgecolor='black',color='blue')
axes[1][1].pie(gas_data.Year,gas_data.Italy,autopct='%.2f %%')
plt.title('gas')
plt.show()