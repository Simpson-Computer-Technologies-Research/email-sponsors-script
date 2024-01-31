##
## read_sponsors.py
##

##
## Libraries
##
from typing import List
from utils.sponsor import Sponsor
import csv


##
## Function to read the sponsors from a csv file
##
def read_sponsors(filename: str = "sponsors.csv"):
    sponsors: List = []

    ##
    ## Open the CSV file
    ##
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        ##
        ## For each row, get the company name and contact email
        ##
        for row in reader:
            ##
            ## If the sponsor email is invalid, skip it
            ##
            if not row["email"] or "@" not in row["email"]:
                continue

            ##
            ## Add the sponsor to the list
            ##
            sponsors.append(Sponsor(row["name"], row["email"]))

    ##
    ## Return the list of sponsors
    ##
    return sponsors
