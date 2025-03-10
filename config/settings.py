import os


class Settings:
    CURIOSITY_MAP = "https://science.nasa.gov/mission/msl-curiosity/location-map/"
    CURIOSITY_JSON = os.path.join("monitoring", "rovers", "fixtures", "curiosity_rover_data.json")
    CURIOSITY_WAYPOINT_MODEL = "rovers.curiositywaypoint"
    PERSEVERANCE_MAP = "https://science.nasa.gov/mission/mars-2020-perseverance/location-map/"
    PERSEVERANCE_JSON = os.path.join(
        "monitoring", "rovers", "fixtures", "perseverance_rover_data.json"
    )
    PERSEVERANCE_WAYPOINT_MODEL = "rovers.perseverancewaypoint"
    INGENUITY_JSON = os.path.join("monitoring", "rovers", "fixtures", "ingenuity_copter_data.json")
    INGENUITY_WAYPOINT_MODEL = "rovers.ingenuitywaypoint"
    SAMPLE_TUBES_JSON = os.path.join("monitoring", "rovers", "fixtures", "sample_tubes_data.json")
    SAMPLE_TUBES_MODEL = "rovers.sampletubespoint"
