import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Dancing(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()
        
        self.metValue  = {3010 : 5.0
            ,3012 : 6.8
            ,3014 : 4.8
            ,3015 : 7.3
            ,3016 : 7.5
            ,3017 : 9.5
            ,3018 : 5.5
            ,3019 : 8.5
            ,3020 : 5.0
            ,3021 : 7.3
            ,3022 : 10.0
            ,3025 : 4.5
            ,3030 : 5.5
            ,3031 : 7.8
            ,3038 : 11.3
            ,3040 : 3.0
            ,3050 : 5.5
            ,3060 : 3.5}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {3010 : "ballet, modern, or jazz, general, rehearsal or class"
            ,3012 : "ballet, modern, or jazz, performance, vigorous effort"
            ,3014 : "tap"
            ,3015 : "aerobic, general"
            ,3016 : "aerobic, step, with 6 - 8 inch step"
            ,3017 : "aerobic, step, with 10 - 12 inch step"
            ,3018 : "aerobic, step, with 4-inch step"
            ,3019 : "bench step class, general"
            ,3020 : "aerobic, low impact"
            ,3021 : "aerobic, high impact"
            ,3022 : "aerobic dance wearing 10-15 lb weights"
            ,3025 : "ethnic or cultural dancing (e.g., Greek, Middle Eastern, hula, salsa, merengue, bamba y plena, flamenco, belly, and swing)"
            ,3030 : "ballroom, fast (Taylor Code 125)"
            ,3031 : "general dancing (e.g., disco, folk, Irish step dancing, line dancing, polka, contra, country)"
            ,3038 : "ballroom dancing, competitive, general"
            ,3040 : "ballroom, slow (e.g., waltz, foxtrot, slow dancing, samba, tango, 19th century dance, mambo, cha cha)"
            ,3050 : "Anishinaabe Jingle Dancing"
            ,3060 : "Caribbean dance (Abakua, Beguine, Bellair, Bongo, Brukin's, Caribbean Quadrills, Dinki Mini, Gere, Gumbay, Ibo, Jonkonnu, Kumina, Oreisha, Jambu)"}

        self.metDescription_fr  = {3010 : "ballet, moderne ou jazz, général, répétition ou cours"
            ,3012 : "ballet, moderne ou jazz, représentation, effort vigoureux"
            ,3014 : "claquettes"
            ,3015 : "aérobic, général"
            ,3016 : "aérobic, step, avec un step de 15-20 cm"
            ,3017 : "aérobic, step, avec un step de 25-30 cm"
            ,3018 : "aérobic, step, avec un step de 10 cm"
            ,3019 : "cours de step sur banc, général"
            ,3020 : "aérobic, faible impact"
            ,3021 : "aérobic, fort impact"
            ,3022 : "aérobic danse avec des lests de 4,5-7 kg"
            ,3025 : "danse ethnique ou culturelle (par ex. grecque, moyen-orientale, hula, salsa, merengue, bamba y plena, flamenco, danse du ventre et swing)"
            ,3030 : "danse de salon, rapide (code Taylor 125)"
            ,3031 : "danse générale (par ex. disco, folk, gigue irlandaise à claquettes, danse de groupe, polka, contra, country)"
            ,3038 : "danse de salon, en compétition, général"
            ,3040 : "danse de salon, lente (par ex. valse, fox-trot, slow, samba, tango, danse du XIX ème siècle, mambo, cha-cha)"
            ,3050 : "danse à clochettes Anishinaabe"
            ,3060 : "danse caribéenne (Abakua, Beguine, Bellair, Bongo, Brukin's, quadrille caribéen, Dinki Mini, Gere, Gumbay, Ibo, Jonkonnu, Kumina, Oreisha, Jambu)"}        

    def printValues(self):
        print("Beginning dump for 'Dancing' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Dancing()
    b.printValues()
    print(b.getMetValue(3060))
    for l in b:
        print(l)