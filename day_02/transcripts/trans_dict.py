Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["anil", 35, "Oracle", "India"]
>>> anil = ["anil", 35, "Oracle", "India"]
>>> sunil = ["sunil", 35, "Infosys", "India"]
>>> raj = ["sunil", 35, "Wipro", "India"]
>>> 
>>> 
>>> anil[2]
'Oracle'
>>> 
>>> anil1 = {"name":"anil", "age":35, "company":"Oracle", "country":"India"}
>>> type(anil1)
<class 'dict'>
>>> anil1["company"]
'Oracle'
>>> sunil1 = {"name":"sunil", "age":35, "company":"Infosys", "country":"India"}
>>> raj1 = {"name":"raj", "age":35, "company":"Wipro", "country":"India"}
>>> 
>>> 
>>> team = { anil1, sunil1, raj1 }
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    team = { anil1, sunil1, raj1 }
TypeError: unhashable type: 'dict'
>>> t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> 
>>> 
>>> 
>>> # ------------------------------------------
>>> 
>>> 
>>> D = {"name":"anil", "age":35, "company":"Oracle", "country":"India"}
>>> D
{'name': 'anil', 'age': 35, 'company': 'Oracle', 'country': 'India'}
>>> D['name']
'anil'
>>> D['age']
35
>>> D['age'] = 36
>>> D
{'name': 'anil', 'age': 36, 'company': 'Oracle', 'country': 'India'}
>>> D['dob'] = "20-09-1999"
>>> D
{'name': 'anil', 'age': 36, 'company': 'Oracle', 'country': 'India', 'dob': '20-09-1999'}
>>> del D["age"]
>>> D
{'name': 'anil', 'company': 'Oracle', 'country': 'India', 'dob': '20-09-1999'}
>>> 
>>> D1 = {"phone":"+918877665544", "addr":"Bangalore"}
>>> D.update(D1)
>>> D
{'name': 'anil', 'company': 'Oracle', 'country': 'India', 'dob': '20-09-1999', 'phone': '+918877665544', 'addr': 'Bangalore'}
>>> 
>>> D.pop("addr")
'Bangalore'
>>> D
{'name': 'anil', 'company': 'Oracle', 'country': 'India', 'dob': '20-09-1999', 'phone': '+918877665544'}
>>> 
>>> 
>>> # ------------------------------------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'country', 'dob', 'phone'])
>>> D.values()
dict_values(['anil', 'Oracle', 'India', '20-09-1999', '+918877665544'])
>>> D.items()
dict_items([('name', 'anil'), ('company', 'Oracle'), ('country', 'India'), ('dob', '20-09-1999'), ('phone', '+918877665544')])
>>> 
>>> 
>>> # ------------------------------------------------------
>>> 
>>> team = {}
>>> team['ANIL001'] = anil1
>>> team.setdefault('SUNIL001', sunil1)
{'name': 'sunil', 'age': 35, 'company': 'Infosys', 'country': 'India'}
>>> team['RAJ001'] = raj1
>>> team
{'ANIL001': {'name': 'anil', 'age': 35, 'company': 'Oracle', 'country': 'India'}, 'SUNIL001': {'name': 'sunil', 'age': 35, 'company': 'Infosys', 'country': 'India'}, 'RAJ001': {'name': 'raj', 'age': 35, 'company': 'Wipro', 'country': 'India'}}
>>> 
>>> team.keys()
dict_keys(['ANIL001', 'SUNIL001', 'RAJ001'])
>>> 'ANIL001' in team
True
>>> 
>>> team['ANIL001']
{'name': 'anil', 'age': 35, 'company': 'Oracle', 'country': 'India'}
>>> team['ANIL001']['name']
'anil'
>>> for key in team:
	if(team[key]['name'] == 'anil'):
		for k, v in team[key].items():
			print(k, ' --> ', v)

			
name  -->  anil
age  -->  35
company  -->  Oracle
country  -->  India
>>> for key in team:
	if(team[key]['name'] == 'sunil'):
		for k, v in team[key].items():
			print(k, ' --> ', v)

			
name  -->  sunil
age  -->  35
company  -->  Infosys
country  -->  India
>>> for key in team:
	if(team[key]['name'] == 'raj'):
		for k, v in team[key].items():
			print(k, ' --> ', v)

			
name  -->  raj
age  -->  35
company  -->  Wipro
country  -->  India
>>> 
>>> def printinfo(name):
	for key in team:
		if(team[key]['name'] == 'sunil'):
			for k, v in team[key].items():
				print(k, ' --> ', v)

				
>>> n = input("Whose data do you want? ")
Whose data do you want? anil
>>> printinfo(n)
name  -->  sunil
age  -->  35
company  -->  Infosys
country  -->  India
>>> def printinfo(name):
	for key in team:
		if(team[key]['name'] == name):
			for k, v in team[key].items():
				print(k, ' --> ', v)
		else:
			print("Record not found")

			
>>> printinfo(n)
name  -->  anil
age  -->  35
company  -->  Oracle
country  -->  India
Record not found
Record not found
>>> printinfo('sunil')
Record not found
name  -->  sunil
age  -->  35
company  -->  Infosys
country  -->  India
Record not found
>>> team['ANIL002'] = {'name': 'anil', 'age': 38, 'company': 'Oracle', 'country': 'India'}
>>> team
{'ANIL001': {'name': 'anil', 'age': 35, 'company': 'Oracle', 'country': 'India'}, 'SUNIL001': {'name': 'sunil', 'age': 35, 'company': 'Infosys', 'country': 'India'}, 'RAJ001': {'name': 'raj', 'age': 35, 'company': 'Wipro', 'country': 'India'}, 'ANIL002': {'name': 'anil', 'age': 38, 'company': 'Oracle', 'country': 'India'}}
>>> printinfo('anil')
name  -->  anil
age  -->  35
company  -->  Oracle
country  -->  India
Record not found
Record not found
name  -->  anil
age  -->  38
company  -->  Oracle
country  -->  India
>>> 
