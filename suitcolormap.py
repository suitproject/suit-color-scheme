import matplotlib
from matplotlib import colors
from matplotlib.colors import LinearSegmentedColormap
from sunpy.map import Map
import matplotlib
import numpy as np

sji2796 = matplotlib.colormaps['irissji2796']
sji2832 = matplotlib.colormaps['irissji2832']
tracewl = matplotlib.colormaps['traceWL']
sjinuv = matplotlib.colormaps['irissjiNUV']

colors1 = [(0, 0, 0), (140/255, 13/255, 14/255), (255/255, 162/255, 54/255), (1, 1, 1)]
colors2 = [(0, 0, 0), (150/255, 50/255, 50/255), (222/255, 111/255, 111/255), (252/255, 172/255, 172/255)]
colors3 = [(0, 0, 0), (245/255, 62/255, 1/255), (253/255, 192/255, 41/255),(252/255, 224/255, 159/255)]#, (1, 1, 1)]
colors4 = [(0, 0, 0), (175/255, 70/255, 179/255), (229/255, 135/255, 232/255), (1, 1, 1)] # fix with equal distitbution
colors5 = [(0, 0, 0), (255/255, 107/255, 176/255),(255/255, 194/255, 111/255), (1, 1, 1)] #titan
colors6 = [(0, 0, 0), (254/255, 155/255, 2/255),(183/255, 244/255, 10/255), (1, 1, 1)]#periperi #pluto [(0, 0, 0), (56/255, 24/255, 54/255),(207/255, 126/255, 98/255), (1, 1, 1)] [(0, 0, 0), (86/255, 47/255, 40/255),(179/255, 158/255, 131/255), (1, 1, 1)]
colors7 = [(0, 0, 0), (129/255, 98/255, 46/255),(252/255, 235/255, 114/255), (1, 1, 1)] #io
colors8 = [(0, 0, 0), (74/255, 30/255, 27/255),(225/255, 125/255, 29/255), (242/255,194/255,136/255), (1, 1, 1)]
colors9 = [(0, 0, 0), (102/255, 163/255, 3/255),(135/255, 209/255, 17/255), (206/255, 250/255, 135/255)]
colors10 = [(0, 0, 0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (1, 1, 1)]
colors11 = [(0, 0, 0), (20/255, 94/255, 94/255), (41/255, 186/255, 186/255), (1, 1, 1)]
colors12 = [(0, 0, 0), (247/255, 247/255, 0), (247/255, 242/255, 121/255), (1, 1, 1)] #sakya
colors13 = [(0, 0, 0), (238/255, 39/255, 49/255), (246/255, 184/255, 183/255), (1, 1, 1)]

# Define the positions of the colors in the gradient
positions = [0, 0.33, 0.66, 1]
positions2 = [0, 0.25, 0.50,0.75, 1]
# Create custom colormaps
cmap1 = LinearSegmentedColormap.from_list("CustomGradient1", list(zip(positions, colors1)))
cmap2 = LinearSegmentedColormap.from_list("CustomGradient2", list(zip(positions, colors2)))
cmap3 = LinearSegmentedColormap.from_list("CustomGradient3", list(zip(positions, colors3)))
cmap4 = LinearSegmentedColormap.from_list("CustomGradient4", list(zip(positions, colors4)))
cmap5 = LinearSegmentedColormap.from_list("CustomGradient5", list(zip(positions, colors5)))
cmap6 = LinearSegmentedColormap.from_list("CustomGradient6", list(zip(positions, colors6)))
cmap7 = LinearSegmentedColormap.from_list("CustomGradient7", list(zip(positions, colors7)))
cmap8 = LinearSegmentedColormap.from_list("CustomGradient8", list(zip(positions, colors8)))
cmap9 = LinearSegmentedColormap.from_list("CustomGradient9", list(zip(positions, colors9)))
cmap10 = LinearSegmentedColormap.from_list("CustomGradient10", list(zip(positions, colors10)))
cmap11 = LinearSegmentedColormap.from_list("CustomGradient11", list(zip(positions, colors11)))
cmap12 = LinearSegmentedColormap.from_list("CustomGradient11", list(zip(positions, colors12)))
cmap13 = LinearSegmentedColormap.from_list("CustomGradient11", list(zip(positions, colors13)))

filterColor = {
    'BB01': cmap4,
    'NB01': cmap10,
    'NB02': cmap3,
    'NB03': cmap1,
    'NB04': cmap12,
    'NB05': sji2832,
    'NB08': cmap7,
    'NB06': cmap11,
    'NB07': cmap9,
    'BB02': cmap2,
    'BB03': cmap13,
    'LD01': cmap2,
    'LD02': cmap13,
    'BB01_roi': cmap4,
    'NB01_roi': cmap10,
    'NB02_roi': cmap3,
    'NB03_roi': cmap1,
    'NB04_roi': cmap12,
    'NB05_roi': sji2832,
    'NB08_roi': 'Greys_r',
    'NB06_roi': cmap11,
    'NB07_roi': cmap9,
    'BB02_roi': cmap2,
    'BB03_roi': cmap13
}


filterName = {
    'BB01': 'BB1',
    'NB01': 'NB1  214 nm',
    'NB02': 'NB2  276 nm',
    'NB03': 'NB3 MgII k 279 nm',
    'NB04': 'NB4 MgII h 280 nm',
    'NB05': 'NB5  283 nm',
    'NB08': 'CaII h 396.8 nm',
    'NB06': 'NB6  300 nm',
    'NB07': 'NB7  388 nm',
    'BB02': 'BB2',
    'BB03': 'BB3',
    'LD01': 'Led 255 nm',
    'LD02': 'Led 355 nm',
    'BB01_roi': 'BB1',
    'NB01_roi': 'NB1  214 nm',
    'NB02_roi': 'NB2  276 nm',
    'NB03_roi': 'NB3 MgII k 279 nm',
    'NB04_roi': 'NB4 MgII h 280 nm',
    'NB05_roi': 'NB5  283 nm',
    'NB08_roi': 'CaII h 396.8 nm',
    'NB06_roi': 'NB6  300 nm',
    'NB07_roi': 'NB7  388 nm',
    'BB02_roi': 'BB2',
    'BB03_roi': 'BB3'
}

def img_norm(a):
    a = np.array(a)
    sliced_array = a[(a > 2000) & (a < 50000)]
    baseline = 1000 if len(sliced_array) == 0 else np.median(sliced_array)
    norm1={'NB05':colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)}
    norm1['NB03']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)
    norm1['NB04']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=6*baseline)
    norm1['NB02']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=6*baseline)
    norm1['NB07']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=5*baseline)
    norm1['NB06']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)
    norm1['BB03']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)
    norm1['BB02']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)
    norm1['BB01']=colors.PowerNorm(gamma=1.0,vmin=.2*baseline,vmax=3*baseline)
    norm1['NB01']=colors.PowerNorm(gamma=0.9,vmin=.1*baseline,vmax=3*baseline)
    norm1['NB08']=colors.PowerNorm(gamma=0.9,vmin=.2*baseline,vmax=3*baseline)
    norm1['NB03_roi']=colors.PowerNorm(gamma=0.9,vmin=.01*baseline,vmax=0.99*baseline)
    norm1['NB04_roi']=colors.PowerNorm(gamma=1.5,vmin=.001*baseline,vmax=1.5*baseline)
    norm1['NB02_roi']=colors.PowerNorm(gamma=1.1,vmin=.1*baseline,vmax=0.9*baseline)
    norm1['NB07_roi']=colors.PowerNorm(gamma=1.3,vmin=.01*baseline,vmax=0.99*baseline)
    norm1['NB06_roi']=colors.PowerNorm(gamma=1.1,vmin=.1*baseline,vmax=0.9*baseline)
    norm1['BB03_roi']=colors.PowerNorm(gamma=1.1,vmin=.01*baseline,vmax=0.99*baseline)
    norm1['BB02_roi']=colors.PowerNorm(gamma=1.1,vmin=.01*baseline,vmax=0.39*baseline)
    norm1['BB01_roi']=colors.PowerNorm(gamma=1.1,vmin=.01*baseline,vmax=0.99*baseline)
    norm1['NB01_roi']=colors.PowerNorm(gamma=1.1,vmin=.1*baseline,vmax=0.99*baseline)
    norm1['NB05_roi']=colors.PowerNorm(gamma=1.,vmin=.02*baseline,vmax=0.8*baseline)
    norm1['NB08_roi']=colors.PowerNorm(gamma=1.3,vmin=.01*baseline,vmax=0.8*baseline)
    return norm1
