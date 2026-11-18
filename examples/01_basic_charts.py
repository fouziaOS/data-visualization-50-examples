"""Basic Charts: examples 1-8.

Run with:  python examples/01_basic_charts.py
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

# %% 1. Simple line plot
x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.set(title="Sine wave", xlabel="x (radians)", ylabel="sin(x)")
plt.show()

# %% 2. Multiple lines with a legend
x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.plot(x, np.sin(x) * np.cos(x), label="sin x cos")
ax.legend(loc="upper right")
ax.set(title="Multiple series", xlabel="x", ylabel="value")
plt.show()

# %% 3. Line styles and markers
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, "o-", color="tab:blue", label="solid + circles")
ax.plot(x, x ** 1.2, "s--", color="tab:orange", label="dashed + squares")
ax.plot(x, x ** 1.4, "^:", color="tab:green", label="dotted + triangles")
ax.plot(x, x ** 1.6, "d-.", color="tab:red", linewidth=2, markersize=6, label="dash-dot + diamonds")
ax.legend()
ax.set_title("Line styles and markers")
plt.show()

# %% 4. Scatter plot
rng = np.random.default_rng(0)
x = rng.normal(size=150)
y = 0.6 * x + rng.normal(scale=0.6, size=150)
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.7, edgecolor="white")
ax.set(title="Scatter plot", xlabel="x", ylabel="y")
plt.show()

# %% 5. Bubble chart with colorbar
rng = np.random.default_rng(1)
x, y = rng.random(40), rng.random(40)
size = rng.integers(50, 600, 40)
color = rng.random(40)
fig, ax = plt.subplots()
sc = ax.scatter(x, y, s=size, c=color, cmap="viridis", alpha=0.75, edgecolor="white")
fig.colorbar(sc, ax=ax, label="value")
ax.set_title("Bubble chart")
plt.show()

# %% 6. Bar chart with value labels
langs = ["Python", "JavaScript", "Java", "C++", "Go"]
users = [48, 62, 35, 22, 14]
fig, ax = plt.subplots()
bars = ax.bar(langs, users, color="tab:blue")
ax.bar_label(bars, padding=3)
ax.set(title="Developers by language (sample data)", ylabel="Share (%)")
plt.show()

# %% 7. Sorted horizontal bar chart
data = {"Alpha": 22.5, "Beta": 15.2, "Gamma": 11.8, "Delta": 7.0, "Epsilon": 3.9}
names, vals = zip(*sorted(data.items(), key=lambda kv: kv[1]))
fig, ax = plt.subplots()
bars = ax.barh(names, vals, color="tab:green")
ax.bar_label(bars, fmt="%.1f", padding=3)
ax.set(title="Ranked values (sample data)", xlabel="Score")
plt.show()

# %% 8. Grouped bar chart
labels = ["Q1", "Q2", "Q3", "Q4"]
a = [20, 35, 30, 35]
b = [25, 32, 34, 20]
x = np.arange(len(labels))
w = 0.38
fig, ax = plt.subplots()
ax.bar(x - w / 2, a, w, label="2025")
ax.bar(x + w / 2, b, w, label="2026")
ax.set_xticks(x, labels)
ax.legend()
ax.set(title="Grouped bar chart", ylabel="Sales")
plt.show()
