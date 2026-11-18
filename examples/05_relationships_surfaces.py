"""Relationships & Surfaces: examples 29-34.

Run with:  python examples/05_relationships_surfaces.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.figsize": (7, 4.2),
    "figure.dpi": 110,
    "figure.constrained_layout.use": True,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# %% 29. Error bars
x = np.arange(1, 7)
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.2])
err = np.array([0.4, 0.5, 0.6, 0.5, 0.7, 0.8])
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=err, fmt="o-", capsize=4)
ax.set(title="Error bars", xlabel="trial", ylabel="measurement")
plt.show()

# %% 30. Scatter with regression line
rng = np.random.default_rng(10)
x = rng.uniform(0, 10, 80)
y = 2.5 * x + 4 + rng.normal(0, 3, 80)
slope, intercept = np.polyfit(x, y, 1)
r = np.corrcoef(x, y)[0, 1]
xs = np.array([x.min(), x.max()])
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.7)
ax.plot(xs, slope * xs + intercept, color="tab:red",
        label=f"y = {slope:.2f}x + {intercept:.2f}  (r = {r:.2f})")
ax.legend()
ax.set(title="Linear regression", xlabel="x", ylabel="y")
plt.show()

# %% 31. Annotated correlation heatmap
rng = np.random.default_rng(11)
base = rng.normal(size=(200, 1))
data = np.hstack([base + rng.normal(0, 0.5, (200, 1)),
                  -0.8 * base + rng.normal(0, 0.7, (200, 1)),
                  rng.normal(size=(200, 2))])
names = ["A", "B", "C", "D"]
corr = np.corrcoef(data, rowvar=False)
fig, ax = plt.subplots()
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(4), names)
ax.set_yticks(range(4), names)
for i in range(4):
    for j in range(4):
        ax.text(j, i, f"{corr[i, j]:.2f}", ha="center", va="center")
fig.colorbar(im, ax=ax, label="correlation")
ax.grid(False)
ax.set_title("Correlation heatmap")
plt.show()

# %% 32. Contour plot
x = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, x)
Z = np.exp(-(X ** 2 + Y ** 2) / 2) - 0.5 * np.exp(-((X - 1.5) ** 2 + (Y + 1) ** 2))
fig, ax = plt.subplots()
cs = ax.contour(X, Y, Z, levels=12, cmap="RdBu")
ax.clabel(cs, inline=True, fontsize=8)
ax.set_aspect("equal")
ax.set_title("Contour plot")
plt.show()

# %% 33. Filled contour plot
x = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, x)
Z = np.exp(-(X ** 2 + Y ** 2) / 2) - 0.5 * np.exp(-((X - 1.5) ** 2 + (Y + 1) ** 2))
fig, ax = plt.subplots()
cf = ax.contourf(X, Y, Z, levels=15, cmap="viridis")
fig.colorbar(cf, ax=ax, label="Z")
ax.set_aspect("equal")
ax.set_title("Filled contour plot")
plt.show()

# %% 34. Scatter with marginal histograms
rng = np.random.default_rng(12)
x = rng.normal(size=800)
y = 0.7 * x + rng.normal(0, 0.7, 800)
fig = plt.figure(figsize=(6, 6), layout="none")
gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.12, right=0.95, bottom=0.1, top=0.92, hspace=0.05, wspace=0.05)
ax = fig.add_subplot(gs[1, 0])
ax_top = fig.add_subplot(gs[0, 0], sharex=ax)
ax_right = fig.add_subplot(gs[1, 1], sharey=ax)
ax.scatter(x, y, alpha=0.5, s=15)
ax_top.hist(x, bins=30)
ax_right.hist(y, bins=30, orientation="horizontal")
ax_top.tick_params(labelbottom=False)
ax_right.tick_params(labelleft=False)
ax.set(xlabel="x", ylabel="y")
fig.suptitle("Scatter with marginal histograms", fontweight="bold")
plt.show()
