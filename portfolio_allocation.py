"""Calculates the allocation of money for investment portfolio"""

def main():
    """Generates the ratios for the allocation of money"""

    assets = {'OFSS' : 0.025, 
              'ITC' : 0.025, 
              'EBBETF0430' : 0.140, 
              'GOLDBEES' : 0.270, 
              'NIFTYBEES' : 0.270, 
              'JUNIORBEES' : 0.270}

    while True:
        command : str = str(input('\nEnter command (q to quit, enter to calculate) :'))

        if command.lower() == 'q':
            print('Quitting now! Hope I helped!')
            break

        else:
            total =  float(input('\nEnter amount here: '))

            for key in assets:
                fraction = assets[key]
                allocation = fraction * total
                print(f'\n{fraction * 100}% of {total} in {key} = {allocation}')

if __name__ == '__main__':
    main()

    
              
    