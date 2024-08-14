
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name.")

    # Get user input for month (all, january, february, ..., june)
    while True:
        month = input("Enter month (all, January, February, ..., June): ").strip().lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    # Get user input for day of week (all, monday, tuesday, ..., sunday)
    while True:
        day = input("Enter day (all, Monday, Tuesday, ..., Sunday): ").strip().lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

  
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print(month) # 3 for march

        # filter by month to create the new dataframe
        df = df[df['month'] == month] # df.loc[(df['month'] == 6)]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month: ", popular_month)
    print("__")

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of week: ", popular_day)
    print("__")

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip ...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", popular_start_station)
    print("__")

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: ", popular_end_station)
    print("__")

    # display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most frequent combination of start station and end station trip: ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel_time)
    print("__")
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types: ", user_types)

    print("__")
    
    # only for NYC and chicago:
    if 'Gender' in df.columns and 'Birth Year' in df.columns:

      # Display counts of gender
      gender = df['Gender'].value_counts()
      print("Counts of gender: ", gender)
      print("__")

      # Display earliest, most recent, and most common year of birth
      earliest_year = df['Birth Year'].min()
      most_recent_year = df['Birth Year'].max()
      most_common_year = df['Birth Year'].mode()[0]

      print("Earliest year of birth: ", earliest_year)
      print("Most recent year of birth: ", most_recent_year)
      print("Most common year of birth: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print("No data available for the selected filters.")
            continue

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Display raw data upon user request
        start_index = 0
        while True:
            view_raw = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if view_raw.lower() != 'yes':
                break
            
            print(df.iloc[start_index:start_index + 5])
            start_index += 5
            
            more_data = input('\nWould you like to see more raw data? Enter yes or no.\n')
            if more_data.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()