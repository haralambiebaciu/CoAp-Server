import xml.dom.minidom
import urllib
import urllib.request


def GetInfoValutar():
    def getText(nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc

    try:
        fp = urllib.request.urlopen("http://www.infovalutar.ro/curs.rss");
    except IOError:
        return -1

    buff = fp.read()
    fp.close()

    dom = xml.dom.minidom.parseString(buff)
    items = dom.getElementsByTagName("item")

    nfoVal = []

    for item in items:
        moneda = getText(item.getElementsByTagName("title")[0].childNodes)
        valoare = getText(item.getElementsByTagName("description")[0].childNodes)
        link = getText(item.getElementsByTagName("link")[0].childNodes)
        nfoVal.append((moneda, valoare, link))

    return nfoVal


test = GetInfoValutar()

if test == -1:
    print ("Eroare citire!")
else:
    for i in test:
        print ("%s = %s - %s" % i)

#
# <OUTPUT>
#
# USD = 2.5814   - http://www.infovalutar.ro/2006/12/7/USD.bnr
# EUR = 3.4295   - http://www.infovalutar.ro/2006/12/7/EUR.bnr
# XDR = 3.9125   - http://www.infovalutar.ro/2006/12/7/XDR.bnr
# XAU = 52.3017  - http://www.infovalutar.ro/2006/12/7/XAU.bnr
# TRY = 1.799    - http://www.infovalutar.ro/2006/12/7/TRY.bnr
# SEK = 0.3796   - http://www.infovalutar.ro/2006/12/7/SEK.bnr
# PLN = 0.8988   - http://www.infovalutar.ro/2006/12/7/PLN.bnr
# NOK = 0.4234   - http://www.infovalutar.ro/2006/12/7/NOK.bnr
# MDL = 0.2027   - http://www.infovalutar.ro/2006/12/7/MDL.bnr
# JPY = 2.2466   - http://www.infovalutar.ro/2006/12/7/JPY.bnr
# HUF = 0.013366 - http://www.infovalutar.ro/2006/12/7/HUF.bnr
# GBP = 5.0804   - http://www.infovalutar.ro/2006/12/7/GBP.bnr
# EGP = 0.4514   - http://www.infovalutar.ro/2006/12/7/EGP.bnr
# DKK = 0.4599   - http://www.infovalutar.ro/2006/12/7/DKK.bnr
# CZK = 0.1224   - http://www.infovalutar.ro/2006/12/7/CZK.bnr
# CHF = 2.1588   - http://www.infovalutar.ro/2006/12/7/CHF.bnr
# CAD = 2.2484   - http://www.infovalutar.ro/2006/12/7/CAD.bnr
# AUD = 2.0403   - http://www.infovalutar.ro/2006/12/7/AUD.bnr
#
# </OUTPUT>
#
