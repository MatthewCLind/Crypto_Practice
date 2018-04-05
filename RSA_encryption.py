import sys


def extract_info(flag):
    i = sys.argv.index(flag) + 1
    return sys.argv[i]


if '-pq' not in sys.argv:
    print ('You must provide PQ using the -pq flag')
    sys.exit(1)

if '--key' not in sys.argv:
    print ('You must provide your key using the --key flag')
    sys.exit(1)

if '-m' not in sys.argv:
    print ('You must provide a message using the -m flag')
    sys.exit(1)

pq = int(extract_info('-pq'))
key = int(extract_info('--key'))
m = int(extract_info('-m'))

exp = m ** key
encrypted_message = exp % pq
print('Your de/encrypted message is: ' + str(encrypted_message))
