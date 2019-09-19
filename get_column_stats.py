
# Input: tab separated file of integers in defined column #
# Output: mean and standard deviation of the integers in column

import sys
import math
import argparse

# define required arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='column mean/std dev')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of file')

    parser.add_argument('--column_number',
                        type=int,
                        help='The column number')

    args = parser.parse_args()
    print(args.file_name, args.column_number)

    file_name = args.file_name
    col_num = args.column_number

    # Validate correct file name with access permission
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not fine' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open' + file_name)
        sys.exit(1)

    V = []

    # input column intergers into generator
    for col in file:
        try:
            A = [int(x) for x in col.split()]
        except ValueError:
            print('Check column values')
            sys.exit(1)
        try:
            V.append(int(A[col_num]))
        except IndexError:
            print('Problems with column number')
            sys.exit(1)

    # calculate mean
    mean = sum(V)/len(V)

    # calculate standard deviation
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)
