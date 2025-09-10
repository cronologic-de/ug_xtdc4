import atompy as ap
import numpy as np
from numpy.typing import NDArray, ArrayLike
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from typing import Final, overload, Literal, Union


CRONOBLUE: Final = "#376eb5"
CRONOORANGE: Final = "#ed7800"
GREY: Final = "#8c8c8c"


def gauss(
    x: ArrayLike, scale: float | None = None, mu: float = 0.0, sigma: float = 1.0
) -> NDArray[np.float64]:
    """
    Return gaussian distribution.

    Parameters
    ----------
    x : ArrayLike
        x values

    scale : float, optional
        Output value at `x = mu`.

        If None, return a probability density.

    mu : float, default 0.0
        Center/mean of the Gaussian.

    sigma : float, default 1.0
        Width/variance of the Gaussian.

    Returns
    -------
    numpy.ndarray
    """
    scale = scale or 1.0 / np.sqrt(2.0 * np.pi * sigma**2)
    exponent = -((np.asarray(x) - mu) ** 2) / sigma**2 / 2.0
    return scale * np.exp(exponent)


import numpy as np


rms_dict_like = dict[
    Union[
        Literal["RMS_total"],
        Literal["RMS_quant"],
        Literal["RMS_jitter"],
        Literal["delta"],
    ],
    float,
]


def rms_from_3bin_histogram(bin_width, intensities) -> rms_dict_like:
    """

    THIS METHOD IS PROBABLY WRONG!


    Calculate total RMS, quantization RMS, and intrinsic jitter RMS
    from a 3-bin histogram of percentages.

    If more than 3 bins significantly contribute to the histogram, this method
    will not produce meaningful results.

    If the center bin is not the largest contribution, this method will not produce
    meaningful results.

    Parameters
    ----------
    bin_width : float
        Width of one bin in ps.
    intensities : list or array-like of 3 floats
        Relative intensities of hits in the three bins [left, center, right].

    Returns
    -------
    dict with keys:
        'RMS_total' : total RMS from histogram (ps)
        'RMS_quant' : RMS contribution from quantization (ps)
        'RMS_jitter': inferred intrinsic jitter RMS (ps)
        'delta'     : estimated intra-bin offset delta (ps)
    """
    intensities = np.asarray(intensities, dtype=float)
    if len(intensities) != 3:
        raise ValueError("intensities needs to be three values")
    if intensities.sum() == 0:
        raise ValueError("Sum of counts must be > 0")

    intensities /= intensities.sum()

    # fractional bin positions: left=-1, center=0, right=1
    centers = np.array([-1, 0, 1], dtype=float)
    mean = np.sum(intensities * centers)

    # in bin units
    var_bins = np.sum(intensities * (centers - mean) ** 2)

    # total RMS in ps
    RMS_total = np.sqrt(var_bins) * bin_width

    # estimate delta from left / total counts
    delta = bin_width * (intensities[0] + 0.5 * intensities[2])
    delta = (1.0 - mean) * bin_width / 2.0

    # quantization RMS
    RMS_quant = np.sqrt(delta * (bin_width - delta))

    # intrinsic jitter RMS
    RMS_jitter = np.sqrt(max(RMS_total**2 - RMS_quant**2, 0))

    return {
        "RMS_total": RMS_total,
        "RMS_quant": RMS_quant,
        "RMS_jitter": RMS_jitter,
        "delta": delta,
    }


def main():
    data_ths = np.loadtxt("cable_delay_hist_THS.dat").T

    plt.style.use("cronostyle.mplstyle")
    plt.rcParams["font.size"] = 9.0

    fig, axs = plt.subplots(nrows=4, ncols=1, squeeze=False)

    fig.suptitle("xTDC4 – Cable Delay Measurements")

    titles = [f"Channel {which}" for which in "ABCD"]

    for i, ax in enumerate(axs[:, 0]):
        xs = data_ths[2 * i + 0]
        ys = data_ths[2 * i + 1]
        ys = ys / np.sum(ys) * 100.0  # percent

        ax.bar(xs, ys, color=CRONOBLUE, zorder=3, width=0.33)

        # probably incorrect calculations
        # binsize = 5000.0 / 384.0
        # imax = np.argmax(ys)
        # rms_dict = rms_from_3bin_histogram(binsize, ys[imax - 1 : imax + 2])
        # rms_total_ps = rms_dict["RMS_total"]
        # rms_quant_ps = rms_dict["RMS_quant"]
        # rms_jitter_ps = rms_dict["RMS_jitter"]

        # labels = "RMS\n" "total:\n" "quant.:\n" "jitter:"
        # numbers = (
        #     "\n"
        #     f"{rms_total_ps/binsize:.2f} bins ({rms_total_ps:.1f} ps)\n"
        #     f"{rms_quant_ps/binsize:.2f} bins ({rms_quant_ps:.1f} ps)\n"
        #     f"{rms_jitter_ps/binsize:.2f} bins ({rms_jitter_ps:.1f} ps)"
        # )
        # xofs, yofs = 1.02, 0.97
        # ax.text(xofs, yofs, labels, transform=ax.transAxes, va="top", ha="left")
        # ax.text(xofs + 0.2, yofs, numbers, transform=ax.transAxes, va="top", ha="left")

        xmax = xs[np.argmax(ys)]
        xlims = (xmax - 1.5, xmax + 1.5)
        ax.set_xlim(*xlims)
        ylims = ax.get_ylim()
        ax.set_ylim(bottom=-ylims[1] * 0.05)
        xticks = [n + xmax for n in range(-1, 2)]
        ax.set_xticks(xticks, ["$N$–1", "$N$", "$N$+1"])

        ax.set_title(titles[i])

    for ax in axs.flat:
        ax.set_xlabel("Bin")
        ax.set_ylabel("Intensity (%)")
        ap.set_axes_size(2.3, 2.3 / 1.618, ax)

    ap.make_me_nice(fix_figwidth=False, margin_pad_pts=(5, 5, 35, 5))

    ap.savefig("*", ftype=("pdf", "svg"))


if __name__ == "__main__":
    main()
