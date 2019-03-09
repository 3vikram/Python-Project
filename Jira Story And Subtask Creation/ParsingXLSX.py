import xlrd
import json

class AssetParsing:

    def __init__(self):
        try:
            self.workbook = xlrd.open_workbook('Asset List - Development Copy.xlsx')
            self.sbseg_asset_list = self.workbook.sheet_by_index(1)

            self.segment_key = input("Please Enter the Segment data as per Master copy csv file: ")
            self.segment_value = input("Please Enter the Component data mapped between segment key and Intuit Component: ")
            self.segment_name = {self.segment_key : self.segment_value}
        except (FileNotFoundError, IndexError) as err:
            raise err
        '''
        Reference to Segment and Component Mapping,
        SBG - PLTF : Platform
        SBG - PAYR : Payroll
        SBG - IDG : IDG
        SBG - INF : Infrastructure
        SBG - Pay : Payments
        SBG - SE : SE
        SBG - BC : BC
        SBG - DATA PLATFORM : Platform
        SBG - DATA PRODUCTS : Platform
        SBG - SMS : SMS
        SBG - sheets : Sheets
        SBG - BM : BM
        SBG - MSaaS : MSaaS
        SBG - DATA : Data
        SBG - BDT : BDT
        SBG - Security : Security
        SBG - GoPay : Pay
        '''

    def readXLSX(self):
        self.area_owner = ''
        self.sbseg_asset_dictionary = {}
        for row in range(1, self.sbseg_asset_list.nrows):
            self.row_values = self.sbseg_asset_list.row_values(row)
            #print(self.row_values[2])
            if self.row_values[1] == self.segment_key:
                self.area_owner = self.row_values[2]
                self.sbseg_asset_dictionary[self.row_values[0]] = {'Segment' : self.row_values[1], 'Area Owner' : self.row_values[2], 'Asset ID' : str(self.row_values[3]).replace("'", ""),
                                             'Asset Alias' : self.row_values[4], 'Single Point of Contact' : self.row_values[5], 'Environment' : self.row_values[6]}
        print(self.area_owner)
        print(self.sbseg_asset_dictionary)

    def convert_to_json(self):
        with open('Asset_details.json', 'w') as write_file:
            json.dump(self.sbseg_asset_dictionary, write_file, indent= 4)


if __name__ == '__main__':
    assetParsingInstance = AssetParsing()
