"""Console script for jmaster."""
import sys
import click
from jmaster import jmaster


@click.command()
def main(args=None):
    """Console script for jmaster."""
    jmaster.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
