import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Sports(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {15000 : 5.5
            ,15010 : 4.3
            ,15020 : 7.0 
            ,15030 : 5.5 
            ,15040 : 8.0 
            ,15050 : 6.0 
            ,15055 : 6.5
            ,15060 : 7.0 
            ,15070 : 4.5 
            ,15072 : 9.3
            ,15075 : 7.8
            ,15080 : 2.5 
            ,15090 : 3.0 
            ,15092 : 3.8
            ,15100 : 12.8 
            ,15110 : 5.5
            ,15120 : 7.8
            ,15130 : 7.0 
            ,15135 : 5.8
            ,15138 : 6.0
            ,15140 : 4.0 
            ,15142 : 8.0
            ,15150 : 4.8
            ,15160 : 3.3
            ,15170 : 4.0 
            ,15180 : 2.5 
            ,15190 : 6.0 
            ,15192 : 8.5
            ,15200 : 6.0 
            ,15210 : 8.0 
            ,15230 : 8.0 
            ,15232 : 4.0
            ,15235 : 2.5 
            ,15240 : 3.0 
            ,15250 : 8.0 
            ,15255 : 4.8 
            ,15265 : 4.3 
            ,15270 : 3.0 
            ,15285 : 5.3
            ,15290 : 3.5 
            ,15300 : 3.8
            ,15310 : 4.0 
            ,15320 : 12.0 
            ,15330 : 8.0 
            ,15335 : 4.0
            ,15340 : 3.5 
            ,15350 : 7.8 
            ,15360 : 8.0 
            ,15362 : 10.0
            ,15370 : 5.5 
            ,15375 : 4.3
            ,15380 : 4.5 
            ,15390 : 5.8
            ,15395 : 7.3
            ,15400 : 3.8
            ,15402 : 9.0
            ,15408 : 1.8
            ,15410 : 3.0 
            ,15420 : 12.0 
            ,15425 : 5.3
            ,15430 : 10.3
            ,15440 : 4.0 
            ,15450 : 7.0 
            ,15460 : 8.0 
            ,15465 : 3.3
            ,15470 : 4.0 
            ,15480 : 9.0 
            ,15490 : 10.0 
            ,15500 : 6.0 
            ,15510 : 8.0 
            ,15520 : 10.0 
            ,15530 : 7.0 
            ,15533 : 8.0
            ,15535 : 7.5
            ,15537 : 5.8
            ,15540 : 5.0 
            ,15542 : 4.0
            ,15544 : 5.5
            ,15546 : 7.0
            ,15550 : 12.3 
            ,15551 : 11.8
            ,15552 : 8.8 
            ,15560 : 8.3 
            ,15562 : 6.3
            ,15570 : 3.0 
            ,15580 : 5.0 
            ,15582 : 6.0
            ,15590 : 7.0 
            ,15591 : 7.5 
            ,15592 : 9.8
            ,15593 : 12.3
            ,15594 : 14.0
            ,15600 : 3.5 
            ,15605 : 10.0 
            ,15610 : 7.0 
            ,15620 : 5.0 
            ,15625 : 4.0
            ,15630 : 4.0 
            ,15640 : 6.0 
            ,15645 : 3.3
            ,15650 : 12.0 
            ,15652 : 7.3
            ,15660 : 4.0 
            ,15670 : 3.0 
            ,15672 : 1.5
            ,15675 : 7.3
            ,15680 : 6.0 
            ,15685 : 4.5
            ,15690 : 8.0 
            ,15695 : 5.0
            ,15700 : 3.5 
            ,15702 : 4.5
            ,15710 : 4.0 
            ,15711 : 6.0 
            ,15720 : 3.0 
            ,15725 : 8.0 
            ,15730 : 6.0 
            ,15731 : 7.0 
            ,15732 : 4.0 
            ,15733 : 6.0 
            ,15734 : 10.0 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {15000 : "Alaska Native Games, Eskimo Olympics, general"
            ,15010 : "archery, non-hunting"
            ,15020 : "badminton, competitive (Taylor Code 450)"
            ,15030 : "badminton, social singles and doubles, general"
            ,15040 : "basketball, game (Taylor Code 490)"
            ,15050 : "basketball, non-game, general (Taylor Code 480)"
            ,15055 : "basketball, general"
            ,15060 : "basketball, officiating (Taylor Code 500)"
            ,15070 : "basketball, shooting baskets"
            ,15072 : "basketball, drills, practice"
            ,15075 : "basketball, wheelchair"
            ,15080 : "billiards"
            ,15090 : "bowling (Taylor Code 390)"
            ,15092 : "bowling, indoor, bowling alley"
            ,15100 : "boxing, in ring, general"
            ,15110 : "boxing, punching bag"
            ,15120 : "boxing, sparring"
            ,15130 : "broomball"
            ,15135 : "children’s games, adults playing (e.g., hopscotch, 4-square, dodge ball, playground apparatus, t-ball, tetherball, marbles, jacks, arcade games), moderate effort"
            ,15138 : "cheerleading, gymnastic moves, competitive"
            ,15140 : "coaching, football, soccer, basketball, baseball, swimming, etc."
            ,15142 : "coaching, actively playing sport with players"
            ,15150 : "cricket, batting, bowling, fielding"
            ,15160 : "croquet"
            ,15170 : "curling"
            ,15180 : "darts, wall or lawn"
            ,15190 : "drag racing, pushing or driving a car"
            ,15192 : "auto racing, open wheel"
            ,15200 : "fencing"
            ,15210 : "football, competitive"
            ,15230 : "football, touch, flag, general (Taylor Code 510)"
            ,15232 : "football, touch, flag, light effort"
            ,15235 : "football or baseball, playing catch"
            ,15240 : "frisbee playing, general"
            ,15250 : "frisbee, ultimate"
            ,15255 : "golf, general"
            ,15265 : "golf, walking, carrying clubs"
            ,15270 : "golf, miniature, driving range"
            ,15285 : "golf, walking, pulling clubs"
            ,15290 : "golf, using power cart (Taylor Code 070)"
            ,15300 : "gymnastics, general"
            ,15310 : "hacky sack"
            ,15320 : "handball, general (Taylor Code 520)"
            ,15330 : "handball, team"
            ,15335 : "high ropes course, multiple elements"
            ,15340 : "hang gliding"
            ,15350 : "hockey, field"
            ,15360 : "hockey, ice, general"
            ,15362 : "hockey, ice, competitive"
            ,15370 : "horseback riding, general"
            ,15375 : "horse chores, feeding, watering, cleaning stalls, implied walking and lifting loads"
            ,15380 : "saddling, cleaning, grooming, harnessing and unharnessing horse"
            ,15390 : "horseback riding, trotting"
            ,15395 : "horseback riding, canter or gallop"
            ,15400 : "horseback riding,walking"
            ,15402 : "horseback riding, jumping"
            ,15408 : "horse cart, driving, standing or sitting"
            ,15410 : "horseshoe pitching, quoits"
            ,15420 : "jai alai"
            ,15425 : "martial arts, different types, slower pace, novice performers, practice"
            ,15430 : "martial arts, different types, moderate pace (e.g., judo, jujitsu, karate, kick boxing, tae kwan do, tai-bo, Muay Thai boxing)"
            ,15440 : "juggling"
            ,15450 : "kickball"
            ,15460 : "lacrosse"
            ,15465 : "lawn bowling, bocce ball, outdoor"
            ,15470 : "moto-cross, off-road motor sports, all-terrain vehicle, general"
            ,15480 : "orienteering"
            ,15490 : "paddleball, competitive"
            ,15500 : "paddleball, casual, general (Taylor Code 460)"
            ,15510 : "polo, on horseback"
            ,15520 : "racquetball, competitive"
            ,15530 : "racquetball, general (Taylor Code 470)"
            ,15533 : "rock or mountain climbing (Taylor Code 470)"
            ,15535 : "rock climbing, ascending rock, high difficulty"
            ,15537 : "rock climbing, ascending or traversing rock, low-to-moderate difficulty"
            ,15540 : "rock climbing, rappelling"
            ,15542 : "rodeo sports, general, light effort"
            ,15544 : "rodeo sports, general, moderate effort"
            ,15546 : "rodeo sports, general, vigorous effort"
            ,15550 : "rope jumping, fast pace, 120-160 skips/min"
            ,15551 : "rope jumping, moderate pace, 100-120 skips/min, general,  2 foot skip, plain bounce"
            ,15552 : "rope jumping, slow pace, < 100 skips/min, 2 foot skip, rhythm bounce"
            ,15560 : "rugby, union, team, competitive"
            ,15562 : "rugby, touch, non-competitive"
            ,15570 : "shuffleboard"
            ,15580 : "skateboarding, general, moderate effort"
            ,15582 : "skateboarding, competitive, vigorous effort"
            ,15590 : "skating, roller (Taylor Code 360)"
            ,15591 : "rollerblading, in-line skating, 14.4 km/h (9.0 mph), recreational pace"
            ,15592 : "rollerblading, in-line skating, 17.7 km/h (11.0 mph), moderate pace, exercise training"
            ,15593 : "rollerblading, in-line skating, 21.0 to 21.7 km/h (13.0 to 13.6 mph), fast pace, exercise training"
            ,15594 : "rollerblading, in-line skating, 24.0 km/h (15.0 mph), maximal effort"
            ,15600 : "skydiving, base jumping, bungee jumping"
            ,15605 : "soccer, competitive"
            ,15610 : "soccer, casual, general (Taylor Code 540)"
            ,15620 : "softball or baseball, fast or slow pitch, general (Taylor Code 440)"
            ,15625 : "softball, practice"
            ,15630 : "softball, officiating"
            ,15640 : "softball,pitching"
            ,15645 : "sports spectator, very excited, emotional, physically moving "
            ,15650 : "squash (Taylor Code 530)"
            ,15652 : "squash, general"
            ,15660 : "table tennis, ping pong (Taylor Code 410)"
            ,15670 : "tai chi, qi gong, general"
            ,15672 : "tai chi, qi gong, sitting, light effort"
            ,15675 : "tennis, general"
            ,15680 : "tennis, doubles (Taylor Code 430)"
            ,15685 : "tennis, doubles"
            ,15690 : "tennis, singles (Taylor Code 420)"
            ,15695 : "tennis, hitting balls, non-game play, moderate effort"
            ,15700 : "trampoline, recreational"
            ,15702 : "trampoline, competitive"
            ,15710 : "volleyball (Taylor Code 400)"
            ,15711 : "volleyball, competitive, in gymnasium"
            ,15720 : "volleyball, non-competitive, 6 - 9 member team, general"
            ,15725 : "volleyball, beach, in sand"
            ,15730 : "wrestling (one match = 5 minutes)"
            ,15731 : "wallyball, general"
            ,15732 : "track and field (e.g., shot, discus, hammer throw)"
            ,15733 : "track and field (e.g., high jump, long jump, triple jump, javelin, pole vault)"
            ,15734 : "track and field (e.g., steeplechase, hurdles)"}

        self.metDescription_fr  = {15000 : "jeux traditionnels d’Alaska, épreuves olympiques esquimaudes, général"
            ,15010 : "tir à l'arc, hors chasse"
            ,15020 : "badminton, compétition (code Taylor 450)"
            ,15030 : "badminton, double ou simple, général"
            ,15040 : "basket-ball, match (code Taylor 490)"
            ,15050 : "basket-ball, hors match, général (code Taylor 480)"
            ,15055 : "basket-ball, général"
            ,15060 : "basket-ball, arbitrage (code Taylor 500)"
            ,15070 : "basket-ball, tir au panier"
            ,15072 : "basket-ball, exercices, entraînement"
            ,15075 : "basket-ball, fauteuil roulant"
            ,15080 : "billard"
            ,15090 : "bowling (code Taylor 390)"
            ,15092 : "bowling, en intérieur, piste de bowling"
            ,15100 : "boxe, sur ring, général"
            ,15110 : "boxe, sac de frappe"
            ,15120 : "boxe, entraînement (sparring-partner)"
            ,15130 : "ballon-balai"
            ,15135 : "jeux d’enfants, jeux d’adultes (par ex. marelle, 4-square, ballon prisonnier, équipement de cours de récréation, t-ball, spirobole, billes, jeux d'arcade), effort modéré"
            ,15138 : "majorette, mouvements de gymnastique, compétition"
            ,15140 : "entraîner, football, football américain, basketball, baseball, natation, etc."
            ,15142 : "entraîner, jouer activement à un sport avec des joueurs"
            ,15150 : "cricket, frappe, service, défense"
            ,15160 : "croquet"
            ,15170 : "curling"
            ,15180 : "fléchettes, mur ou gazon"
            ,15190 : "course de dragster, pousser ou conduire une voiture"
            ,15192 : "course de voiture, monoplace"
            ,15200 : "escrime"
            ,15210 : "football américain, compétition"
            ,15230 : "football américain, touch, flag, général (code Taylor 510)"
            ,15232 : "football américain, touch, flag, effort léger"
            ,15235 : "football américain ou baseball, jeu de balle"
            ,15240 : "frisbee, général"
            ,15250 : "frisbee, ultimate"
            ,15255 : "golf, général"
            ,15265 : "golf, marcher, porter des clubs"
            ,15270 : "golf, minigolf, practice"
            ,15285 : "golf, marcher, tirer des clubs"
            ,15290 : "golf, avec un chariot électrique (code Taylor 070)"
            ,15300 : "gymnastique, général"
            ,15310 : "footbag"
            ,15320 : "handball, général (code Taylor 520)"
            ,15330 : "handball, équipe"
            ,15335 : "accrobranches, éléments multiples"
            ,15340 : "deltaplane"
            ,15350 : "hockey, sur gazon"
            ,15360 : "hockey sur glace, général"
            ,15362 : "hockey sur glace, compétition"
            ,15370 : "équitation, général"
            ,15375 : "toilettage de cheval, donner à manger, à boire, nettoyer les étables avec marche et port de charges"
            ,15380 : "seller, nettoyer, toiletter, poser et retirer le harnais d’un cheval"
            ,15390 : "équitation, trot"
            ,15395 : "équitation, petit ou grand galop"
            ,15400 : "équitation, pas"
            ,15402 : "équitation, saut d’obstacles"
            ,15408 : "charrette à cheval, conduire, être debout ou assis"
            ,15410 : "lancer de fer à cheval, quoits"
            ,15420 : "pelote basque"
            ,15425 : "arts martiaux, différents types, rythme lent, débutants, entraînement"
            ,15430 : "arts martiaux, différents types, rythme modéré (par ex. judo, ju-jitsu, karaté, kick-boxing, taekwondo, tai-bo, boxe thaïe)"
            ,15440 : "jonglage"
            ,15450 : "kickball"
            ,15460 : "crosse"
            ,15465 : "boulingrin, pétanque, activité extérieure"
            ,15470 : "moto-cross, sports automobiles sur circuit, véhicule tous terrains, général"
            ,15480 : "course d'orientation"
            ,15490 : "jokari, compétition"
            ,15500 : "jokari, loisirs, général (code Taylor 460)"
            ,15510 : "polo"
            ,15520 : "racquetball, compétition"
            ,15530 : "racquetball, général (code Taylor 470)"
            ,15533 : "escalade, varappe (code Taylor 470) (ancien code = 17120)"
            ,15535 : "escalade, varappe, grande difficulté"
            ,15537 : "escalade, varappe, difficulté faible à modérée"
            ,15540 : "escalade, descente en rappel"
            ,15542 : "rodéo, général, effort léger"
            ,15544 : "rodéo, général, effort modéré"
            ,15546 : "rodéo, général, effort vigoureux"
            ,15550 : "corde à sauter, rythme rapide, 120-160 sauts/min"
            ,15551 : "corde à sauter, rythme modéré, 100-120 sauts/min, général, saut de 60 cm, saut simple"
            ,15552 : "corde à sauter, rythme lent, < 100 sauts/min, saut de 60 cm, saut rythmé"
            ,15560 : "rugby à quinze, équipe, compétition"
            ,15562 : "rugby, touch, hors compétition"
            ,15570 : "jeu de palets"
            ,15580 : "skate, général, effort modéré"
            ,15582 : "skate, compétition, effort vigoureux"
            ,15590 : "patin à roulettes (code Taylor 360)"
            ,15591 : "roller, patin en ligne, 14,4 km/h, rythme loisir"
            ,15592 : "roller, patin en ligne, 17,7 km/h, rythme modéré, exercice d’entraînement"
            ,15593 : "roller, patin en ligne, 21 à 21,7 km/h, rythme rapide, exercice d’entraînement"
            ,15594 : "roller, patin en ligne, 24,0 km/h, effort maximal"
            ,15600 : "saut en parachute, saut d’un point fixe, saut à l’élastique"
            ,15605 : "football, compétition"
            ,15610 : "football, loisirs, général (code Taylor 540)"
            ,15620 : "softball ou baseball, lancer rapide ou lent, général (code Taylor 440)"
            ,15625 : "softball, entraînement"
            ,15630 : "softball, arbitrage"
            ,15640 : "softball, lancer"
            ,15645 : "spectateur de sport, très excité, passionné, mouvements physiques"
            ,15650 : "squash (code Taylor 530)"
            ,15652 : "squash, général"
            ,15660 : "tennis de table, ping-pong (code Taylor 410)"
            ,15670 : "tai chi, qi gong, général"
            ,15672 : "tai chi, qi gong, position assise, effort léger"
            ,15675 : "tennis, général"
            ,15680 : "tennis, double, (code Taylor 430)"
            ,15685 : "tennis, double"
            ,15690 : "tennis, simple, (code Taylor 420)"
            ,15695 : "tennis, frapper la balle, jeu récréatif, effort modéré"
            ,15700 : "trampoline, récréatif"
            ,15702 : "trampoline, compétition"
            ,15710 : "volley-ball (code Taylor 400)"
            ,15711 : "volley-ball, compétition, gymnase"
            ,15720 : "volley-ball, hors compétition, équipe de 6-9 joueurs, général"
            ,15725 : "beach-volley, dans le sable"
            ,15730 : "lutte (un match = 5 minutes)"
            ,15731 : "wallyball, général"
            ,15732 : "athlétisme (par ex. lancer de poids, lancer de disque, lancer de marteau)"
            ,15733 : "athlétisme (par ex. saut en hauteur, saut en longueur, triple saut, lancer de javelot, saut à la perche)"
            ,15734 : "athlétisme (par ex. steeple, course de haies)"}

    def printValues(self):
        print("Beginning dump for 'Sports' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Sports()
    b.printValues()
    print(b.getMetValue(15610))
    for l in b:
        print(l)