import re
EOF = ''
# Read the file as a text

f = open( "resume.txt", "r" )
content = f.read()
f.close()
# Patterns

jobid = r"#\d{6}"
email = r""    # [TASK] complete this
phone = r"(\d{3}-){2}\d{4}"
linkedin = r"(linkedin.com)/\w+/[\w-]+"
name = r"([Ss]incerely|[Ff]aithfully)[,]?\s(?P<Name>\w+\s\w+)"

# [TASK] Also, add logic to extract the IP address in the resume

# Apply the patterns and store what ever is extracted



m = re.search(jobid, content)
if m:
    print('JOBID     : ', m.group())

m = re.search(email, content)
if m:
    print('EMAIL     : ', m.group())

m = re.search(phone, content)
if m:
    print('PHONE     : ', m.group())

m = re.search(linkedin, content)
if m:
    print('LINKEDIN  : ', m.group())

m = re.search(name, content)
if m:
    print('NAME      : ', m.groupdict()['Name'])