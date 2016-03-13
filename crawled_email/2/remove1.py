import csv
import re
import glob
import codecs
arra_s = []
for f1 in glob.glob('email_manual_checked_data.csv'):
            #print f1
    with codecs.open(f1, 'rb',encoding='utf-8') as csvfile:

                
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        
        for row in spamreader:
            if re.search(r'(?mis)email is valid',row[0]):
                print "yes"
                row0 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[0])
                arra_s.append(row0)
            elif re.search(r'(?mis)email is valid',row[1]):
                row1 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[1])
                arra_s.append(row1)
            elif re.search(r'(?mis)email is valid',row[2]):
                row2 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[2])
                arra_s.append(row2)
            elif re.search(r'(?mis)email is valid',row[3]):
                row3 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[3])
                arra_s.append(row3)
            elif re.search(r'(?mis)email is valid',row[4]):
                row4 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[4])
                arra_s.append(row4)
            elif re.search(r'(?mis)email is valid',row[5]):
                row5 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[5])
                arra_s.append(row5)
            elif re.search(r'(?mis)email is valid',row[6]):
                row6 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[6])
                arra_s.append(row6)
            elif re.search(r'(?mis)email is valid',row[7]):
                row7 = re.sub(r'(?mis)([^\-]*)\-.*',r'\1',row[7])
                arra_s.append(row7)
            else:
                arra_s.append('')

print len(arra_s)
f3 = open("test_data.csv", 'at')
writer = csv.writer(f3,delimiter = ',', lineterminator='\n',quoting=csv.QUOTE_ALL)
writer.writerow(self.headers)
        #count_mis = 0
for write in arra_s:
    print write
            #count_mis = count_mis + 1
            #if count_mis > 1:
    #writer.writerow(write)
print "Completed"
