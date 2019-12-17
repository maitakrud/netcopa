#!/usr/bin/env python

import sys
from ciscoconfparse import CiscoConfParse

args=len(sys.argv) - 1

if (args == 0):
    print("Usage: " + str(sys.argv[0]) + " configurationfile")
    sys.exit(1)

f=sys.argv[1]
print(f)
try:
    infile = open(f, 'r')
    parser=CiscoConfParse(infile)
    outfile=open('vrf.cfg', 'w')
    for vrf in parser.find_objects(r"^ip vrf"):
        outfile.write(vrf.text)
        for line in vrf.children:
            outfile.write(line.text)
    outfile.close()

    outfile=open('svi.cfg', 'w')
    for svi in parser.find_objects(r"^interface Vlan"):
        outfile.write(svi.text)
        for line in svi.children:
            outfile.write(line.text)
    outfile.close()
    
    outfile=open('routes.cfg', 'w')
    for route in parser.find_objects(r"^ip route"):
        outfile.write(route.text)
        for line in route.children:
            outfile.write(line.text)
    outfile.close()

    outfile=open('std-acl.cfg', 'w')
    for acl in parser.find_objects(r"^access-list \d+"):
        outfile.write(acl.text)
    outfile.close()

    outfile=open('ext-acl.cfg', 'w')
    for acl in parser.find_objects(r"^ip access-list"):
        outfile.write(acl.text)
        for line in acl.children:
            outfile.write(line.text)
    outfile.close()

    outfile=open('route-map.cfg', 'w')
    for routemap in parser.find_objects(r"^route-map "):
        outfile.write(routemap.text)
        for line in routemap.children:
            outfile.write(line.text)
    outfile.close()

    infile.close()
except:
    print("Couldn't open file " + str(f))
    sys.exit(1)