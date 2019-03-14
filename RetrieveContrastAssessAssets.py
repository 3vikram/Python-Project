import requests
import json

class RetriveAssetData:

    def __init__(self):

        try:
            with open('Credentials.json') as json_data:
                self.credentials = json.load(json_data)

            self.contrast_url = "https://test.contrastsecurity.com"

            self.contrast_headers = {'Authorization' : self.credentials["Authorization"],
                    'API-Key' : self.credentials["API-Key"],
                    'Accept' : "application/json",
                    'Content-Type': "application/json"}
        except (FileNotFoundError, IndexError) as err:
            raise err

        self.online_applications_count = 0
        self.offline_applications_count = 0
        self.total_applications_count = 0

        self.online_applications = []
        self.offline_applications = []
        self.total_applications = []

    def number_of_applications(self):

        self.number_of_applications = self.response['count']

    def search_assets_by_tag(self):

        self.request = requests.request("GET", "https://test.contrastsecurity.com/Contrast/api/ng/8a632-48e7-8802-d69a4r672f75/applications/filter?filterTags=TEST - APP"
                                   ,headers = self.contrast_headers)

        self.response = self.request.json()
        self.number_of_applications()

        contains_duplicate_assetid_list = []
        self.cleaned_duplicate_assetid = set()
        for application in range(self.number_of_applications):
            if self.response['applications'][application]['status'] == 'offline' or 'online':
                self.total_applications_count += 1
                self.tags_count = len(self.response['applications'][application]['tags'])
                for tags in range(self.tags_count):
                    if self.response['applications'][application]['short_name'] == None:
                        continue
                    else:
                        asset_id = self.response['applications'][application]['short_name']
                        contains_duplicate_assetid_list.append(asset_id)

                if "ASSET ID" in self.response['applications'][application]['tags'][tags]:
                    asset_id = self.response['applications'][application]['tags'][tags]
                    contains_duplicate_assetid_list.append(asset_id.replace("ASSET ID - ", ""))

        for asset in contains_duplicate_assetid_list:
            if asset not in self.cleaned_duplicate_assetid:
                self.total_applications.append(asset)
                self.cleaned_duplicate_assetid.add(asset)

        #print(self.cleaned_duplicate_assetid)
        #print(self.total_applications)

if __name__ == '__main__':
    instance = RetriveAssetData()
    instance.search_assets_by_tag()
