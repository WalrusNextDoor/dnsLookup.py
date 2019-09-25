import socket
import os
import sys
import signal
import csv

#Takes filename as argument (dnsLookup.py names.txt)
filename = sys.argv[1]
count = 0

#Writes findings to CSV file
def writeTocsv(hostname, result):
    with open('dnsResults.csv', mode='a', newline="\n", encoding="utf-8") as dns_file:
        dns_writer = csv.writer(dns_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if result != None:
            dns_writer.writerow([hostname, str(result)])
        elif result == None:
            dns_writer.writerow([hostname, None])
        else:
            print("you fucked it")
            os.exit(1)


try:
    with open(filename, 'r') as file:
        for line in file:
            try:
                #print('looking up %s' % line.rstrip())
                hname = line.rstrip()
                ip = socket.gethostbyname(hname)
                #print(hname, ip)
                writeTocsv(hname, ip)
                count += 1
                print("%s completed" % count)

            except socket.herror:
                writeTocsv(line.rstrip(), None)
            except socket.gaierror:
                writeTocsv(line.rstrip(), None)



except FileNotFoundError:
    print("file does not exist")
    sys.exit(0)
