from dragonfly_schema.model import Room2D, Story, Building, ContextShade, Model
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples")


def test_room2d_simple():
    file_path = os.path.join(target_folder, "room2d_simple.json")
    # Room2D.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Room2D.model_validate_json(json_data)


def test_story_simple():
    file_path = os.path.join(target_folder, "story_simple.json")
    # Story.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Story.model_validate_json(json_data)


def test_story_air_boundary():
    file_path = os.path.join(target_folder, "story_air_boundary.json")
    # Story.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Story.model_validate_json(json_data)


def test_building_simple():
    file_path = os.path.join(target_folder, "building_simple.json")
    # Building.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Building.model_validate_json(json_data)


def test_context_shade_two_tree_canopy():
    file_path = os.path.join(target_folder, "context_shade_two_tree_canopy.json")
    # ContextShade.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ContextShade.model_validate_json(json_data)


def test_model_complete_simple():
    file_path = os.path.join(target_folder, "model_complete_simple.dfjson")
    # Model.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Model.model_validate_json(json_data)


def test_model_with_doors_skylights_and_roof():
    file_path = os.path.join(target_folder, "model_with_doors_skylights.dfjson")
    # Model.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    Model.model_validate_json(json_data)
