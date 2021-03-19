class student(object):

    nstudents = 0
    schoolname = ''

    # Data/attributes
    def __init__(self, name, cls, rid):
        print('Initializing values.....')
        # [TASK 1]Identify and write all the variables needed here
        student.nstudents += 1

    # [TASK 2]Complete the functions/methods

    def setschoolname(self, schoolname):
        pass

    def printinfo(self):
        self.state = 'Karnataka'
        print('STATE : ', self.state)
        print('SCHOOL: ', student.schoolname)
        print('-----------------------------------')
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)
        print('NSTUDENTS  ------> ', student.nstudents)
        print('\n')

    def setMaths(self, marks):
        pass

    def setPhysics(self, marks):
        pass

    def setChemistry(self, marks):
        pass

    def setBiology(self, marks):
        pass

    def calcAverage(self):
        pass

#######################################################################################

if __name__ == '__main__':

    s1 = student('Rohit', 12, 'A001')
    s1.setschoolname("Kendriya Vidyalaya")

    s2 = student('Ram', 12, 'A002')
    s2.setschoolname("Kendriya Vidyalaya")

    s3 = student('Anil', 12, 'A003')
    s3.setschoolname("Kendriya Vidyalaya")

    print(s1)
    print(len(s1))

    # OUTPUT:
    # A001_Rohit_KV
    # 3
    



   