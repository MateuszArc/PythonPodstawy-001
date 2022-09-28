hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(3, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles.insert(0, ' ENJOY THE SILENCE')

hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
hitsToRead.pop(0)
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead.index('WISH YOU WERE HERE'))
print(hitsToRead.index('RIDERS ON THE STORM'))
hitsToRead.clear()
print(hitsToRead)