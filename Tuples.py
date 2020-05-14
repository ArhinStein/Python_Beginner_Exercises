#Lists and Tuples
# // Indexing
print('Hello! Could you please provide the year in which you were born?')

# Print out a date, given year, month, and day as numbers
months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"]

# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
+ ['st', 'nd', 'rd'] + 7 * ['th'] \
+ ['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)

# Split up a URL of the form http://www.something.com
url = input('Please enter the URL: ')
domain = url[11:-4]
print ("Domain name: " + domain)