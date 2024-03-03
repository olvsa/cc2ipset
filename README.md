# cc2ipset<br />
Creates ipset shell script from an country's IP addresses from RIPE database.<br />
Supports both of IPv4 and IPv6.<br />
<br />
Usage:  ./cc2ipset.py <two letters country code> <.{/CC_ipvX.ipset}><br />
<br />
CC_ipv4.ipset:<br />
ipset flush ipv4_CC<br />
ipset x ipv4_CC<br />
ipset n ipv4_CC hash:net hashsize 16384 maxelem 262144<br />
ipset add ipv4_CC A1.B1.C1.D1/E1<br />
ipset add ipv4_CC A2.B2.C2.D2/E2<br />
<br />
CC_ipv6.ipset:<br />
ipset flush ipv6_CC<br />
ipset x ipv6_CC<br />
ipset n ipv6_CC hash:net hashsize 16384 maxelem 262144 family inet6<br />
ipset add ipv6_CC A1::/B1<br />
ipset add ipv6_CC A2::/B2<br />
