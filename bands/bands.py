# -*- coding: utf-8 -*-

from matplotlib import transforms
from matplotlib.collections import BrokenBarHCollection
import matplotlib.pyplot as plt
import os
import pandas as pd
import pkg_resources

# Function that we'll call for each dataframe (once for chromosome
# ideograms, once for genes)
def _chromosome_collections(df, y_positions, height, print_names=False, **kwargs):
  """

  Yields BrokenBarHCollection of features that can be added to an Axes
  object.

  Parameters
  ----------

  df : pandas.DataFrame
      Must at least have columns ['chrom', 'start', 'end', 'color']. If no
      column 'width', it will be calculated from start/end.

  y_positions : dict
      Keys are chromosomes, values are y-value at which to anchor the
      BrokenBarHCollection

  height : float
      Height of each BrokenBarHCollection

  Additional kwargs are passed to BrokenBarHCollection
  """
  del_width = False
  if 'width' not in df.columns:
    del_width = True
    df['width'] = df['end'] - df['start']
  for chrom, group in df.groupby('chrom'):
    yrange = (y_positions[chrom], height)
    xranges = group[['start', 'width']].values
    if print_names:
      names = group[['name', 'colors']].values
      names = [i for i in names if i[1] != '#ffffff']
      ax = plt.gca()
      t = ax.transData
      canvas = ax.figure.canvas
      # Plot names with different colors and spaced
      for i, n in enumerate(names):
        text = ax.text(0, y_positions[chrom] - 2, f'{n[0]}', color=n[1], transform=t, fontsize=10)
        text.draw(canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, x=ex.width, units='dots')
    yield BrokenBarHCollection(
      xranges, yrange, facecolors=group['colors'], **kwargs)
  if del_width:
    del df['width']

def _read_ideo(ref):

  # Read in ideogram.txt, downloaded from UCSC Table Browser
  ideo = pkg_resources.resource_filename('bands',
    os.path.join('ref', f'{ref}_cytoBandIdeo.txt'))
  ideo = pd.read_table(
    ideo, skiprows=1, names=['chrom', 'start', 'end', 'name', 'gieStain']
  )

  return ideo

def _color_lookup():

  # Colors for different chromosome stains
  color_lookup = {
    'gneg': (.9, .9, .9),
    'gpos25': (.75, .75, .75),
    'gpos50': (.7, .7, .7),
    'gpos75': (.65, .65, .65),
    'gpos100': (.55, .55, .55),
    'acen': (.45, .5, .45),
    'gvar': (.8, .8, .8),
    'stalk': (.85, .85, .85),
  }

  return color_lookup

def _plot_chr(figsize, ideo, chrom_ybase, chrom_height, genes, gene_ybase,
    gene_height, chrom_centers, chromosome_list):

  fig = plt.figure(figsize=figsize, dpi=100)
  ax = plt.gca()

  # Ideograms
  for collection in _chromosome_collections(ideo, chrom_ybase, chrom_height):
    ax.add_collection(collection)

  # Genes
  for collection in _chromosome_collections(genes, gene_ybase, gene_height,
      alpha=0.5, linewidths=0, print_names=True):
    ax.add_collection(collection)

  # Axes tweaking
  ax.set_xticks([])
  ax.set_yticks([chrom_centers[i] for i in chromosome_list])
  ax.set_yticklabels(chromosome_list, fontsize=20)
  ax.axis('tight')
  plt.setp(ax.spines.values(), linewidth=0)
  ax.yaxis.set_tick_params(width=0)
  plt.xlim([0, plt.xlim()[1]])

  return fig

def get_bands(gd, figsize=(60, 25), ref='hg19', chrom_height=1, chrom_spacing=3, gene_height=.8,
  gene_padding=.1):

  chromosome_list = ['chr%s' % i for i in list(range(1, 23)) + ['M', 'X', 'Y']]

  # Keep track of the y positions for ideograms and genes for each chromosome,
  # and the center of each ideogram (which is where we'll put the ytick labels)
  ybase = 0
  chrom_ybase = {}
  gene_ybase = {}
  chrom_centers = {}

  # Iterate in reverse so that items in the beginning of `chromosome_list` will
  # appear at the top of the plot
  for chrom in chromosome_list[::-1]:
    chrom_ybase[chrom] = ybase
    chrom_centers[chrom] = ybase + chrom_height / 2.
    gene_ybase[chrom] = ybase - gene_height - gene_padding
    ybase += chrom_height + chrom_spacing

  ideo = _read_ideo(ref)

  # Filter out chromosomes not in our list
  ideo = ideo[ideo.chrom.apply(lambda x: x in chromosome_list)]

  # Add a new column for width
  ideo['width'] = ideo.end - ideo.start

  # Add a new column for colors
  ideo['colors'] = ideo['gieStain'].apply(lambda x: _color_lookup()[x])

  genes = gd[['Chr', 'Start', 'Stop', 'Name', 'colors']]
  genes.columns = ['chrom', 'start', 'end', 'name', 'colors']
  genes = genes[genes.chrom.apply(lambda x: x in chromosome_list)]
  genes['width'] = (genes.end - genes.start)

  fig = _plot_chr(figsize, ideo, chrom_ybase, chrom_height,
    genes, gene_ybase, gene_height, chrom_centers,
    chromosome_list)

  return fig

