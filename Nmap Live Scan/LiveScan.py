import os

class Nmapscan:

    def Live_Scan(self):
        self.IP_Subnet = input("Enter the subnet: " )
        self.IP_Last_Oct = input("Enter the last octet in Subnet address: ")
        self.Port_Scan = input("Do you want to perform port scan?: ").lower().strip()
        self.Vuln_Scan = input("Do you want to perform vulnerability scan for the identified services? ").lower().strip()
        self.Final_IP_Address = self.IP_Subnet + self.IP_Last_Oct
        self.File_Exists_Check()
        a = 'nmap  -sP -oN Livescan.txt ' + self.Final_IP_Address
        print('Running Live IP scan!')
        response = os.system(a)
        with open('Livescan.txt','r+') as ff:
            with open('live_ip.csv','a+') as aa:
                for line in ff:
                    if "Nmap scan report for " in line:
                        aa.write(line[line.index('for ')+ 4:])
                        continue
                aa.close()
        if self.Port_Scan == "yes" or "y":
            self.port_scan_results = self.Service_Scan()
            print(self.port_scan_results)
        elif self.Port_Scan == "no" or "n":
            print("Thank You for using me! See you later for a port scan :)")
        else:
            print("incorrect input")

    def Service_Scan(self):
        print('Running Service detection scan!')
        self.No_Ports_Open = 0
        with open('live_ip.csv', 'r+') as aa:
            for ips in aa:
                b = 'nmap -Pn -sT -oN port_scan.txt ' + ips
                response1 = os.system(b)
                c = 'sudo nmap -Pn -sT -O -sV -vv -oN verbose_scan.txt ' + ips
                response2 = os.system(c)
                if self.Vuln_Scan == 'yes' or 'y':
                    with open('Final_service.txt','a+') as fs:
                        with open('port_scan.txt','r+') as r1:
                            for line1 in r1:
                                if "open" in line1:
                                    self.No_Ports_Open = self.No_Ports_Open + 1
                                    fs.write(line1)
                                    service = line1[line1.index('open  ') + 6:]
                                    vuln_commands = 'nmap  -Pn --script=' + '*' + service.rstrip() + '* ' + '-oN Vuln_report.txt ' + ips
                                    print('Running Vulnerability Scan on service {}'.format(service))
                                    response3 = os.system(vuln_commands)
                                    continue
                            print(self.No_Ports_Open)
                elif self.Vuln_Scan == 'no' or 'n':
                    print("See you next time for a service vulnerability scan on your asset!")

    def File_Exists_Check(self):
        print('Deleting Existing scan files!')
        if os.path.isfile('./live_ip.csv'):
            os.remove("live_ip.csv")
        if os.path.isfile('.Livescan.txt'):
            os.remove("Livescan.txt")
        if os.path.isfile('./port_scan.txt'):
            os.remove("port_scan.txt")
        if os.path.isfile('./Final_service.txt'):
            os.remove("Final_service.txt")
        if os.path.isfile('./Vuln_report.txt'):
            os.remove("Vuln_report.txt")
        print('Deleted scan files!')

result = Nmapscan()
result.Live_Scan()
