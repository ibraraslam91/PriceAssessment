import argparse

from src.output.print import Print
from src.string_formator.uppercase import UpperCase
from src.string_formator.altercase import AlterCase
from src.file_generator.csv_generator import CSVGenerator

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", dest="string", help="input string")


if __name__ == "__main__":
    args = parser.parse_args()
    input_str = args.string

    Print.write(UpperCase.format(input_str))
    Print.write(AlterCase.format(input_str))
    CSVGenerator().write_file(input_str, "csv_file.csv")

