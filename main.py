# import niezbednych bibliotek
from requests_html import HTMLSession
import datetime
import mysql.connector

# zmienna not_wielokrotne ma za zadanie korygowanie adresu linku w przypadku notowania z wielokrotną numeracją

not_wielokrotne = 0

session = HTMLSession()

# laczenie z baza danych

mydb = mysql.connector.connect(
    host="localhost",
    user="python",
    password="python",
    database="lista_portfolio"
)

mycursor = mydb.cursor()


def pobieranie(numer):

    global not_wielokrotne
    numer = numer + 1 + not_wielokrotne
    url = 'https://www.lp3.pl/notowanie/'+str(numer)

    r = session.get(url)

# skrypt ma za zadnie wyeliminowanie ze strony tabeli z outsiderami - nie można było tego zrobić na elementach css
# ze względu na identyczne formatowanie jak w przypadku pozostałych tabel

    script = """
        () => {
        var element = document.getElementById("outsiders");
        if (element) {
        element.parentNode.removeChild(element);}
        }
    """

    r.html.render(sleep=2, script=script)

# notowanie_text zawiera opis danego notowania i zawiera m.in. datę i numer notowania
# zmienna notowanie zawiera numer notowania
# zmienna data_notowania zawiera date notowania

    notowanie_text = r.html.find('.clearfix.current_score')
    pozycja = r.html.find('.numberCircle')
    wykonawca = r.html.find('.song_performer')
    tytul = r.html.find('.song_title')

# w parsowanej witrynie brakuje kilku notowań albo pojawia się błąd strony - poniżej obsługa tego błędu

    try:
        notowanie = notowanie_text[0].text[10:notowanie_text[0].text.find(',')]
    except:
        return print('Błąd w pobieraniu danych w notowaniu nr ', numer)

    not_wielokrotne += notowanie.count('/')

# dlaczego taka skomplikowana formula ponizej? najpierw uzylem do znalezienia drugiego przecinka w tekscie rfind(),
# ale potem znalazlo sie dwoje prowadzacych a wiec kolejny przecinek w tekscie

    data_str = notowanie_text[0].text[notowanie_text[0].text.find('dnia')+5:notowanie_text[0].text.find(',', notowanie_text[0].text.find('dnia')+5, notowanie_text[0].text.find('dnia')+20)]
    data_str_obj = datetime.datetime.strptime(data_str, '%d.%m.%Y')
    data_notowania = data_str_obj.date()

# zmienna zakres ma za zadanie ograniczyc ilosc rekordow ze wzgledu ze na stronie znajduja sie rowniez
# informacje na temat utworow ktore wypadly z listy

    for i in range(len(pozycja)):
        mycursor.execute("INSERT INTO lp3 (pozycja, tytul, wykonawca, notowanie, data_notowania) VALUES (%s, %s, %s, %s, %s)", (int(pozycja[i].text), tytul[i].text, wykonawca[i].text, notowanie, data_notowania))
        mydb.commit()

    return print('Notowanie nr: ', notowanie, ' zostało poprawnie załadowane')


for n in range(2000):
    pobieranie(n)

mydb.close()
