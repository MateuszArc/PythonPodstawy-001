q = "THE EYES"
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
q = "a gentleman"
print(q[3], q[6], q[7], q[2], q[0], q[4], q[5], q[1], q[8])
q = "THE MORSE CODE"
print(q[1], q[2], q[6], q[13], q[10], q[11], q[4], q[13], q[12], q[5], q[0], q[7])

line = 'Program "Kropka nad i"nadamy o: 22:00'
time = line[30:36]
print(time)
tmp = line[0:8]
title = line[8:22]
print(title, time)

line = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time = line[39:45]
print(time)
tmp = line[0:8]
title = line[8:30]
print(title, time)