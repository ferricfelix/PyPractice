# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(teachers):
    return len(teachers)

def num_courses(teachers):
    numCourses = 0
    for teacher in teachers:
        numCourses += len(teachers[teacher])
    return numCourses

def courses(teachers):
    coursesList = []
    for teacher in teachers:
        for course in teachers[teacher]:
            coursesList.append(course)
    return coursesList

def most_courses(teachers):
    mostCourses = 0
    name = ""
    for teacher in teachers:
        testLen = len(teachers[teacher])
        if testLen > mostCourses:
            mostCourses = testLen
            name = teacher
    return name