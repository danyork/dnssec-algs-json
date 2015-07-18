import csv
import json

f = open('dns-sec-alg-numbers-1.csv','r')
output = open('dns-sec-alg-numbers.json','w')

algs = csv.DictReader(f)
print "["
for row in algs:
    if row['Description'] not in ['Reserved','Unassigned']:
        newrow = {k:v for k,v in row.items() if k in ['Number','Mnemonic','Description']}
        print json.dumps(newrow,sort_keys=True,indent=4, separators=(',', ': ')) + ","
    
print "]"
    
#    print json.dumps([row['Number'],row['Mnemonic'],row['Description']])
    
#    print (row['Number'] + ' ' + row['Mnemonic'] + ' ' + row['Description'])

#print json.dump(algs,output)