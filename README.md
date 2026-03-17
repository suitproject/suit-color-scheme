![SUIT Banner](https://suit.iucaa.in/sites/default/files/top_banner_compressed_2_1.png)

# suit-color-scheme

Color schemes for all filters of the SUIT (Solar Ultraviolet Imaging Telescope) instrument.

This repository provides:
- Matplotlib colormaps for each SUIT filter
- Recommended normalization for scientifically meaningful visualization

---

# Colormaps

- BB01 ![BB01](./assets/bb01.png)
- BB02 ![BB02](./assets/bb02.png)
- BB03 ![BB03](./assets/bb03.png)
- NB01 ![NB01](./assets/nb01.png)
- NB02 ![NB02](./assets/nb02.png)
- NB03 ![NB03](./assets/nb03.png)
- NB04 ![NB04](./assets/nb04.png)
- NB05 ![NB05](./assets/nb05.png)
- NB06 ![NB06](./assets/nb06.png)
- NB07 ![NB07](./assets/nb07.png)
- NB08 ![NB08](./assets/nb08.png)

---

# Quick Usage

Download `suitcolormap.py`, place in the same directory and import.

Example:

```python
from suitcolormap import get_cmap, get_norm # Importing colormap
from astropy.io import fits
import matplotlib.pyplot as plt
import sunpy.visualization.colormaps # Needed for NB05 filter
# Load FITS file
inFile = "<input SUIT fits file>"

with fits.open(inFile) as hdul:
    data = hdul[0].data
    filter_name = hdul[0].header["FTR_NAME"]

# Get colormap and normalization
cmap = get_cmap(filter_name)
norm = get_norm(data, filter_name)

# Plot
plt.imshow(data, cmap=cmap, norm=norm, origin="lower")
plt.colorbar()
plt.title(filter_name)
plt.show()
```



