"""
This file comprises of definitions for allWayPoints and currentMissionInfo queries
"""
import graphene
from graphene_django import DjangoObjectType

from monitoring.rovers.models import (
    CuriosityWaypoint,
    PerseveranceWaypoint,
    IngenuityWaypoint,
    SampleTubesPoint,
)


class CuriosityWaypointType(DjangoObjectType):
    """
    Class for transforming CuriosityWaypoint Django model into object type
    """

    class Meta:
        model = CuriosityWaypoint
        fields = "__all__"


class PerseveranceWaypointType(DjangoObjectType):
    """
    Class for transforming PerseveranceWaypoint Django model into object type
    """

    class Meta:
        model = PerseveranceWaypoint
        fields = "__all__"


class IngenuityWaypointType(DjangoObjectType):
    """
    Class for transforming IngenuityWaypoint Django model into object type
    """

    class Meta:
        model = IngenuityWaypoint
        fields = "__all__"


class SampleTubesPointType(DjangoObjectType):
    """
    Class for transforming IngenuityWaypoint Django model into object type
    """

    class Meta:
        model = SampleTubesPoint
        fields = "__all__"


class Query(graphene.ObjectType):
    """
    Class for adding graphql query objects
    """

    curiosity_way_points = graphene.List(CuriosityWaypointType)
    perseverance_way_points = graphene.List(PerseveranceWaypointType)
    ingenuity_way_points = graphene.List(IngenuityWaypointType)
    sample_tubes_points = graphene.List(SampleTubesPointType)

    def resolve_curiosity_way_points(self, info):
        return CuriosityWaypoint.objects.all()

    def resolve_perseverance_way_points(self, info):
        return PerseveranceWaypoint.objects.all()

    def resolve_ingenuity_way_points(self, info):
        return IngenuityWaypoint.objects.all()

    def resolve_sample_tubes_points(self, info):
        return SampleTubesPoint.objects.all()


schema = graphene.Schema(query=Query)
