#!/usr/bin/python3

with open('network_file_no1.net', 'r') as file:
    data = file.read().replace('\n', ' | ')

print(data[0:1000])
