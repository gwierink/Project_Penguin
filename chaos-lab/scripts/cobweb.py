import numpy as np
import matplotlib.pyplot as plt
from maps import logistic


def cobweb_path(f, x0, n):
    # Corner points of the cobweb: up/down to the curve, across to the diagonal
    xs, ys = [x0], [0.0]
    x = x0
    for _ in range(n):
        y = f(x)
        xs += [x, y]
        ys += [y, y]
        x = y
    return xs, ys


def plot_cobweb(ax, r, x0=0.2, n=50):
    f = lambda x: logistic(x, r)
    grid = np.linspace(0, 1, 400)
    ax.plot(grid, f(grid), "k", lw=1.5)      # the map y = r x (1 - x)
    ax.plot(grid, grid, "k--", lw=0.8)       # the diagonal y = x
    xs, ys = cobweb_path(f, x0, n)
    ax.plot(xs, ys, "C0", lw=0.8)            # the cobweb itself
    ax.set(xlim=(0, 1), ylim=(0, 1), aspect="equal",
           xlabel="$x_n$", ylabel="$x_{n+1}$", title=f"r = {r}")


fig, axes = plt.subplots(2, 2, figsize=(8, 8))
for ax, r in zip(axes.flat, [2.8, 3.2, 3.5, 3.9]):
    plot_cobweb(ax, r)
fig.tight_layout()
fig.savefig("figures/cobweb.png", dpi=150)
plt.show()
