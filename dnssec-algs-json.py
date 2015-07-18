# A short program to read the IANA registry of DNSSEC algorithm numbers found at
# http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers-1.csv
# and print it out as a JSON object.
#
# Note that the JSON file has two primary differences from the IANA registry:
# 1. Only 3 of the 6 fields are included: 'Number','Mnemonic' and 'Description'.
# 2. Rows are removed if 'Description' is set to 'Reserved' or 'Unassigned'.
#
# Created by Dan York - dyork@lodestar2.com
# Comments, feedback and pull requests are welcome.
# Repository: https://github.com/danyork/dnssec-algs-json
#

import csv
import json
import urllib2

#f = open('dns-sec-alg-numbers-1.csv','r')

try:
    f = urllib2.urlopen('http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers-1.csv')
except: 
    print("Unable to connect to IANA server.")
    exit()

algs = csv.DictReader(f)
print "["
for row in algs:
    if row['Description'] not in ['Reserved','Unassigned']:
        newrow = {k:v for k,v in row.items() if k in ['Number','Mnemonic','Description']}
        print json.dumps(newrow,sort_keys=True,indent=4, separators=(',', ': ')) + ","
    
print "]"
    