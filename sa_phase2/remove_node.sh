#!/bin/bash
cd /root/sa;
ansible-playbook -i inventory/remove_node.py remove_uge_client.yml -vv
