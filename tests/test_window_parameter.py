from dragonfly_schema.window_parameter import (
    SingleWindow,
    SimpleWindowRatio,
    RepeatingWindowRatio,
    RepeatingWindowWidthHeight,
    RectangularWindows,
    DetailedWindows,
)
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples")


def test_window_par_single_window():
    file_path = os.path.join(target_folder, "window_par_single_window.json")
    # SingleWindow.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    SingleWindow.model_validate_json(json_data)


def test_window_par_simple_window_ratio():
    file_path = os.path.join(target_folder, "window_par_simple_window_ratio.json")
    # SimpleWindowRatio.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    SimpleWindowRatio.model_validate_json(json_data)


def test_window_par_repeating_window_ratio():
    file_path = os.path.join(target_folder, "window_par_repeating_window_ratio.json")
    # RepeatingWindowRatio.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    RepeatingWindowRatio.model_validate_json(json_data)


def test_window_par_repeating_window_width_height():
    file_path = os.path.join(
        target_folder, "window_par_repeating_window_width_height.json"
    )
    # RepeatingWindowWidthHeight.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    RepeatingWindowWidthHeight.model_validate_json(json_data)


def test_window_par_detailed_rectangular_windows():
    file_path = os.path.join(
        target_folder, "window_par_detailed_rectangular_windows.json"
    )
    # RectangularWindows.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    RectangularWindows.model_validate_json(json_data)


def test_window_par_detailed_windows():
    file_path = os.path.join(target_folder, "window_par_detailed_windows.json")
    # DetailedWindows.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    DetailedWindows.model_validate_json(json_data)
