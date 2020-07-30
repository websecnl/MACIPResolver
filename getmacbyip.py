import subprocess
mac = raw_input("Mac Adres: ")
cmd = 'arp -a | findstr '+str(mac)
returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
parse=str(returned_output).split(' ',1)
ip=parse[1].split(' ')
print("IP: " + ip[1])
