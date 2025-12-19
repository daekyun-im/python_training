import numpy as np
import matplotlib.pyplot as plt

x = df["feed"]
y = df["titer"]
x_mean = x.mean()
y_mean = y.mean()

a = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
b = y_mean - a * x_mean

df["titer_hat"] = a * x + b
df["residual"] = y - df["titer_hat"]

imax = df["residual"].abs().idxmax()
row = df.loc[imax, ["run","feed","titer","titer_hat","residual"]]
print(row.to_dict())

# masks for coloring
outlier = df["residual"].abs() >= 0.15
inlier = ~outlier

plt.figure(figsize=(6, 4))

# scatter: inlier / outlier as separate calls -> clean legend + color control
plt.scatter(df.loc[inlier, "feed"], df.loc[inlier, "titer"],
            c="gray", marker="o", s=40, label="inlier (|res| < 0.15)")
plt.scatter(df.loc[outlier, "feed"], df.loc[outlier, "titer"],
            c="red", marker="o", s=40, label="outlier (|res| ≥ 0.15)")

# highlight max-abs-residual point (bigger + black edge)
plt.scatter(df.loc[imax, "feed"], df.loc[imax, "titer"],
            c="red" if outlier.loc[imax] else "gray",
            marker="o", s=140, edgecolor="black", linewidth=1.5,
            label="max |residual|")

# regression line on sorted x-range
x_line = np.linspace(df["feed"].min(), df["feed"].max(), 100)
y_line = a * x_line + b
plt.plot(x_line, y_line, label="fit: titer_hat")

plt.title("Feed vs Titer with Residual Highlight")
plt.xlabel("Feed")
plt.ylabel("Titer (g/L)")
plt.grid(True)
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
