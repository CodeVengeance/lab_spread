# lab_spread
from subprocess import call
import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for i in range(5,7):
  for j in range(2,255):
	  try:
		  ip='10.11.'+str(i)+'.'+str(j)
    #ssh.connect('ip','port','user','pass')
		  print "connecting to "+ip
		  ssh.connect(ip,22,'root','fedora')
    # SCPCLient takes a paramiko transport as its only argument
		  scp = SCPClient(ssh.get_transport())
		  scp.put('test2.txt',remote_path='/usr/local/bin')
#scp.get('test2.txt')
		  print "file transfered to  "+ip
		  scp.close()

	  except:
		  print "exception raised for "+ip
