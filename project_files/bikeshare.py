import time
import pandas as pd
import numpy as np
import calendar

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

    # TO DO: get user input for city (chicago, new york city, washington).
    while True:
        city = input("Enter the city you would like to analyze (chicago, new york city, or washington): ").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Invalid city. Please try again.")

     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month you would like to filter by (all, january, february, ... , june) or type 'all' for no filter: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of the week you would like to filter by (all, monday, tuesday, ... sunday) or type 'all' for no filter: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please try again.")

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load the data file for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        # Get the month number for the specified month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # TO DO: display the most common month
        common_month = df['month'].mode()[0]
        print("Most Common Month:", calendar.month_name[common_month])
    except:
        print("Unable to determine the most common month.")

    try:
        # TO DO: display the most common day of week
        common_day = df['day_of_week'].mode()[0]
        print("Most Common Day of Week:", common_day)
    except:
        print("Unable to determine the most common day of week.")

    try:
        # TO DO: display the most common start hour
        df['Start Hour'] = df['Start Time'].dt.hour    
        print('The most common start hour for your selection is', 
              df['Start Hour'].value_counts().idxmax(), 'o\'clock.\n')
    except:
        print("Unable to determine the most common start hour.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station:", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).index[0]
    print("Most Frequent Start-End Station Combination:", start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of User Types:\n", user_type_counts)

    # TO DO : display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:\n", gender_counts)
    else:
        print("\nGender Data unavailable for this dataset.")

    # TO DO: display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nEarliest Birth Year:", earliest_birth_year)
        print("Most Recent Birth Year:", most_recent_birth_year)
        print("Most Common Birth Year:", most_common_birth_year)
    else:
        print("\nBirth Year Data unavailable for this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display(df):
    """Displays 5 lines of raw data at a time when 'yes' is selected."""
    start = 0
    while True:
        user_input = input(f'\nWould you like to see 5 lines of data? Enter "yes" or "no".\n')
        if user_input.lower() == 'yes':
            print(df.iloc[start:start+5])
            start += 5
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
