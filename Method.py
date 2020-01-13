import urllib
import re
import urllib.request


def GetCursValutar(y, m, d, moneda):
    try:
        fp = urllib.request.urlopen("http://www.infovalutar.ro/" + y + "/" + m
                            + "/" + d + "/" + moneda + ".bnr");
    except IOError:
        return -1

    curs = fp.read()
    fp.close()

    if re.compile(("^not.*$").encode('utf-8')).search(curs):
        return -2

    return curs


def GetCursValutarForToday(moneda):
    try:
        fp = urllib.request.urlopen("http://www.infovalutar.ro/azi/" + moneda + ".bnr");
    except IOError:
        return -1

    curs = fp.read()
    fp.close()

    return curs


y = "2020"
m = "1"
d = "13"
moneda = "XDR"
ex1 = GetCursValutar(y, m, d, moneda).decode()

if ex1 == -1:
    print("Eroare citire!")
elif ex1 == -2:
    print("Valoarea nu a fost gasita pentru %s din %s/%s/%s " % (moneda, d, m, y))
else:
    print("Cursul valutar pentru %s din %s/%s/%s este : %s lei" % (moneda, d, m, y, ex1))

y = "2018"
m = "11"
d = "24"
moneda = "EUR"

ex2 = GetCursValutar(y, m, d, moneda).decode()
if ex2 == -1:
    print("Eroare citire!")
elif ex2 == -2:
    print("Valoarea nu a fost gasita pentru %s din %s/%s/%s " % (moneda, d, m, y))
else:
    print("Cursul valutar pentru %s din %s/%s/%s este : %s lei" % (moneda, d, m, y, ex2))

moneda = "EUR"

ex3 = GetCursValutarForToday(moneda).decode()
if ex3 == -1:
    print("Eroare citire!")
else:
    print("Cursul valutar de astazi pentru %s este : %s lei" % (moneda, ex3))

#
# <OUTPUT>
#
# Cursul valutar pentru EUR din 12/10/2005 este 3.5906
# Valoarea nu a fost gasita pentru EUR din 12/10/2008
# Cursul valutar de astazi pentru USD este 2.5814
#
# </OUTPUT>
#

