CountryLeaders = {'PL':'Duda', 'US':'Trump'}

#print(CountryLeaders['US'])
CountryLeaders['DE'] = 'Merkel'

#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())

#print(CountryLeaders.popitem())

#print(CountryLeaders.setdefault('FR', 'Macron'))

#print(CountryLeaders.get('RU'))

NewLeadres = {'RU':'Putin', 'DE':'Shulz'}
print(NewLeadres)
print(CountryLeaders.update(NewLeadres))
print(CountryLeaders)