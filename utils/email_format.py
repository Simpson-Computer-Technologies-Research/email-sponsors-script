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

I hope this email finds you well. My name is {name} and I’m the {role} for the Google Developer Student Club (GDSC) at the University of Guelph. I am reaching out to express my interest in {company} partnering with the GDSC for our upcoming hackathon that will take place from April 26th to April 28th. The Google Developer Student Club is a student-led organization supported by Google – dedicated to fostering an innovative environment for over 250 young tech professionals in Guelph.

With your financial support, {company} will be able to contribute to a memorable experience for students. In return, you will gain exclusive access to emerging talent and student resumes, significant brand visibility (specific details can be found on our sponsorship package), and recognition for your commitment to education – strengthening your relationship with the University of Guelph. Attached to this email is the sponsorship package where you can find all of the exclusive perks and marketing opportunities that the Google Developer Student Club at the University of Guelph provides.

We are confident that a partnership between the GDSC and {company} will yield substantial mutual benefits. We appreciate your consideration of this partnership opportunity. To see past events held by the GDSC team, which include speaker sessions, workshops, and Google flagship events, visit our website here. Please feel free to reach out if you have any questions or if there is any other information that I can provide.

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
