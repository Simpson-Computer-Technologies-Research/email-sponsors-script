##
## email_format.py
##

##
## Libraries
##


##
## Convert a sponsor info to a formatted email
##
def email_format(company: str, name: str, role: str, email: str) -> str:
    return f"""
Dear {company},

I hope this email finds you well. My name is {name} and I’m an {role} for the Google Developer Student Club (GDSC) at the University of Guelph. I am reaching out to express my interest in {company} partnering with the GDSC for our upcoming hackathon that will take place from May 3rd to May 5th. The Google Developer Student Club is a student-led organization supported by Google – dedicated to fostering an innovative environment for over 250 young tech professionals in Guelph.

With your financial support, {company} will be able to contribute to a memorable experience for students. In return, you will gain exclusive access to emerging talent and student resumes, significant brand visibility (specific details can be found on our sponsorship package), and recognition for your commitment to education – strengthening your relationship with the University of Guelph. We’d be more than happy to provide our sponsorship package with all of the exclusive perks and marketing opportunities that we provide.

We are confident that a partnership between the GDSC and {company} will yield substantial mutual benefits. We appreciate your consideration of this partnership opportunity Please feel free to reach out if you have any questions or if there is any other information that I can provide.

Thank you,

{name}
{role}
Google Developer Student Club, University of Guelph
{email}
"""
    ##
    ## End of email_format function
    ##


##
## End of email_format.py
##
