"""Calculates the allocation of money for investment portfolio"""


import functions
from typing import Dict


def main():
    """Prints the ratios for the allocation of money"""
    # TODO: Delete this once you got the file reading done
    weight_ratios = {
        'OFSS' : 1.0,
        'ITC' : 1.0,
        'EBBETF0430' : 7.0,
        'NETFMID150' : 12.4,
        'GOLDBEES' : 14.0,
        'JUNIORBEES' : 14.0,
        'NIFTYBEES' : 14.0
    }

    print('Where would you like to read stock weight ratios from?\n')

    while True:     # Ensures that only valid input is given to source
        source = input('a for rtf file, b for excel file\nEnter here: ')

        if source.lower() in ('a', 'b'):
            break

        else:
            print('Please enter a valid input!')
            continue
    
    if source == 'a':
        weight_ratios: Dict[str, float] = functions.get_rtf_ratios()
    else:
        weight_ratios: Dict[str, float] = functions.get_excel_ratios()

    # To ensure that weights are in percentages, if not already.
    percentage_weights: Dict[str, float] = functions.get_percentage_weights(weight_ratios)     

    while True:
        command : str = str(input('\nEnter command (q to quit, enter to calculate) :'))

        if command.lower() == 'q':
            print('Quitting now! Hope I helped!')
            break

        elif command.lower() != '':
            print('Please enter a valid command!')
            continue

        else:
            print(
                '\nEnter money here.\n'
                'Note: If you want to check if your overall portfolio needs rebalancing, enter as\n'
                'current value + funds being added OR as total account value')
            total = input('\nEnter amount here: ')
            try:
                if '+' in total:
                    nums = total.split('+')
                    total = sum(map(float, nums))
                
                else:
                    total = float(total)

                print(f'Total value = {total}')
                functions.print_allocations(percentage_weights, total)
                    
            except ValueError as err:
                print(f'{err}\nPlease enter a number!')


        
if __name__ == '__main__':
    main()

    
              
    