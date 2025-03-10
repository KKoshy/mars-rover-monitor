"""
Tool to generate html pages for each current and diff .json file to be published in GH pages.
"""
import json
import logging
import os

import click

logging.basicConfig(
    format="GenerateHTMLPages: %(asctime)s %(name)s %(levelname)s %(processName)s "
    "%(threadName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
log = logging.getLogger(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <script src="https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js"></script>
    <link href="https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css" rel="stylesheet">
    <style>
        #json-table {{ width: 100%; }}
        body {{ font-family: Arial, sans-serif; text-align: center; }}
    </style>
</head>
<body>
    <h2>{title}</h2>
    <div id="json-table"></div>

    <script>
        fetch("{json_file}")
            .then(response => response.json())
            .then(data => {{
                new Tabulator("#json-table", {{
                    data: data,
                    autoColumns: true,
                    layout: "fitDataFill",
                    pagination: "local",
                    paginationSize: 20,
                    movableColumns: true,
                    filterable: true
                }});
            }})
            .catch(error => console.error("Error loading JSON:", error));
    </script>
    <a href="index.html">Back to Home</a>
</body>
</html>
"""


def create_html(temp_json):
    """
    Create HTML page for the JSON file created

    :param temp_json: temporary json file created with reformatted data
    """
    base_name = os.path.basename(temp_json)
    title = base_name.replace(".json", ".html")
    temp_html = os.path.join(os.path.abspath(os.path.dirname(__file__)), title)
    html_content = template.format(
        title=f"Table for {os.path.basename(temp_json)}", json_file=base_name
    )
    with open(temp_html, "w") as h1:
        h1.write(html_content)


def reformat_json_data(file_name):
    """
    Reformat JSON data from fixtures

    :param file1: previous json
    :return: temporary reformatted json file created
    """
    log.info("Converting data to flat JSON")
    flat_data = []
    with open(file_name, "r", encoding="utf-8") as f1:
        prev_data = json.load(f1)
    base_name = (
        os.path.basename(file_name)
        if "json_diffs" not in file_name
        else f"new_{os.path.basename(file_name)}"
    )
    for data in prev_data:
        reformed_data = dict()
        reformed_data["pk"] = data["pk"]
        reformed_data.update(data["fields"])
        flat_data.append(reformed_data)
    temp_json = os.path.join(os.path.abspath(os.path.dirname(__file__)), base_name)
    with open(temp_json, "w", encoding="utf-8") as j1:
        json.dump(flat_data, j1, indent=4)
    return temp_json


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
def render_pages(file_name):
    """
    Creates HTML page from the json provided

    :param file_name: JSON file name
    """
    temp_json = reformat_json_data(file_name)
    create_html(temp_json)


if __name__ == "__main__":
    render_pages()
