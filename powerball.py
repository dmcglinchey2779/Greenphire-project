# @Author: Daniel McGlinchey <dan_mac>
# @Date:   2017-05-06T12:13:46-04:00
# @Email:  dmcglinchey2779@icloud.com
# @Filename: powerball.py
# @Last modified by:   dan_mac
# @Last modified time: 2017-05-06T12:13:52-04:00

#The jackpot is won by matching all five white balls in any order and the red Powerball
#For future analysis, data will preserve the order in which entries are made
from collections import Counter

powerball_data_for_calculator = {}
powerball_entries = input('Press y if you want to enter your powerball favorite numbers. ')
while powerball_entries == 'y':
    first_name = input("What is your first name? ")
    first_name
    last_name = input("What is your last name? ")
    last_name

    #we draw five white balls out of a drum with 69 balls and one red ball out of a drum with 26 red balls
    first_five = []


    for number in range(5):
        number = int(input("Please enter your favorite number between 1 and 69. "))
        while number < 1 or number > 69:
            number = int(input("That number is not valid. Please enter a number between 1 and 69. "))
        while number in first_five:
            number = int(input("You already entered that number. Enter another favorite between 1 and 69. "))

        first_five.append(number)

    #print(first_five)

    power_ball_number_six = int(input("Please enter a number between 1 and 26 for your powerball favorite. "))
    while power_ball_number_six < 1 or power_ball_number_six > 26:
        power_ball_number_six = int(input("Your powerball number must be between 1 and 26. Try again. "))



    #print(power_ball_number_six)



    powerball_data_for_calculator[first_name + " " + last_name] = \
    {'1st': first_five[0], '2nd': first_five[1], '3rd': first_five[2], \
     '4th': first_five[3], '5th': first_five[4], 'Powerball': power_ball_number_six}



    powerball_entries = input("Press y if you want to enter your powerball favorites. Press n to end entries. ")


    #print(powerball_data_for_calculator)
    #print(powerball_data_for_calculator.items())

    #get entries by order of entry by each employee

def powerball_duplicates(position):
    powerball_by_position = []
    for employee,powerball in powerball_data_for_calculator.items():
        if position in powerball.keys():
            #print(powerball[position])
            powerball_by_position.append(powerball[position])
    return powerball_by_position

#Add all entries to list for counting of employee unique entries for the aggregate duplicates

all_entries = []


def aggregate_entries(data):
    for data_point in data:
        all_entries.append(data_point)

aggregate_entries(powerball_duplicates('1st'))
aggregate_entries(powerball_duplicates('2nd'))
aggregate_entries(powerball_duplicates('3rd'))
aggregate_entries(powerball_duplicates('4th'))
aggregate_entries(powerball_duplicates('5th'))



#print(all_entries)

#Counter.most_common() returns the number and its count as a tuple - limit return to the top five
#elements with equal counts are ordered arbitrarily meeting the tie-breaker requirement

top_five_favorites = Counter(all_entries).most_common(5)

#print(top_five_favorites)

top_powerball_favorite = Counter(powerball_duplicates('Powerball')).most_common(1)

#print(top_powerball_favorite)

powerball_winning_number = []

for favorite in top_five_favorites:
    powerball_winning_number.append(favorite[0])


#print(powerball_winning_number)

#print out employee entries
for employee,powerball in powerball_data_for_calculator.items():
    print(employee, end='      ')
    for position in powerball.keys():
        if position == 'Powerball':
            print('Powerball:', end=' ')
        print(powerball[position], end=' ')
    print()


print('Powerball winning number: ')
for number in powerball_winning_number:
    print(number, end=' ')

print('Powerball:', end=' ')
for favorite in top_powerball_favorite:
    print(favorite[0])
