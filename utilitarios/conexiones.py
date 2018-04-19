
from ftplib import FTP,FTP_TLS
from salesforce_simple import Salesforce

def conectaSalesforce():
    sf = Salesforce(username=os.environ["USERNAME_SALESFORCE"], 
				password=os.environ['PASSWORD_SALESFORCE'], 
				security_token=os.environ['TOKEN_SALESFORCE'],
				sandbox=True)
    return sf;

def conectaFtpPort():
	host = os.environ["HOST_FTP"]
	port = os.environ["PORT_FTP"]
	user = os.environ["USER_FTP"]
	pswd = os.environ["PSWD_FTP"]

	tp = FTP_TLS()
	tp.connect(host,ast.literal_eval(port),-999)
	tp.login(user,pswd)
	tp.prot_p()
	tp.dir()
	print (tp)


def conectarFtp():
	host = os.environ["HOST_FTP"]
	user = os.environ["USER_FTP"]
	pswd = os.environ["PSWD_FTP"]

	tp = FTP()
	tp.connect(host)
	tp.login(user,pswd)
	tp.dir()
	print (tp)
