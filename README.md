# cc2ipset
Creates ipset shell script from an country's IP addresses from RIPE database.
Supports both of IPv4 and IPv6.

Usage:  ./cc2ipset.py <two letters country code> <.{/CC_ipvX.ipset}>

CC_ipv4.ipset:
ipset flush ipv4_CC

ipset x ipv4_CC

ipset n ipv4_CC hash:net hashsize 16384 maxelem 262144

ipset add ipv4_CC A1.B1.C1.D1/E1
ipset add ipv4_CC A2.B2.C2.D2/E2

CC_ipv6.ipset:
ipset flush ipv6_CC
ipset x ipv6_CC
ipset n ipv6_CC hash:net hashsize 16384 maxelem 262144 family inet6
ipset add ipv6_CC A1::/B1
ipset add ipv6_CC A2::/B2
