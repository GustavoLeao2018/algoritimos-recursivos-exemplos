#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fatorial(numero):
	if numero == 0:
		return 1
	elif numero == 1:
		return numero
	else:
		return(numero * fatorial(numero-1))

for i in range(0, 55):
	print(fatorial(i))