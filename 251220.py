import pandas as pd

df_result = pd.DataFrame({
    "sample": ["S1","S2","S3","S4","S5"],
    "titer":  [2.1, 2.5, None, 2.9, 2.4]
})
df_cond = pd.DataFrame({
    "sample": ["S1","S2","S3","S4","S5"],
    "temp":   [36.5, 36.5, 37.0, 37.0, 36.5],
    "feed":   ["A",   "B",   "A",  "B",  "A"]
})
df_merged = pd.merge(df_result, df_cond, how='left', on='sample')
display(df_merged)
df_merged['titer']  =df_merged['titer'].fillna(df_merged.groupby('temp')['titer'].transform('mean'))
display(df_merged)
df_feed_mean = df_merged[['titer','feed']].groupby('feed').mean().reset_index()
df_feed_mean
