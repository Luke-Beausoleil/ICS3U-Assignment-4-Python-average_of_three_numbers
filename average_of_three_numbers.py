#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program averages three inputted number from 0 - 100

import constants


def main():
    # this function finds the average

    # input
    first_number_as_string = input("Enter the first number: ")
    second_number_as_string = input("Enter the second number: ")
    third_number_as_string = input("Enter the third number: ")

    # process & output
    try:
        first = float(first_number_as_string)
        second = float(second_number_as_string)
        third = float(third_number_as_string)
        average = (first + second + third) / 3
        if first >= constants.MIN and first <= constants.MAX:
            if second >= constants.MIN and second <= constants.MAX:
                if third >= constants.MIN and third <= constants.MAX:
                    print("\nThe average is {0}".format(average))
                else:
                    print("\nInvalid. Enter numbers from 1 - 100")
            else:
                print("\nInvalid. Enter numbers from 1 - 100")
        else:
            print("\nInvalid. Enter numbers from 1 - 100")
    except (Exception):
        print("\nInvalid. Enter numbers from 1 - 100")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
