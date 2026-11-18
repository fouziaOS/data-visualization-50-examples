"""Layout & Styling: examples 35-40.

Run with:  python examples/06_layout_styling.py
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

# %% 35. Subplot grid
x = np.linspace(0, 2 * np.pi, 100)
funcs = [("sin", np.sin), ("cos", np.cos),
         ("tan (clipped)", lambda t: np.clip(np.tan(t), -5, 5)),
         ("sin(2x)", lambda t: np.sin(2 * t))]
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
for ax, (name, f) in zip(axes.flat, funcs):
    ax.plot(x, f(x))
    ax.set_title(name)
fig.suptitle("2x2 subplot grid", fontweight="bold")
plt.show()

# %% 36. Shared axes
x = np.linspace(0, 10, 300)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(7, 5))
ax1.plot(x, np.sin(x))
ax1.set_ylabel("sin(x)")
ax2.plot(x, np.exp(-x / 3) * np.cos(3 * x), color="tab:orange")
ax2.set_ylabel("damped cos")
ax2.set_xlabel("x")
fig.suptitle("Shared x-axis", fontweight="bold")
plt.show()

# %% 37. GridSpec with uneven panels
x = np.linspace(0, 10, 200)
fig = plt.figure(figsize=(9, 5))
gs = fig.add_gridspec(2, 3)
ax_big = fig.add_subplot(gs[:, :2])
ax_a = fig.add_subplot(gs[0, 2])
ax_b = fig.add_subplot(gs[1, 2])
ax_big.plot(x, np.sin(x))
ax_big.set_title("Main plot (spans 2x2 cells)")
ax_a.hist(np.random.default_rng(0).normal(size=300), bins=20)
ax_a.set_title("Top right")
ax_b.plot(x, np.cos(x), color="tab:orange")
ax_b.set_title("Bottom right")
plt.show()

# %% 38. Inset zoom
x = np.linspace(0, 10, 500)
y = np.sin(x) + 0.3 * np.sin(8 * x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_ylim(-1.5, 3.6)                      # leave headroom for the inset
axins = ax.inset_axes([0.5, 0.62, 0.45, 0.33])
axins.plot(x, y)
mask = (x >= 4) & (x <= 5)
axins.set_xlim(4, 5)
axins.set_ylim(y[mask].min() - 0.1, y[mask].max() + 0.1)
ax.indicate_inset_zoom(axins)
ax.set_title("Inset zoom")
plt.show()

# %% 39. Linear vs log scale
x = np.logspace(0, 4, 50)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
ax1.plot(x, x ** 2)
ax1.set_title("Linear scale")
ax2.loglog(x, x ** 2, label="x^2")
ax2.loglog(x, x ** 1.5, label="x^1.5")
ax2.legend()
ax2.set_title("Log-log scale")
plt.show()

# %% 40. Custom theme with rc_context
x = np.linspace(0, 10, 300)
theme = {"axes.facecolor": "#0f172a", "figure.facecolor": "#0f172a",
         "text.color": "white", "axes.labelcolor": "white",
         "xtick.color": "white", "ytick.color": "white",
         "axes.edgecolor": "#475569", "grid.color": "#334155"}
with plt.rc_context(theme):
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), color="#22d3ee", linewidth=2.5, label="sin")
    ax.plot(x, np.cos(x), color="#f472b6", linewidth=2.5, label="cos")
    ax.legend(facecolor="#1e293b", edgecolor="#475569")
    ax.set_title("Dark theme via rc_context")
plt.show()
