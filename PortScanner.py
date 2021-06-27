import socket
from IPy import IP

def scan(target, timeout, firstport, lastport):
	checked_ip = check_ip(target)
	print('\n [ -> Scanning Target: ' + str(target) + ' ]')
	for port in range(firstport, lastport+1):
		try:
			s = socket.socket()
			s.settimeout(float(timeout))
			s.connect((target, port))
			try:
				banner = get_banner(s)
				print('[+] Open port ' + str(port) + ':' + str(banner))
			except:
				print('[+] Port ' + str(port) + ' is open')
		except:
			if input_showclosed == 'y':
				print('[-] Port ' + str(port) + ' is closed')
			else:
				pass

def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(socket):
	return socket.recv(1024)

if __name__ == "__main__":
	# Settings
	print('----Settings----')
	input_ips = input('[>] Target/s IP/Host (split multiple targets with ","): ')
	input_firstport = input('[>] Enter the first port that you want to scan: ')
	input_lastport = input('[>] Enter the last port that you want to scan: ')
	### Check the ports
	if int(input_firstport) < int(input_lastport):
		try:
			int(input_firstport)
			int(input_lastport)
		except:
			print('[!] Error, invalid port numbers')
			exit()
	else:
		print('[!] Error, invalid port numbers')
		exit()

	input_timeout = input('[>] Timeout: ')
	try:
		float(input_timeout)
	except:
		print('[!] Error, invalid timeout')
	input_showclosed = input('[>] Display closed ports (y/n): ')

	if input_showclosed != 'y' and input_showclosed != 'n':
		print('[!] Error, invalid input')
		exit()

	# check if the user specified multiple targets
	if ',' in input_ips:
		for ip_addr in input_ips.split(','):
			scan(ip_addr.strip(' '), input_timeout, int(input_firstport), int(input_lastport))
	else:
		scan(input_ips, input_timeout, int(input_firstport), int(input_lastport))
