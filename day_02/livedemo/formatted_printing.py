team = { '01':{"name":"anil", "dob":"19-09-1999", "company":"oracle"},
         '02':{"name":"sunil", "dob":"29-09-1997", "company":"oracle"},
         '03':{"name":"raj", "dob":"11-01-1982", "company":"oracle"},
         '04':{"name":"kumar", "dob":"05-09-1989", "company":"oracle"},
         '05':{"name":"anil", "dob":"01-09-1995", "company":"oracle"}
        }

print("\nTEAM")
print("-" * 50)
for person in team:
    print(" |    ", team[person]['name'].ljust(10), " | ", team[person]['dob'].ljust(10), " | ", team[person]['company'].ljust(10), " | ")
print("-" * 50)
