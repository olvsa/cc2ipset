#!/usr/bin/env python3
# coding: utf-8
# version: 0.2
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network, ip_address, summarize_address_range
import sys
import os
import json
import requests
from aggregate_prefixes import aggregate_prefixes

try:
 country_code = sys.argv[1].upper()
 ipset_path = sys.argv[2]
except:
 print('Usage: ', sys.argv[0], ' <two letters country code> </srv/cc{/CC_ipvX.ipset}>')
 exit()

networks4 = []
networks6 = []
filepath = os.path.dirname(sys.argv[0])
result4 = ipset_path + '/' + country_code + '_ipv4.ipset'
result6 = ipset_path + '/' + country_code + '_ipv6.ipset'
url = 'https://stat.ripe.net/data/country-resource-list/data.json?resource=' + country_code
rq = requests.get(url)
if rq.status_code != 200:
 print(str(rq.status_code) + ': ' + str(rq), file=sys.stderr)
 exit(rq.status_code)
ripe_ip4 = json.loads(rq.content)['data']['resources']['ipv4']
ripe_ip6 = json.loads(rq.content)['data']['resources']['ipv6']

out_file4 = open(result4, 'w')
out_file6 = open(result6, 'w')

for ipX in ripe_ip4:
 try:
  print('IPv4:' + str(ipX))
  if ipX.find('-') > -1:
   ips = ipX.split('-')
   ipaddr = list(summarize_address_range(IPv4Address(ips[0]), IPv4Address(ips[1])))
  else:
   ipaddr = [IPv4Network(ipX)]
   networks4.extend(ipaddr)
 except:
  print('invalid IPv4: ' + str(ipX), file=sys.stderr)
  pass

for ipX in ripe_ip6:
 try:
  print('IPv6:' + str(ipX))
  if ipX.find('-') > -1:
   ips = ipX.split('-')
   ipaddr = list(summarize_address_range(IPv6Address(ips[0]), IPv6Address(ips[1])))
  else:
   ipaddr = [IPv6Network(ipX)]
   networks6.extend(ipaddr)
 except:
  print('invalid IPv6: ' + str(ipX), file=sys.stderr)
  pass

print('ipset flush ipv4_' + country_code, file=out_file4)
print('ipset x ipv4_' + country_code, file=out_file4)
print('ipset n ipv4_' + country_code + ' hash:net hashsize 16384 maxelem 262144', file=out_file4)
for line in list(aggregate_prefixes(networks4)):
 print('ipset add ipv4_' + country_code + ' ' + str(line), file=out_file4)

print('ipset flush ipv6_' + country_code, file=out_file6)
print('ipset x ipv6_' + country_code, file=out_file6)
print('ipset n ipv6_' + country_code + ' hash:net hashsize 16384 maxelem 262144 family inet6', file=out_file6)
for line in list(aggregate_prefixes(networks6)):
 print('ipset add ipv6_' + country_code + ' ' + str(line), file=out_file6)
