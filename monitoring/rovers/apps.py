"""
This file comprises of configurations for the graphql API

"""
from django.apps import AppConfig


class RoversConfig(AppConfig):
    """
    Class for configuring Rovers graphql APIs

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "monitoring.rovers"
