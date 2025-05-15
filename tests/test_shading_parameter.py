from dragonfly_schema.shading_parameter import (
    ExtrudedBorder,
    Overhang,
    LouversByDistance,
    LouversByCount,
)

import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples")


def test_shading_par_extruded_border():
    file_path = os.path.join(target_folder, "shading_par_extruded_border.json")
    # ExtrudedBorder.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ExtrudedBorder.model_validate_json(json_data)


def test_shading_par_overhang():
    file_path = os.path.join(target_folder, "shading_par_overhang.json")
    # Overhang.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Overhang.model_validate_json(json_data)


def test_shading_par_louvers_by_distance():
    file_path = os.path.join(target_folder, "shading_par_louvers_by_distance.json")
    # LouversByDistance.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    LouversByDistance.model_validate_json(json_data)


def test_shading_par_louvers_by_count():
    file_path = os.path.join(target_folder, "shading_par_louvers_by_count.json")
    # LouversByCount.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    LouversByCount.model_validate_json(json_data)
