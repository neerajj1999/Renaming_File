import os
from os import path

def main():
    if path.exists("RegData (54)Malayam.xlsx"):
        src = path.realpath("RegData (54)Malayam.xlsx");

        os.rename("RegData (54)Malayam.xlsx","regdata.xlsx")


if __name__ == "__main__":
    main()

