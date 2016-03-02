import urllib.request
import os
import re
import time
import sys
import csv
import xlrd
import subprocess

class Libraries(object):
	#Some websites will keep blocking or will throw different page than live url so we can use any of this function to bypass the blockages
	while True:
		try:

			def wget(self,url):
				self.data = os.popen('wget -qO- %s'% url).read()
				return self.data

			def wget_cookie(self,url):
				self.data = os.popen('wget -qO- --no-cookies --header "Cookie: zipcode=N0P2J0" %s'% url).read()
				return self.data

			def wget_sepcial(self,url):
				self.data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
				return self.data

			def curl(self,url):

				self.url = url 
				self.data = os.popen('curl --silent --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" %s >/dev/null'% self.url).read()
				return self.data

			def curl_special(self,url):

				self.url = url 
				self.data = os.popen('curl -O %s >/dev/null'% self.url).read()
				return self.data

			def urllib(self,url):
				filename = "cookies.txt"
				self.url = url 
				headers = {}
				headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
				req = urllib.request.Request(url, headers = headers)
				resp = urllib.request.urlopen(req)
				self.data = resp.read()

		except:
			continue
			time.sleep(3)
		break

class Out(Libraries):
	#This function will extract a to z pages 

	def excel_iter(self):
		book = xlrd.open_workbook("Swoop_Talent_Pool_Campus3.xls")

# grab the active worksheet
		first_sheet = book.sheet_by_index(0)


		number_of_rows = first_sheet.nrows
		for row in range(1,number_of_rows):
			cell1 = first_sheet.cell(row,2).value
			cell2 = first_sheet.cell(row,8).value
			cell1 = re.sub(r"[\s\n]","+",cell1)
			cell2 = re.sub(r"[\s\n]","+",cell2)
			cell3 = first_sheet.cell(row,0).value
			cell4 = first_sheet.cell(row,1).value
			cell3 = re.sub(r"[\s\n]","",cell3)
			cell3_l = (cell3.lower())
			cell4 = re.sub(r"[\s\n]","",cell4)
			cell4_l = (cell4.lower())
			format = urllib.parse.quote(cell2)
			#print (format)
			url = "https://www.google.co.in/search?q={0}".format(format)
			#url = urllib.parse.quote(url)
			print (url)
			output.links_extract(url,cell3_l,cell4_l)


	def links_extract(self,url,cell3_l,cell4_l):
		url = re.sub(r"[\s\n]*","",url)
		url = re.sub(r'\&','\&',url)
		url = re.sub(r'\+','\+',url)
		output.wget_sepcial(url)
		data = self.data 
		data = str(data)
		#sssprint (data)
		#f1.write(data)
		#

		#if re.search(r'(?mis)90\"\>[^\"]*\"r\"><a\shref\="http[s]*\:\/\/www\.(\w[^\"]*)\"',data):
		#	links = re.findall(r'(?mis)90\"\>[^\"]*\"r\"><a\shref\="http[s]*\:\/\/www\.(\w[^\"]*)\"',data)[0]
		#	links = re.sub(r"/.*","",links)
		#	links = re.sub(r"www\.","",links)
		#	print (links)
		#	output.email_manual_assign(links,cell3_l,cell4_l)
		if re.search(r'(?mis)r\"><a\shref\="http[s]*\:\/\/(\w[^\"]*)\"',data):
			links = re.findall(r'(?mis)r\"><a\shref\="http[s]*\:\/\/(\w[^\"]*)\"',data)[0]
			links = re.sub(r"/.*","",links)
			links = re.sub(r"www\.","",links)
			print (links)
			output.email_manual_assign(links,cell3_l,cell4_l)
		elif re.search(r'(?mis)r\"><a\shref\="http[s]*\:\/\/[^\"]*\"',data):
			links = re.findall(r'(?mis)r\"><a\shref\="http[s]*\:\/\/([^\"]*)\"',data)[0]
			links = re.sub(r"/.*","",links)
			links = re.sub(r"www\.","",links)
			print (links)
			output.email_manual_assign(links,cell3_l,cell4_l)


	def email_manual_assign(self,domain_name,cell3_l,cell4_l):
		f3 = open("email_manual_checked_data.csv", 'at')
		
		final_data = []

		writer = csv.writer(f3)
		f1 = open('email_combinations_results.txt','a')
		print ("**** - {0}".format(cell4_l))
		domain_name = re.sub(r"[\s\n]*","",domain_name)
		#Test Combination
		test_comb =  "sssssss.sakd@{0}".format(domain_name)
		#First combination
		first_comb = "{0}.{1}@{2}".format(cell3_l,cell4_l,domain_name)
		#print (first_comb)
		#Second - last name initial
		second_trans = re.sub(r"(.).*",r"\1",cell4_l)
		second_comb = "{0}.{1}@{2}".format(cell3_l,second_trans,domain_name)
		#print (second_comb)
		#Third combination
		third_comb = "{1}.{0}@{2}".format(cell3_l,cell4_l,domain_name)
		#print (third_comb)
		#Fourth Combination
		third_trans = re.sub(r"(.).*",r"\1",cell3_l)
		fourth_comb = "{0}.{1}@{2}".format(cell4_l,third_trans,domain_name)
		#print (fourth_comb)
		#Fifth Combination
		fifth_comb = "{0}{1}@{2}".format(cell3_l,cell4_l,domain_name)
		#print (fifth_comb)
		#sixth Combination
		sixth_comb = "{0}@{1}".format(cell3_l,domain_name)
		#print (fifth_comb)
		seventh_trans = re.sub(r"(.).*",r"\1",cell3_l)
		seventh_comb = "{0}{1}@{2}".format(seventh_trans,cell4_l,domain_name)

		eigth_trans = re.sub(r"(.).*",r"\1",cell4_l)
		eigth_comb = "{0}{1}@{2}".format(cell3_l,eigth_trans,domain_name)

		pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(test_comb)],stdout=subprocess.PIPE)
		pipe1 = pipe1.stdout.read()
		pipe1 = str(pipe1)
		pipe1 = re.sub(r'^b\'','',pipe1)
		pipe1 = re.sub(r'[\n\']*','',pipe1)
		print ("{0} - {1}".format(test_comb,pipe1)+"\n")

		if re.search(r'(?mis)Email\s*is\s*valid',pipe1):
			f1.write ("{0} - Domain Accpets ALL Emails - Seems like problem with SMPT or DOMAIN\n".format(domain_name))
			f1.write ("\n")
			f1.write ("\n")
			f1.write ("\n")
			f1.write ("\n")
			final_data.append('')
			pass
		else:

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(first_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(first_comb,pipe1))
			f1.write("{0} - {1}\n".format(first_comb,pipe1))
			final_data.append("{0} - {1}".format(first_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(second_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(second_comb,pipe1))
			f1.write ("{0} - {1}\n".format(second_comb,pipe1))
			final_data.append("{0} - {1}".format(second_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(third_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(third_comb,pipe1))
			f1.write ("{0} - {1}\n".format(third_comb,pipe1))
			final_data.append("{0} - {1}".format(third_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(fourth_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(fourth_comb,pipe1))
			f1.write ("{0} - {1}\n".format(fourth_comb,pipe1))
			final_data.append("{0} - {1}".format(fourth_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(fifth_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(fifth_comb,pipe1))
			f1.write ("{0} - {1}\n".format(fifth_comb,pipe1))
			final_data.append("{0} - {1}".format(fifth_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(sixth_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(sixth_comb,pipe1))
			f1.write ("{0} - {1}\n".format(sixth_comb,pipe1))
			final_data.append("{0} - {1}".format(sixth_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(seventh_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(seventh_comb,pipe1))
			f1.write ("{0} - {1}\n".format(seventh_comb,pipe1))
			final_data.append("{0} - {1}".format(seventh_comb,pipe1))

			pipe1 = subprocess.Popen(["perl","./email.pl","{0}".format(eigth_comb)],stdout=subprocess.PIPE)
			pipe1 = pipe1.stdout.read()
			pipe1 = str(pipe1)
			pipe1 = re.sub(r'^b\'','',pipe1)
			pipe1 = re.sub(r'[\n\']*','',pipe1)
			
			print ("{0} - {1}".format(eigth_comb,pipe1))
			f1.write ("{0} - {1}\n".format(eigth_comb,pipe1))
			final_data.append("{0} - {1}".format(eigth_comb,pipe1))
			print(final_data)
			writer.writerow( (final_data) )	

			f1.write ("\n")
			f1.write ("\n")
			f1.write ("\n")
			f1.write ("\n")

		#Excel Iter
		#book = xlrd.open_workbook("Swoop_Talent_Pool.xls")
		#first_sheet = book.sheet_by_index(0)
		#number_of_rows = first_sheet.nrows
		#for row in range(1,number_of_rows):
		#	cell1 = first_sheet.cell(row,0).value
		#	cell2 = first_sheet.cell(row,1).value
		#	cell1 = re.sub(r"[\s\n]","",cell1)
		#	cell1 = (cell1.lower())
		#	cell2 = re.sub(r"[\s\n]","",cell2)
		#	cell2 = (cell2.lower())
			#First combination
		#	first_comb = "{0}.{1}@{2}".format(cell1,cell2,domain_name)
		#	print (first_comb)
			#Second - last name initial
		#	second_trans = re.sub(r"(.).*",r"\1",cell2)
		#	second_comb = "{0}.{1}@{2}".format(cell1,second_trans,domain_name)
		#	print (second_comb)
			#Third combination
		#	third_comb = "{1}.{0}@{2}".format(cell1,cell2,domain_name)
		#	print (third_comb)
			#Fourth Combination
		#	third_trans = re.sub(r"(.).*",r"\1",cell1)
		#	fourth_comb = "{0}.{1}@{2}".format(cell2,third_trans,domain_name)
		#	print (fourth_comb)
			#Fifth Combination
		#	fifth_comb = "{0}{1}@{2}".format(cell1,cell2,domain_name)
		#	print (fifth_comb)


sleep = 2
output = Out()
output.excel_iter()
#output.links_extract("http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=3651&owner=include&match=&start=0&count=100&hidefilings=0")
#output.dedup_one()
#output.data_extract()
#output.dedup_two()
#output.main_data_to_csv()

