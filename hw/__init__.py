__doc__ = """
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

Example Usage: ./run -v
"""

from argparse import ArgumentParser as AP
import os
from pathlib import Path
from pprint import pprint as pp
from shlex import split
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
DESCRIPTION = __doc__[2]
EPILOG = __doc__[-1]
STD_OPTS = [[[],
  {"dest": "args",
   "metavar": "ARGUMENTS",
   "nargs": "*",
   "help": "Files to be processed."
  }
 ],

      [["-V", "--version"], {"action": "version", "version": "ncv 0.0.0", "help": "Display the program name and version, then exit."}],
      [["-d", "--debug"], {"action": "store_true", "dest": "debug", "help": "Set to run the program in DEBUG mode."}],
      [["-v", "--verbose"], {"action": "store_true", "dest": "verbose", "help": "Display extra information."}],
      [["-r", "--recursive"], {"action": "store_true", "dest": "recursive", "help": "Process files recursively."}],
      [["-t", "--testing"], {"action": "store_true", "dest": "testing", "help": "Run the `doctest`s in `main.py`"}],
      [["-s", "--follow"], {"action": "store_true", "dest": "follow", "help": "Follow symbolic links."}],
      [["-a", "--all"], {"action": "store_true", "dest": "all", "help": "Process hidden files."}],
      [["-c", "--config"], {"dest": "config", "help": "Specify a configuration file."}],
      [["-i", "--input"], {"dest": "input", "help": "Specify a file to be used as input."}],
      [["-o", "--output"], {"dest": "output", "help": "Specify a file to be used as output."}],
      [["-q", "--quiet"], {"action": "store_true", "dest": "quiet", "help": "Suppress screen output."}],
      [["-l", "--log"], {"dest": "log", "help": "Specify a log file."}],
      [["-w", "--warnings"], {"dest": "warnings", "help": "Display warning messages."}]
    ]

ap = AP(prog=PROGRAM, description=DESCRIPTION, epilog=EPILOG)
for option in STD_OPTS:
    ap.add_argument(*option[0], **option[1])
if RUNNING_IN_JUPYTER: ap.add_argument("-f")
ARGS = ap.parse_args(sys.argv[1:] if RUNNING_CLI else split(os.environ['CMD_LINE']))

if __debug__:
    print(f'{ARGS.debug=}')
    print(f'{ARGS.verbose=}')

VERBOSE = ARGS.verbose

if VERBOSE:
    print("Checking for log file...")
    print(f'{ARGS.log=}')

