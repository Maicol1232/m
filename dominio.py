import requests
from os import path
import argparse
import sys
import urllib

parser = argparse.ArgumentParser() 
parser.add_argument('-t','--tarjet',help='indica el dominio de la victima')
parser=parser.parse_args()

def main():
	if parser.tarjet:
		if path.exists('dominio.txt'):
			wordlist=open('dominio.txt ','r')
			wordlist=wordlist.read().split('/n')
		
			for dominio in wordlist:
				url	= "http://"+dominio+"."+parser.tarjet  																																																																																																																
			try:
				requests.get(url)

			except requests .ConnectionError:
				pass
			
			else:
				print("(+) dominio encontrado: "+url )

			for dominio in wordlist:
				url	= "https://"+dominio+"."+parser.tarjet  																																																																																																																
			try:
				requests.get(url)

			except requests.ConnectionError:
				pass
			
			else:
				print("(+) dominio encontrado: "+url )

	else:
		print("(-)ingresa un dominio")


if __name__ == '__main__':
	try:
		main()
	
	except KeyboardInterrupt:
		sys.exit()

				
