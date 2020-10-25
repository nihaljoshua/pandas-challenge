#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[34]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = ("Resources/purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(file_to_load)


# In[35]:


purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[36]:


player_count = len(purchase_data_df["SN"])


# In[37]:


print(player_count)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[38]:


unique_item_count = len(purchase_data_df["Item Name"].unique())

average_price = purchase_data_df["Price"].mean()


# In[39]:


summary_df = pd.DataFrame({"Number of Unique Items": [unique_item_count],
                              "Average Price": average_price})
summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[45]:


gender_group = purchase_data_df.groupby("Gender")

gender_work_df = pd.DataFrame(gender_group["Gender"].value_counts())
gender_work_df.head()

gender_work_df = gender_work_df.rename(
    columns={"Gender": "Gender Count"})
gender_work_df.head()


# In[42]:


player_count = len(purchase_data_df)
gender_player = Gender_group["Gender"].count()

gender_percent_df = pd.DataFrame((gender_player/player_count)*100)
gender_percent_df.head()

gender_percent_df = gender_percent_df.rename(
    columns={"Gender": "Percentage"})
gender_percent_df.head()


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[29]:


purchasing_analysis_male = purchase_data_df.loc[purchase_data_df["Gender"] == "Male"]
purchasing_analysis_male


# In[30]:


male_SN_group = purchasing_analysis_male.groupby("SN")

purchase_count = male_SN_group["Item Name"].value_counts()

purchase_price = male_SN_group["Price"].mean()

purchase_average = male_SN_group["Price"].sum()

summary_male_purchase_df = pd.DataFrame({"Purchase count": [purchase_count],
                                        "Average Purchase Price": [purchase_price],
                                        "Average Purchase": [purchase_average]})

summary_male_purchase_df.head()


# In[31]:


purchasing_analysis_female = purchase_data_df.loc[purchase_data_df["Gender"] == "Female"]
purchasing_analysis_female


# In[32]:


female_SN_group = purchasing_analysis_female.groupby("SN")

purchase_count = female_SN_group["Item Name"].value_counts()

purchase_price = female_SN_group["Price"].mean()

purchase_average = female_SN_group["Price"].sum()

summary_female_purchase_df = pd.DataFrame({"Purchase count": [purchase_count],
                                        "Average Purchase Price": [purchase_price],
                                        "Average Purchase": [purchase_average]})

summary_female_purchase_df.head()


# In[33]:


purchasing_analysis_other = purchase_data_df.loc[purchase_data_df["Gender"] == "Other / Non-Disclosed"]
purchasing_analysis_other


# In[34]:


other_SN_group = purchasing_analysis_other.groupby("SN")

purchase_count = other_SN_group["Item Name"].value_counts()

purchase_price = other_SN_group["Price"].mean()

purchase_average = other_SN_group["Price"].sum()

summary_other_purchase_df = pd.DataFrame({"Purchase count": [purchase_count],
                                        "Average Purchase Price": [purchase_price],
                                        "Average Purchase": [purchase_average]})

summary_other_purchase_df.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[35]:


print(purchase_data_df["Age"].max())
print(purchase_data_df["Age"].min())


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[36]:


bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50]
group_labels = ["0 to 5", "6 to 10", "11 to 15", "16 to 20", "21 to 25", "26 to 30", "31 to 35", "36 to 40", "41 to 50"]


# In[37]:


pd.cut(purchase_data_df["Age"], bins, labels=group_labels).head()


# In[38]:


purchase_data_df["Age"] = pd.cut(purchase_data_df["Age"], bins, labels=group_labels)
purchase_data_df.head()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[39]:


purchase_data_group = purchase_data_df.groupby(["SN"])
purchase_data_comparison_df = purchase_data_group.mean()
purchase_data_comparison_df

purchase_data_comparison_df["Total"] = purchase_data_comparison_df.sum(axis=1)
purchase_data_comparison_df["Total"]

topspenders_purchase_df = purchase_data_comparison_df.sort_values(["Total"], ascending=False)
topspenders_purchase_df.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[40]:


most_popular_df = purchase_data_df[["Item ID", "Item Name", "Price"]]
most_popular_df.head()


# In[67]:


average_price_mostpopular_item = most_popular_df["Price"].mean()
print(average_price_mostpopular_item)


# In[44]:


most_popular_group = most_popular_df.groupby(["Item ID", "Item Name"])
most_popular_group_work_df = pd.DataFrame(most_popular_group["Price"].value_counts())
most_popular_group_work_df.head()
most_popular_group_work_df = most_popular_group_work_df.rename(
    columns={"Price": "Purchase Count"})

most_popular_group_work_df = most_popular_group_work_df.reset_index()
most_popular_group_work_df.head()


# In[63]:


most_popular_group_work_df["Total"] = most_popular_group_work_df.sum(axis=1)
most_popular_group_work_df["Total"]


# In[64]:


most_popular_group_work_df = most_popular_group_work_df.merge(most_popular_group_work_df["Total"], on="Item ID")
most_popular_group_work_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[43]:


most_profitable_items_df = most_popular_group_work_df.sort_values(["Total Purchase Value"], ascending=False)
most_profitable_items_df.head()


# In[ ]:




