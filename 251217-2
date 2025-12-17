import pandas as pd

data = {
    "day":   [1,2,3,4,5,6,7,8],
    "value": [10,12,11,15,14,16,18,17]
}
df = pd.DataFrame(data)

import pandas as pd

data = {
    "day":   [1,2,3,4,5,6,7,8],
    "value": [10,12,11,15,14,16,18,17]
}
df = pd.DataFrame(data)

# 1️⃣ 코딩 문제
# value의 3일 이동평균을 계산해서 ma3 컬럼으로 추가하라.
# day=1,2의 ma3는 NaN이어도 된다.
# 2️⃣ 분석 문제
# value - ma3 를 residual 컬럼으로 추가하라.
# residual이 가장 큰 day(= value가 이동평균 대비 가장 “튀는” 날)의 day와 residual 값을 출력하라.
# 3️⃣ 시각화 문제
# matplotlib으로 다음을 한 그래프에 그려라.
# value 선 그래프
# ma3 선 그래프
# residual이 가장 큰 day의 점을 빨간색 점(marker) 으로 표시
# legend 포함, 축 라벨 포함

# 조건
# pandas의 rolling()을 반드시 사용할 것
# for-loop 없이 해결
# seaborn ❌

df['ma3'] = df['value'].rolling(window=3).mean()
df['residual'] = df['value']-df['ma3']
mx_day = df[['day']].iloc[df['residual'].idxmax()].item()
mx_residual = df[['residual']].iloc[df['residual'].idxmax()].item()
print(mx_day, mx_residual)

import matplotlib.pyplot as plt
plt.figure()

plt.plot(df["day"], df["value"], label = 'value')
plt.plot(df["day"], df["ma3"], label = 'ma3')
plt.plot(df["day"][df["residual"] == mx_residual].item(), df['value'][df["residual"] == mx_residual].item(), 'ro')
plt.plot(df["day"][df["residual"] == mx_residual].item(), df['ma3'][df["residual"] == mx_residual].item(), 'ro')
plt.title('rolling')
plt.xlabel('day')
plt.ylabel('value')

plt.legend()
plt.show()

# 모범답안
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day":   [1,2,3,4,5,6,7,8],
    "value": [10,12,11,15,14,16,18,17]
}
df = pd.DataFrame(data)

# rolling mean + residual
df["ma3"] = df["value"].rolling(window=3).mean()
df["residual"] = df["value"] - df["ma3"]

# max residual row (NaN 자동 제외됨)
imax = df["residual"].idxmax()
mx_day = df.loc[imax, "day"]
mx_residual = df.loc[imax, "residual"]
print(mx_day, mx_residual)

# plot
plt.figure()
plt.plot(df["day"], df["value"], label="value")
plt.plot(df["day"], df["ma3"], label="ma3")
plt.plot(mx_day, df.loc[imax, "value"], "ro", label="max residual day")
plt.xlabel("day")
plt.ylabel("value")
plt.title("3-day rolling mean")
plt.legend()
plt.tight_layout()
plt.show()
