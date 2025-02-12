"""
hw
A toolkit for efficient data processing and visualization.

Version: 1.2.0
Author: Jane Doe
License: MIT

This package provides:
    - Data cleaning utilities (data_cleaning)
    - Data transformation tools (data_transformation)
    - Visualization helpers (data_visualization)

Usage:
    from mypackage import clean_data, transform_data, plot_results
    cleaned = clean_data(raw_input)
    transformed = transform_data(cleaned)
    plot_results(transformed)

Dependencies:
    - numpy >= 1.18.0
    - pandas >= 1.0.0
    - matplotlib >= 3.0.0

Changelog:
    v1.2.0 - Added data_visualization module
    v1.1.0 - Optimized data cleaning performance
    v1.0.0 - Initial release
"""
from pathlib import Path
import sys

if __debug__:
    print(f"Initializing {Path(__file__).parent.stem}")

RUNNING_IN_JUPYTER = Path(sys.argv[0]).stem.startswith('ipykernel')
if RUNNING_IN_JUPYTER:
    try:
        import ipynbname
        nb_path = ipynbname.path()
        # print(f"Notebook name: {nb_path.name}")
        # print(f"Full path: {nb_path}")
    except FileNotFoundError:
        print("Can't find the notebook name. Are you running this in a notebook?")

RUNNING_CLI = not RUNNING_IN_JUPYTER
PROGRAM = Path(__file__).parent.stem if RUNNING_CLI else nb_path.stem
