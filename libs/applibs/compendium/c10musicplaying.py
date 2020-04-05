import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class MusicPlaying(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {10010 : 1.8 
            ,10020 : 2.3 
            ,10030 : 2.3 
            ,10035 : 2.5
            ,10040 : 3.8
            ,10045 : 3.0
            ,10050 : 2.0 
            ,10060 : 1.8
            ,10070 : 2.3 
            ,10074 : 2.0
            ,10077 : 2.0
            ,10080 : 3.5 
            ,10090 : 1.8
            ,10100 : 2.5 
            ,10110 : 1.8 
            ,10120 : 2.0 
            ,10125 : 3.0 
            ,10130 : 4.0 
            ,10131 : 5.5
            ,10135 : 3.5 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {10010 : "accordion, sitting"
            ,10020 : "cello, sitting"
            ,10030 : "conducting orchestra, standing"
            ,10035 : "double bass, standing"
            ,10040 : "drums, sitting"
            ,10045 : "drumming (e.g., bongo, conga, benbe), moderate, sitting"
            ,10050 : "flute, sitting"
            ,10060 : "horn, standing"
            ,10070 : "piano, sitting"
            ,10074 : "playing musical instruments, general"
            ,10077 : "organ, sitting"
            ,10080 : "trombone, standing"
            ,10090 : "trumpet, standing"
            ,10100 : "violin, sitting"
            ,10110 : "woodwind, sitting"
            ,10120 : "guitar, classical, folk, sitting"
            ,10125 : "guitar, rock and roll band, standing"
            ,10130 : "marching band, baton twirling, walking, moderate pace, general"
            ,10131 : "marching band, playing an instrument, walking, brisk pace, general"
            ,10135 : "marching band, drum major, walking"}

        self.metDescription_fr  = {10010 : "accordéon, assis"
            ,10020 : "violoncelle, assis"
            ,10030 : "diriger un orchestre, debout"
            ,10035 : "contrebasse, debout"
            ,10040 : "batterie, assis"
            ,10045 : "percussions (par ex. bongo, conga, benbe), effort modéré, assis"
            ,10050 : "flûte, assis"
            ,10060 : "cor, debout"
            ,10070 : "piano, assis"
            ,10074 : "jouer d’un instrument de musique, général"
            ,10077 : "orgue, assis"
            ,10080 : "trombone, debout"
            ,10090 : "trompette, debout"
            ,10100 : "violon, assis"
            ,10110 : "instrument à bois, assis"
            ,10120 : "guitare, classique, folk, assis"
            ,10125 : "guitare, groupe de rock and roll, debout"
            ,10130 : "fanfare, majorette, marcher, rythme modéré, général"
            ,10131 : "fanfare, jouer d'un instrument, marcher, rythme soutenu, général"
            ,10135 : "fanfare, tambour-major, marcher"}

    def printValues(self):
        print("Beginning dump for 'MusicPlaying' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = MusicPlaying()
    b.printValues()
    print(b.getMetValue(10130))
    for l in b:
        print(l)