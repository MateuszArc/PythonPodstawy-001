chanels = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV spot':700}
print(chanels)
print(chanels['Email'])
chanelsUpdate = {'Natural Traffic':520, 'News':600}
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
chanels.pop('Email')
print(chanels)