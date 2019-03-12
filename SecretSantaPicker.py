import random

ListofPeople="People.txt"
ListofSantas="Santas.txt"

def secretsanta():
    with open(ListofSantas, "w") as santalist:
        santalist.write("Secret Santa List:\n---------------------------\n")
    Myfile=open(ListofPeople, "r")
    names=Myfile.readlines()
    count=len(names)
    counter=int(len(names)-1)
    newnames=random.sample(names,count)

    for name in names:
        if name==newnames[counter]:
            print "Somone got themselves... starting over...."
            secretsanta()
            break
        with open(ListofSantas, "a") as santalist:
            santalist.write(name.strip('\n') + " Shops for "+ newnames[counter])
        #print(name.strip('\n') + " Shops for "+ newnames[counter])
        counter=counter-1

secretsanta()
print "done"

