import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams["font.family"] = "Heiti TC"
plt.rcParams["axes.unicode_minus"] = False

out = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    path = os.path.join(out, name)
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(path)


fig, ax = plt.subplots(figsize=(10.5, 5.2))
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis("off")
ax.set_title("因果图", fontsize=20, pad=12)
ax.annotate(
    "",
    xy=(78, 30),
    xytext=(6, 30),
    arrowprops=dict(arrowstyle="-|>", color="#222", lw=1.8),
)
ax.add_patch(
    plt.Rectangle((78, 22), 18, 16, fill=True, facecolor="white", edgecolor="#222", lw=1.6)
)
ax.text(87, 30, "状态更新延迟", ha="center", va="center", fontsize=13)
bones = [
    (28, 30, 18, 50, "人员", "操作不熟", True),
    (55, 30, 45, 50, "系统", "接口超时", True),
    (28, 30, 18, 10, "方法", "节点未定义", False),
    (55, 30, 45, 10, "数据", "进度迟报", False),
]
for x1, y1, x2, y2, cat, cause, top in bones:
    ax.plot([x1, x2], [y1, y2], color="#222", lw=1.4)
    ax.text(x2, y2 + (2.4 if top else -2.8), cat, ha="center", va="center", fontsize=14)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx + 3.2, my + (2.0 if top else -2.0), cause, ha="left", va="center", fontsize=12, color="#333")
save(fig, "因果图.png")

labels = ["接口超时", "进度迟报", "操作不熟", "节点未定义", "其他"]
counts = [42, 28, 14, 9, 7]
cum = [42, 70, 84, 93, 100]
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.bar(labels, counts, color="#e07a3d", width=0.62, zorder=2, label="次数")
ax.plot(labels, cum, color="#2f6fdb", marker="o", lw=1.8, zorder=3, label="累计次数")
for x, c, t in zip(range(len(labels)), counts, cum):
    if c >= 20:
        ax.text(x, c - 2.2, str(c), ha="center", va="top", fontsize=11, color="white")
    else:
        ax.text(x, c + 1.6, str(c), ha="center", va="bottom", fontsize=11, color="#333")
    ax.text(x, min(t + 5.5, 114), "累计" + str(t), ha="center", va="bottom", fontsize=10, color="#2f6fdb")
ax.set_ylim(0, 120)
ax.set_ylabel("次数")
ax.set_xlabel("原因")
ax.set_title("帕累托图", fontsize=20, pad=12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, ls="--", color="#ddd", zorder=0)
ax.legend(frameon=False, loc="center left")
save(fig, "帕累托图.png")

weeks = ["1", "2", "3", "4", "5", "6", "7", "8"]
vals = [4, 5, 6, 5, 7, 4, 12, 5]
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.axhline(10, color="#666", ls="--", lw=1)
ax.axhline(6, color="#666", ls="--", lw=1)
ax.axhline(2, color="#666", ls="--", lw=1)
ax.text(0.05, 10.4, "UCL 10", fontsize=11, color="#444")
ax.text(0.05, 6.4, "CL 6", fontsize=11, color="#444")
ax.text(0.05, 2.4, "LCL 2", fontsize=11, color="#444")
ax.plot(weeks, vals, color="#e07a3d", lw=1.6, zorder=2)
colors = ["#c0392b" if v > 10 or v < 2 else "#e07a3d" for v in vals]
ax.scatter(weeks, vals, c=colors, s=46, zorder=3)
ax.set_ylim(0, 15)
ax.set_xlabel("周")
ax.set_ylabel("延迟次数")
ax.set_title("控制图", fontsize=20, pad=12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, ls="--", color="#ddd")
save(fig, "控制图.png")

hours = [1, 2, 3, 4, 5, 6, 8, 10]
errors = [11, 10, 8, 7, 6, 5, 3, 2]
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.scatter(hours, errors, s=56, color="#e07a3d", zorder=3)
ax.set_xlim(0, 12)
ax.set_ylim(0, 14)
ax.set_xlabel("培训小时")
ax.set_ylabel("失误次数")
ax.set_title("散点图", fontsize=20, pad=12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(True, ls="--", color="#ddd", zorder=0)
save(fig, "散点图.png")
