from datetime import date, timedelta

class Task:
    def __init__(self, name, deadline, hoursNeeded):
        self.name = name
        self.deadline = deadline
        self.hoursNeeded = hoursNeeded
        self.remaining = hoursNeeded

    def timeLeft(self):
        today = date.today()
        left = self.deadline - today
        return left

    def logStudy(self, hours):
         self.remaining -= hours

    def printTask(self):
        print(f"Name: {self.name}, Deadline: {self.deadline}, Hours Left to Complete: {self.remaining}.")


def printTasks(tasks):
    for task in tasks:
        task.printTask()

def printSchedule(schedule):
    for day, task in schedule.items():
        print(day, task)
          

def checkCompleted(tasks, completed):
    for task in tasks[:]:
        if task.remaining <= 0:
            tasks.remove(task)
            completed.append((task.name, task.deadline))

def buildSchedule(tasks, hoursPerDay):
    if not tasks:
        return {}, []
    tasks.sort(key=lambda task: task.deadline)
    left = {task: task.remaining for task in tasks} # Used to plan time in schedule
    schedule = {}
    day = date.today()
    lastDay = tasks[-1].deadline
    while day <= lastDay:
        hoursLeft = hoursPerDay
        plan = []
        for task in tasks:
            if hoursLeft == 0:
                break
            if left[task] > 0 and day <= task.deadline:
                hours = min(left[task], hoursLeft)
                plan.append((task.name, hours))
                left[task] -= hours
                hoursLeft -= hours
        schedule[day] = plan
        day += timedelta(days=1)
    late = [task.name for task in tasks if left[task] > 0]
    return schedule, late

# Want to create hours left so if user study it reduces time needed to do of a task
# Want to create a feature that once task is done it gets moved there
# Create a late feature so if something isn't done it shows up there
def main():
    tasks = [Task("Trial task", date(2026, 10, 20), 5), 
             Task("trial 2", date(2026, 10, 20), 20)]
    completed = []
    checkCompleted(tasks, completed)
    schedule, late = buildSchedule(tasks, 3)
    # printTasks(tasks)
    printSchedule(schedule)
    print(f"Tasks missed: {late}")
    
main()
