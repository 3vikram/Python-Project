import re
from pprint import pprint

class AwsAccountLeadData:
    def format_file(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r+') as file_read:
            with open('buffer.txt', 'w+') as file_write:

                self.total_line_count = 0
                for writeline in file_read.readlines():
                    if not writeline.isspace():
                        file_write.write(writeline)
                        self.total_line_count += 1

    def parse_aws_accountnumber(self):
        with open('buffer.txt', 'r+') as file_write:
            self.file_lines = file_write.readlines()
            self.aws_account_number = []
            self.aws_account_number_line_number = []
            self.final_result = {}

        for readfile in range(len(self.file_lines)):
            self.line = self.file_lines[readfile]
            if re.search('AWS_LEADS\[\d[0-9]+\]', self.line):
                self.aws_account_number.append(self.line.strip().strip('AWS_LEADS[').strip(']'))
                self.aws_account_number_line_number.append(readfile)

        self.counter = 0
        self.result = ''

        while(True):
            if self.counter < len(self.aws_account_number_line_number) - 1:
                for i in range(self.aws_account_number_line_number[self.counter], self.aws_account_number_line_number[self.counter + 1] - 5):
                    self.result += self.file_lines[i + 1].strip()
                self.final_result[self.aws_account_number[self.counter]]= self.result
                self.counter += 1
                self.result = ''
            elif self.counter == len(self.aws_account_number_line_number) - 1:
                for j in range(self.aws_account_number_line_number[self.counter], self.total_line_count - 1):
                    self.result += self.file_lines[j + 1].strip().strip('#')
                    self.final_result[self.aws_account_number[self.counter]]= self.result
                break


        pretty_printed = pprint(self.final_result)
        print(pretty_printed)

if __name__ == "__main__":
    parse = AwsAccountLeadData()
    file_path = input("Enter the .txt file location to parse AWS Account Lead information: "+ '\n')
    parse.format_file(file_path)
    parse.parse_aws_accountnumber()







