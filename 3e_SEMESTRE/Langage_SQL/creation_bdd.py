# -*- coding: utf-8 -*-

""" Pour créer le fichier bdd"""

import sqlite3
from random import randint

c = sqlite3.connect('voyages_affaires.db') # si le fichier n'existe pas, cette instruction le crée
curseur = c.cursor()

def requete(R):
	""" R est la requête écrite en syntaxe SQL, qu'il conviendra d'encadrer par une paire de triples guillemets """
	curseur.execute(R)
	for ligne in curseur:
		print(str(ligne)[1:-1])

# création des tables
requete("""
CREATE TABLE IF NOT EXISTS Employe (
id int(5) NOT NULL,
nom varchar(128) NOT NULL,
prenom varchar(128) NOT NULL,
ville varchar(128) NOT NULL,
region varchar(128) NOT NULL,
poste varchar(128) NOT NULL,
departement varchar(128) NOT NULL,
PRIMARY KEY (id)
)        """)

requete(""" 
CREATE TABLE IF NOT EXISTS Logement (
id int(5) NOT NULL,
nom varchar(128) NOT NULL,
type varchar(128) NOT NULL,
ville varchar(128) NOT NULL,
pays varchar(128) NOT NULL,
prix int(4) NOT NULL,
PRIMARY KEY (id)
)""")

requete("""
CREATE TABLE IF NOT EXISTS Sejour (
id_sejour int(5) NOT NULL,
id_voyageur int(5) NOT NULL REFERENCES Employe,
id_logement int(5) NOT NULL REFERENCES Logement,
debut DATE NOT NULL,
fin DATE NOT NULL,
mission text NOT NULL,
PRIMARY KEY (id_sejour)
)""")


# création des enregistrements


# id_logement = [randint(1, 999) for _ in range(len(41))]
# id_voyageur = [randint(1, 999) for _ in range(23)]
id_logement = [34, 49, 81, 86, 136, 155, 157, 164, 231, 251, 265, 310, 337, 392, 410, 471, 496, 497, 537, 595, 599, 661, 678, 692, 739, 745, 752, 758, 805, 838, 852, 854, 867, 888, 931, 935, 943, 961, 985, 991, 995]
id_voyageur = [99, 156, 163, 214, 263, 279, 371, 409, 472, 493, 536, 588, 605, 606, 626, 642, 659, 675, 759, 816, 851, 924, 957]

missions = ["pop-up", "ventes", "rencontre avec un client", "conférence", "réunion", "étude de marché", "ventes"]


def f(n):
    """
    Crée n lignes de valeurs à insérer dans la table Sejour. 
    
    Les dates de début et de fin de séjour
    ont été créées grossièrement, les seuls contraintes respectées étaient que la date de fin est 
    toujours postérieure à la date de début et qu'il n'y ait pas de date absurde du type 30 février.
    """
    def dates():
        # debut
        annee = randint(2018, 2022)
        mois = randint(1, 11)
        jour = randint(1, 28)
        # fin
        if jour > 22:
            mois_fin = mois + 1
            jour_fin = randint(1, 4)
        elif 22 >= jour > 10: 
            mois_fin = mois
            jour_fin = jour + randint(1, 6)
        else:
            mois_fin = mois
            jour_fin= jour + randint(1, 15)
        return """'{}-{:02d}-{:02d}'""".format(annee, mois, jour), """'{}-{:02d}-{:02d}'""".format(annee, mois_fin, jour_fin)
    
    S = ''
    ids = list(range(1, 1000))
    for i in range(n):
        
        debut, fin = dates()
        mission = missions[randint(0, len(missions)-1)]
        
        s = [ids.pop(randint(0, len(ids)-1)), id_voyageur[randint(0, len(id_voyageur)-1)], id_logement[randint(0, len(id_logement)-1)], debut, fin, mission]
        
        s = tuple(s)
        s = str(s)
        S += s
        S += ',\n'
    S = S.replace("\"", "")
    print(S)
    return S


requete("""INSERT INTO Employe (id, nom, prenom, ville, region, poste, departement) VALUES
(605,   'Durand',   'Alexandre',    'Angers',   'Pays de la Loire',     'Chargé de communication',  'Communication'),
(263,   'Menos',    'Elliot',       'Angers',   'Pays de la Loire',     'Comptable',    'Comptabilité'),
(626,   'Drujont',  'Erwann',       'Angers',   'Pays de la Loire',     'Ingénieur',    'R&D'),
(536,   'Danielo',  'Valentin',     'Angers',   'Pays de la Loire',     'Ingénieur',    'R&D'),
(99,    'Gaillard', 'Matthieu',     'Angers',   'Pays de la Loire',     'DRH',          'RH'),
(642,   'Duhazé',   'Clément',      'Bordeaux', 'Nouvelle-Aquitaine',   'Comptable',    'Comptabilité'),
(214,   'Zai',      'Zahia',        'Bordeaux', 'Nouvelle-Aquitaine',   'DRH',          'RH'),
(279,   'Milan',    'Gabriel',      'Lyon',     'Auvergne-Rhône-Alpes', 'DRH',          'RH'),
(163,   'Pineau',   'Axelle',       'Lyon',     'Auvergne-Rhône-Alpes', 'Vendeur',      'Ventes'),                                      
(659,   'Fredon',   'Maxime',       'Lyon',     'Auvergne-Rhône-Alpes', 'Comptable',    'Comptabilité'),                              
(851,   'Beauquel', 'Maël',         'Marseille','PACA',                 'Vendeur',      'Ventes'),                        
(924,   'Ouri',     'Adel',         'Marseille','PACA',                 'Vendeur',      'Ventes'),                           
(816,   'Valléau',  'Romain',       'Paris',    'Île-de-France',        'Comptable',    'Comptabilité'),
(371,   'Nguyen',   'Tuan',         'Paris',    'Île-de-France',        'DRH',          'RH'),
(606,   'Leiros',   'Jules',        'Paris',    'Île-de-France',        'Vendeur',      'Ventes'), 
(588,   'Routhier', 'Louis',        'Paris',    'Île-de-France',        'Vendeur',      'Ventes'), 
(409,   'Dorval',   'Loïc',         'Paris',    'Île-de-France',        'PDG',          'Direction'),
(957,   'Pennec',   'Jade',         'Paris',    'Île-de-France',        'Manager',      'Ventes'),
(156,   'Saroui',   'Alice',        'Paris',    'Île-de-France',        'Chargé de communication', 'Communication'), 
(675,   'Laffitte', 'Louise',       'Toulouse', 'Occitanie',            'Comptable',    'Comptabilité'),
(759,   'Brzenczek','Cyril',        'Toulouse', 'Occitanie',            'DRH',          'RH'),
(472,   'Victor',   'Claude',       'Toulouse', 'Occitanie',            'Vendeur',      'Ventes'), 
(493,   'Lopez',    'Léo',          'Toulouse', 'Occitanie',            'Vendeur',      'Ventes')
        """)

requete("""INSERT INTO Logement (id, nom, type, ville, pays, prix) VALUES
(155,   'My Nice B&B',              'gîte',         'Nice',         'France',       77),
(86,    'La cabane insolite',       'airbnb',       'Toulouse',     'France',       56),
(692,   'Le 123 Sebastopol',        'hôtel',        'Paris',        'France',       109),
(961,   'Hôtel Axotel Lyon',        'hôtel',        'Lyon',         'France',       138),
(136,   'Hôtel Charlemagne',        'hôtel',        'Lyon',         'France',       115),
(157,   'Radisson Blu Hotel Lyon',  'hôtel',        'Lyon',         'France',       127),
(935,   'Bubble dreams',            'appartement',  'Paris',        'France',       101),
(497,   'Au jardin des soeurs',     'airbnb',       'Paris',        'France',       174),
(867,   'Croissant de Lune',        'gîte',         'Marseille',    'France',       26),

(392,   'Pension Locarno',          'gîte',         'Munich',       'Allemagne',    21),
(805,   'Reichshof Hotel Hamburg',  'hôtel',        'Hambourg',     'Allemagne',    104),
(852,   'Chez Ronny',               'gîte',         'Hambourg',     'Allemagne',    65),
(854,   'Tempelhoferfeld',          'airbnb',       'Berlin',       'Allemagne',    54),
(410,   'Hotel Bett und Buch',      'hôtel',        'Berlin',       'Allemagne',    98),
(678,   'Pestana Berlin Tiergarten','hôtel',        'Berlin',       'Allemagne',    171),
(931,   'Riu Plaza Hotel',          'hôtel',        'Berlin',       'Allemagne',    150),
(985,   'Pension Am Park',          'airbnb',       'Berlin',       'Allemagne',    123),

(888,   'Park Plaza Riverbank',     'hôtel',        'Londres',      'Angleterre',   198),
(661,   'Vilenza Hotel',            'hôtel',        'Londres',      'Angleterre',   201),
(49,    'Kip Hotel',                'hôtel',        'Londres',      'Angleterre',   173),
(310,   'The Standard London',      'hôtel',        'Londres',      'Angleterre',   151),
(81,    'Mcdonald Burlington Hotel','hôtel',        'Birmingham',   'Angleterre',   106),
(943,   'Haya Guest House',         'appartement',  'Manchester',   'Angleterre',   110),

(995,   'Motel One Zürich',         'hôtel',        'Zurich',       'Suisse',       225),
(231,   'Acasa Suites',             'hôtel',        'Zurich',       'Suisse',       201),
(337,   'Hotel Victoria',           'hôtel',        'Lausanne',     'Suisse',       199),
(496,   'Hotel de la Paix',         'hôtel',        'Lausanne',     'Suisse',       145),
(595,   'Cozy studio',              'appartement',  'Genève',       'Suisse',       169),

(745,   'Hotel Veneto Palace',      'hôtel',        'Rome',         'Italie',       89),
(251,   'Black and White Suite',    'appartement',  'Rome',         'Italie',       76),
(838,   'Biancorèroma B&B',         'gîte',         'Rome',         'Italie',       143),
(471,   'Little Aurelius',          'hôtel',        'Rome',         'Italie',       104),

(599,   'Vincci Soma',              'hôtel',        'Madrid',       'Espagne',      105),
(758,   'Principe Pio',             'hôtel',        'Madrid',       'Espagne',      112),
(537,   'One Shot Prado 23',        'hôtel',        'Madrid',       'Espagne',      91),
(164,   'Bob W Chueca',             'airbnb',       'Madrid',       'Espagne',      52),

(34,    'Harborside Inn',           'hôtel',        'Boston',       'Etats-Unis',   187),
(739,   'Charlesmark Hotel',        'hôtel',        'Boston',       'Etats-Unis',   196),

(991,   'Hotel Albergo',            'hôtel',        'Bruxelles',    'Belgique',     87),
(752,   'Marivaux Hotel',           'hôtel',        'Bruxelles',    'Belgique',     94),

(265,   'Grand Millenium Beijing',  'hôtel',        'Pekin',        'Chine',        94)
        """)
        
    
requete("""INSERT INTO Sejour (id_sejour, id_voyageur, id_logement, debut, fin, mission) VALUES
(562, 606, 155, '2022-10-27', '2022-11-01', 'pop-up'),
(428, 851, 805, '2020-04-06', '2020-04-15', 'conférence'),
(856, 605, 410, '2019-11-25', '2019-12-01', 'étude de marché'),
(383, 263, 34, '2022-10-13', '2022-10-18', 'ventes'),
(189, 163, 752, '2021-04-21', '2021-04-27', 'ventes'),
(130, 605, 961, '2022-01-18', '2022-01-19', 'étude de marché'),
(25, 816, 995, '2018-04-23', '2018-05-01', 'ventes'),
(593, 957, 497, '2022-03-10', '2022-03-22', 'ventes'),
(295, 659, 991, '2018-09-13', '2018-09-17', 'étude de marché'),
(280, 659, 678, '2022-04-28', '2022-05-02', 'ventes'),
(463, 472, 595, '2019-02-23', '2019-03-04', 'conférence'),
(151, 99, 471, '2019-03-04', '2019-03-11', 'conférence'),
(854, 99, 164, '2018-05-28', '2018-06-03', 'rencontre avec un client'),
(815, 605, 752, '2018-09-04', '2018-09-11', 'pop-up'),
(838, 924, 265, '2018-03-26', '2018-04-01', 'rencontre avec un client'),
(365, 472, 985, '2019-01-22', '2019-01-26', 'conférence'),
(646, 588, 231, '2019-04-02', '2019-04-10', 'rencontre avec un client'),
(926, 659, 164, '2022-11-17', '2022-11-20', 'pop-up'),
(435, 156, 995, '2022-06-18', '2022-06-20', 'pop-up'),
(243, 371, 739, '2022-11-18', '2022-11-22', 'rencontre avec un client'),
(214, 279, 86, '2021-10-25', '2021-11-04', 'pop-up'),
(589, 279, 49, '2022-04-21', '2022-04-23', 'ventes'),
(438, 957, 136, '2022-04-07', '2022-04-15', 'étude de marché'),
(392, 409, 310, '2018-06-05', '2018-06-09', 'réunion'),
(924, 472, 838, '2021-02-06', '2021-02-21', 'étude de marché'),
(61, 371, 745, '2021-11-14', '2021-11-16', 'rencontre avec un client'),
(992, 816, 471, '2019-08-27', '2019-09-01', 'pop-up'),
(806, 99, 943, '2020-09-22', '2020-09-24', 'ventes'),
(6, 99, 599, '2019-11-07', '2019-11-13', 'rencontre avec un client'),
(849, 536, 337, '2022-09-23', '2022-10-03', 'pop-up'),
(648, 472, 49, '2018-08-09', '2018-08-24', 'rencontre avec un client'),
(355, 493, 692, '2022-05-15', '2022-05-21', 'ventes'),
(991, 163, 678, '2021-08-11', '2021-08-14', 'rencontre avec un client'),
(542, 957, 943, '2022-03-26', '2022-04-04', 'conférence'),
(576, 759, 497, '2019-03-16', '2019-03-18', 'réunion'),
(957, 957, 337, '2020-04-23', '2020-05-02', 'réunion'),
(399, 214, 852, '2022-05-22', '2022-05-23', 'ventes'),
(961, 957, 136, '2020-04-05', '2020-04-06', 'conférence'),
(332, 957, 678, '2021-02-21', '2021-02-23', 'ventes'),
(577, 659, 752, '2022-08-19', '2022-08-24', 'pop-up'),
(919, 642, 157, '2020-11-28', '2020-12-02', 'conférence'),
(679, 957, 935, '2019-05-14', '2019-05-20', 'rencontre avec un client'),
(923, 536, 81, '2020-02-09', '2020-02-17', 'rencontre avec un client'),
(572, 642, 931, '2018-07-22', '2018-07-23', 'conférence'),
(333, 409, 155, '2022-07-21', '2022-07-25', 'rencontre avec un client'),
(947, 472, 661, '2018-08-01', '2018-08-04', 'conférence'),
(307, 924, 739, '2020-02-05', '2020-02-12', 'réunion'),
(858, 605, 888, '2018-05-17', '2018-05-18', 'ventes'),
(249, 957, 497, '2019-09-09', '2019-09-13', 'conférence'),
(389, 642, 854, '2018-06-12', '2018-06-18', 'pop-up'),
(88, 816, 692, '2022-02-01', '2022-02-14', 'pop-up'),
(988, 493, 595, '2020-02-07', '2020-02-08', 'réunion'),
(246, 816, 86, '2019-06-27', '2019-07-02', 'ventes'),
(658, 851, 471, '2020-02-25', '2020-03-01', 'pop-up'),
(622, 156, 854, '2020-06-05', '2020-06-18', 'pop-up'),
(907, 816, 265, '2021-04-14', '2021-04-18', 'conférence'),
(649, 263, 661, '2022-05-25', '2022-06-03', 'étude de marché'),
(931, 371, 86, '2018-01-06', '2018-01-08', 'étude de marché'),
(137, 626, 81, '2020-09-12', '2020-09-17', 'ventes'),
(786, 606, 854, '2020-10-18', '2020-10-22', 'rencontre avec un client'),
(643, 409, 678, '2019-02-12', '2019-02-16', 'rencontre avec un client'),
(990, 214, 471, '2020-02-16', '2020-02-21', 'ventes'),
(536, 642, 931, '2020-02-05', '2020-02-11', 'ventes'),
(728, 675, 931, '2019-05-25', '2019-06-04', 'ventes'),
(548, 924, 537, '2019-05-19', '2019-05-20', 'étude de marché'),
(952, 588, 471, '2019-08-25', '2019-09-03', 'rencontre avec un client'),
(941, 156, 251, '2020-03-12', '2020-03-18', 'rencontre avec un client'),
(139, 214, 995, '2019-08-09', '2019-08-24', 'réunion'),
(884, 536, 81, '2018-09-22', '2018-09-25', 'étude de marché'),
(110, 99, 991, '2018-03-03', '2018-03-05', 'pop-up'),
(256, 606, 81, '2020-04-02', '2020-04-16', 'étude de marché'),
(1, 263, 867, '2022-11-21', '2022-11-22', 'conférence'),
(508, 536, 392, '2018-01-24', '2018-02-03', 'conférence'),
(58, 493, 337, '2022-07-23', '2022-08-01', 'ventes'),
(583, 472, 595, '2020-03-05', '2020-03-10', 'étude de marché'),
(551, 409, 34, '2022-01-18', '2022-01-20', 'ventes'),
(299, 924, 265, '2018-05-14', '2018-05-16', 'étude de marché'),
(987, 214, 496, '2018-10-17', '2018-10-22', 'ventes'),
(532, 409, 49, '2021-05-15', '2021-05-16', 'pop-up'),
(758, 99, 497, '2021-04-04', '2021-04-14', 'ventes'),
(120, 279, 745, '2019-08-13', '2019-08-14', 'ventes'),
(750, 816, 739, '2022-05-12', '2022-05-17', 'ventes'),
(480, 156, 961, '2018-06-02', '2018-06-09', 'ventes'),
(330, 759, 86, '2020-02-05', '2020-02-13', 'réunion'),
(234, 156, 752, '2020-02-20', '2020-02-25', 'rencontre avec un client'),
(799, 606, 49, '2020-05-23', '2020-06-01', 'réunion'),
(269, 472, 595, '2021-03-15', '2021-03-17', 'réunion'),
(102, 605, 854, '2018-10-05', '2018-10-09', 'réunion'),
(424, 626, 854, '2021-11-26', '2021-12-04', 'rencontre avec un client'),
(641, 957, 537, '2019-06-26', '2019-07-02', 'conférence'),
(605, 493, 231, '2021-11-22', '2021-11-26', 'étude de marché'),
(618, 957, 888, '2022-02-11', '2022-02-15', 'pop-up'),
(627, 851, 758, '2021-02-22', '2021-02-25', 'rencontre avec un client'),
(359, 163, 752, '2022-05-17', '2022-05-18', 'ventes'),
(185, 279, 595, '2021-09-01', '2021-09-16', 'réunion'),
(437, 605, 34, '2018-09-11', '2018-09-12', 'ventes'),
(385, 816, 961, '2022-10-12', '2022-10-14', 'rencontre avec un client'),
(785, 279, 599, '2022-06-08', '2022-06-12', 'rencontre avec un client'),
(813, 851, 86, '2022-06-25', '2022-07-03', 'ventes'),
(906, 493, 854, '2020-03-13', '2020-03-14', 'étude de marché'),
(636, 605, 995, '2018-07-01', '2018-07-16', 'conférence'),
(51, 279, 661, '2019-05-27', '2019-06-03', 'étude de marché'),
(441, 924, 931, '2021-05-21', '2021-05-24', 'rencontre avec un client'),
(50, 472, 692, '2022-06-09', '2022-06-10', 'pop-up'),
(654, 409, 752, '2022-03-05', '2022-03-12', 'ventes'),
(80, 214, 888, '2020-08-12', '2020-08-13', 'ventes'),
(967, 588, 661, '2019-02-18', '2019-02-23', 'ventes'),
(216, 99, 661, '2021-02-09', '2021-02-24', 'rencontre avec un client'),
(974, 371, 852, '2020-07-11', '2020-07-12', 'ventes'),
(732, 99, 991, '2019-11-01', '2019-11-05', 'ventes'),
(219, 851, 496, '2022-10-24', '2022-11-01', 'ventes'),
(805, 536, 661, '2022-01-02', '2022-01-14', 'réunion'),
(896, 642, 49, '2020-04-26', '2020-05-03', 'réunion'),
(465, 816, 995, '2021-09-15', '2021-09-17', 'pop-up'),
(141, 675, 852, '2018-01-20', '2018-01-21', 'étude de marché'),
(483, 536, 155, '2019-04-24', '2019-05-02', 'conférence'),
(390, 626, 496, '2021-01-15', '2021-01-20', 'étude de marché'),
(116, 156, 157, '2021-07-19', '2021-07-21', 'réunion'),
(962, 472, 991, '2022-09-02', '2022-09-06', 'conférence'),
(936, 99, 537, '2018-03-08', '2018-03-13', 'étude de marché'),
(581, 675, 867, '2018-09-07', '2018-09-10', 'ventes'),
(929, 851, 49, '2019-03-19', '2019-03-23', 'ventes'),
(882, 759, 410, '2018-06-19', '2018-06-23', 'étude de marché'),
(642, 851, 739, '2021-09-04', '2021-09-16', 'ventes'),
(146, 214, 752, '2019-05-25', '2019-06-03', 'étude de marché'),
(640, 588, 251, '2022-09-13', '2022-09-15', 'ventes'),
(426, 409, 935, '2018-07-09', '2018-07-16', 'réunion'),
(164, 536, 265, '2019-01-28', '2019-02-01', 'pop-up'),
(212, 99, 758, '2020-03-17', '2020-03-23', 'ventes'),
(603, 263, 537, '2021-10-17', '2021-10-20', 'rencontre avec un client'),
(45, 851, 157, '2020-07-14', '2020-07-17', 'rencontre avec un client'),
(326, 605, 995, '2020-02-24', '2020-03-02', 'rencontre avec un client'),
(70, 626, 310, '2022-09-12', '2022-09-14', 'conférence'),
(529, 675, 251, '2018-06-12', '2018-06-13', 'réunion'),
(237, 163, 888, '2022-04-28', '2022-05-03', 'ventes'),
(402, 493, 136, '2018-11-24', '2018-12-02', 'étude de marché'),
(160, 536, 595, '2022-11-20', '2022-11-26', 'ventes'),
(459, 536, 337, '2018-04-01', '2018-04-16', 'ventes'),
(748, 536, 961, '2019-04-18', '2019-04-21', 'ventes'),
(34, 851, 995, '2021-03-11', '2021-03-17', 'pop-up'),
(809, 851, 34, '2022-10-20', '2022-10-21', 'réunion'),
(995, 924, 661, '2020-10-21', '2020-10-23', 'ventes'),
(179, 409, 496, '2019-02-18', '2019-02-19', 'pop-up'),
(765, 605, 935, '2018-07-21', '2018-07-26', 'étude de marché'),
(147, 924, 86, '2022-10-24', '2022-11-01', 'étude de marché'),
(617, 536, 943, '2019-10-07', '2019-10-10', 'étude de marché'),
(186, 642, 251, '2019-10-03', '2019-10-10', 'ventes'),
(731, 536, 410, '2021-05-25', '2021-06-01', 'ventes'),
(83, 409, 805, '2021-11-04', '2021-11-08', 'ventes'),
(623, 588, 991, '2021-08-12', '2021-08-17', 'étude de marché')
        """)

requete("""DELETE FROM Sejour 
WHERE id_logement = 595 or id_logement = 251      
""") 
# pour avoir une ville où personne n'est allé, et une ville avec un logement où personne n'est allé et un logement où quelqu'un est allé
# permet de différencier les bonnes et mauvaises requêtes pour la question 5
c.commit()
c.close()