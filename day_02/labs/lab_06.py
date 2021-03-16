#LAB 06

team = { '01':{"name":"anil", "dob":"19-09-1999", "company":"oracle"},
         '02':{"name":"sunil", "dob":"29-09-1997", "company":"oracle"},
         '03':{"name":"raj", "dob":"11-01-1982", "company":"oracle"},
         '04':{"name":"kumar", "dob":"05-09-1989", "company":"oracle"},
         '05':{"name":"anil", "dob":"01-09-1995", "company":"oracle"}
        }

# Task:
# Remove "dob" from the records and add "age"
# Calculated age from the dob as of todat and update

'''
>>> dob = "19-09-1999"
>>> age = 2021 - int(dob.split('-')[2])
>>> d = {"name":"anil", "dob":"19-09-1999", "company":"oracle"}
>>> d["age"] = 2021 - int(dob.split('-')[2])
>>> d.pop("dob")
'19-09-1999'
>>> d
{'name': 'anil', 'company': 'oracle', 'age': 22}
'''
