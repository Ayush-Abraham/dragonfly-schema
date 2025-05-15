"""Geometry for specifying sloped roofs over a Story."""
from pydantic import StringConstraints, Field

from honeybee_schema._base import NoExtraBaseModel
from honeybee_schema.model import Face3D
from typing import List
from typing_extensions import Annotated


class RoofSpecification(NoExtraBaseModel):
    """Geometry for specifying sloped roofs over a Story."""

    type: Annotated[str, StringConstraints(pattern='^RoofSpecification$')] = 'RoofSpecification'

    geometry: Annotated[List[Face3D], Field(min_length=1)] = Field(
        ...,
        description='An array of Face3D objects representing the geometry of the '
        'Roof. None of these geometries should overlap in plan and, together, these '
        'Face3D should either completely cover or skip each Room2D of the Story '
        'to which the RoofSpecification is assigned.'
    )
