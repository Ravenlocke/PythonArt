import click
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from matplotlib.collections import LineCollection

number_to_degrees = {
    k: (np.cos(np.pi * 2 / 10 * k), np.sin(np.pi * 2 / 10 * k))
    for k in range(10)
}


@click.command()
@click.option(
    "--seed", "-s", default=0, help="Seed for random number generation."
)
@click.option(
    "--length",
    "-l",
    default=10_000,
    help="Number of random numbers to generate.",
)
@click.option(
    "--cmap", "-c", default="RdYlGn", help="The matplotlib colour map to use."
)
@click.option(
    "--outfile",
    default=None,
    help="The outfile to save the image to (default None displays the image).",
)
@click.option(
    "--dpi",
    default=None,
    type=int,
    help="The DPI for the output image -- set for high-quality images if using a format like PNG.",
)
@click.option(
    "--linewidth",
    default=1.0,
    help="The width of the plotted lines -- consider decreasing for large lengths.",
)
def run(seed, length, cmap, outfile=None, dpi=None, linewidth=1.0):
    logger.info(f"Running with seed = {seed}")
    np.random.seed(seed)
    logger.info("Generating sequence of random numbers")
    seq = np.random.randint(0, 10, length)

    logger.info("Generating line coordinates")
    current_point = (0, 0)

    lines = []

    for number in seq:
        previous_x, previous_y = current_point
        delta_x, delta_y = number_to_degrees[number]
        new_point = [previous_x + delta_x, previous_y + delta_y]

        lines.append([current_point, new_point])
        current_point = new_point

    logger.info("Generating colours for lines")
    color_map = plt.get_cmap(cmap)
    colors = [color_map(i) for i in np.linspace(0, 1, length)]
    logger.info("Creating line collection")
    line_collection = LineCollection(
        lines, colors=colors, capstyle="round", linewidth=linewidth
    )

    # Plot
    logger.info("Plotting")
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.add_collection(line_collection)
    ax1.autoscale()

    plt.gca().set_aspect("equal", adjustable="box")
    plt.axis("off")
    plt.tight_layout()

    if outfile and outfile.endswith(".png") and dpi:
        plt.savefig(outfile, dpi=dpi)
    elif outfile:
        plt.savefig(outfile)
    else:
        plt.show()

    logger.success("Complete!")


if __name__ == "__main__":
    run()
