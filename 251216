# 🧩 파이썬 문제 (쉬움 · pandas + matplotlib · 다른 유형)
# 다음은 간단한 실험 결과 데이터다.
# import pandas as pd
# data = {
#     "sample": ["A","B","C","D","E"],
#     "yield": [72, 85, 78, 90, 83]
# }
#
# df = pd.DataFrame(data)
# 1️⃣ 코딩 문제
# yield 값의 평균(mean) 을 계산하라.
# 평균보다 큰 yield 를 가진 sample만 선택하여 새로운 DataFrame df_high를 만들어라.
# df_high에는 sample, yield 두 컬럼만 포함한다.
# 2️⃣ 분석 문제
# 전체 sample 중 평균 이상인 sample의 비율(%) 을 계산하라.
# 예: 5개 중 3개면 60.0 (%)
# 3️⃣ 시각화 문제
# matplotlib을 사용하여 아래를 만족하는 bar plot을 그려라.
# x축: sample
# y축: yield
# 평균 이상 sample의 bar는 초록색
# 평균 미만 sample의 bar는 회색
# 평균값을 수평선(line) 으로 표시
# 범례 포함

# 작성 코드
avg_yield = df['yield'].mean()
df_high = df[df['yield']>avg_yield].reset_index(drop=True)
display(df_high)
ratio = (len(df_high)/len(df))*100
print(f'ratio는 {ratio}% 입니다.')
plt.bar(df[df['yield'] > avg_yield]['sample'], df[df['yield'] > avg_yield]['yield'], color='green', label='above avg.')
plt.bar(df[df['yield'] < avg_yield]['sample'], df[df['yield'] < avg_yield]['yield'], color='gray', label='below avg.')
plt.axhline(avg_yield, color='lightgray', linestyle='--', linewidth=2, label = 'avg.')
plt.title('Matplotlib Bar Plot')
plt.legend()
plt.xlabel('Sample')
plt.ylabel('Yield')
plt.show()

#평가 결과
# 4️⃣ 점수 (100점 만점)
# 항목	점수
# 문제 해결 정확성	40 / 40
# 로직 품질	23 / 25
# pandas 활용	15 / 15
# 시각화	9 / 10
# 가독성	9 / 10
# 총점	96 / 100
import pandas as pd
import matplotlib.pyplot as plt

# data
# data = {
#     "sample": ["A","B","C","D","E"],
#     "yield": [72, 85, 78, 90, 83]
# }
# df = pd.DataFrame(data)
#
# # analysis
# avg_yield = df["yield"].mean()
# df["group"] = df["yield"] >= avg_yield
# colors = df["group"].map({True: "green", False: "gray"})
# 
# ratio = df["group"].mean() * 100
# print(f"ratio는 {ratio:.1f}% 입니다.")
# 
# # visualization (order preserved, no hardcoding)
# plt.figure()
# plt.bar(df["sample"], df["yield"], color=colors)
# plt.axhline(avg_yield, linestyle="--", linewidth=2, label="Average")
# plt.xlabel("Sample")
# plt.ylabel("Yield")
# plt.title("Yield by Sample")
# plt.legend()
# plt.tight_layout()
# plt.show()
