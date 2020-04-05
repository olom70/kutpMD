import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class WinterActivities(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {19005 : 7.5
            ,19006 : 2.5
            ,19010 : 6.0 
            ,19011 : 2.0 
            ,19018 : 14.0
            ,19020 : 5.5 
            ,19030 : 7.0 
            ,19040 : 9.0 
            ,19050 : 13.3
            ,19060 : 7.0 
            ,19075 : 7.0 
            ,19080 : 6.8
            ,19090 : 9.0
            ,19100 : 12.5
            ,19110 : 15.0
            ,19130 : 15.5
            ,19135 : 13.3
            ,19140 : 13.5
            ,19150 : 4.3
            ,19160 : 5.3
            ,19170 : 8.0
            ,19175 : 12.5
            ,19180 : 7.0 
            ,19190 : 5.3
            ,19192 : 10.0
            ,19200 : 3.5 
            ,19202 : 2.0
            ,19252 : 5.3
            ,19254 : 7.5
            ,19260 : 2.5 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {19005 : "dog sledding, mushing"
            ,19006 : "dog sledding, passenger"
            ,19010 : "moving ice house, set up/drill holes"
            ,19011 : "ice fishing, sitting"
            ,19018 : "skating, ice dancing"
            ,19020 : "skating, ice, 9 mph or less"
            ,19030 : "skating, ice, general (Taylor Code 360)"
            ,19040 : "skating, ice, rapidly, more than 9 mph, not competitive"
            ,19050 : "skating, speed, competitive"
            ,19060 : "ski jumping, climb up carrying skis"
            ,19075 : "skiing, general"
            ,19080 : "skiing, cross country, 2.5 mph, slow or light effort, ski walking"
            ,19090 : "skiing, cross country, 4.0-4.9 mph, moderate speed and effort, general"
            ,19100 : "skiing, cross country, 5.0-7.9 mph, brisk speed, vigorous effort"
            ,19110 : "skiing, cross country, >8.0 mph, elite skier, racing"
            ,19130 : "skiing, cross country, hard snow, uphill, maximum, snow mountaineering"
            ,19135 : "skiing, cross-country, skating"
            ,19140 : "skiing, cross-country, biathlon, skating technique"
            ,19150 : "skiing, downhill, alpine or snowboarding, light effort, active time only"
            ,19160 : "skiing, downhill, alpine or snowboarding, moderate effort, general, active time only"
            ,19170 : "skiing, downhill, vigorous effort, racing"
            ,19175 : "skiing, roller, elite racers"
            ,19180 : "sledding, tobogganing, bobsledding, luge (Taylor Code 370)"
            ,19190 : "snow shoeing, moderate effort"
            ,19192 : "snow shoeing, vigorous effort"
            ,19200 : "snowmobiling, driving, moderate"
            ,19202 : "snowmobiling, passenger"
            ,19252 : "snow shoveling, by hand, moderate effort"
            ,19254 : "snow shoveling, by hand, vigorous effort"
            ,19260 : "snow blower, walking and pushing"}


        self.metDescription_fr  = {19005 : "randonnée en traîneau à chiens en tant que musher"
            ,19006 : "randonnée en traîneau à chiens en tant que passager"
            ,19010 : "retrait de la glace, maison, créer/forer des trous"
            ,19011 : "pêche sur glace, position assise"
            ,19018 : "patinage, dance sur glace"
            ,19020 : "patinage sur glace à 14,5 km/h ou moins"
            ,19030 : "patinage sur glace, général (code Taylor 360)"
            ,19040 : "patinage sur glace, rythme rapide, plus de 14,5 km/h, hors compétition"
            ,19050 : "patinage de vitesse, compétition"
            ,19060 : "saut à ski, monter en portant des skis"
            ,19075 : "ski, général"
            ,19080 : "ski de fond à 4 km/h, rythme lent ou effort léger, marche nordique"
            ,19090 : "ski de fond à 6,5-8 km/h, rythme et effort modérés, général"
            ,19100 : "ski de fond à 8-12,5 km/h, rythme rapide, effort vigoureux"
            ,19110 : "ski de fond à plus de 13 km/h, skieur d’élite, course"
            ,19130 : "ski de fond, neige dure, montée, maximum, alpinisme"
            ,19135 : "ski de fond, patinage"
            ,19140 : "ski de fond, biathlon, pas de patineur"
            ,19150 : "ski, descente, ski alpin ou snowboard, effort léger, périodes d’activité uniquement"
            ,19160 : "ski, descente, ski alpin ou snowboard, effort modéré, général, périodes d’activité uniquement"
            ,19170 : "ski, descente, effort vigoureux, course"
            ,19175 : "ski, ski à roulettes, coureurs d’élite"
            ,19180 : "traîneau, toboggan, bobsleigh, luge (code Taylor 370)"
            ,19190 : "raquettes à neige, effort modéré"
            ,19192 : "raquettes à neige, effort vigoureux"
            ,19200 : "moto des neiges, conduire, effort modéré"
            ,19202 : "moto des neiges, passager"
            ,19252 : "déblayer la neige à la pelle, à la main, effort modéré"
            ,19254 : "déblayer la neige à la pelle, à la main, effort vigoureux"
            ,19260 : "passer la souffleuses à neige, marcher et pousser"}

    def printValues(self):
        print("Beginning dump for 'WinterActivities' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = WinterActivities()
    b.printValues()
    print(b.getMetValue(19018))
    for l in b:
        print(l)