import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Bicycling(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {1003 : 14.0
         ,1004 : 16.0
         ,1008 : 8.5
         ,1009 : 8.5
         ,1010 : 4.0
         ,1011 : 6.8
         ,1013 : 5.8
         ,1015 : 7.5
         ,1018 : 3.5
         ,1019 : 5.8
         ,1020 : 6.8
         ,1030 : 8.0
         ,1040 : 10.0
         ,1050 : 12.0
         ,1060 : 15.8
         ,1065 : 8.5
         ,1066 : 9.0
         ,1070 : 5.0 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {1003 : "bicycling, mountain, uphill, vigorous"
        ,1004 : "bicycling, mountain, competitive, racing"
        ,1008 : "bicycling, BMX"
        ,1009 : "bicycling, mountain, general"
        ,1010 : "bicycling, <10 mph, leisure, to work or for pleasure (Taylor Code 115)"
        ,1011 : "bicycling, to/from work, self selected pace"
        ,1013 : "bicycling, on dirt or farm road, moderate pace"
        ,1015 : "bicycling, general"
        ,1018 : "bicycling, leisure, 5.5 mph"
        ,1019 : "bicycling, leisure, 9.4 mph"
        ,1020 : "bicycling, 10-11.9 mph, leisure, slow, light effort"
        ,1030 : "bicycling, 12-13.9 mph, leisure, moderate effort"
        ,1040 : "bicycling, 14-15.9 mph, racing or leisure, fast, vigorous effort"
        ,1050 : "bicycling, 16-19 mph, racing/not drafting or > 19 mph drafting, very fast, racing general"
        ,1060 : "bicycling, > 20 mph, racing, not drafting"
        ,1065 : "bicycling, 12 mph, seated, hands on brake hoods or bar drops, 80 rpm"
        ,1066 : "bicycling, 12 mph, standing, hands on brake hoods, 60 rpm"
        ,1070 : "unicycling"}

        self.metDescription_fr  = {1003 : "cyclisme, en montagne, en montée, effort vigoureux"
        ,1004 : "cyclisme, en montagne, en compétition, en course"
        ,1008 : "cyclisme, BMX"
        ,1009 : "cyclisme, en montagne, général"
        ,1010 : "cyclisme, <16 km/h, loisirs, pour aller au travail ou pour le plaisir (code Taylor 115)"
        ,1011 : "cyclisme, pour aller/revenir du travail, à son rythme"
        ,1013 : "cyclisme, sur terre ou route de campagne, rythme modéré"
        ,1015 : "cyclisme, général"
        ,1018 : "cyclisme, loisir, 9 km/h"
        ,1019 : "cyclisme, loisir, 15 km/h"
        ,1020 : "cyclisme, 16-19,2 km/h, loisirs, rythme lent, effort léger"
        ,1030 : "cyclisme, 19,3-22,4 km/h, loisirs, effort modéré"
        ,1040 : "cyclisme, 22,5-25,6 km/h, course ou loisirs, rythme rapide, effort vigoureux"
        ,1050 : "cyclisme, 25,7-30,6 km/h, course/sans aspiration ou > 30,6 km/h avec aspiration, rythme très rapide, course générale"
        ,1060 : "cyclisme, > 32 km/h, course, sans aspiration"
        ,1065 : "cyclisme, 19,3 km/h, assis, mains sur les cocottes de frein ou en bas du guidon, 80 tr/min"
        ,1066 : "cyclisme, 19,3 km/h, en danseuse, mains sur les cocottes de frein, 60 tr/min"
        ,1070 : "monocyclisme"}

    def printValues(self):
        print("Beginning dump for 'Bicycling' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)


if __name__ == "__main__":
    b = Bicycling()
    b.printValues()
    print(b.getMetValue(1004))
    for l in b:
        print(l)