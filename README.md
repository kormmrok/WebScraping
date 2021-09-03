# WebScraping
Pierwszy z plików w ramach skromnego portfolio służacego do znalezienia posady Juniora.

Zadaniem programu jest scraping witryny https://www.lp3.pl/ w celu pobrania danych na temat wszytskich notowań Listy Przebojów Programu 3.
Notowania mają zostać umieszczone w bazie danych (mySQL) w prostej tabeli o kolumnach: pozycja, tytul, wykonawca, notowanie, data_notowania.

Baza ta ma dalej posłużyć do stworzenia kolejnego programu do portfolio związny z utworzeniem dashboardu z wizualiacją danych.

Z racji tego, że witryna posiada pewne luki związane notowaniami, a sam kod strony posiada nadmiarowe informacje (outsiders) zastosowano kilka mechanizmów korygujących i zabezpieczających przed błędami.
