import urllib.request
import os
import re
import time
import sys
import csv
import xlrd

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
		book = xlrd.open_workbook("Swoop_Talent_Pool_Campus4.xls")

# grab the active worksheet
		first_sheet = book.sheet_by_index(0)


		number_of_rows = first_sheet.nrows
		for row in range(1,number_of_rows):
			cell1 = first_sheet.cell(row,2).value
			cell2 = first_sheet.cell(row,3).value
			cell1 = re.sub(r"[\s\n]","+",cell1)
			cell2 = re.sub(r"[\s\n]","+",cell2)
			cell3 = first_sheet.cell(row,0).value
			cell4 = first_sheet.cell(row,1).value
			cell3 = re.sub(r"[\s\n]","",cell3)
			cell3_l = (cell3.lower())
			cell4 = re.sub(r"[\s\n]","",cell4)
			cell4_l = (cell4.lower())
			url = "https://www.google.co.in/search?q={0}{1}".format(cell1,cell2)
			output.links_extract(url,cell3_l,cell4_l)


	def links_extract(self,url,cell3_l,cell4_l):
		f1 = open('a-to-z-links.txt','w')
		f2 = open('main-urls.txt','w')
		url = re.sub(r"[\s\n]*","",url)
		url = re.sub(r'\&','\&',url)
		url = re.sub(r'\+','\+',url)
		output.wget_sepcial(url)
		data = self.data 
		data = str(data)
		#f1.write(data)

		if re.search(r'(?mis)<a\shref\=\"([^\"]*)\"\sonmouse',data):
			links = re.findall(r'(?mis)<a\shref\=\"([^\"]*)\"\sonmouse',data)
			print (links)
			output.main_data_to_csv(links,cell3_l,cell4_l)
			#for link in links:
			#	if re.search(r'^htt',link):
			#		output.main_data_to_csv(link)
				


	def main_data_to_csv(self,links,cell3_l,cell4_l):
		#This page will extract data what we need
		f3 = open("test_check.csv", 'at')
		writer = csv.writer(f3)
		data_store = []
		for link in links:
			
			link = re.sub(r"[\s\n]*","",link)
			link = re.sub(r'\&','\&',link)
			link = re.sub(r'\+','\+',link)
			link = re.sub(r'https://support.google.com.*','',link)
			print (link)
			try:
				output.wget_sepcial(link)
				data = self.data 
				data = str(data)

				if re.search(r'(?mis)email\"\:\"([^\"]*)\"\}\]',data):
					email = re.findall(r'(?mis)email\"\:\"([^\"]*)\"\}\]',data)[0]
					if re.search(r'(?mis)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',email):
						email = re.sub(r'nr\@context\".*','',email)
						email = re.sub(r'\?.*','',email)
						email = re.sub(r'\".*','',email)
						email = re.sub(r'\'.*','',email)
						email = re.sub(r'(.*)\s.*',r'\1',email)
						data_store.append(email)
				if re.search(r'(?mis)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?mis)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?mis)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',email):
						email = re.sub(r'nr\@context\".*','',email)
						email = re.sub(r'\?.*','',email)
						email = re.sub(r'\".*','',email)
						email = re.sub(r'\'.*','',email)
						email = re.sub(r'(.*)\s.*',r'\1',email)
						data_store.append(email)
				if re.search(r'(?mis)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?mis)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?mis)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							mail = re.sub(r'\?.*','',mail)
							mail = re.sub(r'\".*','',mail)
							mail = re.sub(r'\'.*','',mail)
							mail = re.sub(r'(.*)\s.*',r'\1',mail)
							data_store.append(mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							mail = re.sub(r'\?.*','',mail)
							mail = re.sub(r'\".*','',mail)
							mail = re.sub(r'\'.*','',mail)
							mail = re.sub(r'(.*)\s.*',r'\1',mail)
							data_store.append(mail)
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					email = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)[0]
					email = re.sub(r'nr\@context\".*','',email)
					email = re.sub(r'\".*','',email)
					email = re.sub(r'\'.*','',email)
					email = re.sub(r'(.*)\s.*',r'\1',email)
					data_store.append(email)
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							mail = re.sub(r'\?.*','',mail)
							mail = re.sub(r'\".*','',mail)
							mail = re.sub(r'\'.*','',mail)
							mail = re.sub(r'(.*)\s.*',r'\1',mail)
							data_store.append(mail)


				

			except:
				pass

		print (data_store)
		writer.writerow( (data_store) )
		output.email_check(data_store,cell3_l,cell4_l)

	def email_check(self,data_store,cell3_l,cell4_l):
		f3 = open("email_crawl_checked_data.csv", 'at')
		f4 = open("email_crawl_checked.csv", 'at')
		f5 = open("final_data.txt", 'a')
		writer = csv.writer(f3)
		writer1 = csv.writer(f4)
		final_data = []
		final_data1 = []
		print ("came inside the email_check")
		for datas in data_store:
			print (datas)
			data_removed_at = re.sub(r'(.*)\@.*',r'\1',datas)
			data_size = len(datas)
			datas = str(datas)
			print ("{0} - ssss".format(datas))
			if data_size > 0:
				if re.search(r'(?mis)gmail|yahoo|rediff|sify|hotmail',datas):
					final_data.append("hi - {0}".format(datas))
				else:
					print ("Checking")
					first_name_last_name = "{0}.{1}".format(cell3_l,cell4_l)
					first_name_last_name_1 = "{0}.{1}".format(cell3_l,cell4_l)
					if re.search(r'(?mis){0}'.format(first_name_last_name),data_removed_at):
						final_data.append(datas)
						final_data1.append(datas)
					first_name = "{0}".format(cell3_l)
					if re.search(r'(?mis){0}'.format(first_name),data_removed_at):
						final_data.append(datas)
						final_data1.append(datas)
					last_name = "{0}".format(cell4_l)
					if re.search(r'(?mis){0}'.format(last_name),data_removed_at):
						final_data.append(datas)
						final_data1.append(datas)
					first_name_initial = re.sub(r"(.).*",r"\1",cell3_l)
					data_removed_at_fi = re.sub(r"(.).*",r"\1",datas)
					if re.search(r'(?mis){0}'.format(first_name_initial),data_removed_at_fi):
						final_data.append(datas)
						final_data1.append(datas)
					last_name_initial = re.sub(r"(.).*",r"\1",cell4_l)
					data_removed_at_li = re.sub(r"(.).*",r"\1",datas)
					if re.search(r'(?mis){0}'.format(last_name_initial),data_removed_at_li):
						final_data.append(datas)
						final_data1.append(datas)

		print(final_data1)
		writer.writerow( (final_data) )
		che = len(final_data1)
		if che <= 0:
			f5.write("Email Not Found\n")
		else:
			f5.write(final_data1[0]+"\n")

		writer1.writerow( (final_data1) )
		

		

			

			
							
				


sleep = 2
output = Out()
output.excel_iter()
#output.links_extract("http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=3651&owner=include&match=&start=0&count=100&hidefilings=0")
#output.dedup_one()
#output.data_extract()
#output.dedup_two()
#output.main_data_to_csv()