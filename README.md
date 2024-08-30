>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
14/8/2024

### Project Title
Explore US Bikeshare Data

### Description
This project provides an analysis of bike share systems data for three major U.S. cities: Chicago, New York City, and Washington, D.C. The script offers insights into popular travel times, stations, trip durations, and user demographics. It also provides an interactive terminal experience to explore the raw data and statistics based on user input.

### Project File

- **bikeshare.py**: The main Python script that allows users to filter the data by city, month, and day of the week, and then displays various statistics.
- **chicago.csv**: Dataset containing bike share data for Chicago (January - June 2017).
- **new_york_city.csv**: Dataset containing bike share data for New York City (January - June 2017).
- **washington.csv**: Dataset containing bike share data for Washington, D.C. (January - June 2017).

### Requirements

To run this project, you'll need:

- Python 3.x
- pandas (`pip install pandas`)
- numpy (`pip install numpy`)

### How to Use

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

