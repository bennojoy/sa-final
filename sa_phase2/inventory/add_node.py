#!/bin/env python
import os
import sys
import json
from pprint import pprint

def getHost(fname="inventory/autoscale_pool"):
	f = open(fname)
	lines = f.readlines()
	hostname = lines.pop().strip()
	f.close()
	f = open(fname, 'w')
	f.writelines(lines)
	f.close()
	return hostname

if len(sys.argv) == 2 and (sys.argv[1] == '--list'):	
	filename="inventory/petrol_hosts"
	groups = {}
	group_name = None
	fh = open(filename)
	lines = fh.readlines()
	fh.close()
	count = 0
	for line in lines:
		count += 1
		if line.startswith("["):
			hosts = []
			group_name = line.split("#")[0].replace("[","").replace("]","").strip()
			if group_name.find(":") != -1:
				group_name = None
				continue
			group_hosts = { "hosts": hosts}
			groups[group_name] = group_hosts
			if group_name == "clients":
				hname = getHost(fname="inventory/autoscale_pool")
				hosts.append(hname)
				hname = hname + "\n"
				lines.insert(count + 1, hname) 
			continue
		if line.strip() == '' or group_name == "clients" or group_name == None:
                	continue
		hosts.append(line.strip())
			
	f = open(filename, 'w')
        f.writelines(lines)
        f.close()
	print json.dumps(groups)
	sys.exit(0)			

elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):
    results = {}
    print json.dumps(results)
    sys.exit(0)
	
