import pandas as pd

data = {
    "day": [1,2,3,4,5,6],
    "temp": [36.5, 36.7, 36.6, 36.9, 37.1, 36.8],
    "ph":   [7.1,  7.0,  7.0,  6.9,  6.8,  6.9]
}

df = pd.DataFrame(data)

df['temp_diff'] =df['temp'].diff(periods=1)
df['ph_diff'] = df['ph'].diff(periods=1)
display(df)
selected_days = list(df[(df['temp_diff']>0) & (df['ph_diff']<0)]['day'])
display(selected_days)
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
plt.plot(df['day'], df['temp'], color = 'red', marker='o', label='Temperature')
plt.plot(df['day'], df['ph'],  color = 'blue', marker='s', label='pH')
# for x_point in selected_days:
#     plt.axvline(x=x_point, color='gray', linestyle='--', alpha=  0.5)
ymin, ymax = plt.ylim()
plt.vlines(x=selected_days, ymin=ymin, ymax=ymax,  colors='gray', linestyle='--', alpha=  0.5)
plt.xlabel('Day')
plt.ylabel('Value')
plt.title("Temperature and pH Trend")
plt.legend()
plt.grid(False)
plt.tight_layout()
