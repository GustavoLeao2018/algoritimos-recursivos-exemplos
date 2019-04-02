#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fibonacci(numero):
	if numero <= 1:
		return numero
	else:
		return(fibonacci(numero-1)+fibonacci(numero-2))

for i in range(0, 50):
	print(fibonacci(i))

