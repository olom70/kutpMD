import os
import sys
import uuid
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import libs.applibs.profilem.enumandconst as enumandconst
from  libs.applibs.profilem.iterregistry import IterRegistry

class Profile(object):
    '''
        This class holds :
        - all the characteristics of a person (age, weigth, etc.)
        - and the infered metrics (BMI, RMR, etc.)
        - the activity factor ( do I lay all day long or do I have multiple physical activities ?)
    '''
    _counter = 0
    _registry = []
    

    def __init__(self, profileName='a profile'):
        # populate iteration dictionary
        self._registry.append(self)
        #Assigning an id to this instance
        Profile._counter += +1
        self.uid = uuid.uuid1()
        self.id = Profile._counter

        self.isdefault = False
        self.profileName = profileName
        self.maleSign = '♂'
        self.femaleSign = '♀'
        # facts
        self.fileName = None #String
        self.profileGoal = None #string
        self.metricChoice = None #from the tuple MetricChoice
        self.defaultProfile = False
        self.weight = None # float 
        self.weightIntegerPart = None
        self.weightDecimalPart = None
        self.heightIntegerPart = None
        self.heightDecimalPart = None
        self.age = None
        self.chest = None
        self.abdomen = None
        self.thigh = None
        self.triceps = None
        self.suprailium = None
        self.gender = None # from the tuple Gender
        self.activityFactor = None # from the tuple Activity Factor
        # infered
        self.bBMI = None # classic way to calculate it
        self.nBMI = None # new way to calculate it
        self.rRMRcal = {}
        self.rRMRml = {}
        self.hHBE = {}
        self.quadraticBodyDensity = None
        self.exponentialBodyDensity = None
        self.quadraticFatPercentage = None
        self.exponentialFatPercentage = None

    def addToRegistry(self):
        '''
            populate the registry when a profile is loaded from the shelf
        '''
        self._registry.append(self)

    def getAllGenders(self):
        '''
            Return all the occurences of the Enum Gender in a dictionary
            content of the dictionary : {1 : '♂', 2: '♀' }
        '''
        dictOfGenders = {}
        for genderList in enumandconst.Gender:
            name = self.displayGender(from_getAllGenders=genderList)
            dictOfGenders.update({str(genderList.value): name})
        return dictOfGenders

    def displayGender(self, **kwargs):
        '''
            Display the current gender of the profile
        '''
        if ('from_getAllGenders' in kwargs):
            g = kwargs['from_getAllGenders']
        else:
            g = self.gender
        
        if (g == enumandconst.Gender.FEMALE):
            return self.femaleSign
        elif (g == enumandconst.Gender.MALE):
            return self.maleSign
        else:
            return '?'

    def getAllActivityFactors(self):
        '''
            Return all the occurences of the Enum ActivityFactor in a dictionary
            content of the dictionary : {1: '>', 2: '>>, etc.
        '''
        dictOfActivityFactors = {}
        for ActivityFactorList in enumandconst.ActivityFactor:
            name = self.displayActivityFactor(from_getAllActivityFactors=ActivityFactorList)
            dictOfActivityFactors.update({str(ActivityFactorList.value): name})
        return dictOfActivityFactors

    def displayActivityFactor(self, **kwargs ):
        '''
            display the current activity factor on a scale going from > to >>>>>>
        '''
        if ('from_getAllActivityFactors' in kwargs):
            af = kwargs['from_getAllActivityFactors']
        else:
            af = self.activityFactor

        if (af == enumandconst.ActivityFactor.SEDENTARY):
            return '>'
        elif (af == enumandconst.ActivityFactor.LIGHTLYACTIVE):
            return '>>'
        elif (af == enumandconst.ActivityFactor.MODERATELYACTIVE):
            return '>>>'
        elif (af == enumandconst.ActivityFactor.ACTIVE):
            return '>>>>'
        elif (af == enumandconst.ActivityFactor.VIGOROUS):
            return '>>>>>'
        elif (af == enumandconst.ActivityFactor.VIGOROUSLYACTIVE):
            return '>>>>>>'
        else:
            return '?'


    def computeWeigth(self):
        '''
            Add the decimal part of the weight to the integer part to obtain one number
        '''
        if (self.weightDecimalPart is not None
                and self.weightIntegerPart is not None):
            self.weight = self.weightIntegerPart + (self.weightDecimalPart / 100)
        else:
            raise ValueError("weight has to be initialized first")
    
    def __computeBMIISO(self):
        '''
            Compute the BMI from ISO metrics
            This is a private function called by "ComputeBMI"
            There are 2 formulas to compute the BMI :
                see the main function "Compute BMI"
        '''
        self.bBMI = 10000 * (self.weight / math.pow((self.heightIntegerPart*100+self.heightDecimalPart),2))  
        self.nBMI = 100000 * (self.weight*1.3 / math.pow((self.heightIntegerPart*100+self.heightDecimalPart),2.5))

    def __computeBMIImperial(self):
        '''
            Compute the BMI from imperial metrics
             ** DO NOT USE DIRECTLY **
            ** use computeBMI instead **

        '''
        self.bBMI = 10000*(self.weight / math.pow((self.heightIntegerPart*12+self.heightDecimalPart),2))*703
        self.nBMI = 5734*self.weight / math.pow(self.heightIntegerPart*12+self.heightDecimalPart,2.5)


    def displaynBMI(self):
        '''
            Trunc the new BMI to the nearest integer
            return 0 if there is not enough values to calculate it
        '''
        if self.nBMI is not None:
            truncatednBMI = math.trunc(self.nBMI)
            return str(truncatednBMI)
        else:
            return '0'

    
    def displaybBMI(self):
        '''
            Trunc the classic BMI to the nearest integer
            return 0 if there is not enough values to calculate it
        '''
        if self.bBMI is not None:
            truncatedbBMI = math.trunc(self.bBMI)
            return str(truncatedbBMI)
        else:
            return '0'


    def computeBMI(self):
        '''
            Compute BMI from weight and height of a person
            
            classic way
                http://www.bmi-calculator.net/bmi-formula.php
                Imperial : BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
                ISO : BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
            new way
                https://www.medicalnewstoday.com/articles/255712.php
                ISO: BMI = 1.3 x weight (kg) / height (m)2.5
                or
                imperial : BMI = 5734*weight(lb)/height(in)2.5
        '''
        try:
            self.computeWeigth()
        except:
            raise
        
        if (self.weight is not None
                and self.heightIntegerPart is not None
                and self.heightDecimalPart is not None
                and self.metricChoice is not None
                and self.metricChoice in enumandconst.MetricChoice):
            if (self.metricChoice == enumandconst.MetricChoice.ISO):
                self.__computeBMIISO()
            if (self.metricChoice == enumandconst.MetricChoice.IMPERIAL):
                self.__computeBMIImperial()
        else:
            raise ValueError("Profile has to be fully initialized with weight, height and metric choice (iso, imperial)")


        return self.bBMI, self.nBMI

    def __computeRMRml(self, rmrcal):
        '''
            To convert kilocalories per day obtained from the Harris Benedict equation2 to ml.kg-1.min-1
            the following formula is used.
            kcal.day-1/1440 = kcal.min-1; kcal.min-1/5 = L.min-1; L.min-1/(weight kg)x1000 = ml.kg-1.min-1
             ** DO NOT USE DIRECTLY **
            ** use computeRMR instead **

        '''
        rmrml = (rmrcal / 1440 / 5 / self.weight)*1000
        return rmrml


    def __computeISORMRFemale(self):
        '''
            compute RMR for a female using ISO metrics
            populate the dictionary "RMRcal" and the float "RMRml"
            ** DO NOT USE DIRECTLY **
            ** use computeRMR instead **
        '''
        self.rRMRcal.clear
        self.rRMRml.clear
        # formula from 1918
        rmrtemp = 655.0955 + (9.5634*self.weight) + (1.8496*(self.heightIntegerPart*100+self.heightDecimalPart)) - (4.6756*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1918 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1918 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1918))})
        # formula from 1984
        rmrtemp = 447.593 + (9.247*self.weight) + (3.098*(self.heightIntegerPart*100+self.heightDecimalPart)) - (4.330*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1984 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1984 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1984))})
        # formula from 1990
        rmrtemp = -161 + (10*self.weight) + (6.25*(self.heightIntegerPart*100+self.heightDecimalPart)) - (5*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1990 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1990 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1990))})


    def __computeISORMRMale(self):
        '''
            compute RMR for a male using ISO metrics
            populate the dictionary "RMRcal" and the float "RMRml"
            ** DO NOT USE DIRECTLY **
            ** use computeRMR instead **
        '''
        self.rRMRcal.clear
        self.rRMRml.clear
        # formula from 1918
        rmrtemp = 66.4730 + (13.7516*self.weight) + (5.0033*(self.heightIntegerPart*100+self.heightDecimalPart)) - (6.7550*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1918 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1918 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1918))})
        # formula from 1984
        rmrtemp = 88.362 + (13.397*self.weight) + (4.799*(self.heightIntegerPart*100+self.heightDecimalPart)) - (5.677*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1984 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1984 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1984))})
        # formula from 1990
        rmrtemp = 5 + (10*self.weight) + (6.25*(self.heightIntegerPart*100+self.heightDecimalPart)) - (5*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1990 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1990 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1990))})

    def __computeImperialRMRFemale(self):
        '''
            compute RMR for a female using Imperial metrics
            populate the dictionary "RMRcal" and the float "RMRml"
            ** DO NOT USE DIRECTLY **
            ** use computeRMR instead **
        '''
        self.rRMRcal.clear
        self.rRMRml.clear
        # formula from 1918
        rmrtemp = 655.0955 + (9.5634*(self.weight*0.453592)) + (1.8496*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) -(4.6756*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1918 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1918 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1918))})
        # formula from 1984
        rmrtemp = 447.593 + (9.247*(self.weight*0.453592)) + (3.098*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) - (4.330*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1984 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1984 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1984))})
        # formula from 1990
        rmrtemp = -161 + (10*(self.weight*0.453592)) + (6.25*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) - (5*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1990 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1990 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1990))})

    def __computeImperialRMRMale(self):
        '''
            compute RMR for a male using Imperial metrics
            populate the dictionary "RMRcal" and the float "RMRml"
            ** DO NOT USE DIRECTLY **
            ** use computeRMR instead **
        '''
        self.rRMRcal.clear
        self.rRMRml.clear
        # formula from 1918
        rmrtemp = 66.4730 + (13.7516*(self.weight*0.453592)) + (5.033*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) - (6.7550*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1918 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1918 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1918))})
        # formula from 1984
        rmrtemp = 88.362 + (13.397*(self.weight*0.453592)) + (4.799*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) - (5.677*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1984 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1984 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1984))})
        # formula from 1990
        rmrtemp = 5 + (10*(self.weight*0.453592)) + (6.25*((self.heightIntegerPart*12+self.heightDecimalPart)*0.0508)) - (5*self.age)
        self.rRMRcal.update({enumandconst.RmrDates.A1990 : rmrtemp})
        self.rRMRml.update({enumandconst.RmrDates.A1990 : self.__computeRMRml(self.rRMRcal.get(enumandconst.RmrDates.A1990))})

    def displayRMR(self):
        '''
            Trunc the RMR (kilocalories per day) to the nearest integer
            return the 3 values in a list in this order :
              - 1918 formula
              - 1984 formula
              - 1990 formula
            return 0 if there is not enough values to calculate it
        '''
        if (len(self.rRMRcal) != 0):
            rmr1918 = str(math.trunc(self.rRMRcal.get(enumandconst.RmrDates.A1918)))
            rmr1984 = str(math.trunc(self.rRMRcal.get(enumandconst.RmrDates.A1984)))
            rmr1990 = str(math.trunc(self.rRMRcal.get(enumandconst.RmrDates.A1990)))
            return rmr1918, rmr1984, rmr1990
        else:
            return '0', '0', '0'

    def displayRMRml(self):
        '''
            Round the RMR (ml.kg-1.min-1) to 2 digit
            return the 3 values in a list in this order :
              - 1918 formula
              - 1984 formula
              - 1990 formula
            return 0 if there is not enough values to calculate it
        '''
        if (len(self.rRMRml) != 0):
            rmr1918 = str(round(self.rRMRml.get(enumandconst.RmrDates.A1918), 2))
            rmr1984 = str(round(self.rRMRml.get(enumandconst.RmrDates.A1984), 2))
            rmr1990 = str(round(self.rRMRml.get(enumandconst.RmrDates.A1990), 2))
            return rmr1918, rmr1984, rmr1990
        else:
            return '0', '0', '0'

    def computeRMR(self):
        '''
            compute the RMR.
        '''
        try:
            self.computeWeigth()
        except:
            raise
        
        if (self.weight is not None
                and self.heightDecimalPart is not None
                and self.heightIntegerPart is not None
                and self.age is not None
                and self.metricChoice in enumandconst.MetricChoice
                and self.gender in enumandconst.Gender):
            
            if self.metricChoice == enumandconst.MetricChoice.ISO:
                if self.gender == enumandconst.Gender.FEMALE:
                    self.__computeISORMRFemale()
                elif self.gender == enumandconst.Gender.MALE:
                    self.__computeISORMRMale()
                else: 
                    raise ValueError("unexpected Gender. A new Gender must have been added and is yet to handle")
            elif self.metricChoice == enumandconst.MetricChoice.IMPERIAL:
                if self.gender == enumandconst.Gender.FEMALE:
                    self.__computeImperialRMRFemale
                elif self.gender == enumandconst.Gender.MALE:
                    self.__computeImperialRMRMale
                else:
                    raise ValueError("unexpected Gender. A new Gender must have been added and is yet to handle")
            else:
                raise ValueError("unexpected Metric Choice. A new Metric Choice must have been added and is yet to handle")
        else:
            raise ValueError("Profile has to be fully initialized with height, age, metric choice, gender")


    def displayHBE(self):
        '''
            Trunc the HBE to the nearest integer
            return the 3 values in a list in this order :
              - 1918 formula
              - 1984 formula
              - 1990 formula
            return 0 if there is not enough values to calculate it
        '''
        if (len(self.hHBE) != 0):
            hbe1918 = str(math.trunc(self.hHBE.get(enumandconst.RmrDates.A1918)))
            hbe1984 = str(math.trunc(self.hHBE.get(enumandconst.RmrDates.A1984)))
            hbe1990 = str(math.trunc(self.hHBE.get(enumandconst.RmrDates.A1990)))
            return hbe1918, hbe1984, hbe1990
        else:
            return '0', '0', '0'


    def computeHBE(self):
        '''
            compute the HBE that depends of the level of activity for a typical week
        '''
        if (len(self.rRMRcal) != 0
            and self.activityFactor in enumandconst.ActivityFactor):
            
            self.hHBE.clear
            if self.activityFactor == enumandconst.ActivityFactor.SEDENTARY:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 1.4})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 1.4})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 1.4})
            elif self.activityFactor == enumandconst.ActivityFactor.LIGHTLYACTIVE:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 1.6})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 1.6})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 1.6})
            elif self.activityFactor == enumandconst.ActivityFactor.MODERATELYACTIVE:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 1.7})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 1.7})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 1.7})
            elif self.activityFactor == enumandconst.ActivityFactor.ACTIVE:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 1.9})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 1.9})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 1.9})
            elif self.activityFactor == enumandconst.ActivityFactor.VIGOROUS:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 2.0})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 2.0})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 2.0})
            elif self.activityFactor == enumandconst.ActivityFactor.VIGOROUSLYACTIVE:
                self.hHBE.update({enumandconst.RmrDates.A1918 : self.rRMRcal.get(enumandconst.RmrDates.A1918) * 2.4})
                self.hHBE.update({enumandconst.RmrDates.A1984 : self.rRMRcal.get(enumandconst.RmrDates.A1984) * 2.4})
                self.hHBE.update({enumandconst.RmrDates.A1990 : self.rRMRcal.get(enumandconst.RmrDates.A1990) * 2.4})
            else:
                raise ValueError("Unexpected activity factor. A new value have been added and is yet to handle")
        else:
            raise ValueError("The computation of HBR needs these values initialised : Activity Factor and RMR")

    def displayFAT(self):
        '''
            Trunc the fat percentage to the nearest integer
            return in a list the results il a list in this order :
            - quadratic formula
            - exponential formula
            return 0 if there is not enough values to calculate it
        '''
        if (self.quadraticFatPercentage is not None
                and self.exponentialFatPercentage is not None):
            truncatedQFP = math.trunc(self.quadraticFatPercentage)
            truncatedEFP = math.trunc(self.exponentialFatPercentage)
            return str(truncatedQFP), str(truncatedEFP)
        else:
            return '0', '0'

    def __computeFatPercentage(self):
        '''
            compute Fat Percentage from quadratic & exponential fat formula
            *** DO NOT CALL DIRECTLY *** use computeFat
        '''
        self.quadraticFatPercentage = ((4.95/self.quadraticBodyDensity)-4.5)*100
        self.exponentialFatPercentage = ((4.95/self.exponentialBodyDensity)-4.5)*100
    
    def computeFAT(self):
        '''
            compute fat percentage of body
            using 2 formulas :
              - exponential formula :	BD = exp(a − b ⋅ Sk − c ⋅ age)
              - quadratic formula :	BD = a − b ⋅ S + c ⋅ S² − d ⋅ age
            see more details in the comment of the function
        '''

        # Quadratic formula :	BD = a − b ⋅ S + c ⋅ S² − d ⋅ age
        #     man
        #     BD :	Body density
        #     a :	1.10938
        #     b :	0.0008267
        #     S :	"sum of skinfolds in mm for chest, abdomen and thigh"
        #     c :	0.0000016
        #     d :	0.0002574
        #     age :	year
        #     woman
        #     BD :	Body density
        #     a :	1.0994921
        #     b :	0.0009929
        #     S :	"sum of skinfolds in mm
        #     for triceps, thigh, and suprailium"
        #     c :	0.0000023
        #     d :	0.0001392
        #     age :	year
        # exponential formula :	BD = exp(a − b ⋅ Sk − c ⋅ age)
        #   man
        #   BD :	body density
        #   a :	0.109648
        #   b :	0.0021745
        #   k :	0.747
        #   c :	0.0002516
        #   S :	"sum of skinfolds in mm for chest, abdomen and thigh"
        #   woman
        #   BD :	body density
        #   a :	0.120936
        #   b :	0.0084087
        #   k :	0.532
        #   c :	0.0001178
        #   S :	"sum of skinfolds in mm for triceps, thigh, and suprailium"
        #   To find out the approximate body fat percentage, the body density score must be plugged into another formula. The Siri equation, which was designed to estimate body fat percent from body density, is:
        # [(4.95/body density) - 4.5] x 100 = percent body fat
        if (self.gender in enumandconst.Gender):
            if (self.gender == enumandconst.Gender.FEMALE):
                if (self.triceps is not None
                    and self.suprailium is not None
                    and self.thigh is not None
                    and self.age is not None):
                    self.quadraticBodyDensity =  \
                        (1.0994921 - 0.0009929
                        * (self.triceps+self.suprailium+self.thigh)
                        + 0.0000023
                        * math.pow((self.triceps+self.suprailium+self.thigh),2)
                        -0.0001392*self.age)
                    self.exponentialBodyDensity = \
                         math.exp(0.120936-0.0084087
                         *math.pow((self.triceps+self.suprailium+self.thigh),0.532)
                         -0.0001178*self.age)
                    self.__computeFatPercentage()
                else:
                    raise ValueError("computeFAT : triceps, suprailium, thigh or age is yet to initialise ")
            elif (self.gender == enumandconst.Gender.MALE):
                if (self.triceps is not None
                    and self.abdomen is not None
                    and self.age is not None
                    and self.thigh is not None):
                    self.quadraticBodyDensity =  \
                        (1.10938 - 0.0008267
                        * (self.triceps+self.abdomen+self.thigh)
                        + 0.0000016
                        * math.pow((self.triceps+self.abdomen+self.thigh),2)
                        - 0.0002574*self.age)
                    self.exponentialBodyDensity = \
                        math.exp(0.109648-0.0021745
                        * math.pow((self.triceps+self.abdomen+self.thigh),0.747)
                        - 0.0002516*self.age)
                    self.__computeFatPercentage()
                else:
                    raise ValueError("computeFAT, triceps, abdomen, age, thigh is yet to initialise ")
            else:
                raise ValueError("computeFat : a Gender value has been added and is yet to handle")
        else:
            raise ValueError("computeFAT : Initialise Gender first")
    
    def computeAll(self):
        '''
            compute all the values from the metrics entered.
        '''
        try:
            self.computeBMI()
        except ValueError:
            pass
        try:
            self.computeRMR()
        except ValueError:
            pass
        try:
            self.computeHBE()
        except ValueError:
            pass
        try:
            self.computeFAT()
        except ValueError:
            pass
    

if __name__ == "__main__":
    myProfile = Profile('clode')
    myProfile.age = 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weightIntegerPart = 60
    myProfile.weightDecimalPart = 0
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    myProfile.computeBMI()
    print(myProfile.nBMI)
    print(myProfile.bBMI)
    print(myProfile.displaybBMI())
    myProfile.computeRMR()
    print(myProfile.rRMRcal)
    print(myProfile.rRMRml)
    myProfile.activityFactor = enumandconst.ActivityFactor.SEDENTARY
    myProfile.computeHBE()
    print(myProfile.hHBE)
    myProfile.triceps = 25
    myProfile.thigh = 80
    myProfile.suprailium = 2
    myProfile.computeFAT()
    print(myProfile.quadraticBodyDensity)
    print(myProfile.exponentialBodyDensity)
    print(myProfile.quadraticFatPercentage)
    print(myProfile.id)
    print(myProfile.getAllActivityFactors())
    print(myProfile.getAllActivityFactors()['1'])
    print(myProfile.displayActivityFactor())
    print(myProfile.displayActivityFactor(from_getAllActivityFactors=enumandconst.ActivityFactor.VIGOROUSLYACTIVE))
    print(myProfile.getAllGenders())
    print(myProfile.displayGender(from_getAllGenders=enumandconst.Gender.MALE))
    print(myProfile.displayRMR())

