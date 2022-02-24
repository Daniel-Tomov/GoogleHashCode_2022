#open file
file = open("a_an_example.in.txt", "r").read()
#split file into lines
split = file.split("\n")

###Variable Declarations###

names  = [] #make names list

n = 1 #make variable for line number

recordNames = 0 #variable of number of indexes before record names again

#print(split)
#get the first line
lineOne = split[0]

#get number of contributers
numberOfContributers = lineOne.split(" ")[0]
#get number of projects
numberOfProjects = lineOne.split(" ")[1]

print("Number of Contributors " + str(numberOfContributers))
print("Number of Projects " + str(numberOfProjects))

#for loop
for i in range(1, len(split)):
  #get name
  #print(split[i])
  amountOfSkills = int(split[i].split(" ")[1])
  #print(amountOfSkills)
  
  currentIndex = i - 1 #get current index in the list
  #print(currentIndex)
  
  if recordNames == 0:
    recordNames = currentIndex + amountOfSkills
    print("Current Index: " + str(currentIndex) + " Amount of skills: " + str(amountOfSkills) + " Recording Names at index: " + str(recordNames))
    print(split[recordNames])
    #print(recordNames)
    names.append(split[i].split(" ")[0])
    
  recordNames = recordNames - 1
  #print("Recording Names after: " + str(recordNames))
  #print(recordNames)
  
  
  
  if (n != 0):
    n = n - 1
    

  


print(names)
