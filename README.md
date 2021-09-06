# WebScraping
Pierwszy z plików w ramach skromnego portfolio służacego do znalezienia posady Juniora.

Zadaniem programu jest scraping witryny https://www.lp3.pl/ w celu pobrania danych na temat wszytskich notowań Listy Przebojów Programu 3.
Notowania mają zostać umieszczone w bazie danych (mySQL) w prostej tabeli o nazwie lp3 i kolumnach: 
pozycja (int), tytul (varchar255), wykonawca(varchar255), notowanie (varchar 255), data_notowania (date).

Do sprawdzenie kodu można stworzyć sobie taką tabelę we własnej bazie, ew. lekko zmodyfikować kod i zobaczyć wyniki po prostu na konsoli lub wrzucić do pliku csv.
Do pętli pobierającej podano wartość 2 000, gdyż mniej więcej tyle odbyło się notowań.

Baza ta ma dalej posłużyć do stworzenia kolejnego programu do portfolio związnego z utworzeniem dashboardu z wizualiacją danych.

Z racji tego, że witryna posiada pewne luki związane notowaniami, a sam kod strony posiada nadmiarowe informacje (outsiders) 
zastosowano kilka mechanizmów korygujących i zabezpieczających przed błędami.
