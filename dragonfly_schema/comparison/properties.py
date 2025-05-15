"""Model comparison properties."""
from pydantic import StringConstraints, Field
from typing import List, Union

from honeybee_schema._base import NoExtraBaseModel

from ..window_parameter import SingleWindow, SimpleWindowArea, SimpleWindowRatio, \
    RepeatingWindowRatio, RectangularWindows, DetailedWindows
from ..skylight_parameter import GriddedSkylightArea, GriddedSkylightRatio, \
    DetailedSkylights
from typing_extensions import Annotated


class Room2DComparisonProperties(NoExtraBaseModel):

    type: Annotated[str, StringConstraints(pattern='^Room2DComparisonProperties$')] = \
        'Room2DComparisonProperties'

    floor_boundary: List[Annotated[List[float], Field(min_length=2, max_length=2)]] = Field(
        None,
        min_length=3,
        description='A list of 2D points representing the outer boundary vertices of '
        'the Room2D to which the host Room2D is being compared. The list should '
        'include at least 3 points and each point should be a list of 2 (x, y) values.'
    )

    floor_holes: List[Annotated[List[Annotated[List[float], Field(min_length=2, max_length=2)]], Field(min_length=3)]] \
        = Field(
        None,
        description='Optional list of lists with one list for each hole in the floor '
        'plate of the Room2D to which the host Room2D is being compared. Each hole '
        'should be a list of at least 2 points and each point a list '
        'of 2 (x, y) values. If None, it will be assumed that there are no '
        'holes in the floor plate.'
    )

    comparison_windows: List[Union[
        None, SingleWindow, SimpleWindowArea, SimpleWindowRatio, RepeatingWindowRatio,
        RectangularWindows, DetailedWindows
    ]] = Field(
        default=None,
        description='A list of WindowParameter objects that dictate the window '
        'geometries of the Room2D to which the host Room2D is being compared.'
    )

    comparison_skylight: Union[
        None, GriddedSkylightArea, GriddedSkylightRatio, DetailedSkylights
    ] = Field(
        default=None,
        description='A SkylightParameter object for the Room2D to which the host '
        'Room2D is being compared.'
    )


class ModelComparisonProperties(NoExtraBaseModel):

    type: Annotated[str, StringConstraints(pattern='^ModelComparisonProperties$')] = 'ModelComparisonProperties'
