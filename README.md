![Logo](https://suit.iucaa.in/sites/default/files/top_banner_compressed_2_1.png)

# suit-color-scheme


Color scheme for all the filters of SUIT

# Colormap
- BB01 ![BB01](./assets/bb01.png)
- BB02 ![BB02](./assets/bb02.png)
- BB03 ![BB03](./assets/bb03.png)
- NB01 ![NB01](./assets/bb03.png)
- NB02 ![NB02](./assets/nb02.png)
- NB03 ![NB03](./assets/nb03.png)
- NB04 ![NB04](./assets/nb04.png)
- NB05 ![NB05](./assets/nb05.png)
- NB06 ![NB06](./assets/nb06.png)
- NB07 ![NB07](./assets/nb07.png)
- NB08 ![NB08](./assets/nb08.png)

# Quick Guide

Load the suitcolormap.py file to your python code

```python
from suitcolormap import *
```

When applying the color scheme to your plots, you need to add the cmap.

```python

from astropy.io import fits
import matplotlib.pyplot as plt
#Load the data

inFile = '<input SUIT fits file>'
with fits.open(inFile) as inF:
	inData = inF[0].data
	filterName = inF[0].header['FTR_NAME'] #Get the filter name from the headers

#plot the image
plt.imshow(inData, cmap=filterColor.get(filterName), origin='lower', interpolation='none')
plt.show()
```
You are always free to play around with `vmin`, `vmax`, and `norm` properties to have a better feel of the image.


Email us for your queries: suit@iucaa.in
