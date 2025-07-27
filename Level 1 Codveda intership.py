#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd

#Load CSV file 
data  = pd.read_csv("churn-bigml-80.csv")
data.head(10)


# In[32]:


#data cleaning
#Find the missing Value
data.isnull().sum()
print(df.isnull().sum())


# In[33]:


# 2. find  duplicate rows
duplicates = data.duplicated().sum()
print(f"\n🧾 Number of duplicate rows: {duplicates}")


# In[26]:


# 3. Standardize 'Yes/No' columns to 1/0
# Now safely map 'Yes'/'No' to 1/0
data['International plan'] = data['International plan'].map({'Yes': 1, 'No': 0})
data['Voice mail plan'] = data['Voice mail plan'].map({'Yes': 1, 'No': 0})

# Check the result
print(data[['International plan', 'Voice mail plan']].head())



# In[34]:


# Convert 'Churn' from boolean to integer
data['Churn'] = data['Churn'].astype(int)

print(data['Churn'].head())



# In[35]:


# 5. Final data check
print("\n Cleaned Data Info:")
print(data.info())


# In[30]:


#  Save the cleaned dataset
df.to_csv("cleaned_churn_data.csv", index=False)


# In[36]:


#task2 level 1
import matplotlib.pyplot as plt
import seaborn as sns


# In[38]:


print(" Summary Statistics:")
print(data.describe())


# In[44]:


# Mean
# Calculate the mean of all numeric columns
mean_data = data.mean(numeric_only=True)

#  Print the mean values with a clear label
print(" Mean of Each Numeric Column:\n")

print(mean_data)


# In[46]:


# Calculate the median of all numeric columns
median_data = data.median(numeric_only=True)

# Print the median values with a clear label
print("Median of Each Numeric Column:\n")
print(median_data)


# In[47]:


#  Calculate mode of numeric columns
mode_data = data.mode().iloc[0]

# Print the result
print(" Mode of Each Column:\n")
print(mode_data)


# In[48]:


# Calculate standard deviation of numeric columns
std_values = data.std(numeric_only=True)

# ✅ Print the result
print(" Standard Deviation of Each Numeric Column:\n")
print(std_values)


# In[49]:


#Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Plot histograms for all numeric columns
data.hist(bins=30, figsize=(15, 12), edgecolor='black')
plt.suptitle(" Histograms of Numeric Features", fontsize=16)
plt.tight_layout()
plt.show()


# In[50]:


# Boxplots for numeric columns
plt.figure(figsize=(15, 8))
sns.boxplot(data=data.select_dtypes(include='number'))
plt.xticks(rotation=90)
plt.title(" Boxplots of Numeric Features")
plt.show()


# In[51]:


# Scatter plot of Total day minutes vs. Total day charge
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Total day minutes', y='Total day charge', data=data)
plt.title('💬 Total Day Minutes vs. Total Day Charge')
plt.xlabel('Total Day Minutes')
plt.ylabel('Total Day Charge')
plt.show()


# In[52]:


#Scatter Plot: Total Intl Minutes vs. Total Intl Charge
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Total intl minutes', y='Total intl charge', data=data)
plt.title(' Intl Minutes vs Intl Charge')
plt.xlabel('Total Intl Minutes')
plt.ylabel('Total Intl Charge')
plt.show()


# In[53]:


# Total Day Minutes vs Day Charge, colored by Churn
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Total day minutes', y='Total day charge', hue='Churn', data=data)
plt.title('📈 Total Day Minutes vs Charge (Colored by Churn)')
plt.xlabel('Total Day Minutes')
plt.ylabel('Total Day Charge')
plt.legend(title='Churn')
plt.show()


# In[56]:


#Perform Correlation Analysis
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlation only for numeric columns
correlation_matrix = data.select_dtypes(include='number').corr()

#  Plot a heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("🔗 Correlation Heatmap")
plt.show()



# In[57]:


#task 3 visualization
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', data=data)
plt.title(" Count of Churned vs Non-Churned Customers")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.show()


# In[58]:


# Prepare average charges
avg_charges = data[['Total day charge', 'Total eve charge', 'Total night charge', 'Total intl charge']].mean()

# Plot
plt.figure(figsize=(8, 5))
avg_charges.plot(kind='line', marker='o')
plt.title(" Average Call Charges by Time of Day")
plt.ylabel("Average Charge ($)")
plt.xlabel("Time Period")
plt.grid(True)
plt.show()


# In[59]:


plt.figure(figsize=(6, 4))
sns.scatterplot(x='Total day minutes', y='Total day charge', hue='Churn', data=data)
plt.title("📍 Day Minutes vs Day Charge (Colored by Churn)")
plt.xlabel("Total Day Minutes")
plt.ylabel("Total Day Charge")
plt.legend(title='Churn')
plt.show()


# In[60]:


plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', data=data)
plt.title("Churn Distribution")
plt.savefig("churn_bar_plot.png")  # Saves to your working directory
plt.show()


# In[ ]:




