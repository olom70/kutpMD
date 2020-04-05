import abc

class Compendium(abc.ABC):
    '''
        ** abstract class **
        provides the mean to print and get the values of a domain (bicycling, Dancing, Home Activity, etc.)
    '''
    def __init__(self):
        self.metDescription_fr = {}
        self.metDescription = {}
        self.metValue = {}
        self.index = 0
        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())
        self.name = 'none defined'
    
    def printValues(self):
        for key, value in self.metValue.items():
            print({key},":",{value})

        for key, value in self.metDescription.items():
            print({key},":",{value})

        for key, value in self.metDescription_fr.items():
            print({key},":",{value})

    def getMetValue(self, code):
        try:
            return self.metValue[code]
        except (KeyError):
            raise ValueError("The met code :  "+str(code)+" is unknown.")

    def __iter__(self):
        return self

    def __next__(self):
        '''
            Returns in a list the value the english description and the french description
        '''
        if self.index == len(self.metValue):
            self.index = 0
            raise StopIteration
        currentKey = self.ckeys[self.index]
        listToReturn = currentKey, self.metValue[currentKey], self.metDescription[currentKey], self.metDescription_fr[currentKey]
        self.index += 1
        return listToReturn
