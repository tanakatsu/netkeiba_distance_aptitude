# encoding: utf-8
import netkeiba

netkeiba = netkeiba.Netkeiba()
name = u'アドマイヤフライト'
html = netkeiba.searchHorseByName(name)
factor = netkeiba.getHorseDistanceAptitude(html)
print name, factor
