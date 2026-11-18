"""Distributions: examples 9-16.

Run with:  python examples/02_distributions.py
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

# %% 9. Histogram with mean line
rng = np.random.default_rng(2)
data = rng.normal(170, 8, 1000)
fig, ax = plt.subplots()
ax.hist(data, bins=30, color="tab:blue", edgecolor="white")
ax.axvline(data.mean(), color="tab:red", linestyle="--", label=f"mean = {data.mean():.1f}")
ax.legend()
ax.set(title="Histogram", xlabel="Height (cm)", ylabel="Count")
plt.show()

# %% 10. Histogram with kernel density estimate
rng = np.random.default_rng(3)
data = np.concatenate([rng.normal(0, 1, 500), rng.normal(4, 0.8, 300)])
xs = np.linspace(data.min() - 1, data.max() + 1, 400)
h = 1.06 * data.std() * len(data) ** (-1 / 5)      # Silverman's rule
kde = np.exp(-0.5 * ((xs[:, None] - data[None, :]) / h) ** 2).sum(axis=1)
kde /= len(data) * h * np.sqrt(2 * np.pi)
fig, ax = plt.subplots()
ax.hist(data, bins=35, density=True, alpha=0.5, edgecolor="white")
ax.plot(xs, kde, color="tab:red", linewidth=2, label="KDE")
ax.legend()
ax.set(title="Histogram with density estimate", xlabel="value", ylabel="Density")
plt.show()

# %% 11. Box plot
rng = np.random.default_rng(4)
groups = [rng.normal(m, s, 100) for m, s in [(50, 5), (55, 8), (48, 4), (60, 10)]]
fig, ax = plt.subplots()
ax.boxplot(groups, patch_artist=True)
ax.set_xticks([1, 2, 3, 4], ["A", "B", "C", "D"])
ax.set(title="Box plot", ylabel="value")
plt.show()

# %% 12. Violin plot
rng = np.random.default_rng(4)
groups = [rng.normal(m, s, 100) for m, s in [(50, 5), (55, 8), (48, 4), (60, 10)]]
fig, ax = plt.subplots()
ax.violinplot(groups, showmedians=True)
ax.set_xticks([1, 2, 3, 4], ["A", "B", "C", "D"])
ax.set(title="Violin plot", ylabel="value")
plt.show()

# %% 13. Overlapping histograms
rng = np.random.default_rng(5)
a = rng.normal(0, 1, 1000)
b = rng.normal(1.5, 1.3, 1000)
fig, ax = plt.subplots()
ax.hist(a, bins=40, density=True, alpha=0.55, label="Group A")
ax.hist(b, bins=40, density=True, alpha=0.55, label="Group B")
ax.legend()
ax.set(title="Overlapping distributions", xlabel="value", ylabel="Density")
plt.show()

# %% 14. Empirical CDF
rng = np.random.default_rng(6)
data = np.sort(rng.exponential(2.0, 300))
y = np.arange(1, len(data) + 1) / len(data)
fig, ax = plt.subplots()
ax.step(data, y, where="post")
ax.axhline(0.5, color="gray", linestyle=":")
ax.set(title="Empirical CDF", xlabel="value", ylabel="Cumulative proportion")
plt.show()

# %% 15. Hexbin density plot
rng = np.random.default_rng(7)
x = rng.normal(size=5000)
y = x * 0.5 + rng.normal(size=5000)
fig, ax = plt.subplots()
hb = ax.hexbin(x, y, gridsize=30, cmap="magma", mincnt=1)
fig.colorbar(hb, ax=ax, label="count")
ax.set_title("Hexbin density")
plt.show()

# %% 16. 2D histogram
rng = np.random.default_rng(7)
x = rng.normal(size=5000)
y = x * 0.5 + rng.normal(size=5000)
fig, ax = plt.subplots()
counts, xedges, yedges, img = ax.hist2d(x, y, bins=40, cmap="viridis")
fig.colorbar(img, ax=ax, label="count")
ax.set_title("2D histogram")
plt.show()
