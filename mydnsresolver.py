import sys
import dns.resolver

# Function to lookup DNS name
def nslookup(domain_name, my_type):
    DNS_found = True
    upperType = my_type.upper()
    resolver = dns.resolver.Resolver()

    if upperType == "NS":
        try:
            results = resolver.resolve(domain_name, upperType)
        except dns.resolver.NXDOMAIN:
            DNS_found = False

    elif upperType == "MX":
        try:
            results = resolver.resolve(domain_name, upperType)
        except dns.resolver.NXDOMAIN:
            DNS_found = False

    else:
        upperType = "A"
        try:
            results = resolver.resolve(domain_name, upperType)
        except dns.resolver.NXDOMAIN:
            DNS_found = False
    
    if(DNS_found):
        print('Looking up ' + domain_name + ' with type -' + upperType)
        print('Results:\n')
        for result in results:
            print(result)
        print('')
    else:
        print('Non-existant Domain Name')

domain_name = sys.argv[1]

if(len(sys.argv) > 2):
    my_type = sys.argv[2]
else: my_type = "A"

results = nslookup(domain_name, my_type)