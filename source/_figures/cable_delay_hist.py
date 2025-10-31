import atompy as ap
import numpy as np
from numpy.typing import NDArray, ArrayLike
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.ticker import MultipleLocator

from typing import Final


CRONOBLUE: Final = "#376eb5"
CRONOORANGE: Final = "#ed7800"
GREY: Final = "#8c8c8c"


def load_data() -> NDArray[np.float64]:
    return np.loadtxt("cable_delay_hist_THS.dat").T


def plot():
    data_ths = load_data()

    plt.style.use("cronostyle.mplstyle")
    plt.rcParams["axes.spines.left"] = True
    plt.rcParams["axes.spines.bottom"] = True
    plt.rcParams["axes.spines.top"] = True
    plt.rcParams["axes.spines.right"] = True
    plt.rcParams["font.size"] = 9.0

    fig, axs = plt.subplots(nrows=1, ncols=4)

    fig.suptitle("xTDC4 – Cable Delay Measurements")

    titles = [f"Channel {which}" for which in "ABCD"]
    binsize = 13.0

    for i, ax in enumerate(axs):
        xs_ths = data_ths[2 * i + 0] * binsize
        ys_ths = data_ths[2 * i + 1]
        ys_ths = ys_ths / np.sum(ys_ths) * 100.0  # percent
        ax.plot(xs_ths, ys_ths, drawstyle="steps-mid", zorder=3)

        xmax = xs_ths[np.argmax(ys_ths)]
        xlims = (xmax - 5.55 * binsize, xmax + 5.55 * binsize)
        ax.set_xlim(*xlims)
        ax.set_title(titles[i])

    for ax in axs:
        ax.set_ylim(-1, axs[3].get_ylim()[1])
        ap.set_axes_size(1.0, 1.0 * 3, ax)
        ax.xaxis.set_major_locator(MultipleLocator(50))

    for ax in axs[1:]:
        ax.set_yticklabels([])

    axs[0].set_ylabel("Intensity (%)")
    axs[2].set_xlabel("Delay (ps)")
    axs[2].xaxis.set_label_coords(0, -0.055)

    ap.make_me_nice(
        fix_figwidth=False,
        margin_pad_pts=(5, 5, 25, 5),
        col_pad_ignores_labels=True,
        col_pad_pts=0,
    )

    ap.savefig("*", ftype=("pdf", "svg"))

    plt.close()


if __name__ == "__main__":
    plot()
