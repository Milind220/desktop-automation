"""Calculates the allocation of money for investment portfolio"""


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
    
    weight_ratios: Dict[str, float] = get_ratio_data(source)

    # To ensure that weights are in percentages, if not already.
    percentage_weights: Dict[str, float] = get_percentage_weights(weight_ratios)     

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
                print_allocations(percentage_weights, total)
                    
            except ValueError as err:
                print(f'{err}\nPlease enter a number!')


def get_percentage_weights(weight_ratios: Dict[str, float]) -> Dict[str, float]:
    """Returns the fractional weightages of instruments

    Args:
        weight_ratios (Dict[str, float]): Weightage ratios that you set

    Returns:
        Dict[str, float]: Final fractional weightages
    """
    percentage_weight_dict = {}
    total = sum(weight_ratios.values())
    unit_fraction = 1/total

    for key in weight_ratios:
        weight = weight_ratios[key]
        weight_fraction = unit_fraction * weight
        percentage_weight_dict.update({key: weight_fraction}) 

    return percentage_weight_dict


def print_allocations(
                    weights: Dict[str, float],
                    total: float) -> None: 
    """Prints the final division of funds

    Args:
        weights (Dict[str, float]): fractional weightages of instruments
        total (float): total money to be invested
    """
    for key in weights:
        fraction = weights[key]
        allocation = fraction * total

        print(f'\n{round((fraction * 100), 2)}% of {total} in {key} = {allocation}')


def get_rtf_ratios() -> Dict[str, float]:
    return {'sample': 1.0}


def get_excel_ratios() -> Dict[str, float]:
    return {'sample': 1.0}


def get_ratio_data(source: str) -> Dict[str, float]:

    if source == 'a':
        data = get_rtf_ratios()

    else: 
        data = get_excel_ratios()
    
    return data
        



if __name__ == '__main__':
    main()

    
              
    