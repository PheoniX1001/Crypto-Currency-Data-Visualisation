import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Data reading and basic cleaning:
file_path='/home/sulav/Desktop/python/plt/Crypto_data.csv'
df=pd.read_csv(file_path)
print(f'''
	Keys: \n{df.keys()}
	Head: \n{df.head(5)}
	Tail: \n{df.tail(5)}
	''')
df['Date']=pd.to_datetime(df['Date'])

#Visualization
#1.Histogram for bitcoin prices and frequency:
plt.figure(figsize=(10,10))
sns.histplot(df['Bitcoin (USD)'],kde=True,bins=30)
plt.title('Distribution of Bitcoin prices')
plt.xlabel('Bitcoin (USD)')
plt.ylabel('Frequency')
plt.savefig('Bitcoin_histogram.png')
plt.close()
#2.Correlation Heatmap
num_type=df.select_dtypes(include=[np.number])
if num_type.shape[1]>=4:
	plt.figure(figsize=(10,10))
	c_mat=num_type.corr()
	print(c_mat)
	sns.heatmap(c_mat,annot=True,cmap='coolwarm',fmt='.2f')
	plt.title('Correlation heatmap')
	plt.savefig('Correlation_map.png')
	plt.close()
else:
	print('Mapping for columns less than 4 is insignificant')

#3.Trend analysis  with rolling average over 30 day window
df.set_index('Date',inplace=True)
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(12,12))
fig.suptitle('Cryptocurrency price trend',fontsize=16)
df['Bitcoin avg']=df['Bitcoin (USD)'].rolling(window=30).mean()
df['Ethereum avg']=df['Ethereum (USD)'].rolling(window=30).mean()

#plotting bitcoin all time vs 30d averages
axes[0].plot(df['Bitcoin (USD)'],label='Daily price',color='green',alpha=0.5)
axes[0].plot(df['Bitcoin avg'],label='Monthly (average) price',color='orange',linewidth=2)
axes[0].set_title('Daily vs Monthly average Bitcoin price')
axes[0].set_ylabel('Price in USD')
axes[0].set_xlabel('Date')
axes[0].legend()
axes[0].grid(True,linestyle='--',alpha=0.6)

#plotting ethereum all time vs 30d averages
axes[1].plot(df['Ethereum (USD)'], label='Daily Price', color='purple', alpha=0.5)
axes[1].plot(df['Ethereum avg'], label='Monthly (average) price', color='darkviolet', linewidth=2)
axes[1].set_title('Daily vs Monthly average Ethereum price')
axes[1].set_ylabel('Price in USD')
axes[1].set_xlabel('Date')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout(rect=[0,0.03,1,0.95])
plt.savefig('ethereum_vs_bitcoin.png')
plt.close()
#4. Correlation between rise of ethereum and bitcoin by scatter plot
plt.figure(figsize=(9,9))
sns.regplot(x=df['Bitcoin (USD)'],y=df['Ethereum (USD)'],color='blue',scatter_kws={'alpha':0.6},line_kws={'color':'red'})
plt.title('Correlation bewtween Ethereum and Bitcoin in USD')
plt.xlabel('Bitcoin Price')
plt.ylabel('Ethereum Price')
plt.grid(True,linestyle='--')
plt.savefig('Correlation_between_bitcoin_and_ethereum.png')
plt.close()
Corl=df['Bitcoin (USD)'].corr(df['Ethereum (USD)'])
print(f'\nThe correlation between Bitcoin and Ethereum is: {Corl:.4f} ')
