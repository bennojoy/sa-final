#!/bin/bash
cd /root/sa;
ansible-playbook -i inventory/add_node.py add_uge_client.yml -e "gname=petrol gmond_port=8649" -vv
