import pickle


class HabitTracker:
    
    default_save_path = "habitTracker/HabitTrackerObj.pickle"

    def __init__(self):
        # Initialize habits
        self.habits = []
        self.initializeAllHabits()



    def addHabit(self, habitName, pointValue):

        thisHabitObject = {
            "habitName" : habitName,
            "pointValue" : pointValue,
            "index" : len(self.habits),
            "total" : 0,
            Individual.MOM : 0,
            Individual.DAD : 0,
        }

        self.habits.append(thisHabitObject)

        return thisHabitObject
    
    def initializeAllHabits(self):

        self.addHabit("No added sweetener-processed food day", 3)
        self.addHabit("Meditate-headspace", 2)
        self.addHabit("1 log gratitude and pray", 1)
        self.addHabit("Exercise", 3)
        self.addHabit("Scripture study", 1)
        self.addHabit("Walk dogs", 3)
        self.addHabit("No social media day", 5)
        self.addHabit("Responsible phone-computer use day", 5)
        self.addHabit("Church attendance", 5)
        self.addHabit("Temple attendance", 10)
        self.addHabit("Weekly marriage building talk", 10)
        self.addHabit("Personal improvement activity", 3)
        self.addHabit("Start day on time", 1)
        self.addHabit("Eat meal at table with no electronics-TV", 1)
        self.addHabit("Clean up your daily clutter", 1)
        self.addHabit("Say or do something meaningful to spouse each day", 1)
        self.addHabit("Begin day with hug or kiss", 1)
        self.addHabit("End day with hug or kiss", 1)
        self.addHabit("Go on a date", 10)
        self.addHabit("Each validation", 1) # Assuming 1 point per validation


        # Dynamic Habits
        self.addHabit("Complete approved procrastinated or highly difficult task", -1) 

    def addPoints(self, habitIndex, individual, customValue=None):
        
        thisValue = 0
        if customValue == None:
            thisValue = self.habits[habitIndex]['pointValue']
        else:
            thisValue = int(customValue)

        self.habits[habitIndex][individual] += thisValue
        self.habits[habitIndex]["total"] += thisValue


    def removePoints(self, habitIndex, individual, customValue=None):

        thisValue = 0
        if customValue == None:
            thisValue = self.habits[habitIndex]['pointValue']
        else:
            thisValue = int(customValue)
        
        self.habits[habitIndex][individual] -= thisValue
        self.habits[habitIndex]["total"] -= thisValue

    def getHabitData(self):
        return self.habits

    def getTotalPoints(self):
        # Add together both individual's points
        total = 0
        total += self.getIndividualsTotalPoints(Individual.DAD)
        total += self.getIndividualsTotalPoints(Individual.MOM)

        return total


    def getIndividualsTotalPoints(self, individual):
        total = 0
        for habit in self.habits:
            total += habit[individual]

        return total


    def getHabitTotalPoints(self, habitIndex):
        
        total = self.habits[habitIndex][Individual.MOM] + self.habits[habitIndex][Individual.DAD]
        return total
    

    @staticmethod
    def loadFromFile(path=default_save_path):
        """
        Loads and returns an instance of MyClass from the specified path using pickle.
        """
        with open(path, 'rb') as file:
            return pickle.load(file)

    def save(self, path=default_save_path):
        """
        Saves the current instance of MyClass to the specified path using pickle.
        """
        with open(path, 'wb') as file:
            pickle.dump(self, file)

class Individual:
    MOM = "MOM"
    DAD = "DAD"
