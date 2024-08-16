from utils import filter_words, substitute_user_mentions_and_links, sample_rows, lemmatize, calculate_statistics
import pandas as pd
import random
random.seed(7)

df= pd.read_csv("ruslan_martsinkiv.csv")

df['text_mod'] = df['text'].apply(substitute_user_mentions_and_links)
df[['tokens', 'num_words']]  = df['text_mod'].apply(lambda x: pd.Series(filter_words(x)))

# Convert 'date_time' column to datetime type
df['date_time'] = pd.to_datetime(df['date_time'])

# Define the split date
split_date = pd.to_datetime('2023-02-25')

# Split the DataFrame into two groups based on the split date
before_date = df[df['date_time'] < split_date]
after_date = df[df['date_time'] >= split_date]

# Create an empty DataFrame to store the sampled rows
after_date_sampled_df = pd.DataFrame(columns=after_date.columns)  
before_date_sampled_df = pd.DataFrame(columns=before_date.columns)

sample_rows(after_date, after_date_sampled_df)
sample_rows(before_date, before_date_sampled_df)

print(after_date_sampled_df.num_words.sum())
print(before_date_sampled_df.num_words.sum())

after_date_sampled_df['lemmatized_words'] = after_date_sampled_df['tokens'].apply(lemmatize)
before_date_sampled_df['lemmatized_words'] = before_date_sampled_df['tokens'].apply(lemmatize)

# after_date_sampled_df.to_csv("after_date_sampled_df.csv")
# before_date_sampled_df.to_csv("before_date_sampled_df.csv")

after_date_sampled_df_stats = calculate_statistics(after_date_sampled_df)

before_date_sampled_df_stats = calculate_statistics(before_date_sampled_df)

df_stats = pd.DataFrame([before_date_sampled_df_stats, after_date_sampled_df_stats], index=['before_date', 'after_date'])

df_stats = df_stats.T

print(df_stats)