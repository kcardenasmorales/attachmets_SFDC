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
	records = sf.query("SELECT Id, Name,BodyLength,Body,ParentId FROM Attachment WHERE id='00Pm000000AENmQ'")
	records = records['records']
	attributes = records[0]
 
	print (attributes['Id'])
	print (attributes['Body'])
	print (attributes['ParentId'])
	# url = "https://cs20.salesforce.com/services/data/v38.0/sobjects/Attachment/00Pm000000AENmQEAX/Body"
	response = requests.get('https://cs20.salesforce.com/'+attributes['Body'],
	    headers = { 'Content-Type': 'pdf', 'Authorization': 'Bearer '+ sessionId }
	)

	# Configurar ftp y guardar archivos en el ftp
	data = base64.encodestring(response.content)
	os.chdir("C:\Python34\CargaDocumentosAllianz_COL")
	with open(os.path.expanduser('pruebaSFAtt4.pdf'),'wb') as output:
	 	output.write(base64.decodestring(data))
	 	output.close()
