"""
This file comprises of models for Curiosity Waypoint

"""
from django.db import models


class CuriosityWaypoint(models.Model):
    """
    Class for defining fields of CuriosityWaypoint

    """

    type = models.CharField(max_length=20, default="Feature")

    # Properties field
    RMC = models.CharField(max_length=20)
    site = models.IntegerField()
    drive = models.IntegerField()
    sol = models.IntegerField()
    easting = models.FloatField()
    northing = models.FloatField()
    elev_geoid = models.FloatField()
    lon = models.FloatField()
    lat = models.FloatField()
    roll = models.FloatField()
    pitch = models.FloatField()
    yaw = models.FloatField()
    yaw_rad = models.FloatField()
    tilt = models.FloatField()
    dist_m = models.FloatField()
    dist_total_m = models.FloatField()
    dist_km = models.FloatField()
    dist_mi = models.FloatField()
    drive_type = models.CharField(max_length=20)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    z_coordinate = models.FloatField()

    def __str__(self):
        return f"Curiosity feature for {self.sol}"


class PerseveranceWaypoint(models.Model):
    """
    Class for defining fields of PerseveranceWaypoint

    """

    type = models.CharField(max_length=20, default="Feature")

    # Properties field
    RMC = models.CharField(max_length=20)
    site = models.IntegerField()
    drive = models.IntegerField()
    sol = models.IntegerField()
    easting = models.FloatField()
    northing = models.FloatField()
    elev_geoid = models.FloatField()
    elev_radii = models.FloatField()
    radius = models.FloatField()
    lon = models.FloatField()
    lat = models.FloatField()
    roll = models.FloatField()
    pitch = models.FloatField()
    yaw = models.FloatField()
    yaw_rad = models.FloatField()
    tilt = models.FloatField()
    dist_m = models.FloatField()
    dist_total_m = models.FloatField()
    dist_km = models.FloatField()
    dist_mi = models.FloatField()
    final = models.CharField(max_length=20)
    Note = models.CharField(max_length=20)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    z_coordinate = models.FloatField()

    def __str__(self):
        return f"Perseverance feature for {self.sol}"


class IngenuityWaypoint(models.Model):
    """
    Class for defining fields of IngenuityWaypoint

    """

    Flight = models.IntegerField()
    Sol = models.IntegerField()
    SF3_X = models.FloatField()
    SF3_Y = models.FloatField()
    SF3_Z = models.FloatField()
    Easting = models.FloatField()
    Northing = models.FloatField()
    Elev_Geoid = models.FloatField()
    Lon = models.FloatField()
    Lat = models.FloatField()
    Dist_m = models.FloatField()
    Total_m = models.FloatField()
    Total_km = models.FloatField()
    Dist_ft = models.FloatField()
    Total_ft = models.FloatField()
    Total_mi = models.FloatField()
    Max_Alt_m = models.FloatField()
    Max_Alt_ft = models.FloatField()
    Max_Spd_m = models.FloatField()
    Max_mph = models.FloatField()
    Duration_s = models.FloatField()
    total_s = models.FloatField()
    total_min = models.FloatField()
    Earth_Date = models.CharField(max_length=100)
    SCLK_START = models.FloatField()
    SCLK_END = models.FloatField()
    FromAirfld = models.CharField(max_length=100)
    ToAirfld = models.CharField(max_length=100)
    QUAT_X = models.FloatField()
    QUAT_Y = models.FloatField()
    QUAT_Z = models.FloatField()
    QUAT_C = models.FloatField()
    roll = models.FloatField()
    pitch = models.FloatField()
    yaw = models.FloatField()
    yaw_rad = models.FloatField()
    tilt = models.FloatField()
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    z_coordinate = models.FloatField()

    def __str__(self):
        return f"Flight {self.Flight} on {self.Earth_Date}"


class SampleTubesPoint(models.Model):
    """
    Class for defining fields of SampleTubesPoint
    """

    sample_start = models.CharField(max_length=10)
    sample_num = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    sol = models.CharField(max_length=10)
    sample_name = models.CharField(max_length=100)
    outcrop_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=50)
    easting = models.FloatField()
    northing = models.FloatField()
    elev = models.FloatField()
    lon = models.FloatField()
    lat = models.FloatField()
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    z_coordinate = models.FloatField()

    def __str__(self):
        return f"Sample {self.sample_name} on {self.date}"
