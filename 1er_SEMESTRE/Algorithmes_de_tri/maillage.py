# maillage de l'exercice "Orientation d'un maillage"

import numpy as np

NOEUDS = np.array([
    [0.5, 0],
    [0.4587024678069033, 0.0994887506553591],
    [0.3723196585212996, 0.1668667671216942],
    [0.2712246999281967, 0.2100221191618038],
    [0.1643555413586649, 0.2361076322488857],
    [0.05502005476478438, 0.2484817868444688],
    [-0.05502005476478034, 0.248481786844469],
    [-0.1643555413586608, 0.2361076322488864],
    [-0.2712246999281925, 0.2100221191618052],
    [-0.3723196585212945, 0.166866767121697],
    [-0.4587024678069003, 0.09948875065536253],
    [-0.5, 2.584128115483419e-15],
    [-0.4587024678069036, -0.0994887506553587],
    [-0.3723196585212991, -0.1668667671216945],
    [-0.2712246999281965, -0.2100221191618039],
    [-0.1643555413586635, -0.2361076322488859],
    [-0.05502005476478333, -0.2484817868444689],
    [0.05502005476478183, -0.2484817868444689],
    [0.1643555413586629, -0.236107632248886],
    [0.2712246999281911, -0.2100221191618056],
    [0.3723196585212981, -0.166866767121695],
    [0.4587024678069012, -0.09948875065536153],
    [-0.001248710667954504, -0.1626884316590377],
    [0.1980182501326675, 0.1346157432898888],
    [-0.2064611512750002, 0.1335077831308666],
    [1.831867990631508e-15, 0.1531899915627816],
    [-0.1952082257193729, -0.1305496124868998],
    [0.1937789184016852, -0.1304245240984052],
    [-0.3621045029505491, 0.06091790445063334],
    [0.3642442733230122, 0.07188054526621808],
    [0.3642442733230109, -0.07188054526621908],
    [-0.3435281165466834, -0.0436398006762509],
    [-0.1074346366229355, 0.1461745760961798],
    [-0.05566771234147858, 0.05565002462994918],
    [0.04930512275396116, 0.05672826968188793],
    [-0.003620944772342934, -0.03571400682741763],
    [-0.1150379858737566, -0.0480559822541808],
    [0.1076487008612113, -0.04504903877949325],
    [0.1017825061477651, 0.1497564956007195],
    [-0.09853153873432649, -0.1527631243657557],
    [-0.2307255817756732, -0.04284558253106419],
    [0.09489734152150037, -0.152601953380428],
    [0.2117163188676979, -0.03122209963551952],
    [0.1491992221932906, 0.04674194124657238],
    [0.2897426997475828, 0.1072674351194353],
    [-0.2984890233783076, 0.1221280028493559],
    [0.2859411786244204, -0.1066172671696142],
    [-0.2826012564982451, -0.1187847763955427],
    [-0.1632223031280439, 0.04466687190796574],
    [0.3093382989543838, 0.004235357741615144],
    [0.4113180266809279, 0.0005042092549534644],
    [-0.2674217798423761, 0.04578919652191774],
    [-0.4206853919308366, 0.001763071813714364],
    [0.2316029579791246, 0.05232767555239842],
    [-0.05339535216858682, -0.09270515848184831],
    [0.0443700125864146, -0.09413358111431588]
])

TRIANGLES = np.array([
    [41, 52, 32],
    [27, 40, 37],
    [28, 43, 38],
    [37, 41, 27],
    [32, 48, 41],
    [33, 49, 34],
    [38, 42, 28],
    [40, 55, 37],
    [25, 52, 49],
    [25, 49, 33],
    [32, 52, 29],
    [35, 44, 39],
    [47, 50, 43],
    [28, 47, 43],
    [3, 30, 2],
    [11, 29, 10],
    [22, 31, 21],
    [14, 32, 13],
    [9, 25, 8],
    [5, 24, 4],
    [16, 27, 15],
    [20, 28, 19],
    [18, 23, 17],
    [7, 26, 6],
    [36, 38, 35],
    [34, 37, 36],
    [34, 36, 35],
    [41, 48, 27],
    [39, 44, 24],
    [34, 35, 26],
    [46, 52, 25],
    [35, 39, 26],
    [38, 56, 42],
    [33, 34, 26],
    [45, 50, 30],
    [31, 50, 47],
    [34, 49, 37],
    [45, 54, 50],
    [8, 33, 7],
    [6, 39, 5],
    [25, 33, 8],
    [5, 39, 24],
    [19, 42, 18],
    [17, 40, 16],
    [28, 42, 19],
    [16, 40, 27],
    [43, 44, 38],
    [7, 33, 26],
    [26, 39, 6],
    [23, 40, 17],
    [18, 42, 23],
    [30, 51, 2],
    [11, 53, 29],
    [29, 53, 32],
    [22, 51, 31],
    [32, 53, 13],
    [2, 51, 1],
    [1, 51, 22],
    [13, 53, 12],
    [12, 53, 11],
    [50, 51, 30],
    [31, 51, 50],
    [49, 52, 41],
    [37, 49, 41],
    [4, 45, 3],
    [10, 46, 9],
    [38, 44, 35],
    [3, 45, 30],
    [29, 46, 10],
    [21, 47, 20],
    [15, 48, 14],
    [31, 47, 21],
    [14, 48, 32],
    [24, 45, 4],
    [9, 46, 25],
    [20, 47, 28],
    [27, 48, 15],
    [23, 56, 55],
    [55, 56, 36],
    [37, 55, 36],
    [36, 56, 38],
    [23, 55, 40],
    [42, 56, 23],
    [43, 54, 44],
    [44, 54, 24],
    [29, 52, 46],
    [24, 54, 45],
    [50, 54, 43],
])
