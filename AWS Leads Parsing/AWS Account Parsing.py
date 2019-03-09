import re
import json


class AWS_Account_Leads_Parser():

    def __init__(self, file_path):
        self.path = file_path
        self.aws_id = []
        self.aws_id_index = []
        self.aws_index_length = 0
        self.final_format = {}
        self.temp_dict = {}
        self.temp_aws_id_index = 0
        self.counter = 0

    def get_aws_account_id(self):

        with open(self.path, 'r') as file_read:
            self.lines_read = file_read.readlines()


        for self.line in range(len(self.lines_read)):
            if re.search('AWS_LEADS\[\d[0-9]+\]', self.lines_read[self.line]):
                self.aws_id.append(self.lines_read[self.line].replace('AWS_LEADS[', '').replace(']', '').strip('\n'))
                self.aws_id_index.append(self.line+4)

        return self.aws_id

    def get_aws_leads(self):

        with open(self.path, 'r') as file_read:
            self.line_read = file_read.readlines()
            self.aws_id_index_length = len(self.line_read)

        self.aws_index_length = len(self.aws_id_index)

        for index in range(self.aws_index_length):
            list = []

            if index < self.aws_index_length-1:

                for value in range(self.aws_id_index[index], self.aws_id_index[index+1]-8):
                    line = self.line_read[value].replace(",", '').strip()
                    if "uid" in line:
                        key = line[:5].replace('"', "")
                        value = line[7:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "cn" in line:
                        key = line[:4].replace('"', "")
                        value = line[6:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "mail" in line:
                        key = line[:6].replace('"', "")
                        value = line[8:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "corpId" in line:
                        key = line[:8].replace('"', "")
                        value = int(float(line[10:].strip('"')))
                        self.temp_dict[key] = value
                    else:
                        continue
                    list.append(self.temp_dict)
                    self.temp_dict = {}

            elif index == self.aws_index_length - 1:
                for value in range(self.aws_id_index[index], self.aws_id_index_length-1):
                    line = self.line_read[value].replace(",", '').strip()
                    if "uid" in line:
                        key = line[:5].replace('"', "")
                        value = line[7:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "cn" in line:
                        key = line[:4].replace('"', "")
                        value = line[6:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "mail" in line:
                        key = line[:6].replace('"', "")
                        value = line[8:].replace('"', "")
                        self.temp_dict[key] = value
                        continue
                    elif "corpId" in line:
                        key = line[:8].replace('"', "")
                        value = int(float(line[10:].strip('"')))
                        self.temp_dict[key] = value
                    else:
                        continue
                    list.append(self.temp_dict)
                    self.temp_dict = {}

            self.temp_aws_id_index = self.counter
            self.aws_account_index = self.aws_id[self.temp_aws_id_index]
            self.final_format[self.aws_account_index] = list
            self.counter += 1

    def remove_aws_users(self):
        for key, values in self.final_format.items():
            for item2 in values:
                for key1 in list(item2.keys()):
                    try:
                        if any(item2[key1] == item for item in self.aws_users_filter_list()):
                            del item2[key1]
                            continue
                        elif item2[key1] == "corpId" and any(item2[key1] == item for item in self.aws_users_filter_list()):
                            del item2[key1]
                    except ValueError and TypeError and KeyError:
                        print("The value trying to pass in filter_aws_users method is not string")
                    except RuntimeError:
                        print("Dictionary changed size during iteration")

                    length_aws_key = len(self.final_format[key])

                    for key_index in range(length_aws_key):
                        if not bool(self.final_format[key][0]):
                            del self.final_format[key][key_index]

        #print(self.final_format)

    def aws_users_filter_list(self):

        with open('remove_users.txt', 'r') as users_list:
            self.filter_list = users_list.readlines()
            filter_list_index = 0
            for line in self.filter_list:
                self.filter_list[filter_list_index] = line.strip('\n')
                filter_list_index += 1

            indexing = 0
            for filter_list in self.filter_list:
                try:
                    convert_to_num = int(filter_list)
                    if convert_to_num > 0:
                        self.filter_list[indexing] = convert_to_num
                        indexing += 1
                        continue
                    else:
                        indexing += 1

                except ValueError:
                    pass
                finally:
                        indexing += 1
            return self.filter_list

    def convert_to_json(self):
        with open('AWS_Account_Lead.json', 'w') as write_file:
            json.dump(self.final_format, write_file, indent= 4)

if __name__ == '__main__':
    path = input("Please enter the .txt file location for parsing AWS Leads: " + '\n')
    instance = AWS_Account_Leads_Parser(path)
    instance.get_aws_account_id()
    instance.get_aws_leads()
    instance.remove_aws_users()
    instance.convert_to_json()
