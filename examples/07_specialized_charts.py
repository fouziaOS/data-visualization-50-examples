"""Specialized Charts: examples 41-50.

Run with:  python examples/07_specialized_charts.py
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

# %% 41. Radar chart
labels = ["Speed", "Power", "Defense", "Stamina", "Skill"]
players = {"Player 1": [8, 6, 7, 5, 9], "Player 2": [5, 9, 6, 8, 6]}
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
for name, vals in players.items():
    v = vals + vals[:1]
    ax.plot(angles, v, label=name)
    ax.fill(angles, v, alpha=0.2)
ax.set_xticks(angles[:-1], labels)
ax.set_ylim(0, 10)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
ax.set_title("Radar chart", pad=20)
plt.show()

# %% 42. Stem plot
x = np.arange(0, 12)
y = np.cos(x * 0.6)
fig, ax = plt.subplots()
ax.stem(x, y)
ax.set(title="Stem plot", xlabel="n", ylabel="value")
plt.show()

# %% 43. Quiver plot (vector field)
x, y = np.meshgrid(np.linspace(-2, 2, 15), np.linspace(-2, 2, 15))
u, v = -y, x
fig, ax = plt.subplots()
q = ax.quiver(x, y, u, v, np.hypot(u, v), cmap="plasma")
fig.colorbar(q, ax=ax, label="magnitude")
ax.set_aspect("equal")
ax.set_title("Vector field (rotation)")
plt.show()

# %% 44. Streamplot
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X ** 2 + Y
V = 1 + X - Y ** 2
speed = np.hypot(U, V)
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=speed, cmap="viridis", linewidth=1.2)
fig.colorbar(strm.lines, ax=ax, label="speed")
ax.set_title("Streamplot")
plt.show()

# %% 45. 3D surface
x = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, x)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
fig.colorbar(surf, shrink=0.6, label="Z")
ax.set_title("3D surface")
plt.show()

# %% 46. 3D scatter
rng = np.random.default_rng(13)
pts = rng.normal(size=(200, 3))
dist = np.linalg.norm(pts, axis=1)
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(projection="3d")
sc = ax.scatter(*pts.T, c=dist, cmap="plasma")
fig.colorbar(sc, shrink=0.6, label="distance")
ax.set_title("3D scatter")
plt.show()

# %% 47. imshow with colorbar
x = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, x)
Z = np.sin(X) * np.cos(Y) * np.exp(-0.1 * (X ** 2 + Y ** 2))
fig, ax = plt.subplots()
im = ax.imshow(Z, cmap="magma", origin="lower", extent=[-3, 3, -3, 3])
fig.colorbar(im, ax=ax, label="value")
ax.grid(False)
ax.set_title("imshow")
plt.show()

# %% 48. Gantt-style timeline
tasks = ["Design", "Develop", "Test", "Deploy"]
start = [0, 2, 6, 9]
duration = [3, 5, 4, 1]
fig, ax = plt.subplots()
ax.barh(tasks, duration, left=start,
        color=["tab:blue", "tab:orange", "tab:green", "tab:red"])
ax.invert_yaxis()
ax.set(title="Gantt-style timeline", xlabel="Week")
plt.show()

# %% 49. Waterfall chart
labels = ["Opening", "Sales", "Refunds", "Costs", "Tax", "Closing"]
steps = [60, -15, -40, -10]
opening = 100
levels = opening + np.concatenate([[0], np.cumsum(steps)])
fig, ax = plt.subplots()
ax.bar(0, opening, color="tab:blue")
for i, d in enumerate(steps, start=1):
    ax.bar(i, d, bottom=levels[i - 1], color="tab:green" if d > 0 else "tab:red")
ax.bar(len(steps) + 1, levels[-1], color="tab:blue")
ax.set_xticks(range(len(labels)), labels)
ax.set(title="Waterfall chart", ylabel="Amount")
plt.show()

# %% 50. Dumbbell chart
cats = ["Team A", "Team B", "Team C", "Team D"]
before = np.array([55, 40, 62, 48])
after = np.array([70, 58, 60, 75])
y = np.arange(len(cats))
fig, ax = plt.subplots()
ax.hlines(y, before, after, color="gray", linewidth=2)
ax.scatter(before, y, s=80, label="Before", zorder=3)
ax.scatter(after, y, s=80, label="After", zorder=3)
ax.set_yticks(y, cats)
ax.legend()
ax.set(title="Dumbbell chart", xlabel="Score")
plt.show()
