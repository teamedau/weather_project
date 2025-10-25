import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    ##return f"{temp}{DEGREE_SYMBOL}"

    return f"{temp}{DEGREE_SYMBOL}"





def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    now = datetime.fromisoformat(iso_string)
    formatted_date = now.strftime("%A %d %B %Y")
    return formatted_date
        


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celcius = 5/9*(float(temp_in_fahrenheit) - float(32))
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    number_weather_data = [float(i) for i in weather_data]
    total_sum = sum(number_weather_data)
    count = len(number_weather_data)
    mean_value =float(total_sum / count)
    return mean_value

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    #0. create empty list named empty_list
    empty_list = []
    # 1. Open the file
    with open(csv_file) as file:
        reader = csv.reader(file)
        # 2. Skips the header row
        next(reader)
        
        for row in reader:
            #print(row)
            if len(row) > 0:
                #3. append to your 
                row [1] = int(row[1])
                #print(row)
                row [2] = int(row[2])
                #print(row)
                empty_list.append(row)
            #print ('row=' ,row)
            #print ('list=',empty_list)

#4. return list
    return empty_list




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, 
        return the index of the *last* example in the list.)
    """
    if not weather_data: 
        return ()
    weather_data = [float(i) for i in weather_data]
    min_value=min(weather_data)
    index = len(weather_data)-1-weather_data[::-1].index(min_value)
    return (min_value, index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, 
        return the index of the *last* example in the list.)
    """
    if not weather_data: 
        return ()
    weather_data = [float(i) for i in weather_data]
    max_value=max(weather_data)
    index = len(weather_data)-1-weather_data[::-1].index(max_value)
    return (max_value, index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_days = len(weather_data)
    min_temps = [float(day[1]) for day in weather_data]
    max_temps = [float(day[2]) for day in weather_data]
    # Find lowest temperature and its day
    min_temp = min(min_temps)
    min_index = min_temps.index(min_temp)
    min_day = convert_date(weather_data[min_index][0])
    # Find highest temperature and its day
    max_temp = max(max_temps)
    max_index = max_temps.index(max_temp)
    max_day = convert_date(weather_data[max_index][0])
    avg_min = sum(min_temps) / num_days
    avg_max = sum(max_temps) / num_days
    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {min_day}.\n"
        f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {max_day}.\n"
        f"  The average low this week is {convert_f_to_c(avg_min):.1f}°C.\n"
        f"  The average high this week is {convert_f_to_c(avg_max):.1f}°C."
    )
    return summary+"\n"


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    lines = []
    for day in weather_data:
        date_str = convert_date(day[0])
        min_temp = format_temperature(convert_f_to_c(float(day[1])))
        max_temp = format_temperature(convert_f_to_c(float(day[2])))
        lines.append(f"---- {date_str} ----")
        lines.append(f"  Minimum Temperature: {min_temp}")
        lines.append(f"  Maximum Temperature: {max_temp}\n")
    return "\n".join(lines).strip()+"\n"+"\n"