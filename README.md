# dnssec-algs-json
A script to take the IANA registry of DNSSEC algorithms and make it available as JSON

The IANA registry of DNSSEC algorithm numbers is available at:

http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml

However, the actual table of DNSSEC algorithm number is not easily available in a form that developers can easily check, such as a JSON interface.

The table _is_ available as a CSV file:

http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers-1.csv

This script is will convert that CSV into JSON.

Fields in the table are:

['Number', 'Description', 'Mnemonic', 'ZoneSigning', 'Trans.Sec.', 'Reference']

