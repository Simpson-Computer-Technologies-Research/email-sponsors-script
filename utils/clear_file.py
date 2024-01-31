##
## clear_file.py
##

##
## Libraries
##


##
## Function to clear a file
##
def clear_file(filename: str):
    with open(filename, "w") as file:
        file.write("")

    ##
    ## End of clear_file function
    ##


##
## End of clear_file.py
##
