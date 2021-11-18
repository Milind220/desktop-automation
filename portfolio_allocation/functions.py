

from typing import Dict, List

import openpyxl


def get_percentage_weights(weight_ratios: Dict[str, float]) -> Dict[str, float]:
    """Returns the fractional weightages of instruments.

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
    """Prints the final division of funds.

    Args:
        weights (Dict[str, float]): fractional weightages of instruments
        total (float): total money to be invested
    """
    for key in weights:
        fraction = weights[key]
        allocation = fraction * total

        print(f'\n{round((fraction * 100), 2)}% of {total} in {key} = {allocation}')


def get_rtf_ratios() -> Dict[str, float]:
    """Gets the ratios from the rtf file in directory.

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    result_dict = {}
    try:
        with open('portfolio_allocation/ratios.rtf', 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line[0].isalpha():   # RTF files have a lot of random setting lines in the beginning.

                line_list: List[str] = line.split(',')
                instrument: str = line_list[0]
                for i, x in enumerate(line_list[1][::-1]): # Iterate backwards.
                    if x.isdigit():
                        break
                    n = -i - 1 # find the index from the end where the float begins.
                ratio: float = float(line_list[1][:n])

                result_dict.update({instrument: ratio}) 
        return result_dict

    except Exception:
        print('Sorry, RTF file could not be read! Try the Excel file...')
        return {'sample': 1.0}
         

def get_excel_ratios() -> Dict[str, float]:
    """Gets the ratios from the excel file in the directory.

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    result_dict = {}
    try:
        wb = openpyxl.load_workbook(filename='portfolio_allocation/ratios.xlsx', read_only=True)
        ws = wb.active
        for row in ws.rows:
            result_dict.update({str(row[0].value): float(row[1].value)})
        return result_dict
                
    except Exception:
        print('Sorry, Excel file could not be read! Try the .rtf file...')
        return {'sample': 1.0}

    
if __name__ == '__main__':
    pass