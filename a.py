import inflect
p = inflect.engine()

#open file
file = open("a_an_example.in.txt", "r").read()
#split file into lines
split = file.split("\n")

###Variable Declarations###

names  = [] #make names list
skills = [] #make skills list for each person

skillsRequired = []
taskName = []


recordNames = 1 #variable of number of indexes before record names again

#print(split)
#get the first line
lineOne = split[0]

#get number of contributers
numberOfContributers = lineOne.split(" ")[0]
#get number of projects
numberOfProjects = lineOne.split(" ")[1]

#print("Number of Contributors " + str(numberOfContributers))
#print("Number of Projects " + str(numberOfProjects))

#print(str(numberOfContributers) + " contributers, " + str(numberOfProjects) + " projects")
print(str(numberOfProjects) + "\t \t" + p.number_to_words(numberOfProjects) + " projects are planned")


#for loop
for i in range(1, len(split)):
  #get name
  #print(split[i])
  amountOfSkills = int(split[i].split(" ")[1])
  #print(amountOfSkills)
  
  currentIndex = i #get current index in the list
  #print(split[currentIndex] + " Current index: " + str(currentIndex) + " Amount of Skills: " + str(amountOfSkills))
  #print(str(currentIndex) + " " + str(recordNames))
  
  #print(str(len(split[i].split(" "))) + " " + split[i])
  if recordNames == currentIndex:
    userSkills = []
    if len(split[i].split(" ")) == 5:
      break

    recordNames = currentIndex + amountOfSkills + 1
    #print(split[currentIndex] + " Current index: " + str(currentIndex) + " Amount of Skills: " + str(amountOfSkills) + " Recording names again at: " + str(recordNames))
    
    #print(recordNames)
    #print(str(len(split[i].split(" "))) + " " + split[i])

    names.append(split[i].split(" ")[0])

    for n in range(int(split[i].split(" ")[1])):
      userSkills.append(split[currentIndex + n + 1])

    skills.append(userSkills)
  #print("Recording Names after: " + str(recordNames))
  #print(recordNames)
  
  
print(names)
print(skills)



recordNamesTask = recordNames

for i in range(recordNames, len(split)):



  currentIndex = i #get current index in the list
  
  if recordNamesTask == currentIndex:
    nameOfTask = split[i].split(" ")[0]
    daysToComplete = int(split[i].split(" ")[1])
    points = int(split[i].split(" ")[2])
    bestBefore = int(split[i].split(" ")[3])
    numberOfSkillsForTask = int(split[i].split(" ")[4])

    taskSkills = []
    recordNamesTask = currentIndex + numberOfSkillsForTask + 1
    #print(split[currentIndex] + " Current index: " + str(currentIndex) + " Amount of Skills: " + str(numberOfSkillsForTask) + " Recording names again at: " + str(recordNamesTask))
    
    #print(recordNames)
    #print(str(len(split[i].split(" "))) + " " + split[i])

    taskName.append(split[i].split(" ")[0])
    #print(split[i].split(" ")[4])
    for n in range(int(split[i].split(" ")[4])):
      #print(currentIndex + n + 1)
      taskSkills.append(split[currentIndex + n + 1])

    skillsRequired.append(taskSkills)
  #print("Recording Names after: " + str(recordNames))
  #print(recordNames)

#for i in range():

print(taskName)
print(skillsRequired)
