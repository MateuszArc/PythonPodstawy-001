s = "A Python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message = 'document "Max Payne 3: headshot" was printed on printer: Xerro200'
print(message.find(':'))
print(message[message.find(':')+2:])

print(message[message.find('"')+1:])

tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])