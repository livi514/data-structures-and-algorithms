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
- **`LOOK.py`** - Implementation of the LOOK scheduling algorithm applied to lift movement.Featuring modular functions for better maintainability, optimized movement, and real-time scheduling. 

### SCAN Algorithm Variants
- **`scan.py`** - Implements the SCAN algorithm, which moves the lift in a single direction, serving requests, and only reversing when it reaches the top or bottom floor.

### Documentation & Reports
- **`specification.txt`** - Contains project specifications, detailing the goals, methodologies, and expected outcomes of the lift simulation.
- **`simulationreport.txt`** - A detailed report analyzing the results of various scheduling simulations, comparing different algorithmic approaches.
- **`generalconsiderations.txt`**, **`lookconsiderations.txt`**, **`scanconsiderations.txt`** - Various notes and considerations on the approaches, challenges, and improvements made to the algorithms.

# How the Lift System Works
1. The system reads a lift configuration file, which includes:
   - The number of floors in the building.
   - The capacity of the lift.
   - A list of requests from different floors.
2. The algorithm processes these requests using either the **LOOK** or **SCAN** scheduling strategies.
3. The lift moves in an optimized path, reducing unnecessary travel and ensuring efficiency.
## Author
This project was created by **Oghenemaro Emuophedaro**, **Livia Banyai**, **Thalia Champ**, #Please add your names.

## License



