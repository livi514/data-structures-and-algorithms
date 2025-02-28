# Data Structures and Algorithms Project

## Overview
This project contains various implementations and explorations of data structures and algorithms specifically designed for a **lift/elevator simulation system**. It includes Python scripts, a Jupyter notebook, and supporting text files documenting different considerations, reports, and algorithmic approaches.

This project's primary focus is on implementing and analyzing scheduling and scanning algorithms that optimize lift movement by efficiently handling real-time requests. The different versions of these algorithms explore various improvements to response time, queue management, and path optimization.

## Installation

### Prerequisites
- Ensure you have Python installed (recommended version: 3.1).
- Install Jupyter Notebook if you wish to explore the notebook file:
 ```sh
  pip install notebook
 ```

## Usage

- Open `Data_structuers.ipynb` in Jupyter Notebook to explore structured implementations and algorithmic analysis.
- Run Python scripts using:
 ```sh
  python script_name.py
 ```
- Refer to text files for detailed documentation, considerations, and reports on each approach.

## File Descriptions

### Core Implementations
- **`Data_structuers.ipynb`** - Jupyter notebook containing structured implementations and analysis of the lift scheduling algorithms.
- **`mylift.py`** - Core lift simulation script implementing queue-based scheduling, handling multiple lift requests dynamically.

### LOOK Algorithm Variants
- **`look.py`** - Initial implementation of the LOOK scheduling algorithm applied to lift movement.
- **`look v2.py` - `look v5 real time requests.py`** - Iterative improvements and optimizations of the LOOK algorithm for handling real-time lift requests and optimizing efficiency.
- **`look v6 broken down functions.py`** - The **final and official** version of `look.py`, featuring modular, well-structured code optimized for real-time lift scheduling, including request prioritization and movement efficiency.

### SCAN Algorithm Variants
- **`scan.py`**, **`SCAN1.py`** - Implementations of the SCAN disk scheduling algorithm adapted for lift operations, optimizing floor visits to reduce overall travel time.

### Documentation & Reports
- **`specification.txt`** - Contains project specifications, detailing the goals, methodologies, and expected outcomes of the lift simulation.
- **`simulationreport.txt`** - A detailed report analyzing the results of various scheduling simulations, comparing different algorithmic approaches.
- **`generalconsiderations.txt`**, **`lookconsiderations.txt`**, **`scanconsiderations.txt`** - Various notes and considerations on the approaches, challenges, and improvements made to the algorithms.

## Author
This project was created by **Oghenemaro Emuophedaro**, **Livia Banyai** #Please add your names.

## License



