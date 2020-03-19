##Author - balachandar duraiswamy

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease select the city(chicago, new york city, washington):\n')
        if city in CITY_DATA:
            break
        print('Invalid entry. Try Again!! ')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease select the month(all, january, february, ... , june):\n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may' , 'june']:
            break
        print('Invalid entry. Try Again!! ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease select the week(all, monday, tuesday, ... sunday):\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' , 'saturday','sunday']:
            break
        print('Invalid entry. Try Again!! ')

    print('-'*40)
    month = month.lower()
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
    # load data file into a dataframe
    print('\nLoading the data... .. .. ..\n')
    df = pd.read_csv('./'+ CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    df['hour'] = df['Start Time'].dt.hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    commonMon = df['month'].value_counts().idxmax()
    print('\nMost common month: ',commonMon)

    # display the most common day of week
    commonDay = df['day_of_week'].value_counts().idxmax()
    print('\nMost common day of the week: ', commonDay)

    # display the most common start hour
    commonStartHour = df['hour'].value_counts().idxmax()
    print('\nMost Start Hour: ', commonStartHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nmost commonly used start station: ',start_station)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nmost commonly used end station: ',end_station)

    # display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("\nmost commonly used start station and end station : {}, {}".format(common_start_end_station[0], common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("\nTotal travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("\nMean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nCounts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print("{}: {}".format(user_counts.index[index], user_count))

    # Display counts of gender
    print("\nCounts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    for index, gender_count in enumerate(gender_counts):
        print("{}: {}".format(gender_counts.index[index], gender_count))

    # Display earliest, most recent, and most common year of birth
    birth_years_list = [x for x in df['Birth Year'] if pd.notnull(x)]
    birth_years = sorted(set(birth_years_list))
    print("\nEarliest birth year :", birth_years[0])
    print("\nMost recent birth year :", birth_years[len(birth_years)-1])
    commonYearBirth = max(set(birth_years_list), key=birth_years_list.count)
    print("\nCommon birth year :", commonYearBirth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
