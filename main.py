##
## main.py
##

##
## Libraries
##
from utils.clear_file import clear_file
from utils.email_format import email_format
from utils.read_sponsors import read_sponsors


##
## Main function
##
## The main function reads the sponsors from a csv file and
## generates a formatted email for each sponsor. The emails
## are then written to a text file.
##
def main():
    ##
    ## Constants
    ##
    EMAIL_FILE: str = "emails/emails.txt"
    SPONSORS_FILE: str = "sponsors/sponsors.csv"

    ##
    ## Open the emails text file and clear it
    ##
    clear_file(EMAIL_FILE)

    ##
    ## Read the sponsors from the csv file
    ##
    sponsors = read_sponsors(SPONSORS_FILE)

    ##
    ## For each sponsor, generate a formatted email
    ##
    for sponsor in sponsors:
        ##
        ## Generate the formatted email
        ##
        formatted_email = email_format(
            sponsor.name,
            "Tristan Simpson",
            "Events Director",
            "tsimps01@uoguelph.ca",
        )

        ##
        ## Append the formatted email to the emails text file
        ##
        with open(EMAIL_FILE, "a") as file:
            file.write(formatted_email + "\n\n\n")


##
## Run the main function
##
if __name__ == "__main__":
    main()

##
## End of main.py
##
