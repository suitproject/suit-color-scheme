#suitcolormap.py

"""
SUIT colormaps and recommended normalization.

This module provides colormaps for SUIT filters along with a corresponding
normalization function required for correct visual representation.

Usage
-----
>>> from suitcolormap import suit_cmap, suit_norm
>>> cmap = suit_cmap("NB03")
>>> norm = suit_norm(data, "NB03")

Notes
-----
- The colormaps are designed to be used WITH the provided normalization.
- Normalization is data-dependent and based on median intensity.
- If no valid pixels are found, a default baseline of 1000 is used.
"""

import numpy as np
import matplotlib
from matplotlib.colors import LinearSegmentedColormap, PowerNorm
import sunpy.visualization.colormaps

_POS = [0.0, 0.33, 0.66, 1.0]


def _cmap(name, colors):
    """Create a linear segmented colormap."""
    return LinearSegmentedColormap.from_list(name, list(zip(_POS, colors)))


SUIT_CMAPS = {
    "BB01": _cmap("BB01", [(0,0,0),(175/255,70/255,179/255),(229/255,135/255,232/255),(1,1,1)]),
    "BB02": _cmap("BB02", [(0,0,0),(150/255,50/255,50/255),(222/255,111/255,111/255),(252/255,172/255,172/255)]),
    "BB03": _cmap("BB03", [(0,0,0),(238/255,39/255,49/255),(246/255,184/255,183/255),(1,1,1)]),

    "NB01": _cmap("NB01", [(0,0,0),(0.25,0.25,0.25),(0.5,0.5,0.5),(1,1,1)]),
    "NB02": _cmap("NB02", [(0,0,0),(245/255,62/255,1/255),(253/255,192/255,41/255),(252/255,224/255,159/255)]),
    "NB03": _cmap("NB03", [(0,0,0),(140/255,13/255,14/255),(255/255,162/255,54/255),(1,1,1)]),
    "NB04": _cmap("NB04", [(0,0,0),(247/255,247/255,0),(247/255,242/255,121/255),(1,1,1)]),
    "NB06": _cmap("NB06", [(0,0,0),(20/255,94/255,94/255),(41/255,186/255,186/255),(1,1,1)]),
    "NB07": _cmap("NB07", [(0,0,0),(102/255,163/255,3/255),(135/255,209/255,17/255),(206/255,250/255,135/255)]),
    "NB08": _cmap("NB08", [(0,0,0),(129/255,98/255,46/255),(252/255,235/255,114/255),(1,1,1)]),

    "NB05": matplotlib.colormaps["irissji2832"],
}


def suit_cmap(filter_name):
    """
    Return the SUIT colormap for a given filter.

    Parameters
    ----------
    filter_name : str
        Filter name (NB01–NB08, BB01–BB03)

    Returns
    -------
    matplotlib.colors.Colormap
    """
    return SUIT_CMAPS[filter_name]


def suit_norm(data, filter_name):
    """
    Return recommended normalization for a SUIT filter.

    The normalization is based on the median intensity of pixels within
    the range (2000, 50000). If no such pixels exist, a default baseline
    value of 1000 is used.

    Parameters
    ----------
    data : array-like
        Image data
    filter_name : str
        Filter name (NB01–NB08, BB01–BB03)

    Returns
    -------
    matplotlib.colors.PowerNorm
    """
    data = np.asarray(data)
    valid = data[(data > 2000) & (data < 50000)]

    baseline = np.median(valid) if valid.size else 1000.0

    settings = {
        "NB05": (0.9, 3), "NB03": (0.9, 3),
        "NB04": (0.9, 6), "NB02": (0.9, 6),
        "NB07": (0.9, 5), "NB06": (0.9, 3),
        "BB03": (0.9, 3), "BB02": (0.9, 3),
        "BB01": (1.0, 3), "NB01": (0.9, 3),
        "NB08": (0.9, 3),
    }

    gamma, vmax = settings[filter_name]

    return PowerNorm(
        gamma=gamma,
        vmin=0.1 * baseline,
        vmax=vmax * baseline
    )
