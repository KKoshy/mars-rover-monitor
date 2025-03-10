"""
Tool to compare the waypoints .json file generated in the previous run with the current run
and create diff file for each previous and current .json file.
"""
import json
import logging

import click

logging.basicConfig(
    format="UpdatesDiff: %(asctime)s %(name)s %(levelname)s %(processName)s "
    "%(threadName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
log = logging.getLogger(__name__)


def trace_new_points(file1, file2, output_file):
    """
    Compares two files and returns the differences.

    :param file1: previous json
    :param file2: current json
    :param output_file: output json with new trace points
    """
    difference = []
    log.info("Capture new points obtained")
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        prev_data = json.load(f1)
        current_data = json.load(f2)
        prev_points = set([item["pk"] for item in prev_data][:-1])
        difference = [item for item in current_data if item["pk"] not in prev_points]

    log.info(f"Difference: {difference}")
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(difference, file, indent=4)


@click.command()
@click.argument("file1", type=click.Path(exists=True))
@click.argument("file2", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
def main(file1, file2, output_file):
    """
    Compares file1 and file2 and saves the differences in output_file.

    :param file1: previous json
    :param file2: current json
    :param output_file: output json with new trace points
    """
    trace_new_points(file1, file2, output_file)
    click.echo(f"Differences saved to {output_file}")


if __name__ == "__main__":
    main()
