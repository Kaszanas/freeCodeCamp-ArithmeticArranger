from arithmetic_arranger import arithmetic_arranger
from unittest import main
import argparse

# Adding command line argument parser:
parser = argparse.ArgumentParser(description='Provide list of operations')
parser.add_argument('-a', '--arrange', action='append', type=str, help="Provide a list of operations in a following format ['int + int', 'int - int']. Available operations are addition and subtraction.")
parser.add_argument('-o', '--output', type=bool, help='Flag which decides if the output will be calculated.')

# Parsing arguments:
args = parser.parse_args()

# Printing output:
print(arithmetic_arranger(problems=args.arrange, output_flag=args.output))