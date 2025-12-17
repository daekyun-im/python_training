import pandas as pd

data = {
    "batch": ["B1","B1","B1","B2","B2","B2","B3","B3","B3"],
    "day":   [1,2,3,1,2,3,1,2,3],
    "value": [10,12,11,9,11,13,14,13,15]
}

df = pd.DataFrame(data)

# 1️⃣ 코딩 문제
# batch별로 value의 평균(mean) 을 계산하라.
# 결과를 아래 컬럼을 가진 DataFrame df_summary로 만들어라.
# batch
# mean_value
# 2️⃣ 분석 문제
# 전체 batch 평균(mean_value의 평균)을 계산하라.
# 각 batch가
# 전체 평균 이상인지(True/False) 를 나타내는 컬럼 above_overall_mean을 df_summary에 추가하라.
# 3️⃣ 시각화 문제
# matplotlib으로 batch별 평균 value bar plot을 그려라.
# x축: batch
# y축: mean_value
# 전체 평균 이상 batch → 파란색
# 전체 평균 미만 batch → 회색
# 전체 평균을 수평선으로 표시
# 범례 포함

# 조건
# groupby를 반드시 사용할 것
# for-loop 없이 해결할 것
# seaborn ❌

df_summary = pd.DataFrame(df.groupby('batch').mean()['value'])
df_summary = df_summary.reset_index()
df_summary.columns = ['batch','mean_value']
all_mean = df_summary['mean_value'].mean()
df_summary['above_overall_mean'] = df_summary['mean_value']>all_mean
import matplotlib.pyplot as plt
colors_list = df_summary['above_overall_mean'].map({True: "blue", False: "gray"})
legend_list = df_summary['above_overall_mean'].map({True: "above mean", False: "not above mean"})
plt.bar(df_summary['batch'],df_summary['mean_value'],  color=colors_list, label=df_summary['batch'])
plt.axhline(all_mean, color='lightgray', linestyle='--', linewidth=2, label = 'avg.')
plt.legend()

# 모범답안
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# data
data = {
    "batch": ["B1","B1","B1","B2","B2","B2","B3","B3","B3"],
    "day":   [1,2,3,1,2,3,1,2,3],
    "value": [10,12,11,9,11,13,14,13,15]
}
df = pd.DataFrame(data)

# 1) summary with groupby (no loops)
df_summary = (
    df.groupby("batch", as_index=False)["value"]
      .mean()
      .rename(columns={"value": "mean_value"})
)

# 2) overall mean + flag
overall_mean = df_summary["mean_value"].mean()
df_summary["above_overall_mean"] = df_summary["mean_value"] >= overall_mean

# 3) plot (colors + proper legend)
colors = df_summary["above_overall_mean"].map({True: "blue", False: "gray"})

plt.figure()
plt.bar(df_summary["batch"], df_summary["mean_value"], color=colors)
plt.axhline(overall_mean, linestyle="--", linewidth=2, label="Overall mean")

# custom legend for color meaning
legend_handles = [
    Patch(label="Above overall mean"),
    Patch(label="Below overall mean"),
]
plt.legend(handles=legend_handles + [plt.Line2D([0], [0], linestyle="--", linewidth=2, label="Overall mean")])

plt.xlabel("batch")
plt.ylabel("mean_value")
plt.title("Mean value by batch")
plt.tight_layout()
plt.show()

df_summary
