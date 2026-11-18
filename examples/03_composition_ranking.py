"""Composition & Ranking: examples 17-22.

Run with:  python examples/03_composition_ranking.py
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

# %% 17. Pie chart
sizes = [40, 25, 20, 10, 5]
labels = ["Rent", "Food", "Transport", "Savings", "Other"]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=90,
       explode=[0.05, 0, 0, 0, 0], wedgeprops={"edgecolor": "white"})
ax.set_title("Monthly budget")
plt.show()

# %% 18. Donut chart
sizes = [40, 25, 20, 10, 5]
labels = ["Rent", "Food", "Transport", "Savings", "Other"]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=90, pctdistance=0.8,
       wedgeprops={"width": 0.4, "edgecolor": "white"})
ax.text(0, 0, "Budget", ha="center", va="center", fontsize=14, fontweight="bold")
plt.show()

# %% 19. Stacked bar chart
months = ["Jan", "Feb", "Mar", "Apr"]
a = np.array([20, 25, 30, 22])
b = np.array([15, 18, 12, 20])
c = np.array([10, 8, 14, 9])
fig, ax = plt.subplots()
ax.bar(months, a, label="Product A")
ax.bar(months, b, bottom=a, label="Product B")
ax.bar(months, c, bottom=a + b, label="Product C")
ax.legend()
ax.set(title="Stacked bar chart", ylabel="Units")
plt.show()

# %% 20. 100% stacked bar chart
months = ["Jan", "Feb", "Mar", "Apr"]
a = np.array([20, 25, 30, 22])
b = np.array([15, 18, 12, 20])
c = np.array([10, 8, 14, 9])
totals = a + b + c
fig, ax = plt.subplots()
bottom = np.zeros(4)
for vals, name in [(a, "Product A"), (b, "Product B"), (c, "Product C")]:
    share = vals / totals * 100
    ax.bar(months, share, bottom=bottom, label=name)
    bottom += share
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
ax.set(title="100% stacked bar", ylabel="Share (%)")
plt.show()

# %% 21. Stacked area chart
x = np.arange(2018, 2027)
y1 = np.linspace(5, 12, 9)
y2 = np.linspace(8, 10, 9)
y3 = np.linspace(3, 14, 9)
fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=["Web", "Mobile", "Cloud"], alpha=0.85)
ax.legend(loc="upper left")
ax.set(title="Stacked area chart", xlabel="Year", ylabel="Revenue")
plt.show()

# %% 22. Lollipop chart
names = np.array(list("ABCDEFG"))
vals = np.array([5, 9, 3, 7, 8, 2, 6])
order = np.argsort(vals)
ypos = np.arange(len(vals))
fig, ax = plt.subplots()
ax.hlines(ypos, 0, vals[order], color="gray")
ax.plot(vals[order], ypos, "o", markersize=9, color="tab:red")
ax.set_yticks(ypos, names[order])
ax.set(title="Lollipop chart", xlabel="Score")
plt.show()
