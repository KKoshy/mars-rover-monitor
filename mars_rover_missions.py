"""
This file helps collect waypoints data from the MSL website

"""
import json
import logging
from urllib.parse import urlparse

from playwright.sync_api import Response, sync_playwright

from config.settings import Settings

logging.basicConfig(
    format="CuriosityWaypoints: %(asctime)s %(name)s %(levelname)s %(processName)s "
    "%(threadName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
log = logging.getLogger(__name__)


class MarsRoverMissions:
    def __init__(self):
        self.settings = Settings()
        self.pw = sync_playwright().start()

    def start_browser(self):
        """
        Starts the browser
        """
        log.info("Starting browser")
        self.browser = self.pw.chromium.launch(headless=True)
        context_params = {"viewport": {"width": 1280, "height": 720}}
        self.context = self.browser.new_context(**context_params)
        self.context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True,
        )
        self.context.set_default_navigation_timeout(60000)
        self.context.set_default_timeout(60000)
        self.page = self.context.new_page()

    def stop_browser(self):
        """
        Stops the browser
        """
        log.info("Stopping browser")
        self.context.tracing.stop(path="curiosity_trace.zip")
        self.browser.close()
        self.pw.stop()

    def predicate_response(self, response: Response, method: str, paths: tuple, statuses: tuple):
        """
        Collects data from the UI API request
        """
        url_parser = urlparse(response.url)
        check = True
        if (
            response.request.method == method
            and url_parser.path in paths
            and (response.ok or response.status in statuses)
        ):
            return check

    def load_site_map(self, endpoint: str, site_map: str):
        """
        Loads the Curiosity Rover site map from MSL
        """
        log.info("Loading mission site map")
        with self.page.expect_response(
            lambda response: self.predicate_response(response, "GET", (endpoint,), (200,))
        ) as response_info:
            self.page.goto(site_map)
        self.mission_data = response_info.value.json()["features"]

    def serialize_curiosity_json(self, mission_model: str):
        """
        Serialize the json obtained in django format
        """
        serialized_data = []
        for feature in self.mission_data:
            feature_data, fields = dict(), dict()
            pk = (
                "sample_start"
                if "sample_start" in feature["properties"]
                else "sol"
                if "sol" in feature["properties"]
                else "Sol"
            )
            feature_data["pk"] = feature["properties"][pk]
            feature_data["model"] = mission_model
            fields.update(feature["properties"])
            fields["x_coordinate"] = feature["geometry"]["coordinates"][0]
            fields["y_coordinate"] = feature["geometry"]["coordinates"][1]
            fields["z_coordinate"] = feature["geometry"]["coordinates"][2]
            if "images" in fields:
                del fields["images"]
            feature_data["fields"] = fields
            serialized_data.append(feature_data)
        self.mission_data = serialized_data

    def create_json_data(self, file_name: str):
        """
        Creates a json file with the mission data
        """
        with open(file_name, "w") as wd:
            json.dump(self.mission_data, wd, indent=4)

    def collect_curiosity_waypoints(self):
        """
        Control method for collecting the curiosity waypoints data
        """
        self.load_site_map(
            endpoint="/mmgis-maps/MSL/Layers/json/MSL_waypoints.json",
            site_map=self.settings.CURIOSITY_MAP,
        )
        self.serialize_curiosity_json(mission_model=self.settings.CURIOSITY_WAYPOINT_MODEL)
        self.create_json_data(self.settings.CURIOSITY_JSON)

    def collect_perseverance_waypoints(self):
        """
        Control method for collecting the perseverance waypoints data
        """
        self.load_site_map(
            endpoint="/mmgis-maps/M20/Layers/json/M20_waypoints.json",
            site_map=self.settings.PERSEVERANCE_MAP,
        )
        self.serialize_curiosity_json(mission_model=self.settings.PERSEVERANCE_WAYPOINT_MODEL)
        self.create_json_data(self.settings.PERSEVERANCE_JSON)

    def collect_ingenuity_waypoints(self):
        """
        Control method for collecting the ingenuity waypoints data
        """
        self.load_site_map(
            endpoint="/mmgis-maps/M20/Layers/json/m20_heli_waypoints.json",
            site_map=self.settings.PERSEVERANCE_MAP,
        )
        self.serialize_curiosity_json(mission_model=self.settings.INGENUITY_WAYPOINT_MODEL)
        self.create_json_data(self.settings.INGENUITY_JSON)

    def collect_sample_tube_points(self):
        """
        Control method for collecting the sample points
        """
        self.load_site_map(
            endpoint="/mmgis-maps/M20/Layers/json/M20_SAMPLE_v3.json",
            site_map=self.settings.PERSEVERANCE_MAP,
        )
        self.serialize_curiosity_json(mission_model=self.settings.SAMPLE_TUBES_MODEL)
        self.create_json_data(self.settings.SAMPLE_TUBES_JSON)


if __name__ == "__main__":
    mrm = MarsRoverMissions()
    mrm.start_browser()
    mrm.collect_curiosity_waypoints()
    mrm.collect_perseverance_waypoints()
    mrm.collect_ingenuity_waypoints()
    mrm.collect_sample_tube_points()
    mrm.stop_browser()
