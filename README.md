# Description des datasets

<br>

### Games.csv

|nom de la colonne|Description|Exemple|
|---|---|---|
|GAME_DATE_EST|Date du match|2021-05-26|
|GAME_ID    |Id du match|           42000102|
|GAME_STATUS_TEXT  |Statut du match|       Final|
|HOME_TEAM_ID     |Id de l'équipe home|   1610612755|
|VISITOR_TEAM_ID  |Id de l'équipe visiteur|   1610612764|
|SEASON          |année de la saison|          2020|
|TEAM_ID_home    |Id de l'équipe home|    1610612755|
|PTS_home        |Points de l'équipe home|           120|
|FG_PCT_home     |Pourcentage de tirs réussi 2pts équipe home|         0.557|
|FT_PCT_home       |Pourcentage de lancers francs réussi équipe home|       0.684|
|FG3_PCT_home     |Pourcentage de tirs réussi 3pts équipe home|        0.429|
|AST_home        |Nombre passes décisives équipe home|            26|
|REB_home      |Nombre de rebonds équipe home|              45|
|TEAM_ID_away   |Id de l'équipe visitor|     1610612764|
|PTS_away        |Points de l'équipe visitor|            95|
|FG_PCT_away      |Pourcentage de tirs réussi 2pts équipe visitor|        0.402|
|FT_PCT_away      |Pourcentage de lancers francs réussi équipe visitor|        0.633|
|FG3_PCT_away     |Pourcentage de tirs réussi 3pts équipe visitor|        0.091|
|AST_away         |Nombre passes décisives équipe visitor|           22|
|REB_away         |Nombre de rebonds équipe visitor|           40|
|HOME_TEAM_WINS     |Résultats booléen, si home wins|          1|

---

<br>

### Games_details.csv

|nom de la colonne|Description|Exemple|
|---|---|---|
|GAME_ID        |Id du match|          42000102|
|TEAM_ID        |Id de l'équipe (2 par game id)|        1610612764|
|TEAM_ABBREVIATION        |abréviation team|     WAS|
|TEAM_CITY       |ville|       Washington|
|PLAYER_ID        |id des joueurs|          203078|
|PLAYER_NAME      |nom des joueurs|    Bradley Beal|
|START_POSITION    |Position|              F|
|COMMENT          |Commentaire|             NaN|
|MIN              |nombre de minutes jouées|           34:36|
|FGM             |nombre paniers marqués 2pts|               14|
|FGA             |nombre de tirs ratés 2pts|               28|
|FG_PCT         |pourcentage de tirs 2pts marqués|               0.5|
|FG3M        |nombre paniers marqués 3pts|                    1|
|FG3A              |nombre de tirs ratés 3pts|              6|
|FG3_PCT         |pourcentage de tirs 3pts marqués|            0.167|
|FTM             |Nombre de lancers francs marqués|                4|
|FTA             |Nombre de lancers francs ratés|                6|
|FT_PCT          |Pourcentage de lancers francs réussis|            0.667|
|OREB            |Nombre de rebonds offensifs|                0|
|DREB            |Nombre de rebonds defensifs|                4|
|REB              |nombre de rebonds|               4|
|AST             |nombre d'assists|                3|
|STL              |nombre de steals|               1|
|BLK             |nombre de blocks|                0|
|TO              |nombre de pertes de balle|                1|
|PF              |nombre de fautes|                0|
|PTS              |nombre de points|              33|
|PLUS_MINUS      |Differentiel de points du joueur|              -22|

___

<br>

### Players.csv

|nom de la colonne|Description|Exemple|
|---|---|---|
|PLAYER_NAME  |nom du joueur|  Royce O'Neale|
|TEAM_ID      |id de sa team|     1610612762|
|PLAYER_ID       |id du joueur|     1626220|
|SEASON         |saison|         2019|


---

<br>

### ranking.csv

|nom de la colonne|Description|Exemple|
|---|---|---|
|TEAM_ID     |id de la team|     1610612762|
|LEAGUE_ID       |id de la league (tous la même)|          0|
|SEASON_ID       |id de la saison|      22020|
|STANDINGSDATE  |Date du classement|  2021-05-26|
|CONFERENCE       |Conférence|      West|
|TEAM           |Equipe|        Utah|
|G             |Nombre de matchs joués|           72|
|W            |Nombre de matchs gagnés|            52|
|L            |Nombre de matchs perdus|            20|
|W_PCT         |Pourcentage de matchs gagnés|        0.722|
|HOME_RECORD       |Record de matchs gagnés/perdus à domicile|     31-5|
|ROAD_RECORD       |Record de matchs gagnés/perdus à l'exterieur|    21-15|
|RETURNTOPLAY      |???|      NaN|


---

<br>

### teams.csv

|nom de la colonne|Description|Exemple|
|---|---|---|
|LEAGUE_ID             |id de la league (la même pour tous)|               0|
|TEAM_ID            |id de l'équipe|         1610612737|
|MIN_YEAR            |?|              1949|
|MAX_YEAR              |?|            2019|
|ABBREVIATION          |abréviation|             ATL|
|NICKNAME              |pseudo|           Hawks|
|YEARFOUNDED           |année de création|            1949|
|CITY             |ville|              Atlanta|
|ARENA          |nom du stade|       State Farm Arena|
|ARENACAPACITY           |capacité du stade|         18729|
|OWNER            |Propriétaire|         Tony Ressler|
|GENERALMANAGER      |Directeur|    Travis Schlenk|
|HEADCOACH          |Coach|       Lloyd Pierce|
|DLEAGUEAFFILIATION    |?|   Erie Bayhawks|


---