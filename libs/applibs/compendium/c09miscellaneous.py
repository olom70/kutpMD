import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Miscellaneous(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {9000 : 1.5
            ,9005 : 2.5
            ,9010 : 1.5 
            ,9013 : 1.5
            ,9015 : 1.5
            ,9020 : 1.8 
            ,9025 : 1.0
            ,9030 : 1.3 
            ,9040 : 1.3
            ,9045 : 1.0
            ,9050 : 1.8 
            ,9055 : 1.5 
            ,9060 : 1.3
            ,9065 : 1.8 
            ,9070 : 1.8 
            ,9071 : 2.5 
            ,9075 : 1.8
            ,9080 : 3.0 
            ,9085 : 2.5 
            ,9090 : 3.3 
            ,9095 : 3.5 
            ,9100 : 1.8
            ,9101 : 3.0
            ,9105 : 2.0 
            ,9106 : 3.5
            ,9110 : 2.5 
            ,9115 : 1.5}

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {9000 : "board game playing, sitting"
            ,9005 : "casino gambling, standing"
            ,9010 : "card playing, sitting"
            ,9013 : "chess game, sitting"
            ,9015 : "copying documents, standing"
            ,9020 : "drawing, writing, painting, standing"
            ,9025 : "laughing, sitting"
            ,9030 : "sitting, reading, book, newspaper, etc."
            ,9040 : "sitting, writing, desk work, typing"
            ,9045 : "sitting, playing traditional video game, computer game"
            ,9050 : "standing, talking in person, on the phone, computer, or text messaging, light effort"
            ,9055 : "sitting, talking in person, on the phone, computer, or text messaging, light effort"
            ,9060 : "sitting, studying, general, including reading and/or writing, light effort"
            ,9065 : "sitting, in class, general, including note-taking or class discussion"
            ,9070 : "standing, reading"
            ,9071 : "standing, miscellaneous"
            ,9075 : "sitting, arts and crafts,  carving wood, weaving, spinning wool, light effort"
            ,9080 : "sitting, arts and crafts,  carving wood, weaving, spinning wool, moderate effort"
            ,9085 : "standing, arts and crafts, sand painting, carving, weaving, light effort"
            ,9090 : "standing, arts and crafts, sand painting, carving, weaving, moderate effort"
            ,9095 : "standing, arts and crafts, sand painting, carving, weaving, vigorous effort"
            ,9100 : "retreat/family reunion activities involving sitting, relaxing, talking, eating"
            ,9101 : "retreat/family reunion activities involving playing games with children"
            ,9105 : "touring/traveling/vacation involving riding in a vehicle"
            ,9106 : "touring/traveling/vacation involving walking"
            ,9110 : "camping involving standing, walking, sitting, light-to-moderate effort"
            ,9115 : "sitting at a sporting event, spectator"}

        self.metDescription_fr  = {9000 : "jouer à des jeux de société, en position assise"
            ,9005 : "jouer au casino, debout"
            ,9010 : "jouer aux cartes, en position assise"
            ,9013 : "jouer aux échecs, en position assise"
            ,9015 : "copier des documents, debout"
            ,9020 : "dessiner, écrire, peindre, debout"
            ,9025 : "rire, en position assise"
            ,9030 : "être assis, lire un livre, un journal, etc."
            ,9040 : "être assis, écrire, faire du travail de bureau, taper sur un clavier"
            ,9045 : "être assis, jouer à des jeux vidéo traditionnels, jeux d'ordinateur"
            ,9050 : "être debout, parler en face à face, au téléphone, à l’ordinateur ou envoyer des messages textuels, effort léger"
            ,9055 : "être assis, parler en face à face, au téléphone, à l’ordinateur ou envoyer des messages textuels, effort léger"
            ,9060 : "être assis, étudier, général, y compris lire et/ou écrire, effort léger"
            ,9065 : "être assis, en classe, général, y compris prendre des notes ou discuter en classe"
            ,9070 : "être debout, lire"
            ,9071 : "être debout, divers"
            ,9075 : "être assis, arts et artisanat, sculpture sur bois, tissage, filage de la laine, effort léger"
            ,9080 : "être assis, arts et artisanat, sculpture sur bois, tissage, filage de la laine, effort modéré"
            ,9085 : "être debout, arts et artisanat, peinture sur sable, sculpture, tissage, effort léger"
            ,9090 : "être debout, arts et artisanat, peinture sur sable, sculpture, tissage, effort modéré"
            ,9095 : "être debout, arts et artisanat, peinture sur sable, sculpture, tissage, effort vigoureux"
            ,9100 : "activités de repos/réunions de famille impliquant de s'asseoir, de se détendre, de parler et de manger"
            ,9101 : "activités de repos/réunions de famille impliquant de jouer avec des enfants"
            ,9105 : "tourisme/voyage/vacances impliquant de conduire un véhicule"
            ,9106 : "tourisme/voyage/vacances impliquant de marcher"
            ,9110 : "faire du camping impliquant d'être debout, de marcher, d'être assis, effort léger à modéré"
            ,9115 : "être assis lors d'un événement sportif, spectateur"}

    def printValues(self):
        print("Beginning dump for 'Miscellaneous' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Miscellaneous()
    b.printValues()
    print(b.getMetValue(9070))
    for l in b:
        print(l)