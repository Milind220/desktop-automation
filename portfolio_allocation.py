"""Calculates the allocation of money for investment portfolio"""


from typing import Dict


def main():
    """Generates the ratios for the allocation of money"""
    
    weight_ratios = {
        'OFSS' : 1.0,
        'ITC' : 1.0,
        'EBBETF0430' : 7.0,
        'NETFMID150' : 12.4,
        'GOLDBEES' : 14.0,
        'JUNIORBEES' : 14.0,
        'NIFTYBEES' : 14.0
    }

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

    for key in weights:
        fraction = weights[key]
        allocation = fraction * total

        print(f'\n{round((fraction * 100), 2)}% of {total} in {key} = {allocation}')


if __name__ == '__main__':
    main()

    
              
    