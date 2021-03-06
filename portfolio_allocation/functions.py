"""Functions to be used in main.py for this script"""


import logging
import sys
from typing import Dict, List

import matplotlib.pyplot as plt
import openpyxl

# TODO: format private and public functions in correct order.
# TODO: Add print statement reminder to tell user to close the plot.


def configure_logs(logfile_name: str = "portfolio_allocation_errors.log") -> None:
    """Configures settings for the script log.

    Args:
        logfile_name (str, optional): Name of the log file. Defaults to
            'portfolio_allocation_errors.log'.  
    """
    logging.basicConfig(
        filename=logfile_name,
        filemode="w",
        level=logging.ERROR,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    print(
        "\n\nStatus: Logs configured."
        f"\n\tLogs for this run can be found in {logfile_name}"
    )


def get_percentage_weights(weight_ratios: Dict[str, float]) -> Dict[str, float]:
    """Returns the fractional weightages of instruments.

    Args:
        weight_ratios (Dict[str, float]): Weightage ratios that you set

    Returns:
        Dict[str, float]: Final fractional weightages
    """
    percentage_weight_dict = {}
    total = sum(weight_ratios.values())
    unit_fraction = 1 / total

    for key in weight_ratios:
        weight = weight_ratios[key]
        weight_fraction = unit_fraction * weight
        percentage_weight_dict.update({key: weight_fraction})

    return percentage_weight_dict


def _print_allocations(weights: Dict[str, float], total: float) -> None:
    """Prints the final division of funds.

    Args:
        weights (Dict[str, float]): fractional weightages of instruments
        total (float): total money to be invested
    """
    for ticker in weights:
        fraction = weights[ticker]
        allocation = fraction * total

        print(f"\n{round((fraction * 100), 2)}% of {total} in {ticker} = {allocation}")


def get_rtf_ratios() -> Dict[str, float]:
    """Gets the ratios from the rtf file in directory.

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    result_dict = {}
    try:
        with open("ratios.rtf", "r") as f:
            lines = f.readlines()

        for line in lines:
            # RTF files have a lot of random setting lines in the beginning.
            if line[0].isalpha():
                line_list: List[str] = line.split(",")
                instrument: str = line_list[0]

                for i, x in enumerate(line_list[1][::-1]):  # Iterate backwards.
                    if x.isdigit():
                        break
                    n = -i - 1  # find the index from the end where the float begins.
                ratio: float = float(line_list[1][:n])

                result_dict.update({instrument: ratio})
        return result_dict

    except Exception:
        print("Sorry, RTF file could not be read! Try the Excel file...")
        _log_error(section="RTF file")
        return {"sample": 1.0}


def get_excel_ratios() -> Dict[str, float]:
    """Gets the ratios from the excel file in the directory.

    Returns:
        Dict[str, float]: Dictionary of stocks and ratios
    """
    result_dict = {}
    try:
        wb = openpyxl.load_workbook(filename="ratios.xlsx", read_only=True)
        ws = wb.active
        for row in ws.rows:
            result_dict.update({str(row[0].value): float(row[1].value)})
        return result_dict

    except Exception:
        print("Sorry, Excel file could not be read! Try the .rtf file...")
        _log_error(section="Excel file")
        return {"sample": 1.0}


def get_input_total():
    while True:
        try:
            total = input("\nEnter amount here: ")
            if "+" in total:
                nums = total.split("+")
                total = sum(map(float, nums))

            total = float(total)
            break

        except ValueError:
            print("Sorry\nPlease enter a number!")
            _log_error(section="get_input_total")
            continue

    return total


def _generate_allocation_figure(weights: Dict[str, float], total: float):
    values: List[float] = list(weights.values())
    labels: List[str] = []
    for ticker in weights:
        fraction: float = weights[ticker]
        allocation: float = total * fraction
        labels.append(f"{ticker}: {fraction*100}% = {allocation}")

    plt.bar(range(len(weights)), values, tick_label=labels)
    plt.tick_params(axis="x", labelsize=6, rotation=20)
    plt.show()


def _log_error(section: str) -> None:
    logging.error(f"Scraping error: {section}\n" f"\tError: {sys.exc_info()[0]}\n")


def show_output(weights: Dict[str, float], total: float):
    print("See allocations in command line or graphical output")
    choice = input(
        "Enter 1 for command line, 2 for graphical output, anything else for both : "
    )
    if choice == "1":
        _print_allocations(weights, total)
    elif choice == "2":
        _generate_allocation_figure(weights, total)
    else:
        _print_allocations(weights, total)
        _generate_allocation_figure(weights, total)


if __name__ == "__main__":
    pass
