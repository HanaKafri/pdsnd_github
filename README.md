>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

## Udacity Project 3
# BikeShare Project Refactoring with Git

This project demonstrates a realistic workflow for version control using Git. The task involves refactoring a **previous project** (project 2) on analyzing bike share systems in various cities using Python, while practicing Git commands to manage branches, commits, and merges effectively.

## Date created
14/8/2024

## Udacity Project 2 Title:
Explore US Bikeshare Data

## Project Overview

This project provides an analysis of bike share systems data for three major U.S. cities: Chicago, New York City, and Washington, D.C. The script offers insights into popular travel times, stations, trip durations, and user demographics. It also provides an interactive terminal experience to explore the raw data and statistics based on user input.
In this refactoring project, we will use Git to manage the workflow and improve the project's codebase and documentation.

## Project Workflow

### 1. Set Up The Repository

- **Fork and Clone Repository**
- **Add Files:**
  - Add the `bikeshare.py` file, which contains the python code that allows users to analyze bike share data.
  - Add the `data` folder containing data files (e.g., `chicago.csv`, `new_york_city.csv`, `washington.csv`). 
  - Create a `.gitignore` file to exclude the data files from version control to prevent tracking large datasets and to maintain privacy.

### 2. Branches: 

- Documentation Branch: to handle all documentation improvements.
- Refactoring Branch: to work on code improvements.

### 3. Merge Branches

- **Merge Branches to Master**

### Requirements

To run this project, you'll need:

- Python 3.x
- pandas (`pip install pandas`)
- numpy (`pip install numpy`)

### How to Run Python Code

1. **Run the Script**: Execute `bikeshare.py` in your terminal or command prompt.

   ```bash
   python bikeshare.py
   ```

2. **Interactive Prompts**: You will be prompted to select a city (Chicago, New York City, Washington), a month (all, January, February, ..., June), and a day of the week (all, Monday, Tuesday, ..., Sunday). Based on your selection, the script will load and filter the data.

3. **View Statistics**: The script will display statistics on:
   - **Popular times of travel**: Most common month, day of the week, and start hour.
   - **Popular stations and trip**: Most common start station, end station, and most frequent combination of start and end stations.
   - **Trip duration**: Total and average trip durations.
   - **User information**: Breakdown of user types, gender counts (for Chicago and NYC), and birth year statistics (earliest, most recent, and most common).

4. **Raw Data Display**: After viewing the statistics, you will be asked if you want to see the raw data. If you choose to, the script will display 5 lines of raw data at a time, and continue showing more if requested.

5. **Restart or Exit**: You will be prompted to restart the analysis or exit the program.


### Notes

- The dataset for Washington, does not include `Gender` and `Birth Year` columns, so the related statistics will not be displayed for this city.

