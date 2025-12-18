import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# data
data = {
    "batch": ["B1","B1","B1","B1","B2","B2","B2","B2","B3","B3","B3","B3"],
    "condition": ["Low","Low","High","High","Low","Low","High","High","Low","Low","High","High"],
    "titer": [2.1, 2.3, 2.8, 2.9, 1.9, 2.0, 2.5, 2.6, 2.4, 2.2, 3.0, 3.1]
}
df = pd.DataFrame(data)

# 1) df_summary: mean/std by batch & condition
df_summary = (
    df.groupby(["batch", "condition"], as_index=False)["titer"]
      .agg(mean_titer="mean", std_titer="std")
)

# 2) df_delta: High - Low per batch (pivot/unstack)
wide = df_summary.pivot(index="batch", columns="condition", values="mean_titer")
df_delta = (wide["High"] - wide["Low"]).rename("delta_high_minus_low").reset_index()

# -------------------------
# Plot 1: boxplot (separate figure)
# -------------------------
# Make arrays (no loops): rows=batch, cols=condition
pivot_list = (df.pivot_table(index="batch", columns="condition", values="titer", aggfunc=list)
                .reindex(index=["B1","B2","B3"], columns=["Low","High"]))

# order: Low(B1,B2,B3), High(B1,B2,B3)
data_to_plot = (
    pivot_list["Low"].tolist() + pivot_list["High"].tolist()
)

# positions for grouped boxes under Low/High
base_low, base_high = 1.0, 2.0
offsets = [-0.25, 0.0, 0.25]  # B1,B2,B3
positions = [base_low + o for o in offsets] + [base_high + o for o in offsets]

batch_colors = {"B1": "blue", "B2": "orange", "B3": "green"}
box_colors = [batch_colors["B1"], batch_colors["B2"], batch_colors["B3"],
              batch_colors["B1"], batch_colors["B2"], batch_colors["B3"]]

plt.figure()
bp = plt.boxplot(
    data_to_plot,
    positions=positions,
    widths=0.22,
    patch_artist=True
)

# color the boxes (no explicit for-loop using vectorized-style assignment is not supported;
# but a tiny loop over 6 artists is standard matplotlib usage)
for box, c in zip(bp["boxes"], box_colors):
    box.set_facecolor(c)

plt.title("Titer Distribution by Condition")
plt.xlabel("Condition")
plt.ylabel("Titer (g/L)")
plt.xticks([1, 2], ["Low", "High"])

legend_handles = [
    Patch(label="B1", facecolor=batch_colors["B1"]),
    Patch(label="B2", facecolor=batch_colors["B2"]),
    Patch(label="B3", facecolor=batch_colors["B3"]),
]
plt.legend(handles=legend_handles, title="Batch", loc="upper left")
plt.tight_layout()
plt.show()

# -------------------------
# Plot 2: bar plot (separate figure)
# -------------------------
plt.figure()
bar_colors = (df_delta["delta_high_minus_low"] >= 0).map({True: "blue", False: "gray"})

plt.bar(df_delta["batch"], df_delta["delta_high_minus_low"], color=bar_colors, label="Δ mean (High−Low)")
plt.axhline(0, color="lightgray", linestyle="--", linewidth=2, label="y=0")

plt.title("High–Low Mean Titer Difference")
plt.xlabel("Batch")
plt.ylabel("Δ Mean Titer (High − Low)")
plt.legend()
plt.tight_layout()
plt.show()

df_summary, df_delta
