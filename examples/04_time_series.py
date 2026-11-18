"""Time Series: examples 23-28.

Run with:  python examples/04_time_series.py
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

# %% 23. Time series with date axis
import matplotlib.dates as mdates

rng = np.random.default_rng(9)
dates = np.arange("2026-01-01", "2026-04-01", dtype="datetime64[D]")
values = 100 + rng.normal(0, 2, len(dates)).cumsum()
fig, ax = plt.subplots()
ax.plot(dates, values)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.set(title="Time series", ylabel="Price")
plt.show()

# %% 24. Moving average overlay
import matplotlib.dates as mdates

rng = np.random.default_rng(9)
dates = np.arange("2026-01-01", "2026-04-01", dtype="datetime64[D]")
values = 100 + rng.normal(0, 2, len(dates)).cumsum()
window = 7
ma = np.convolve(values, np.ones(window) / window, mode="valid")
fig, ax = plt.subplots()
ax.plot(dates, values, alpha=0.4, label="daily")
ax.plot(dates[window - 1:], ma, linewidth=2.5, label="7-day average")
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.legend()
ax.set(title="Moving average", ylabel="Price")
plt.show()

# %% 25. Confidence band with fill_between
x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.1 * x
err = 0.2 + 0.03 * x
fig, ax = plt.subplots()
ax.plot(x, y, label="estimate")
ax.fill_between(x, y - err, y + err, alpha=0.25, label="uncertainty")
ax.legend()
ax.set(title="Line with confidence band", xlabel="x", ylabel="y")
plt.show()

# %% 26. Dual-axis chart
months = np.arange(1, 13)
rain = np.array([5, 8, 20, 60, 150, 300, 350, 330, 250, 120, 20, 5])
temp = np.array([19, 23, 27, 30, 30, 29, 29, 29, 29, 28, 24, 20])
fig, ax1 = plt.subplots()
ax1.bar(months, rain, color="tab:blue", alpha=0.6)
ax1.set_ylabel("Rainfall (mm)", color="tab:blue")
ax2 = ax1.twinx()
ax2.plot(months, temp, "o-", color="tab:red")
ax2.set_ylabel("Temperature (°C)", color="tab:red")
ax2.spines["right"].set_visible(True)
ax1.set(title="Dual-axis chart (sample data)", xlabel="Month")
plt.show()

# %% 27. Annotating a peak
x = np.linspace(0, 10, 200)
y = np.sin(x) * np.exp(-0.1 * x)
i = y.argmax()
fig, ax = plt.subplots()
ax.plot(x, y)
ax.annotate(f"peak = {y[i]:.2f}", xy=(x[i], y[i]), xytext=(x[i] + 2, y[i]),
            arrowprops={"arrowstyle": "->"})
ax.set(title="Annotated peak", xlabel="time", ylabel="amplitude")
plt.show()

# %% 28. Step plot
x = np.arange(8)
y = np.array([1, 3, 2, 5, 4, 6, 6, 3])
fig, ax = plt.subplots()
ax.step(x, y, where="mid", linewidth=2)
ax.plot(x, y, "o", color="gray", alpha=0.6)
ax.set(title="Step plot", xlabel="step", ylabel="value")
plt.show()
