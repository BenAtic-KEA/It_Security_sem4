import hashlib
from passlib.hash import sha512_crypt

## Crypted password

## $6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0

salt = 'penguins'
password = '$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0'
initRounds = 1000
digits = 1000
roundsLoop = True
rounds = initRounds

while(roundsLoop):
    for x in range(digits):
        if x < 10:
            x = '00' + str(x)
        elif x < 100 and x >= 10:
            x = '0' + str(x)
        elif x == 1000:
            x = '000'
        else:
            x = str(x)
        currenthash = sha512_crypt.using(salt=salt, rounds=rounds).hash(x)
        if password == currenthash:
            print("password is = " + x)
            print(currenthash)
            roundsLoop = False
            break
        else:
            print('its not: ' + str(x) + ' with ' + str(rounds) + ' rounds') 
    rounds = rounds + initRounds
    
## password is = 479

