##
## email_format.py
##

##
## Libraries
##


##
## Convert a sponsor info to a formatted email
##
def email_format(
    company: str, contact_name: str, name: str, role: str, email: str
) -> str:
    if contact_name == "":
        contact_name = company

    return f"""
Dear {contact_name},

I hope this email finds you well. My name is {name} and I’m the {role} for the Google Developer Student Club (GDSC) at the University of Guelph. I’m reaching out to express our interest in {company} partnering with the GDSC for our upcoming hackathon that will take place from May 3rd to May 5th.

As a partner, {company} will gain significant visibility through branding opportunities and access to hundreds of students. Some perks include:
1. Your logo on merchandise, the GDSC Hacks website, a banner, and screens.
2. Direct engagement with our student body by hosting tech talks and interactive workshops.
3. A dedicated sponsor booth, the opportunity for 1-on-1 interviews with potential talent, and access to attendee resumes.

We truly appreciate your consideration. If you’d like to see the full list of perks the GDSC offers, I’d be more than happy to share our sponsorship package. If you require any more information, please let me know.

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
