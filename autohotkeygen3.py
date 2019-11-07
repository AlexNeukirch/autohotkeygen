print("   _           _                        _                      ")
print("  /_\   _   _ | |_  ___    /\  /\ ___  | |_   /\ /\ ___  _   _ ") 
print(" //_\\\ | | | || __|/ _ \  / /_/ // _ \ | __| / //_// _ \| | | |") 
print("/  _  \| |_| || |_| (_) |/ __  /| (_) || |_ / __ \|  __/| |_| |") 
print("\_/ \_/ \__,_| \__|\___/ \/ /_/  \___/ _\__|\/  \/ \___| \__, |") 
print("  __ _   ___  _ __    ___  _ __  __ _ | |_  ___   _ __   |___/ ") 
print(" / _` | / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|        ") 
print("| (_| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |           ") 
print(" \__, | \___||_| |_| \___||_|   \__,_| \__|\___/ |_| ___  _  _ ")
print(" |___/                                       __   __/ _ \| || | ") 
print("                                             \ \ / / | | | || |_ ")
print("                                              \ V /| |_| |__   _| ")
print("                                               \_/  \___(_) |_|") 

content1 = []

print("Nazwa Hotkey")
name = raw_input()
print("Temat: ")
title = raw_input()
print("Customer's Product*:\n\n1. none\n2. Hosting Web\n3. Domain\n4. Domain Zone")
print("5. Email MXplan\n6. Email PRO\n7. Email exchange\n8. Inne...")
while True:
	try:	
		customerProduct1 = raw_input()
		customerProduct = "siema"
		if int(customerProduct1) == 1:
			customerProduct = "none"
			break
			
		elif int(customerProduct1) == 2:
			customerProduct = "hosting web"
			break
			
		elif int(customerProduct1) == 3:
			customerProduct = "domain"
			break
			
		elif int(customerProduct1) == 4:
			customerProduct = "domain zone"
			break
			
		elif int(customerProduct1) == 5:
			customerProduct = "email mxplan"
			break
			
		elif int(customerProduct1) == 6:
			customerProduct = "email pro"
			break

		elif int(customerProduct1) == 7:
			customerProduct = "email exchange"    
			break
			
		elif int(customerProduct1) == 8:
			 customerProduc = raw_input()
			 break

		else:
			print('Bledna wartosc')
	
	except ValueError:
		print('Bledna wartosc')

print("Typologia:\n\n1. forwarded to KeepBiz\n2. MultiSite changes\n3. DNS zone configuration\n4. Non OVH Request\n5. inna wartosc...")
while True:
	try:
		typologia1 = raw_input()
		typologia = "elo"
		if int(typologia1) == 1:
			typologia = "call SVI keepbiz"
			break

		elif int(typologia1) == 2:
			typologia = "multisite"
			break

		elif int(typologia1) == 3:
			typologia = "dns configuration"
			break

		elif int(typologia1) == 4:
			typologia = "lack of information"
			break

		elif int (typologia1) == 5:
			print("Wpisz typologie: ")
			typologia = raw_input()
			break
			
		else:
			print('Bledna wartosc')
			
	except ValueError:
		print('Bledna wartosc')

while True:
    
    print("Tresc: (pozostaw puste, aby zakonczyc)")
    content = raw_input()
    if content == "":
        break
    else:
        content1.append(content)

#name = str(input("Podaj nazwe Hotkeya: "))
#title = input("Podaj Temat: ")
#customerProduct = input("Customer's Product: ")
#typologia = input("Typologia: ")
#content = input("Tresc: ")

file = open("autohotkey.txt","w") 

file.write("::" + name + "1::\n\n")
file.write("Send, " + str(title) + "\n") 
file.write("Send, ^a^c^v\n")
file.write("Loop, 6 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, " + str(customerProduct) + "\n")
file.write("Loop, 5 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, Pol\n")
file.write("Loop, 19 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, " + str(typologia) + "\n")
file.write("Loop, 3 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, ^v{enter}" + "{enter}".join(content1) + "\n\n")
file.write("return\n\n")
file.write("::" + name + "2::\n") 
file.write("\n") 
file.write("Send, " + str(title) + "\n") 
file.write("Send, ^a^c^v\n")
file.write("Loop, 4 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, " + str(customerProduct) + "\n")
file.write("Loop, 5 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, Pol\n")
file.write("Loop, 19 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, " + str(typologia) + "\n")
file.write("Loop, 3 {\n")
file.write("Send, {tab}\n")
file.write("}\n")
file.write("Send, ^v{enter}" + "{enter}".join(content1) + "\n\n")
file.write("return")

file.close()

print('zapisano plik pomyslnie do autohotkey.txt')
print('\x1b[6;30;42m' + 'zapisano plik pomyslnie do autohotkey.txt' + '\x1b[0m')
