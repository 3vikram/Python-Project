from jira import JIRA
from RetrieveContrastAssessAssets import *
import json

class JiraVerifyAndClosure:

    def __init__(self):

        try:
            with open('Credentials.json') as json_data:
                credentials = json.load(json_data)

            self.jira = JIRA(basic_auth= (credentials['username'], credentials['password']),
                            options = {'server' : 'https://jira.test.com'})
        except (FileNotFoundError, IndexError) as err:
            raise err

        self.jira_ticket_instance = RetriveAssetData()
        self.jira_ticket_instance.search_assets_by_tag()

    def verify_contrast_subtasks(self):

        count = 0
        self.jql_query = 'project = "TEST Security Defects" AND labels = TEST_SSDLC_Tools_Onboarding_ContrastAssess AND status not in (Closed)'
        self.jql_result = self.jira.search_issues(self.jql_query, maxResults= 500)
        for issue in self.jql_result:
            for self.assetid in self.jira_ticket_instance.cleaned_duplicate_assetid:
                if self.assetid in issue.fields.summary:
                    self.jira.transition_issue(issue.key, 'Close Issue', comment= 'Asset ID : {} is already on-board to Contrast Assess.'.format(self.assetid))
                    break

if __name__ == '__main__':
    instance = JiraVerifyAndClosure()
    instance.verify_contrast_subtasks()
