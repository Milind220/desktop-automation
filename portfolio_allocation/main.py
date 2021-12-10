"""Calculates the allocation of money for investment portfolio"""


from typing import Dict

import functions


def main():
    """Prints the ratios for the allocation of money"""
    functions.configure_logs()
    print("\nWhere would you like to read stock weight ratios from?\n")

    while True:  # Ensures that only valid input is given to source
        source = input("a for rtf file, b for excel file\nEnter here: ")

        if source.lower() in ("a", "b"):
            break
        else:
            print("Please enter a valid input!")
            continue

    if source == "a":
        weight_ratios: Dict[str, float] = functions.get_rtf_ratios()
    else:
        weight_ratios: Dict[str, float] = functions.get_excel_ratios()

    # To ensure that weights are in percentages, if not already.
    percentage_weights: Dict[str, float] = functions.get_percentage_weights(
        weight_ratios
    )
    while True:
        command: str = str(input("\nEnter command (q to quit, enter to calculate) :"))

        if command.lower() == "q":
            print("Quitting now! Hope I helped!")
            break
        elif command.lower() != "":
            print("Please enter a valid command!")
            continue
        else:
            print(
                "\nEnter funds here.\n"
                "Note: If you want to check if your overall portfolio needs rebalancing, enter as\n"
                "current value + funds being added OR as total account value"
            )
            total: float = functions.get_input_total()
            print(f"Total value = {total}")

            functions.show_output(percentage_weights, total)


if __name__ == "__main__":
    main()
