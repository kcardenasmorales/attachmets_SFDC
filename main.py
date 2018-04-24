import requests
import os
import json
import base64
import ast
import binascii
from utilitarios import *
from ftplib import FTP
from simple_salesforce import Salesforce


def obtenerdocumentos():
	sf = conectaSalesforce();
	sessionId = sf.session_id
	print('sf: ' + str(sessionId))
	records = sf.query("SELECT Id, Name,BodyLength,Body,ParentId FROM Attachment WHERE id='{id}'")
	records = records['records']
	attributes = records[0]
 
	print (attributes['Id'])
	print (attributes['Body'])
	print (attributes['ParentId'])
	# url = "https://{ambiente}.salesforce.com/services/data/v38.0/sobjects/Attachment/{id}/Body"
	response = requests.get('https://{ambiente}.salesforce.com/'+attributes['Body'],
	    headers = { 'Content-Type': 'pdf', 'Authorization': 'Bearer '+ sessionId }
	)

	# Configurar ftp y guardar archivos en el ftp
	data = base64.encodestring(response.content)
	os.chdir("{dirlocal}")
	with open(os.path.expanduser('pruebaSFAtt4.pdf'),'wb') as output:
	 	output.write(base64.decodestring(data))
	 	output.close()
