# suit-color-scheme
Color scheme for all the filters of SUIT


# Quick Guide


Load the suitcolormap.py file to your python code

```python
from suitcolormap import *
```

When applying the color scheme to your plots, you need to add cmap and norm.

```python

from astropy.io import fits
import matplotlib.pytplot as plt
#Load the data

inFile = '<input SUIT fits file>'
with fits.open(inFile) as inF:
	inData = inF[0].data
	filterName = inF[0].header['FTR_NAME'] #Get the filter name from the headers

#Load the norm
suitnorm = img_norm(inData).get(filterName)
#plot the image
plt.imshow(inData, cmap=filterColor.get(filterName), origin='lower', interpolation='none', norm = suitnorm)
plt.show()
```
Email us for your queries: suit@iucaa.in
