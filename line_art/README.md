# line_art.py
Inspired by [Nadieh Brehmer's The Art in Pi](https://www.visualcinnamon.com/portfolio/the-art-in-pi), `line_art.py` is a simple Python script that generates beautiful line art using random numbers. 

## Quickstart
For the most basic use, simply type `python line_art.py`:

![](https://github.com/Ravenlocke/PythonArt/raw/master/line_art/example_10000.png)


## Options
`line_art.py` has options to set:
  - the seed / length, which will generate a different configuration of lines
  - the colour map of the resultant image (which must be a valid [matplotlib colour map](https://matplotlib.org/examples/color/colormaps_reference.html))
  - the line width (smaller often works better for greater lengths 
  - a filename to save your desired output. The file type is determined from the extension (e.g., "example.pdf" will save the image to the file example.pdf). If you save your image as a PNG, you may want to set the DPI to ~1,000 to get a high quality image).

The options can be obtained by running `python line_art.py --help`

    $ python line_art.py --help
    Usage: line_art.py [OPTIONS]

    Options:
      -s, --seed INTEGER    Seed for random number generation.
      -l, --length INTEGER  Number of random numbers to generate.
      -c, --cmap TEXT       The matplotlib colour map to use.
      --outfile TEXT        The outfile to save the image to (default None
                            displays the image).

      --dpi INTEGER         The DPI for the output image -- set for high-quality
                            images if using a format like PNG.

      --linewidth FLOAT     The width of the plotted lines -- consider decreasing
                            for large lengths.

      --help                Show this message and exit.
      
## Requirements
`line_art.py` requires the following four Python packages, which are all available in pip:
  - `matplotlib` -- `pip install matplotlib`
  - `click` -- `pip install click`
  - `numpy` -- `pip install numpy`
  - `loguru` -- `pip install loguru`
