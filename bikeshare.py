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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityname=['chicago','new york city','washington']
    
    city=input("Enter the city (chicago, new york city, washington)  ").lower()
    while city not in cityname:
        city=input(" plese enter  the city agin (chicago, new york city, washington) ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)f
    monthname=['all','january', 'february', 'march', 'april', 'may', 'june']
    month=input("Enter the monthe you want to filter by (january, february, ... , june)  or all if you want to see all month      ").lower()
    while month not in monthname:
        month=input("Enter agin the monthe you want to filter by (january, february, ... , june)  or all if you want to see all month  ").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayname=['all','monday','tuesday','wendsday','thursday','friday','saturday','sunday']
    day=input("enter the day  you want to filter on (monday, tuesday, ... sunday) or all if you want to see all day ").lower()
    while day not in dayname:
        day=input("enter the day  you want to filter on (monday, tuesday, ... sunday) or all if you want to see all day ").lower()
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.day_name()
    
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month  ',common_month)

    # TO DO: display the most common day of week
    common_dayof_week=df['day_of_week'].mode()[0]
    print('The most common day of week ',common_dayof_week)
    # TO DO: display the most common start hour
    
    common_hour=df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour',common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station=df['Start Station'].mode()
    print('Most commonly used start station',common_start_station)

    # display most commonly used end station
    common_end_station=df['End Station'].mode()
    print('Most commonly used end station',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination_station=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip \n ',combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltraveltime=df['Trip Duration'].sum()
    print('total travel time ',totaltraveltime)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
   
    # Display counts of user types
    usertypes=df['User Type'].value_counts()
    print('user types ',usertypes)
    
    # Display counts of gender
    if city!= 'washington':
      gender=df['Gender'].value_counts()
      print(gender)
       # Display earliest, most recent, and most common year of birth
    
      df['Birth Year'] = pd.to_datetime(df['Birth Year']) 

      df['year'] = df['Birth Year'].dt.year
    
      maxyear=df['year'].max()
      print('recent year of birth ',maxyear)
      commanyear=df['year'].mode()
      print('most common year of birth ',commanyear)
      minyear=df['year'].min()
      print('earliest year of birth ',minyear)  
    else:print('counts of gender and  year of birth only available for NYC and Chicago')    

   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_row_data(df):
    choice = input('Do you like to see example from the raw Data, if you want type \'yes\' if else type \'no\' \n>').lower()
    c=['yes','no']
    print(choice)
    while choice not in c :
      choice=input("Enter yes or no ").lower()
 
    x=0   
    if choice == 'no':
                 print('Thank you for Exploring US BikeShare')
                 
    elif choice == 'yes':
                 #city, month, day = get_filters()
                 #df = load_data(city, month, day)
                 print(df.iloc[x: x + 5])  
                 
                 more=input("more data  yes or no ")
                 if(more not in c):
                   more=input("enter yes or no ")     
                 while (more =='yes'):   
                    if x<(len(df.index)-5):    
                         x = x + 5
                         print(df.iloc[x: x + 5])
                         more=input("more data  yes or no ")
                         if(more not in c):
                            more=input("enter   yes or no ")     
                    else:
                         break;   
    
 


def main():
    while True:
     
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
