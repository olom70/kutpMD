import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class WaterActivities(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {18010 : 2.5 
            ,18012 : 1.3
            ,18020 : 4.0 
            ,18025 : 3.3 
            ,18030 : 7.0 
            ,18040 : 2.8
            ,18050 : 5.8
            ,18060 : 12.5
            ,18070 : 3.5 
            ,18080 : 12.0 
            ,18090 : 3.0 
            ,18100 : 5.0 
            ,18110 : 4.0 
            ,18120 : 3.0 
            ,18130 : 4.5
            ,18140 : 3.3
            ,18150 : 6.0 
            ,18160 : 7.0 
            ,18180 : 15.8 
            ,18190 : 11.8
            ,18200 : 7.0 
            ,18210 : 5.0 
            ,18220 : 3.0 
            ,18222 : 5.0
            ,18225 : 6.0
            ,18230 : 9.8
            ,18240 : 5.8 
            ,18250 : 9.5
            ,18255 : 4.8
            ,18260 : 10.3 
            ,18265 : 5.3
            ,18270 : 13.8
            ,18280 : 10.0 
            ,18290 : 8.3 
            ,18300 : 6.0 
            ,18310 : 6.0 
            ,18320 : 7.0
            ,18330 : 8.0 
            ,18340 : 9.8
            ,18350 : 3.5
            ,18352 : 2.3
            ,18355 : 5.5
            ,18360 : 10.0 
            ,18365 : 3.0 
            ,18366 : 9.8
            ,18367 : 2.5
            ,18368 : 4.5
            ,18369 : 6.8
            ,18370 : 5.0 
            ,18380 : 5.0
            ,18385 : 11.0
            ,18390 : 13.5}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {18010 : "boating, power, driving"
            ,18012 : "boating, power, passenger, light"
            ,18020 : "canoeing, on camping trip (Taylor Code 270)"
            ,18025 : "canoeing, harvesting wild rice, knocking rice off the stalks"
            ,18030 : "canoeing, portaging"
            ,18040 : "canoeing, rowing, 2.0-3.9 mph, light effort"
            ,18050 : "canoeing, rowing, 4.0-5.9 mph, moderate effort"
            ,18060 : "canoeing, rowing, kayaking, competition, >6 mph, vigorous effort"
            ,18070 : "canoeing, rowing, for pleasure, general (Taylor Code 250)"
            ,18080 : "canoeing, rowing, in competition, or crew or sculling (Taylor Code 260)"
            ,18090 : "diving, springboard or platform"
            ,18100 : "kayaking, moderate effort"
            ,18110 : "paddle boat"
            ,18120 : "sailing, boat and board sailing, windsurfing, ice sailing, general (Taylor Code 235)"
            ,18130 : "sailing, in competition"
            ,18140 : "sailing, Sunfish/Laser/Hobby Cat, Keel boats, ocean sailing, yachting, leisure"
            ,18150 : "skiing, water or wakeboarding (Taylor Code 220)"
            ,18160 : "jet skiing, driving, in water"
            ,18180 : "skindiving, fast"
            ,18190 : "skindiving, moderate"
            ,18200 : "skindiving, scuba diving, general (Taylor Code 310)"
            ,18210 : "snorkeling (Taylor Code 310)"
            ,18220 : "surfing, body or board, general"
            ,18222 : "surfing, body or board, competitive"
            ,18225 : "paddle boarding, standing"
            ,18230 : "swimming laps, freestyle, fast, vigorous effort"
            ,18240 : "swimming laps, freestyle, front crawl, slow, light or moderate effort"
            ,18250 : "swimming, backstroke, general, training or competition"
            ,18255 : "swimming, backstroke, recreational"
            ,18260 : "swimming, breaststroke, general, training or competition"
            ,18265 : "swimming, breaststroke, recreational"
            ,18270 : "swimming, butterfly, general"
            ,18280 : "swimming, crawl, fast speed, ~75 yards/minute, vigorous effort"
            ,18290 : "swimming, crawl, medium speed, ~50 yards/minute, vigorous effort"
            ,18300 : "swimming, lake, ocean, river (Taylor Codes 280, 295)"
            ,18310 : "swimming, leisurely, not lap swimming, general"
            ,18320 : "swimming, sidestroke, general"
            ,18330 : "swimming, synchronized"
            ,18340 : "swimming, treading water, fast, vigorous effort"
            ,18350 : "swimming, treading water, moderate effort, general"
            ,18352 : "tubing, floating on a river, general"
            ,18355 : "water aerobics, water calisthenics"
            ,18360 : "water polo"
            ,18365 : "water volleyball"
            ,18366 : "water jogging"
            ,18367 : "water walking, light effort, slow pace"
            ,18368 : "water walking, moderate effort, moderate pace"
            ,18369 : "water walking, vigorous effort, brisk pace"
            ,18370 : "whitewater rafting, kayaking, or canoeing"
            ,18380 : "windsurfing, not pumping for speed"
            ,18385 : "windsurfing or kitesurfing, crossing trial"
            ,18390 : "windsurfing, competition, pumping for speed"}


        self.metDescription_fr  = {18010 : "navigation, au moteur, barrer"
            ,18012 : "navigation, au moteur, passager, effort léger"
            ,18020 : "canoë, pendant une randonnée avec camping (code Taylor 270)"
            ,18025 : "canoë, récolte de riz sauvage en faisant tomber le riz des tiges"
            ,18030 : "canoë, portage"
            ,18040 : "canoë, pagayer à 3,2-4,8 km/h, effort léger"
            ,18050 : "canoë, pagayer à 6,4-8 km/h, effort modéré"
            ,18060 : "canoë, pagayer, kayak, compétition, > 9,65 km/h, effort vigoureux"
            ,18070 : "canoë, pagayer pour le plaisir, général (code Taylor 250)"
            ,18080 : "canoë, pagayer, compétition, en équipe ou en couple (code Taylor 260)"
            ,18090 : "plongeon, tremplin ou plateforme"
            ,18100 : "kayak, effort modéré"
            ,18110 : "bateau à aubes"
            ,18120 : "voile, voilier et planche à voile, windsurf, voile sur glace, général (code Taylor 235)"
            ,18130 : "voile, compétition"
            ,18140 : "voile, Sunfish/Laser/Hobby Cat, quillards, navigation hauturière, croisière, plaisance"
            ,18150 : "ski nautique ou wakeboard (code Taylor 220)"
            ,18160 : "scooter des mers, conduire, dans l'eau"
            ,18180 : "plongée sous-marine, rythme rapide"
            ,18190 : "plongée sous-marine, rythme modéré"
            ,18200 : "plongée sous-marine, général (code Taylor 310)"
            ,18210 : "plongée libre (code Taylor 310)"
            ,18220 : "surf, corps ou planche, général"
            ,18222 : "surf, corps ou planche, compétition"
            ,18225 : "planche à rame, en position debout"
            ,18230 : "longueurs de piscine, nage libre, rythme rapide, effort vigoureux"
            ,18240 : "longueurs de piscine, nage libre, crawl, rythme lent, effort modéré ou léger"
            ,18250 : "natation, nage sur le dos, général, entraînement ou compétition"
            ,18255 : "natation, nage sur le dos, loisirs"
            ,18260 : "natation, brasse, général, entraînement ou compétition"
            ,18265 : "natation, brasse, loisirs"
            ,18270 : "natation, papillon, général"
            ,18280 : "natation, crawl, rythme rapide (~70 mètres/minute), effort vigoureux"
            ,18290 : "natation, crawl, rythme rapide (~45 mètres/minute), effort vigoureux"
            ,18300 : "natation, lac, océan, rivière (codes Taylor 280, 295)"
            ,18310 : "natation, loisirs, sans longueurs, général"
            ,18320 : "natation, nage indienne, général"
            ,18330 : "natation, synchronisée"
            ,18340 : "natation, sur-place, rythme rapide, effort vigoureux"
            ,18350 : "natation, sur-place, effort modéré, général"
            ,18352 : "descendre en chambre à air, flotter sur une rivière, général"
            ,18355 : "aérobic aquatique, gymnastique suédoise aquatique"
            ,18360 : "water polo"
            ,18365 : "water volley-ball"
            ,18366 : "water jogging"
            ,18367 : "marcher dans l’eau, effort léger, rythme lent"
            ,18368 : "marcher dans l’eau, effort modéré, rythme modéré"
            ,18369 : "marcher dans l’eau, effort vigoureux, rythme soutenu"
            ,18370 : "rafting, kayak, canoë en eau vive"
            ,18380 : "planche à voile, sans pomper pour gagner en vitesse"
            ,18385 : "planche à voile ou kitesurf, entraînement"
            ,18390 : "planche à voile, compétition, en pompant pour gagner en vitesse"}


    def printValues(self):
        print("Beginning dump for 'WaterActivities' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = WaterActivities()
    b.printValues()
    print(b.getMetValue(18012))
    for l in b:
        print(l)