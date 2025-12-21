import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df_merged = pd.merge(df_result, df_cond, how="left", on="sample")
df_merged["titer"] = df_merged.groupby("temp")["titer"].transform(lambda x: x.fillna(x.mean()))

df_feed_mean = (
    df_merged.groupby("feed", as_index=False)["titer"]
             .mean()
             .rename(columns={"titer": "mean_titer"})
)

df_feed_summary = df_feed_mean.copy()
global_mean = df_feed_summary["mean_titer"].mean()
df_feed_summary["above_global_mean"] = df_feed_summary["mean_titer"] >= global_mean

# feed order fixed (A, B)
df_feed_summary = df_feed_summary.set_index("feed").loc[["A", "B"]].reset_index()

colors = df_feed_summary["above_global_mean"].map({True: "blue", False: "gray"})

plt.figure(figsize=(6, 4))
plt.bar(df_feed_summary["feed"], df_feed_summary["mean_titer"], color=colors)
plt.axhline(global_mean, color="lightgray", linestyle="--", linewidth=2, label="Global mean")

plt.title("Mean Titer by Feed")
plt.xlabel("Feed")
plt.ylabel("Mean Titer (g/L)")

# legend: ensure 2+ items
legend_handles = [
    Patch(label="above_global_mean=True", facecolor="blue"),
    Patch(label="above_global_mean=False", facecolor="gray"),
]
plt.legend(handles=legend_handles + [plt.Line2D([0], [0], color="lightgray", linestyle="--", linewidth=2, label="Global mean")])

plt.tight_layout()
plt.show()
