#!/usr/bin/env python
# coding: utf-8

# # import lib

# In[67]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import ast


# # Reading Files

# In[68]:


df_movies = pd.read_csv(r"C:\Users\navee\Downloads\movie_data\movies.csv")
df_ratings = pd.read_csv(r"C:\Users\navee\Downloads\movie_data\ratings.csv")
df_links = pd.read_csv(r"C:\Users\navee\Downloads\movie_data\links.csv")
df_tags = pd.read_csv(r"C:\Users\navee\Downloads\movie_data\tags.csv")


# In[69]:


df_movies


# In[70]:


df_ratings


# In[71]:


df_links


# In[72]:


df_tags


# # Download the data from the above link. How many ".csv" files are available in the dataset?

# #### ans: 4

# # What is the shape of "movies.csv"?
# 

# In[73]:


df_movies.shape


# # What is the shape of "ratings.csv"?
# *

# In[74]:


df_ratings.shape


# # How many unique "userId" are available in "ratings.csv"?
# *
# 

# In[75]:


unique_users = df_ratings['userId'].nunique()


# In[76]:


unique_users


# # Which movie has recieved maximum number of user ratings?
# 

# In[77]:


df_merge = df_movies.merge(df_ratings, how='inner', on = 'movieId')


# In[78]:


df_merge


# # Select all the correct tags submitted by users to "Matrix, The (1999)" movie?

# In[79]:


df_merge = df_movies.merge(df_tags, how='inner', on = 'movieId')


# In[80]:


df_merge 


# In[81]:


matrix_tags = df_merge[df_merge['title'] == 'Matrix, The (1999)']['tag'].tolist()
matrix_tags


# # What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?

# In[82]:


avg_ratings = df_ratings[df_ratings['movieId'].isin(df_movies[df_movies['title'] == 'Terminator 2: Judgment Day (1991)']['movieId'])]['rating'].mean()


# In[83]:


avg_ratings


# # How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?

# In[84]:


import matplotlib.pyplot as plt
import seaborn as sns

# FOCAL CELL
fight_club_ratings = df_ratings[df_ratings['movieId'].isin(df_movies[df_movies['title'] == 'Fight Club (1999)']['movieId'])]['rating']

plt.figure(figsize=(10, 6))
sns.countplot(x=fight_club_ratings, palette='viridis')
plt.title('User Ratings Distribution for "Fight Club (1999)"')
plt.xlabel('User Ratings')
plt.ylabel('Count')
plt.show()


# #### ans:Left Skewed Distribution

# # operations

# In[85]:


movie_ratings_stats = df_ratings.groupby('movieId')['rating'].agg(['count', 'mean'])


# In[86]:


movie_ratings_stats


# In[87]:


df_movies_ratings = df_movies.merge(movie_ratings_stats, how='inner', left_on='movieId', right_index=True)


# In[88]:


df_movies_ratings


# # Which movie is the most popular based on  average user ratings?
# 

# In[90]:


popular_movies_50_ratings = df_movies_ratings.sort_values(by='mean', ascending=False).head(50)
most_popular_movie = popular_movies_50_ratings[popular_movies_50_ratings['mean'] == popular_movies_50_ratings['mean'].max()]
most_popular_movie_title = most_popular_movie['title'].values[0]


# In[91]:


popular_movies_50_ratings


# In[95]:


most_popular_movie = popular_movies_50_ratings[popular_movies_50_ratings['mean'] == popular_movies_50_ratings['mean'].max()]
most_popular_movie_title = most_popular_movie['title'].values[0]


# In[96]:


most_popular_movie


# In[ ]:


3. Filter only those movies which have more than 50 user ratings (i.e. > 50).


# In[97]:


popular_movies_50_ratings = df_movies_ratings[df_movies_ratings['count'] > 50]


# In[98]:


popular_movies_50_ratings


# In[99]:


most_popular_movie = popular_movies_50_ratings[popular_movies_50_ratings['mean'] == popular_movies_50_ratings['mean'].max()]
most_popular_movie_title = most_popular_movie['title'].values[0]


# In[100]:


most_popular_movie


# In[102]:


top5_popular_movies = popular_movies_50_ratings.nlargest(5, 'count')['title'].tolist()


# # Select all the correct options which comes under top 5 popular movies based on number of user ratings.

# In[103]:


top5_popular_movies


# # Which Sci-Fi movie is "third most popular" based on the number of user ratings?

# In[104]:


third_most_popular_sci_fi = df_movies_ratings[df_movies_ratings['genres'].str.contains('Sci-Fi')].nlargest(3, 'count').iloc[-1]['title']


# In[105]:


third_most_popular_sci_fi


# In[ ]:




