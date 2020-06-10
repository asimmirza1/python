courses = {"CS1": "Introduction to Java",
             "CS2": "Java II",
             "CS3": "Data Structures in Java",
             "Calc1": "Calculs I",
             "Calc2": "Calculs II",
             "Calc3": "Calculs III",
             "AI1": "Introduction to AI",
             "ML1": "Introduction to Machine learning",
             "ML2": "Advance Machine Learning",
}

courseIndexMapping = {1: "CS1",
                      2: "CS2",
                      3: "CS3",
                      4: "Calc1",
                      5: "Calc2",
                      6: "Calc3",
                      7: "AI1",
                      8: "ML1",
                      9: "ML2"}

selectedCourses = {}

def showRegisteredCourses():
  if len(selectedCourses) == 0:
    print("\n-- No courses are registered --")
    return
  cnt = 1
  print("\n Registered courses are\n")
  for course in selectedCourses:
    print(f"  -- {cnt}  {selectedCourses[course]} \n")
    cnt += 1

def showAvailableCourses():
  print("\n")
  print("* Please select a course from the following list\n")
  index = 0
  for course in courses:
    index += 1
    print(f"{index}" + " " + courses[course] + "\n")
  print("!! Enter 0 to exit course selection menu\n")

def dropACourse():
  showRegisteredCourses()
  counter = 1
  while(True):
    if len(selectedCourses) == 0:
      print("-- No courses registered --\n")
      break
    selection = int(input("Select course number to drop or 0 to exit: "))
    if selection == 0:
      break
    for course in selectedCourses:
      if counter == selection:
        del selectedCourses[course]
        break
      else:
        counter += 1
    showRegisteredCourses()

def registerCourse():
  showAvailableCourses()
  while(True):
    selection = int(input("* Please select course number to register or 0 to exit: "))

    if selection == 0:
      break
    elif selection not in (1,2,3,4,5,6,7,8, 9):
      print("\n -- Invliad course selection -- ")
    elif len(selectedCourses) >= 4:
      print("\n-- You have already registered for 4 courses. --\n")
      break
    else:
      selectedCourses[courseIndexMapping[selection]] = courses[courseIndexMapping[selection]] 
    showAvailableCourses()
    showRegisteredCourses()

def showMenu():
  print("\n")
  print("Enter 1 to Register course\n")
  print("Enter 2 to Drop course\n")
  print("Enter 3 to Browse registered courses\n")
  print("!! Enter 0 to Exit registration system\n")

def processCourseRegistration(response):
    if response == 1:
      registerCourse()
    elif response == 2:
      dropACourse()
    elif response == 3:
      showRegisteredCourses()

#main program loop
print("\n")
print("Course Registration System")
print("__________________________")
while(True):
  showMenu()
  #read the input here.
  response = (int(input("* Enter your choice from the menu: ")))
  if response == 0:
    break;
  elif response not in (1,2,3,4):
     print("\n\n")
     print("-- Invalid response, please enter the correct choice --")
  else: 
    processCourseRegistration(response)