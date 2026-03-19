![SUIT Banner](https://suit.iucaa.in/sites/default/files/top_banner_compressed_2_1.png)

# suit-color-scheme

Color schemes for all filters of the SUIT (Solar Ultraviolet Imaging Telescope) instrument.

This repository provides:
- Matplotlib colormaps for each SUIT filter
- Recommended normalization for scientifically meaningful visualization
---

## Available Colormaps

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

## Installation

Download `suitcolormap.py`, place in the same directory and import.

## Dependencies

This package requires the following Python libraries:
- `numpy`
- `matplotlib`
- `astropy` (for FITS file handling)
- `sunpy` (for `SUITMap` integration)

## Usage

### Basic Usage

Here is a quick example of how to use the colormaps and normalization with a FITS file.

```python
from suitcolormap import suit_cmap, suit_norm
from astropy.io import fits
import matplotlib # Needed for NB05 filter colormap
import matplotlib.pyplot as plt

# Load FITS file
inFile = "<input SUIT fits file>"

with fits.open(inFile) as hdul:
    data = hdul[0].data
    filter_name = hdul[0].header["FTR_NAME"]

# Get colormap and normalization
cmap = suit_cmap(filter_name)
norm = suit_norm(data, filter_name)

# Plot the data
plt.imshow(data, cmap=cmap, norm=norm, origin="lower")
plt.colorbar()
plt.title(filter_name)
plt.show()
```

# With SunPy

The SUITMap is now part of the sunpy python package. If you are plotting with SUITMap,
Then, you can plot with `sunpy`'s plot functions. We recommend not to use the `peek` function in sunpy.

Additionally, when generating plots, apply the normalization (norm) associated with the `suitcolormap` to ensure consistent and accurate visualization.

Here is an example usage.


```python
from suitcolormap import suit_norm
import sunpy.map
import matplotlib.pyplot as plt 

file = <SUIT fits file path>
suit_map = sunpy.map.Map(file)

filter_name = suit_map.meta['FTR_NAME'] # Filter name fetching from headers
fig = plt.figure()
ax = fig.add_subplot(projection=suit_map)
suit_map.plot(axes=ax, norm=suit_norm(suit_map.data, filter_name))
plt.show()

```

This will apply the norm defined by suitcolormap.

For any queries, contact: suit@iucaa.in
