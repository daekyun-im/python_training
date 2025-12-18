# 1️⃣ 코딩 문제
# day별로 value의 합(total)을 계산해서 df에 새로운 컬럼 total로 붙여라.
# (힌트: groupby + transform)
# 각 행에 대해 fraction = value / total 을 계산해서 df에 fraction 컬럼을 추가하라.
# day가 1~4일 때, 각 nutrient의 fraction이 어떻게 변하는지 보기 위해
# 다음 형태의 요약 테이블 pivot_frac을 만들어라.
# index: day
# columns: nutrient
# values: fraction
# 2️⃣ 시각화 문제 (명시 조건 아주 구체적)
# pivot_frac를 이용해 stacked bar plot(누적 막대그래프) 을 그려라.
# 그래프 요구사항 (반드시 그대로)
# 차트 타입: stacked bar
# x축: day (1,2,3,4)
# y축: fraction (0~1 범위)
# 제목(title): "Nutrient Fraction by Day"
# x축 라벨(xlabel): "Day"
# y축 라벨(ylabel): "Fraction of Total"
# x tick:
# 위치: day 값(1,2,3,4)
# 라벨: "D01", "D02", "D03", "D04" 로 표시
# y tick:
# 0.0 ~ 1.0을 0.2 간격으로 표시 (0.0,0.2,0.4,0.6,0.8,1.0)
# legend:
# 표시 위치: upper right
# legend 제목: "Nutrient"
# legend 항목 순서: Glu, Gln, Lac (이 순서 고정)
# grid:
# y축 방향으로만 점선 그리드 표시 (--)
# figure size:
# (8, 4) 로 설정
# 마지막에 plt.tight_layout() 호출

# 조건
# pandas: groupby, transform, pivot 또는 pivot_table 중 최소 2개 이상 사용
# matplotlib만 사용 (seaborn ❌)
# for-loop 없이 풀기

import pandas as pd

data = {
    "day": [1,1,1, 2,2,2, 3,3,3, 4,4,4],
    "nutrient": ["Glu","Gln","Lac", "Glu","Gln","Lac", "Glu","Gln","Lac", "Glu","Gln","Lac"],
    "value": [5.0, 2.0, 0.5,  4.5, 1.8, 0.9,  4.0, 1.6, 1.3,  3.6, 1.4, 1.6]
}

df = pd.DataFrame(data)
# total = df.groupby('day').sum()['value'].rename('total').reset_index()
# df = df.merge(total)
df["total"] = df.groupby('day')["value"].transform('sum')
df['fraction'] = df['value']/df['total']
pivot_frac = df.pivot(index = 'day', columns = 'nutrient', values='fraction')

import matplotlib.pyplot as plt
import numpy as np
list_column_label = list(pivot_frac.columns)
list_raw_label = list(map(lambda x: 'D0'+str(x),pivot_frac.index))
# 3. Plot the stacked bar chart
ax = pivot_frac.plot(kind='bar', stacked=True, figsize=(8, 4))

# 4. Customize the plot using Matplotlib
plt.title('Nutrient Fraction by Day', fontsize=14)
plt.xlabel('Day')
plt.ylabel('Fraction of Total')
plt.xticks(rotation=0,ticks =range(0, len(pivot_frac.index)),  labels=list_raw_label ) # Keep x-axis labels horizontal
plt.yticks(ticks=np.arange(0, 1.1, 0.2))
plt.legend(title='Nutrient', loc='upper right')
plt.grid(True, axis='y', linestyle='--')
# Display the plot
plt.tight_layout()
plt.show()

# 모범답안
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df["total"] = df.groupby("day")["value"].transform("sum")
df["fraction"] = df["value"] / df["total"]

pivot_frac = df.pivot(index="day", columns="nutrient", values="fraction")

# ✅ legend 항목 순서 고정
order = ["Glu", "Gln", "Lac"]
pivot_frac = pivot_frac.reindex(columns=order)

# x tick label
xlabels = [f"D{d:02d}" for d in pivot_frac.index]

# plot
ax = pivot_frac.plot(kind="bar", stacked=True, figsize=(8, 4))

plt.title("Nutrient Fraction by Day")
plt.xlabel("Day")
plt.ylabel("Fraction of Total")

plt.xticks(ticks=range(len(pivot_frac.index)), labels=xlabels, rotation=0)
plt.yticks(ticks=np.arange(0, 1.01, 0.2))

# ✅ legend 제목/위치/순서 모두 충족
plt.legend(title="Nutrient", loc="upper right")

plt.grid(True, axis="y", linestyle="--")
plt.tight_layout()
plt.show()
