# dnssec-algs-json
A script to take the IANA registry of DNSSEC algorithms and make it available as JSON.

The IANA registry of DNSSEC algorithm numbers is available at:

http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml

However, the actual table of DNSSEC algorithm numbers is not easily available in a form that developers can easily check, such as a JSON interface.

The IANA table _is_ available as a CSV file:

http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers-1.csv

This script will convert that CSV into JSON.

Fields in the IANA table are:

['Number', 'Description', 'Mnemonic', 'ZoneSigning', 'Trans.Sec.', 'Reference']

This script creates a JSON object that is a list of dictionary objects.  It only outputs the following fields:

['Number', 'Description', 'Mnemonic']

As of 18 July 2015, the output of the script is as follows:

----

```
[
{
    "Description": "RSA/MD5 (deprecated, see 5)",
    "Mnemonic": "RSAMD5",
    "Number": "1"
},
{
    "Description": "Diffie-Hellman",
    "Mnemonic": "DH",
    "Number": "2"
},
{
    "Description": "DSA/SHA1",
    "Mnemonic": "DSA",
    "Number": "3"
},
{
    "Description": "RSA/SHA-1",
    "Mnemonic": "RSASHA1",
    "Number": "5"
},
{
    "Description": "DSA-NSEC3-SHA1",
    "Mnemonic": "DSA-NSEC3-SHA1",
    "Number": "6"
},
{
    "Description": "RSASHA1-NSEC3-SHA1",
    "Mnemonic": "RSASHA1-NSEC3-SHA1",
    "Number": "7"
},
{
    "Description": "RSA/SHA-256",
    "Mnemonic": "RSASHA256",
    "Number": "8"
},
{
    "Description": "RSA/SHA-512",
    "Mnemonic": "RSASHA512",
    "Number": "10"
},
{
    "Description": "GOST R 34.10-2001",
    "Mnemonic": "ECC-GOST",
    "Number": "12"
},
{
    "Description": "ECDSA Curve P-256 with SHA-256",
    "Mnemonic": "ECDSAP256SHA256",
    "Number": "13"
},
{
    "Description": "ECDSA Curve P-384 with SHA-384",
    "Mnemonic": "ECDSAP384SHA384",
    "Number": "14"
},
{
    "Description": "Reserved for Indirect Keys",
    "Mnemonic": "INDIRECT",
    "Number": "252"
},
{
    "Description": "private algorithm",
    "Mnemonic": "PRIVATEDNS",
    "Number": "253"
},
{
    "Description": "private algorithm OID",
    "Mnemonic": "PRIVATEOID",
    "Number": "254"
},
]
```