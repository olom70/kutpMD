import os
import sys
import libs.applibs.compendium.abstractcompendium as abstractcompendium

class Occupation(abstractcompendium.Compendium):

    def __init__(self):
        super().__init__()

        self.metValue  = {11003 : 2.3
            ,11006 : 3.0
            ,11010 : 4.0 
            ,11015 : 2.0 
            ,11020 : 2.3 
            ,11030 : 6.0 
            ,11035 : 2.0 
            ,11038 : 2.5 
            ,11040 : 4.3
            ,11042 : 7.0
            ,11050 : 8.0 
            ,11060 : 8.0 
            ,11070 : 4.0
            ,11080 : 5.3
            ,11090 : 5.0
            ,11100 : 5.5
            ,11110 : 6.3
            ,11115 : 2.5
            ,11120 : 4.0
            ,11125 : 2.3
            ,11126 : 3.8
            ,11128 : 2.0
            ,11130 : 3.3 
            ,11135 : 1.8
            ,11145 : 7.8
            ,11146 : 4.8
            ,11147 : 2.0
            ,11170 : 2.8
            ,11180 : 3.5 
            ,11190 : 4.3
            ,11191 : 4.3 
            ,11192 : 4.5 
            ,11195 : 3.8
            ,11210 : 3.5
            ,11220 : 1.3 
            ,11240 : 8.0
            ,11244 : 6.8
            ,11245 : 8.0
            ,11246 : 9.0
            ,11247 : 3.5
            ,11248 : 5.0
            ,11249 : 7.0
            ,11250 : 17.5 
            ,11260 : 5.0 
            ,11262 : 8.0
            ,11264 : 4.5
            ,11266 : 8.0
            ,11370 : 4.5
            ,11375 : 4.0
            ,11378 : 1.8
            ,11380 : 7.3
            ,11381 : 4.3
            ,11390 : 7.3
            ,11400 : 5.8
            ,11410 : 3.8
            ,11413 : 3.0
            ,11415 : 4.0
            ,11418 : 3.3
            ,11420 : 3.0
            ,11430 : 3.0
            ,11450 : 5.0
            ,11472 : 1.8
            ,11475 : 2.8
            ,11476 : 4.5
            ,11477 : 6.5
            ,11480 : 4.3
            ,11482 : 2.5
            ,11485 : 4.0 
            ,11490 : 7.5 
            ,11495 : 12.0 
            ,11500 : 2.5 
            ,11510 : 4.5 
            ,11514 : 3.3
            ,11516 : 3.0
            ,11520 : 2.0 
            ,11525 : 2.5 
            ,11526 : 2.5 
            ,11527 : 1.3 
            ,11528 : 4.0 
            ,11529 : 2.3
            ,11530 : 2.0 
            ,11540 : 7.8
            ,11550 : 8.8
            ,11560 : 5.0 
            ,11570 : 6.5 
            ,11580 : 1.5 
            ,11585 : 1.5 
            ,11590 : 2.5 
            ,11593 : 2.8
            ,11600 : 3.0
            ,11610 : 3.0 
            ,11615 : 4.5 
            ,11620 : 3.5 
            ,11630 : 4.5
            ,11708 : 5.3 
            ,11710 : 8.3
            ,11720 : 2.3 
            ,11730 : 2.5 
            ,11740 : 1.8 
            ,11750 : 2.5 
            ,11760 : 3.5 
            ,11763 : 2.0
            ,11765 : 4.0 
            ,11766 : 6.5 
            ,11770 : 1.3 
            ,11780 : 6.3 
            ,11790 : 8.0 
            ,11791 : 2.0 
            ,11792 : 3.5 
            ,11793 : 4.3 
            ,11795 : 3.5 
            ,11796 : 3.0 
            ,11797 : 3.8
            ,11800 : 4.5 
            ,11805 : 3.5 
            ,11810 : 4.8 
            ,11820 : 5.0 
            ,11830 : 6.5 
            ,11840 : 7.5 
            ,11850 : 8.5 
            ,11870 : 3.0 }

        # Unpacking with * works with any object that is iterable and, since dictionaries return their keys when iterated through, you can easily create a list by using it within a list literal.
        self.ckeys = [*self.metValue] # another option : list(self.metValue.keys())

        self.metDescription  = {11003 : "active workstation, treadmill desk, walking"
            ,11006 : "airline flight attendant"
            ,11010 : "bakery, general, moderate effort "
            ,11015 : "bakery, light effort "
            ,11020 : "bookbinding "
            ,11030 : "building road, driving heavy machinery "
            ,11035 : "building road, directing traffic, standing "
            ,11038 : "carpentry, general, light effort"
            ,11040 : "carpentry, general, moderate effort"
            ,11042 : "carpentry, general, heavy or vigorous effort"
            ,11050 : "carrying heavy loads (e.g., bricks, tools) "
            ,11060 : "carrying moderate loads up stairs, moving boxes 25-49 lbs "
            ,11070 : "chambermaid, hotel housekeeper, making bed, cleaning bathroom, pushing cart "
            ,11080 : "coal mining, drilling coal, rock "
            ,11090 : "coal mining, erecting supports "
            ,11100 : "coal mining, general "
            ,11110 : "coal mining, shoveling coal "
            ,11115 : "cook, chef"
            ,11120 : "construction, outside, remodeling, new structures (e.g., roof repair, miscellaneous "
            ,11125 : "custodial work, light effort (e.g., cleaning sink and toilet, dusting, vacuuming, light cleaning)"
            ,11126 : "custodial work, moderate effort (e.g., electric buffer, feathering arena floors, mopping, taking out trash, vacuuming)"
            ,11128 : "driving delivery truck, taxi, shuttle bus, school bus"
            ,11130 : "electrical work (e.g., hook up wire, tapping-splicing)"
            ,11135 : "engineer (e.g., mechanical or electrical)"
            ,11145 : "farming, vigorous effort (e.g., baling hay, cleaning barn)"
            ,11146 : "farming, moderate effort (e.g., feeding animals, chasing cattle by walking and/or horseback, spreading manure, harvesting crops)"
            ,11147 : "farming, light effort (e.g., cleaning animal sheds, preparing animal feed)"
            ,11170 : "farming, driving tasks (e.g., driving tractor or harvester) "
            ,11180 : "farming, feeding small animals "
            ,11190 : "farming, feeding cattle, horses "
            ,11191 : "farming, hauling water for animals, general hauling water"
            ,11192 : "farming, taking care of animals (e.g., grooming, brushing, shearing sheep, assisting with birthing, medical care, branding), general"
            ,11195 : "farming, rice, planting, grain milling activities"
            ,11210 : "farming, milking by hand, cleaning pails, moderate effort "
            ,11220 : "farming, milking by machine, light effort "
            ,11240 : "fire fighter, general "
            ,11244 : "fire fighter, rescue victim, automobile accident, using pike pole"
            ,11245 : "fire fighter, raising and climbing ladder with full gear, simulated fire suppression"
            ,11246 : "fire fighter, hauling hoses on ground, carrying/hoisting equipment, breaking down walls, wearing full gear "
            ,11247 : "fishing, commercial, light effort"
            ,11248 : "fishing, commercial, moderate effort"
            ,11249 : "fishing, commercial, vigorous effort"
            ,11250 : "forestry, ax chopping, very fast, 1.25 kg axe, 51 blows/min, extremely vigorous effort "
            ,11260 : "forestry, ax chopping, slow, 1.25 kg axe, 19 blows/min, moderate effort"
            ,11262 : "forestry, ax chopping, fast, 1.25 kg axe, 35 blows/min, vigorous effort"
            ,11264 : "forestry, moderate effort (e.g., sawing wood with power saw, weeding, hoeing)"
            ,11266 : "forestry, vigorous effort (e.g., barking, felling, or trimming trees, carrying or stacking logs, felling trees, planting seeds, sawing lumber by hand )"
            ,11370 : "furriery "
            ,11375 : "garbage collector, walking, dumping bins into truck"
            ,11378 : "hairstylist (e.g., plaiting hair, manicure, make-up artist)"
            ,11380 : "horse grooming, including feeding, cleaning stalls, bathing, brushing, clipping, longeing and exercising horses."
            ,11381 : "horse, feeding, watering, cleaning stalls, implied walking and lifting loads"
            ,11390 : "horse racing, galloping "
            ,11400 : "horse racing, trotting "
            ,11410 : "horse racing, walking "
            ,11413 : "kitchen maid"
            ,11415 : "lawn keeper, yard work, general"
            ,11418 : "laundry worker"
            ,11420 : "locksmith "
            ,11430 : "machine tooling (e.g., machining, working sheet metal, machine fitter, operating lathe, welding) light-to-moderate effort"
            ,11450 : "machine tooling, operating punch press, moderate effort"
            ,11472 : "manager, property"
            ,11475 : "manual or unskilled labor, general, light effort"
            ,11476 : "manual or unskilled labor, general, moderate effort"
            ,11477 : "manual or unskilled labor, general, vigorous effort"
            ,11480 : "masonry, concrete, moderate effort "
            ,11482 : "masonry, concrete, light effort"
            ,11485 : "massage therapist, standing "
            ,11490 : "moving, carrying or pushing heavy objects, 75 lbs or more, only active time (e.g., desks, moving van work) "
            ,11495 : "skindiving or SCUBA diving as a frogman, Navy Seal "
            ,11500 : "operating heavy duty equipment, automated, not driving "
            ,11510 : "orange grove work, picking fruit"
            ,11514 : "painting,house, furniture, moderate effort"
            ,11516 : "plumbing activities"
            ,11520 : "printing, paper industry worker, standing "
            ,11525 : "police, directing traffic, standing "
            ,11526 : "police, driving a squad car, sitting "
            ,11527 : "police, riding in a squad car, sitting "
            ,11528 : "police, making an arrest, standing "
            ,11529 : "postal carrier, walking to deliver mail"
            ,11530 : "shoe repair, general "
            ,11540 : "shoveling, digging ditches "
            ,11550 : "shoveling, more than 16 pounds/minute, deep digging, vigorous effort "
            ,11560 : "shoveling, less than 10 pounds/minute, moderate effort "
            ,11570 : "shoveling, 10 to 15 pounds/minute, vigorous effort "
            ,11580 : "sitting tasks, light effort (e.g., office work, chemistry lab work, computer work, light assembly repair, watch repair, reading, desk work)"
            ,11585 : "sitting meetings, light effort, general, and/or with talking involved (e.g., eating at a business meeting)"
            ,11590 : "sitting tasks, moderate effort (e.g., pushing heavy levers, riding mower/forklift, crane operation)"
            ,11593 : "sitting, teaching stretching or yoga, or light effort exercise class"
            ,11600 : "standing tasks, light effort (e.g., bartending, store clerk, assembling, filing, duplicating, librarian, putting up a Christmas tree, standing and talking at work, changing clothes when teaching physical education,standing)"
            ,11610 : "standing, light/moderate effort (e.g., assemble/repair heavy parts, welding,stocking parts,auto repair,standing, packing boxes, nursing patient care)"
            ,11615 : "standing, moderate effort, lifting items continuously, 10 – 20 lbs, with limited walking or resting"
            ,11620 : "standing, moderate effort, intermittent lifting 50 lbs, hitch/twisting ropes"
            ,11630 : "standing, moderate/heavy tasks (e.g., lifting more than 50 lbs, masonry, painting, paper hanging)"
            ,11708  : "steel mill, moderate effort (e.g., fettling, forging, tipping molds)"
            ,11710 : "steel mill, vigorous effort (e.g., hand rolling, merchant mill rolling, removing slag, tending furnace)"
            ,11720 : "tailoring, cutting fabric"
            ,11730 : "tailoring, general "
            ,11740 : "tailoring, hand sewing "
            ,11750 : "tailoring, machine sewing "
            ,11760 : "tailoring, pressing "
            ,11763 : "tailoring, weaving, light effort (e.g., finishing operations, washing, dyeing, inspecting cloth, counting yards, paperwork)"
            ,11765 : "tailoring, weaving, moderate effort (e.g., spinning and weaving operations, delivering boxes of yam to spinners, loading of warp bean, pinwinding, conewinding, warping, cloth cutting) "
            ,11766 : "truck driving, loading and unloading truck, tying down load, standing, walking and carrying heavy loads"
            ,11770 : "typing, electric, manual or computer "
            ,11780 : "using heavy power tools such as pneumatic tools (e.g., jackhammers, drills) "
            ,11790 : "using heavy tools (not power) such as shovel, pick, tunnel bar, spade"
            ,11791 : "walking on job, less than 2.0 mph, very slow speed, in office or lab area"
            ,11792 : "walking on job, 3.0 mph, in office, moderate speed, not carrying anything "
            ,11793 : "walking on job, 3.5 mph, in office, brisk speed, not carrying anything "
            ,11795 : "walking on job, 2.5 mph, slow speed and carrying light objects less than 25 pounds "
            ,11796 : "walking, gathering things at work, ready to leave "
            ,11797 : "walking, 2.5 mph, slow speed, carrying heavy objects more than 25 lbs"
            ,11800 : "walking, 3.0 mph, moderately and carrying light objects less than 25 lbs "
            ,11805 : "walking, pushing a wheelchair "
            ,11810 : "walking, 3.5 mph, briskly and carrying objects less than 25 pounds "
            ,11820 : "walking or walk downstairs or standing, carrying objects about 25 to 49 pounds "
            ,11830 : "walking or walk downstairs or standing, carrying objects about 50 to 74 pounds "
            ,11840 : "walking or walk downstairs or standing, carrying objects about 75 to 99 pounds "
            ,11850 : "walking or walk downstairs or standing, carrying objects about 100 pounds or over "
            ,11870 : "working in scene shop, theater actor, backstage employee "}

        self.metDescription_fr  = {11003 : "poste de travail actif, bureau sur tapis roulant, marcher"
            ,11006 : "agent de bord d'avion"
            ,11010 : "boulangerie, général, effort modéré"
            ,11015 : "boulangerie, effort léger"
            ,11020 : "reliure de livres"
            ,11030 : "construction de routes, conduire des machines lourdes"
            ,11035 : "construction de routes, gérer la circulation, debout"
            ,11038 : "charpenterie, général, effort léger"
            ,11040 : "charpenterie, général, effort modéré"
            ,11042 : "charpenterie, général, effort lourd ou vigoureux"
            ,11050 : "port de charges lourdes (par ex. briques, outils)"
            ,11060 : "montée de charges modérées dans des escaliers, transport de cartons (11-22 kg)"
            ,11070 : "femme de chambre, concierge d'hôtel, faire le lit, nettoyer une salle de bains, pousser un chariot"
            ,11080 : "extraction de charbon, perforation du charbon, de la roche"
            ,11090 : "extraction de charbon, montage des supports"
            ,11100 : "extraction de charbon, général"
            ,11110 : "extraction de charbon, pelleter le charbon"
            ,11115 : "cuisiner, chef"
            ,11120 : "construction, à l'extérieur, rénovation, structures nouvelles (par ex. réparation de toit, divers)"
            ,11125 : "travail de concierge, effort léger (par ex. nettoyer lavabos et toilettes, épousseter, passer l'aspirateur, nettoyage léger)"
            ,11126 : "travail de concierge, effort modéré (par ex. armoire électrique, balayer, passer la serpillère, sortir les poubelles, passer l'aspirateur)"
            ,11128 : "conduire un camion de livraison, taxi, bus (scolaire, navette)"
            ,11130 : "travaux d'électricité (par ex. brancher des fils, dériver-connecter)"
            ,11135 : "ingénieur (par ex. mécanique ou électrique)"
            ,11145 : "agriculture, effort vigoureux (par ex. fabriquer des bottes de foin, nettoyer une grange)"
            ,11146 : "agriculture, effort modéré (par ex. nourrir des animaux, regrouper du bétail à pied et/ou cheval, épandre du fumier, récolter des cultures)"
            ,11147 : "agriculture, effort léger (par ex. nettoyer des déjections animales, préparer de la nourriture pour animaux)"
            ,11170 : "agriculture, conduites (par ex. conduire un tracteur ou une moissonneuse)"
            ,11180 : "agriculture, alimenter de petits animaux"
            ,11190 : "agriculture, alimenter le bétail, les chevaux"
            ,11191 : "agriculture, transporter de l'eau pour les animaux, transporter de l'eau en général"
            ,11192 : "agriculture, s'occuper des animaux (par ex. toilettage, brossage, tonte des moutons, aide à la mise bas, soins médicaux, marquage), général"
            ,11195 : "agriculture, riz, plantation, activités de traitement du grain"
            ,11210 : "agriculture, traire à la main, nettoyage des seaux, effort modéré"
            ,11220 : "agriculture, traire à la machine, effort léger"
            ,11240 : "pompier, général"
            ,11244 : "pompier, secours de victime, accident automobile, utilisation d’une gaffe"
            ,11245 : "pompier, levage et montée de l’échelle avec l’équipement complet, exercice d’extinction de feu"
            ,11246 : "pompier, transport de tuyaux au sol, transport du matériel, ouverture de murs, etc., en portant l’équipement complet"
            ,11247 : "pêche, commerciale, effort léger"
            ,11248 : "pêche, commerciale, effort modéré"
            ,11249 : "pêche, commerciale, effort vigoureux"
            ,11250 : "foresterie, couper du bois à la hache, très vite, hache de 1,25 kg, 51 coups/minute, effort violent"
            ,11260 : "foresterie, couper du bois à la hache, lentement, hache de 1,25 kg, 19 coups/minute, effort modéré"
            ,11262 : "foresterie, couper du bois à la hache, vite, hache de 1,25 kg, 35 coups/minute, effort vigoureux"
            ,11264 : "foresterie, effort modéré (par ex. scier du bois à la tronçonneuse, désherber, biner)"
            ,11266 : "foresterie, effort vigoureux (par ex. écorcer, abattre ou élaguer des arbres, porter ou empiler des buches, planter des semences, scier du bois à la main)"
            ,11370 : "pelleterie (Préparation des peaux destinée à les transformer en fourrure.)"
            ,11375 : "collecte d’ordures, marcher, verser des conteneurs dans un camion"
            ,11378 : "coiffeur (par ex. tresser des cheveux, manucurer, maquiller)"
            ,11380 : "palefrenier, nourrir des chevaux, nettoyer des stalles, laver, bouchonner, coiffer, faire travailler les chevaux à la longe ou les monter"
            ,11381 : "cheval, nourrir, abreuver, nettoyer des stalles, impliquant de marcher et porter des charges"
            ,11390 : "course de chevaux, galop"
            ,11400 : "course de chevaux, trot"
            ,11410 : "course de chevaux, pas"
            ,11413 : "cuisinière"
            ,11415 : "jardinier, jardinage, général"
            ,11418 : "blanchisseur"
            ,11420 : "serrurier"
            ,11430 : "travail à la machine (par ex. usinage, tôlerie, montage de machine, tournage, soudage), effort léger à modéré"
            ,11450 : "travail à la machine, utilisation d'une poinçonneuse, effort modéré"
            ,11472 : "gestionnaire, propriété"
            ,11475 : "travail manuel ou non qualifié, général, effort léger"
            ,11476 : "travail manuel ou non qualifié, général, effort modéré"
            ,11477 : "travail manuel ou non qualifié, général, effort vigoureux"
            ,11480 : "maçonnerie, béton, effort modéré"
            ,11482 : "maçonnerie, béton, effort léger"
            ,11485 : "massothérapeute, debout"
            ,11490 : "déplacer, porter ou pousser des objets lourds, 34 kg ou plus (par ex. bureaux, déménagement), périodes actives uniquement"
            ,11495 : "plongée sous-marine, homme-grenouille, commandos de marine"
            ,11500 : "utiliser un équipement de travail lourd, automatisé, sans conduire"
            ,11510 : "travail dans une orangeraie, cueillette des oranges"
            ,11514 : "peinture, maison, meubles, effort modéré"
            ,11516 : "activités de plomberie"
            ,11520 : "impression, travailleur de l'industrie du papier, debout"
            ,11525 : "police, faire la circulation, debout"
            ,11526 : "police, conduire un véhicule de police, assis"
            ,11527 : "police, être conduit dans un véhicule de police, assis"
            ,11528 : "police, effectuer une arrestation, debout"
            ,11529 : "postier, marcher pour livrer le courrier"
            ,11530 : "cordonnerie, général"
            ,11540 : "pelleter, creuser des fossés"
            ,11550 : "pelleter, plus de 7 kg/minute, en creusant profondément, effort vigoureux"
            ,11560 : "pelleter, moins de 4,5 kg/minute, effort modéré"
            ,11570 : "pelleter, 4,5-7 kg/minute, effort vigoureux"
            ,11580 : "travail assis, effort léger (par ex. travail de bureau, travail de laboratoire de chimie, travail sur ordinateur, réparation d’ensemble léger, réparation de montre, lecture)"
            ,11585 : "être assis, réunions, effort léger, général, et/ou impliquant une discussion (par ex. déjeuner d'affaires)"
            ,11590 : "travail assis, effort modéré (par ex. pousser de lourds leviers, conduire une tondeuse/un chariot élévateur, commander une grue)"
            ,11593 : "être assis, enseigner le stretching ou le yoga, ou cours d’exercices légers"
            ,11600 : "être debout, effort léger (par ex. barman, employé de magasin, assemblage, remplissage, reproduction, bibliothécaire, installer un sapin de Noël, être debout et parler au travail, changer de vêtements lors de l'enseignement de l'éducation physique, debout)"
            ,11610 : "être debout, effort léger/modéré (par ex. assembler/réparer des pièces lourdes, souder, stocker des pièces, réparer des automobiles, être debout, emballer des objets, soins infirmiers à des patients)"
            ,11615 : "être debout, effort modéré, soulever des articles en permanence, 5–10 kg, avec une marche limitée ou sur place"
            ,11620 : "être debout, effort modéré, levage intermittent de 23 kg, nouer/lover des cordages"
            ,11630 : "être debout, effort modéré/important (par ex. soulever plus de 23 kg, maçonner, peindre, tapisser)"
            ,11708  : "aciérie, effort modéré (par ex. ébarber, forger, retourner des moules)"
            ,11710 : "aciérie, effort vigoureux (par ex. laminer à la main, laminer des aciers marchands, enlever des scories, alimenter un four)"
            ,11720 : "confection, coupe de tissu"
            ,11730 : "confection, général"
            ,11740 : "confection, coudre à la main"
            ,11750 : "confection, coudre à la machine"
            ,11760 : "confection, pressing"
            ,11763 : "confection, tisser, effort léger (par ex. opérations de finition, lavage, teinture, visite, métrage, paperasse)"
            ,11765 : "confection, tissage, effort modéré (par ex. opérations de filage et tissage, apporter des boîtes de fil aux filateurs, chargement d’ensouple de chaîne, bobinage, ourdissage, découpe de tissu)"
            ,11766 : "conduite de camion, chargement et déchargement du camion, arrimage de la charge, marcher en portant des charges lourdes"
            ,11770 : "taper des documents avec une machine à écrire électrique, mécanique ou un ordinateur"
            ,11780 : "utiliser des outils motorisés lourds tels que des outils pneumatiques (par ex. marteaux-piqueurs, foreuses)"
            ,11790 : "utiliser des outils lourds (non motorisés) tels que des pelles, des pioches, des barres à mine, des bêches"
            ,11791 : "marcher au travail, à moins de 3,5 km/h, dans un bureau ou laboratoire, rythme très lent"
            ,11792 : "marcher au travail à 5 km/h, dans un bureau, rythme modéré, sans rien porter"
            ,11793 : "marcher au travail à 6 km/h, dans un bureau, rythme rapide, sans rien porter"
            ,11795 : "marcher au travail, à 3 km/h, rythme lent, en portant des objets légers pesant moins de 11 kg"
            ,11796 : "marcher, ranger des affaires au travail, se préparer à partir"
            ,11797 : "marcher, à 4 km/h, rythme lent, en portant des objets lourds de plus de 11 kg"
            ,11800 : "marcher à 5 km/h, rythme modéré, en portant des objets légers de moins de 11 kg"
            ,11805 : "marcher, pousser un fauteuil roulant"
            ,11810 : "marcher à 6 km/h, rythme rapide, en portant des objets pesant moins de 11 kg"
            ,11820 : "marcher ou descendre des escaliers ou se tenir debout en portant des objets pesant de 11 à 22 kg"
            ,11830 : "marcher ou descendre des escaliers ou se tenir debout en portant des objets pesant de 22 à 33 kg"
            ,11840 : "marcher ou descendre des escaliers ou se tenir debout en portant des objets pesant de 33 à 45 kg"
            ,11850 : "marcher ou descendre des escaliers ou se tenir debout en portant des objets pesant de 45 kg ou plus"
            ,11870 : "employé d'un magasin de décor, acteur de théâtre, technicien de coulisses"}

    def printValues(self):
        print("Beginning dump for 'Occupation' ")
        super().printValues()

    def getMetValue(self, code):
        return super().getMetValue(code)

if __name__ == "__main__":
    b = Occupation()
    b.printValues()
    print(b.getMetValue(11805))
    for l in b:
        print(l)