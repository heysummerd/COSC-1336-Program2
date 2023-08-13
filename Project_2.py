#---------------------
# Name: Summer Davis
# COSC 1336
# Project 2
#---------------------
# Objective
# This program will calculate a theater's gross and net box office profit
# for a single night.
#
# The program will ask users for the name of the movie, and how many
# adult and child tickets were sold.
#
# The price of a ticket is $6 for each adult, $3 for each child.
# The theater keeps 20% of the gross box office profit and the rest goes
# to the distributor.
#---------------------

# Named constants
ADULT_PRICE = 6
CHILD_PRICE = 3
DISTRIBUTOR_CUT = 0.8

# This function displays the start of the project
def header ():
    print('\n  Box Office Entry')
    print('-' * 80 + '\n')
    
def main():
    # Header of the project
    header()

    # Get movie name and ticket count
    movieName = input('  Enter Movie Name: ')
    adultTickets = getIntegerEntry('  Adult Tickets Sold: ')
    childTickets = getIntegerEntry('  Children Tickets Sold: ')

    # Calculate gross profit, amount paid to distributor, and net profit
    grossProfit = adultTickets * ADULT_PRICE + childTickets * CHILD_PRICE
    distributorCut = grossProfit * DISTRIBUTOR_CUT
    netProfit = grossProfit - distributorCut

    # Display movie summary
    movieSummary(movieName, grossProfit, distributorCut, netProfit)
    
    # End of project display
    footer()

# This will display the Movie Summary
def movieSummary(movie, gross, distributor, net):
    print('\n ' + '-' * 80)
    print('  Movie Summary (Daily)')
    print(' ' + '-' * 80 + '\n')
    print(f'    Movie Name: {movie}')
    print(f'    Gross Box Office Profit: ${gross:.2f}')
    print(f'    Amount Paid to Distributor: ${distributor:.2f}')
    print(f'    Net Box Office Profit: ${net:.2f}')

# This will get users entry of float data
def getFloatEntry(prompt):
    value = float(input(prompt))
    return value

# This will get users entry of integer data
def getIntegerEntry(prompt): 
    value = int(input(prompt))
    return value
    
# This function displays the end of the project
def footer():
    print('-' * 80)
    print('End of Project 2')
    
main()

