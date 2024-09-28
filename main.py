
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Housing.csv.csv')


fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].hist(df['area'], bins=20, color='blue', alpha=0.7)
axs[0].set_title('Histogram of Area')
axs[0].set_xlabel('Area')
axs[0].set_ylabel('Frequency')

axs[1].hist(df['bedrooms'], bins=10, color='green', alpha=0.7)
axs[1].set_title('Histogram of Bedrooms')
axs[1].set_xlabel('Bedrooms')
axs[1].set_ylabel('Frequency')

axs[2].hist(df['stories'], bins=10, color='orange', alpha=0.7)
axs[2].set_title('Histogram of Stories')
axs[2].set_xlabel('Stories')
axs[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()


avg_bathrooms = df.groupby('bathrooms')['price'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='bathrooms', y='price', data=avg_bathrooms, palette='viridis')
plt.title('Average House Prices by Number of Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Price')
plt.show()


avg_furnishing = df.groupby('furnishingstatus')['price'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='furnishingstatus', y='price', data=avg_furnishing, palette='viridis')
plt.title('Average House Prices by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()


correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()
