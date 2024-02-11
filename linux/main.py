import pandas as pd
import csv
import os
import sys
from matplotlib import pyplot as plt
if(os.path.exists(os.getcwd()+"//info.csv")):
	pass
else:
	with open(os.getcwd()+"//info.csv","x") as e:
		pass
	with open(os.getcwd()+"//info.csv","a") as s:
		filem=csv.writer(s)
		filem.writerow(['Account no','Account name','Mobile no','Aadhar no','Pan no','Type','Balance'])

def main_page():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("*"*36)
	print("\tPunjab National Bank")
	print("*"*36)
	print("1>> create account")
	print("2>> account entry")
	print("3>> update account")
	print("4>> delete account")
	print("5>> detailed statement")
	print("6>> account info")
	print("7>> graphical presentation")
	print("8>> generate report")
	print("9>> about")
	print("10>> exit")
	print()
	print()
	print()
	choice=input(">> ")
	if(choice=="1" or choice.lower()=="create account"):
		create_account()
	elif(choice=="2" or choice.lower()=="account entry"):
		account_entry()
	elif(choice=="3" or choice.lower()=="update account"):
		update()
	elif(choice=="4" or choice.lower()=="delete account"):
		delete()
	elif(choice=="5" or choice.lower()=="detailed statement"):
		statement()
	elif(choice=="6" or choice.lower()=="account info"):
		acc_info()
	elif(choice=="7" or choice.lower()=="graphical presentation"):
		plot_pres()
	elif(choice=="8" or choice.lower()=="generate report"):
		records()
	elif(choice=="9" or choice.lower()=="about"):
		about()
	elif(choice=="10" or choice.lower()=="exit"):
		exit()
	else:
		print()
		input("!! bad choice")
		main_page()
	

def records():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tReport")
	print("-"*36)
	df=pd.read_csv(os.getcwd()+"//info.csv")
	print(df)
	input("press enter to exit")
	main_page()

def statement():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tDetailed Statement")
	print("-"*36)
	lr=0
	accno5=input("Account no : ")
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			try:
				if(line[0]==accno5):
					ll1=line
					lr=1
				else:
					continue
			except:
				pass
	if(lr==0):
		print("!!account doesnt exist")
		input()
		main_page()
	else:
		print()
		print()
		print("Account no :\t",ll1[0])
		print("Account holder:\t",ll1[1])
		print("Mobile no :\t",ll1[2])
		print("Account type:\t",ll1[5])
		print("Balance :\t",ll1[6])
		df=pd.read_csv(os.getcwd()+"//acc_"+accno5+".csv",index_col=0)
		print()
		print(df)
		input("press enter to exit")
		main_page()
def delete():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tDelete Account")
	print("-"*36)
	ll=[]
	var_1=0
	accno4=input("Account no : ")
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			ll.append(line)
			try:
				if(line[0]==accno4):
					del ll[var_1]
					os.remove(os.getcwd()+"//acc_"+accno4+".csv")
				else:
					pass
			except:
				pass
			var_1+=1
	with open(os.getcwd()+"//info.csv","w") as fwrite:
			filew=csv.writer(fwrite)
			filew.writerows(ll)
	input("press enter to exit")
	main_page()

def plot_pres():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tGraphical presentation")
	print("-"*36)
	lr=0
	accno5=input("Account no : ")
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			try:
				if(line[0]==str(accno5)):
					ll1=line
					lr=1
				else:
					continue
			except:
				pass
	if(lr==0):
		print("!!account doesnt exist")
		input()
		main_page()
	else:
		print()
		print()
		print("Account no :\t",ll1[0])
		print("Account holder:\t",ll1[1])
		print("Mobile no :\t",ll1[2])
		print("Account type:\t",ll1[5])
		print("Balance :\t",ll1[6])
		df=pd.read_csv(os.getcwd()+"//acc_"+str(accno5)+".csv",index_col=0)
		print()
		plt.plot(df.index,df["Balance"])
		plt.title("Graphical presentation")
		plt.xlabel("Date")
		plt.ylabel("Balance")
		plt.show()
		input("press enter to exit")
		main_page()
	
	
def acc_info():
	lvr=0
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tAccount Info")
	print("-"*36)
	accn=input("Account no : ")
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			try:
				if(line[0]==accn):
					ll1=line
					lvr=1
				else:
					continue
			except:
				pass
	if(lvr==0):
		print("!!account doesnt exist")
		input()
		main_page()
	else:
		print()
		print()
		print("Account no :\t",ll1[0])
		print("Account holder:\t",ll1[1])
		print("Mobile no :\t",ll1[2])
		print("Aadhar no :\t",ll1[3])
		print("PAN no :\t",ll1[4])
		print("Account type:\t",ll1[5])
		print("Balance :\t",ll1[6])
		input("\n\n press enter to exit")
		main_page()

def update():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tUpdate Account")
	print("-"*36)
	accno3=int(input("Account no : "))
	print("1 >> account name")
	print("2 >> mobile no")
	print("3 >> aadhar no")
	print("4 >> pan no")
	print("5 >  none")
	opt=input(">> ")
	if(opt=="1" or opt=="account name"):
		s=1
	elif(opt=="2" or opt=="mobile no"):
		s=2
	elif(opt=="3" or opt=="aadhar no"):
		s=3
	elif(opt=="4" or opt=="pan no"):
		s=4
	elif(opt=="5" or opt=="none"):
		s=0
		input("press enter to exit")
		main_page()
	else:
		input("!! cannot be changed...")
		main_page()
	vwant=input(" New : ")
	l1=[]
	lvar=0
	var1=0
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			l1.append(line)
			try:
				if(str(line[0])==str(accno3)):
					l1[lvar][s]=vwant.upper()
					var1=1
				else:
					pass
			except:
				pass
			lvar+=1
		if(var1==0):
			print("!! Account doesnt exist...")
			input()
			main_page()
		else:
			pass
		with open(os.getcwd()+"//info.csv","w") as fwrite:
			filew=csv.writer(fwrite)
			filew.writerows(l1)
	input("press enter to exit")
	main_page()



def change(accno2,bal):
	l=[]
	lv=0
	with open(os.getcwd()+"//info.csv","r") as readf:
		filer=csv.reader(readf)
		for line in filer:
			l.append(line)
			try:
				if(str(line[0])==str(accno2)):
					l[lv][6]=bal
			except:
				pass
			lv+=1
		with open(os.getcwd()+"//info.csv","w") as fwrite:
			filew=csv.writer(fwrite)
			filew.writerows(l)


def create_account():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tCreate Account")
	print("-"*36)
	templ=[]
	#input taking....
	date=input("Date(dd-mm-yyyy) : ")
	accno=int(input("Account number: "))
	accname=input("Account holder's name: ")
	mobno=int(input("Mobile no: "))
	aadharno=int(input("Aadhar no: "))
	panno=input("pan no:")
	type=input("Account type(s/c) : ")
	if(type.lower()=="s"):
		type="SAVING"
	elif(type.lower()=="c"):
		type="CURRENT"
	else:
		input("!! No account type available..")
		create_account()
	initial=float(input("initial amount(INR) : "))
	#appending list
	templ.append(accno)
	templ.append(accname.upper())
	templ.append(mobno)
	templ.append(aadharno)
	templ.append(panno.upper())
	templ.append(type)
	templ.append(initial)
	#checking old records and entering record in csv
	templ1=[]
	lvar=0
	with open(os.getcwd()+"//info.csv","r") as filer:
		fileread=csv.reader(filer)
		for rows in fileread:
			try:
				templ1.append(rows[0])
			except:
				pass
		if(str(accno) in templ1):
			pass
		else:
			lvar=1
	if(lvar==0):
		print("!! same account number cannot be assigned")
		input()
		create_account()
	else:
		with open(os.getcwd()+'//info.csv', 'a') as info_file:
			file=csv.writer(info_file)
			file.writerow(templ)
			with open(os.getcwd()+'//acc_'+str(accno)+'.csv','x') as x:
					pass
			with open(os.getcwd()+'//acc_'+str(accno)+'.csv','a') as writef:
				writefile=csv.writer(writef)
				writefile.writerow(['Date','Particular','Debit','Credit','Balance'])
				writefile.writerow([date,"initial DEPOSIT",0.00,initial,initial])
		input("press enter to exit")
		main_page()

def exit():
	sys.exit()


def account_entry():
	if(os.name=='posix'):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\tAccount entry")
	print("-"*36)
	accno1=input("Account no : ")
	date=input("Date(dd-mm-yyyy) : ")
	particular=input("Particular : ")
	etype=input("Type(dr/cr) : ")
	amount=float(input("Amount : "))
	bal=0.0
	if(etype.upper()=="DR"):
		try:
		   if(os.path.exists(os.getcwd()+"//acc_"+str(accno1)+".csv")):
		   	with open(os.getcwd()+"//acc_"+str(accno1)+".csv","a") as filee:
		   		write_file=csv.writer(filee)
		   		with open(os.getcwd()+"//acc_"+str(accno1)+".csv","r") as filere:
		   			filer=csv.reader(filere)
		   			for rows in filer:
		   				try:
		   					bal=float(rows[4])
		   				except:
		   					pass
		   		write_file.writerow([date,particular.upper(),amount,0.0,str(bal-amount)])
		   		change(accno1,bal-amount)
		   else:
		   	input("account doesnot exists!!")
		   	main_page()
		except:
		    input("account doesnot exists!!")
		    main_page()
		
	elif(etype.upper()=="CR"):
		try:
		   if(os.path.exists(os.getcwd()+"//acc_"+str(accno1)+".csv")):
		   	with open(os.getcwd()+"//acc_"+str(accno1)+".csv","a") as filee:
		   		write_file=csv.writer(filee)
		   		with open(os.getcwd()+"//acc_"+str(accno1)+".csv","r") as filere:
		   			filer=csv.reader(filere)
		   			for rows in filer:
		   				try:
		   					bal=float(rows[4])
		   				except:
		   					pass
		   		write_file.writerow([date,particular.upper(),0.0,amount,str(bal+amount)])
		   		change(accno1,bal+amount)
		   else:
		   	input("account doesnot exists!!")
		   	main_page()
		except:
		    input("account doesnot exists!!")
		    main_page()
			
	else:
	   input("\tType doesnot exists!!")
	   account_entry()
	input("press enter to exit")
	main_page()

def about():
	if(os.name=="posix"):
		os.system("clear")
	else:
		os.system("cls")
	print("-"*36)
	print("\t About")
	print("-"*36)
	print("This is bank management system\n\n Created by : Deepanshu,Deepak and kunal \nof class : 12th B commerce of Navyug Public School\n\n This system is for entering data of customers of a bank\n This system is created according to the view of employee of that bank\n\n Thankyou for using this system...")
	print("This is bank management system\n\n Created by : Deepanshu Dixit\n\n This system is for entering data of customers of a bank\n This system is created according to the view of employee of that bank\n\n Thankyou for using this system...")
	print()
	input("press enter to exit")
	main_page()

main_page()