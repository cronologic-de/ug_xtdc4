import atompy as ap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

HIT_WIDTH = 1.0

XLIM = 12
YLIM = 4

orange = "#ED7807"
lightorange = "#F6BB82"
blue = "#376EB5"
lightblue = "#569fd6"
grey = "#8c8c8c"

XSTART = -10.5
ARROWPROPS = dict(arrowstyle="->", shrinkA=0, shrinkB=0, color=grey)


def add_square_pulse(
    x: np.ndarray,
    y: np.ndarray,
    positions: tuple[float, ...],
    height: float = 0.3,
    width: float = 1.0,
):
    """Adds a square pulse to a line at a given position."""

    x_new = x
    y_new = y
    for position in positions:
        # Create the x and y coordinates for the square pulse
        x_pulse = [
            position,
            position,
            position + width,
            position + width,
        ]
        y_pulse = np.array((y[0], y[0] - height, y[0] - height, y[0]))

        # Insert the pulse into the original line
        insert_index = np.searchsorted(
            x_new, x_pulse[0]
        )  # Find where to insert the pulse

        x_new = list(x_new)
        x_new[insert_index:insert_index] = x_pulse  # Insert x values

        y_new = list(y_new)
        y_new[insert_index:insert_index] = list(y_pulse)  # Insert y values

    return x_new, y_new


def add_rectangle(
    ax: Axes,
    xpos: float,
    color: str,
    height: float = 0.5,
    width: float = 1.0,
    ypos: float = 0.0,
):
    """Adds a rectangle to the plot at a given position."""
    import matplotlib.patches as patches

    rect = patches.Rectangle(
        (xpos, ypos), width, height, facecolor=color, ec=color, lw=0.8
    )
    ax.add_patch(rect)


def plot_start(ax: Axes):
    x = np.array((-12.0, 12.0))
    y = np.array((5.5, 5.5))
    x, y = add_square_pulse(x, y, (-10.5,))

    ax.plot(x, y, lw=1.3, color=grey)
    ax.axvline(XSTART, ls=":", lw=0.8, c=grey)

    ax.text(-12.0 - 0.2, 5.5, "Start", ha="right", va="center", color=grey)


def plot_stopB(ax: Axes):
    y0 = 3.0
    x = np.array((-12.0, 12.0))
    y = np.array((y0, y0))
    x, y = add_square_pulse(x, y, (-11, -6, 1, 8, 10))
    ax.plot(x, y, lw=1.3, color=blue)

    # for xpos in (-11, -6, 8, 10):
    #     add_rectangle(ax, xpos, grey, height=-0.3, ypos=y0)
    for xpos in (1,):
        add_rectangle(ax, xpos, orange, height=-0.3, ypos=y0)

    ax.text(-12.2, 3, "Stop B", ha="right", va="center", color=grey)

    ax.annotate("", xytext=(XSTART, y0 + 0.2), xy=(-1, y0 + 0.2), arrowprops=ARROWPROPS)
    ax.text(-1, y0 + 0.3, "channel[1].start", ha="right", color=grey)
    ax.annotate(
        "", xytext=(XSTART, y0 + 0.1), xy=(6.3, y0 + 0.1), arrowprops=ARROWPROPS
    )
    ax.text(6.3, y0 + 0.2, "channel[1].stop", ha="right", color=grey)


def plot_stopA(ax: Axes):
    y0 = 4
    x = np.array((-12.0, 12.0))
    y = np.array((4.0, 4.0))
    x, y = add_square_pulse(x, y, (-8, -4, 2, 5))
    ax.plot(x, y, lw=1.3, color=blue)

    # for xpos in (-8, 5):
    #     add_rectangle(ax, xpos, grey, height=-0.3, ypos=4)
    for xpos in (-4, 2):
        add_rectangle(ax, xpos, orange, height=-0.3, ypos=4)

    ax.text(-12.2, 4, "Stop A", ha="right", va="center", color=grey)

    ax.annotate(
        "", xytext=(XSTART, y0 + 0.2), xy=(-7.4, y0 + 0.2), arrowprops=ARROWPROPS
    )
    ax.text(-7.4, y0 + 0.3, "channel[0].start", ha="right", color=grey)
    ax.annotate("", xytext=(XSTART, y0 + 0.1), xy=(4, y0 + 0.1), arrowprops=ARROWPROPS)
    ax.text(4, y0 + 0.2, "channel[0].stop", ha="right", color=grey)


def plot_stopC(ax: Axes):
    y0 = 2
    x = np.array((-12.0, 12.0))
    y = np.array((2.0, 2.0))
    x, y = add_square_pulse(x, y, (-7, -2, 3, 6))
    ax.plot(x, y, lw=1.3, color=blue)

    # for xpos in (-7, -2):
    #     add_rectangle(ax, xpos, grey, height=-0.3, ypos=2)
    for xpos in (3, 6):
        add_rectangle(ax, xpos, orange, height=-0.3, ypos=2)

    ax.text(-12.2, 2, "Stop C", ha="right", va="center", color=grey)

    ax.annotate("", xytext=(XSTART, y0 + 0.2), xy=(-1, y0 + 0.2), arrowprops=ARROWPROPS)
    ax.text(-1, y0 + 0.3, "channel[2].start", ha="right", color=grey)
    ax.annotate(
        "", xytext=(XSTART, y0 + 0.1), xy=(6.3, y0 + 0.1), arrowprops=ARROWPROPS
    )
    ax.text(6.3, y0 + 0.2, "channel[2].stop", ha="right", color=grey)


def plot_stopD(ax: Axes):
    y0 = 1
    x = np.array((-12.0, 12.0))
    y = np.array((1.0, 1.0))
    x, y = add_square_pulse(x, y, (-8, 0, 5, 9))
    ax.plot(x, y, lw=1.3, color=blue)

    for xpos in (-0, 5):
        add_rectangle(ax, xpos, orange, height=-0.3, ypos=1)
    # for xpos in (9,):
    #     add_rectangle(ax, xpos, grey, height=-0.3, ypos=1)

    ax.text(-12.2, 1, "Stop D", ha="right", va="center", color=grey)

    ax.annotate("", xytext=(XSTART, y0 + 0.2), xy=(-1, y0 + 0.2), arrowprops=ARROWPROPS)
    ax.text(-1, y0 + 0.3, "channel[3].start", ha="right", color=grey)
    ax.annotate(
        "", xytext=(XSTART, y0 + 0.1), xy=(6.3, y0 + 0.1), arrowprops=ARROWPROPS
    )
    ax.text(6.3, y0 + 0.2, "channel[3].stop", ha="right", color=grey)


def main():
    plt.rcParams["figure.figsize"] = 130 / ap.MM_PER_INCH, 5
    plt.rcParams["font.family"] = "arial"

    ax = plt.subplot(111)
    ax.set_axis_off()

    ax.set_box_aspect(1.0 / 1.5)

    ax.set_xlim(-12, 12)
    ax.set_ylim(0.6, 5.7)

    plot_start(ax)
    plot_stopA(ax)
    plot_stopB(ax)
    plot_stopC(ax)
    plot_stopD(ax)

    ap.make_me_nice(margin_pad_pts=0)

    ap.savefig(ftype=("pdf", "svg"), transparent=True)


if __name__ == "__main__":
    main()
