

from typing import Dict, List


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
    """Get the ratios from the rtf file in directory

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    file = 'portfolio_allocation/ratios.rtf'
    result_dict = {}
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        if line[0].isalpha():   # RTF files have a lot of random setting lines in the beginning.
            line = line[:-2]
            list1: List[str] = line.split(',')
            list1[1] = list1[1].strip()
            list1[1] = float(list1[1])
            
            result_dict.update({list1[0]: list1[1]})

    return result_dict


def get_excel_ratios() -> Dict[str, float]:
    """Get the ratios from the excel file in the directory

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    
    return {'sample': 1.0}


if __name__ == '__main__':
    pass