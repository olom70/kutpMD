import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class ConditionningExercises(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()
        
        self.metValue  = {2001 : 2.3
        ,2003 : 3.8
        ,2005 : 7.2
        ,2008 : 5.0
        ,2010 : 7.0
        ,2011 : 3.5
        ,2012 : 6.8
        ,2013 : 8.8
        ,2014 : 11.0
        ,2015 : 14.0
        ,2017 : 4.8
        ,2019 : 8.5
        ,2020 : 8.0
        ,2022 : 3.8
        ,2024 : 2.8
        ,2030 : 3.5
        ,2035 : 4.3
        ,2040 : 8.0
        ,2045 : 3.5
        ,2048 : 5.0
        ,2050 : 6.0
        ,2052 : 5.0
        ,2054 : 3.5
        ,2060 : 5.5
        ,2061 : 5.0
        ,2062 : 7.8
        ,2064 : 3.8
        ,2065 : 9.0
        ,2068 : 11.0
        ,2070 : 6.0
        ,2071 : 4.8
        ,2072 : 7.0
        ,2073 : 8.5
        ,2074 : 12.0
        ,2080 : 6.8
        ,2085 : 11.0
        ,2090 : 6.0
        ,2150 : 2.5
        ,2101 : 2.3
        ,2105 : 3.0
        ,2110 : 6.8
        ,2112 : 2.8
        ,2115 : 2.8
        ,2117 : 4.3
        ,2120 : 5.3
        ,2135 : 1.3
        ,2140 : 2.3
        ,2143 : 4.0
        ,2146 : 6.0
        ,2160 : 4.0
        ,2170 : 2.0
        ,2180 : 3.3
        ,2200 : 5.3
        ,2205 : 6.8}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {2001 : "activity promoting video game (e.g., Wii Fit), light effort (e.g., balance, yoga)"
        ,2003 : "activity promoting video game (e.g., Wii Fit), moderate effort (e.g., aerobic, resistance)"
        ,2005 : "activity promoting video/arcade game (e.g., Exergaming, Dance Dance Revolution), vigorous effort"
        ,2008 : "army type obstacle course exercise, boot camp training program "
        ,2010 : "bicycling, stationary, general"
        ,2011 : "bicycling, stationary, 30-50 watts, very light to light effort"
        ,2012 : "bicycling, stationary, 90-100 watts, moderate to vigorous effort"
        ,2013 : "bicycling, stationary, 101-160 watts, vigorous effort"
        ,2014 : "bicycling, stationary, 161-200 watts, vigorous effort"
        ,2015 : "bicycling, stationary, 201-270 watts, very vigorous effort"
        ,2017 : "bicycling, stationary, 51-89 watts, light-to-moderate effort"
        ,2019 : "bicycling, stationary, RPM/Spin bike class"
        ,2020 : "calisthenics (e.g., push ups, sit ups, pull-ups, jumping jacks), vigorous effort"
        ,2022 : "calisthenics (e.g., push ups, sit ups, pull-ups, lunges), moderate effort"
        ,2024 : "calisthenics (e.g., situps, abdominal crunches), light effort"
        ,2030 : "calisthenics, light or moderate effort, general (example: back exercises), going up & down from floor (Taylor Code 150)"
        ,2035 : "circuit training, moderate effort"
        ,2040 : "circuit training, including kettlebells, some aerobic movement with minimal rest, general, vigorous intensity"
        ,2045 : "CurvesTM exercise routines in women "
        ,2048 : "Elliptical trainer, moderate effort "
        ,2050 : "resistance training (weight lifting - free weight, nautilus or universal-type), power lifting or body building, vigorous effort (Taylor Code 210)"
        ,2052 : "resistance (weight) training, squats , slow or explosive effort"
        ,2054 : "resistance (weight) training, multiple exercises, 8-15 repetitions at varied resistance "
        ,2060 : "health club exercise, general (Taylor Code 160)"
        ,2061 : "health club exercise classes, general, gym/weight training combined in one visit"
        ,2062 : "health club exercise, conditioning classes"
        ,2064 : "home exercise, general "
        ,2065 : "stair-treadmill ergometer, general"
        ,2068 : "rope skipping, general"
        ,2070 : "rowing, stationary ergometer, general, vigorous effort"
        ,2071 : "rowing, stationary, general, moderate effort"
        ,2072 : "rowing, stationary, 100 watts, moderate effort"
        ,2073 : "rowing, stationary, 150 watts, vigorous effort"
        ,2074 : "rowing, stationary, 200 watts, very vigorous effort"
        ,2080 : "ski machine, general"
        ,2085 : "slide board exercise, general"
        ,2090 : "slimnastics, jazzercise"
        ,2101 : "stretching, mild"
        ,2105 : "pilates, general"
        ,2110 : "teaching exercise class (e.g., aerobic, water)"
        ,2112 : "therapeutic exercise ball, Fitball exercise"
        ,2115 : "upper body exercise, arm ergometer"
        ,2117 : "upper body exercise, stationary bicycle - Airdyne (arms only) 40 rpm, moderate"
        ,2120 : "water aerobics, water calisthenics, water exercise"
        ,2135 : "whirlpool, sitting"
        ,2140 : "video exercise workouts, TV conditioning programs (e.g., yoga, stretching), light effort"
        ,2143 : "video exercise workouts, TV conditioning programs (e.g., cardio-resistance), moderate effort"
        ,2146 : "video exercise workouts, TV conditioning programs (e.g., cardio-resistance), vigorous effort"
        ,2150 : "yoga, Hatha"
        ,2160 : "yoga, Power"
        ,2170 : "yoga, Nadisodhana"
        ,2180 : "yoga, Surya Namaskar"
        ,2200 : "native New Zealander physical activities (e.g., Haka Powhiri, Moteatea, Waita Tira, Whakawatea, etc.) , general, moderate effort"
        ,2205 : "native New Zealander physical activities (e.g., Haka, Taiahab), general, vigorous effort"}

        self.metDescription_fr  = {2001 : "jeu vidéo réclamant une activité (par ex. Wii Fit), effort léger (par ex. position d’équilibre, yoga)"
        ,2003 : "jeu vidéo réclamant une activité (par ex. Wii Fit), effort modéré (par ex. aérobic, résistance)"
        ,2005 : "jeu vidéo/d’arcade réclamant une activité (par ex. Exergaming, Dance Dance Revolution), effort vigoureux"
        ,2008 : "parcours d’obstacle de type militaire, programme de formation de camp d’entraînement"
        ,2010 : "cyclisme, vélo d'appartement, général"
        ,2011 : "cyclisme, vélo d'appartement, 30-50 watts, effort très léger à léger"
        ,2012 : "cyclisme, vélo d'appartement, 90-100 watts, effort modéré à vigoureux"
        ,2013 : "cyclisme, vélo d'appartement, 101-160 watts, effort vigoureux"
        ,2014 : "cyclisme, vélo d'appartement, 161-200 watts, effort vigoureux"
        ,2015 : "cyclisme, vélo d'appartement, 201-270 watts, effort très vigoureux"
        ,2017 : "cyclisme, vélo d'appartement, 51-89 watts, effort léger à modéré"
        ,2019 : "cyclisme, vélo d’appartement, cardiovélo RPM"
        ,2020 : "gymnastique suédoise (par ex. pompes, abdominaux, tractions, sauts en écart), effort vigoureux"
        ,2022 : "gymnastique suédoise (par ex. pompes, redressements assis, fentes), effort modéré"
        ,2024 : "gymnastique suédoise (par ex. redressements assis, abdominaux), effort léger"
        ,2030 : "gymnastique suédoise, effort léger à modéré, général (par ex. exercices pour le dos), monter et descendre les escaliers (code Taylor 150)"
        ,2035 : "entraînement en circuit, effort modéré"
        ,2040 : "entraînement en circuit, avec des haltères, comprenant des mouvements d'aérobic avec un temps de repos minimal, général, effort vigoureux"
        ,2045 : "exercices Curves TM chez les femmes"
        ,2048 : "machine elliptique, effort modéré"
        ,2050 : "entraînement en résistance (haltérophilie, poids libre, nautilus ou universel), force athlétique ou body-building, effort vigoureux (code Taylor 210)"
        ,2052 : "entraînement en résistance (à une masse), squats, effort lent ou explosif"
        ,2054 : "entraînement en résistance (à une masse), exercices multiples, 8-15 répétitions à des résistances variées"
        ,2060 : "exercice de club de remise en forme, général (code Taylor 160)"
        ,2061 : "exercice de club de remise en forme, général, gym/musculation en une même séance"
        ,2062 : "exercice de club de remise en forme, cours de conditionnement"
        ,2064 : "exercice à la maison, général"
        ,2065 : "tapis de course, général"
        ,2068 : "corde à sauter, général"
        ,2070 : "rame, rameur d'appartement, général, effort vigoureux"
        ,2071 : "rame, rameur d’appartement, général, effort modéré"
        ,2072 : "rame, rameur d’appartement, 100 watts, effort modéré"
        ,2073 : "rame, rameur d'appartement, 150 watts, effort vigoureux"
        ,2074 : "rame, rameur d'appartement, 200 watts, effort très vigoureux"
        ,2080 : "machine d'entraînement au ski, général"
        ,2085 : "tapis pour glissements latéraux, général"
        ,2090 : "slimnastics, jazzercise"
        ,2101 : "stretching doux"
        ,2105 : "Pilates, général"
        ,2110 : "cours d’exercices (par ex. aérobic, aquagym)"
        ,2112 : "ballon d’exercice thérapeutique, exercice au Fitball"
        ,2115 : "exercices du haut du corps, ergomètre à bras"
        ,2117 : "exercices du haut du corps, vélo d’appartement – Airdyne (bras uniquement) 40 tr/min, effort modéré"
        ,2120 : "aérobic aquatique, gymnastique suédoise aquatique, exercices dans l’eau"
        ,2135 : "bain à remous, position assise"
        ,2140 : "exercices de gymnastique en vidéo, programmes TV de remise en forme (par ex. yoga, stretching), effort léger"
        ,2143 : "exercices de gymnastique en vidéo, programmes TV de remise en forme (par ex. entraînement cardio-pulmonaire), effort modéré"
        ,2146 : "exercices de gymnastique en vidéo, programmes TV de remise en forme (par ex. entraînement cardio-pulmonaire), effort vigoureux"
        ,2150 : "yoga, Hatha"
        ,2160 : "yoga, Power"
        ,2170 : "yoga, Nadisodhana"
        ,2180 : "yoga, Surya Namaskar"
        ,2200 : "activités physiques néozélandaises (par ex. Haka Powhiri, Moteatea, Waita Tira, Whakawatea, etc.), général, effort modéré"
        ,2205 : "activités physiques néozélandaises (par ex. Haka, Taiahab), général, effort vigoureux"}        

    def printValues(self):
        print("Beginning dump for 'Conditionning exercices' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = ConditionningExercises()
    b.printValues()
    print(b.getMetValue(2205))
    for l in b:
        print(l)