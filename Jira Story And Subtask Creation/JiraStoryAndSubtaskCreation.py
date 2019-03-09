from jira import JIRA
from ParsingXLSX import *
import json

class JiraStory:

    def __init__(self):

        try:
            with open('Credentials.json') as json_data:
                self.credentials = json.load(json_data)

            self.jira = JIRA(basic_auth= (self.credentials['Username'], self.credentials['Password']), options= {'server' : 'https://jira.test.com'})
        except (FileNotFoundError, IndexError) as err:
            raise err

        self.parsing_asset_instance = AssetParsing()
        self.parsing_asset_instance.readXLSX()
        self.parsing_asset_instance.convert_to_json()

    def create_story(self):
        self.keys = ''
        self.values = None
        for self.keys, self.values in self.parsing_asset_instance.sbseg_asset_dictionary.items():
            jira_story_field_information = {
                        'project' : {'key' : 'SBGSEC'},
                        'summary' : 'SSDLC Tools Onboarding | Asset ID: {} | Asset Alias: {} | Service Name: {}'.format(self.values['Asset ID'], self.values['Asset Alias'], self.keys),
                        'description' : "This is with respect to the initiative that is driven across test regarding *Secure Software Development Life Cycle (SSDLC)* adoption for all services in test and the same adoption is happening in SBSEG and the ask is that this service requires to be onboarded to the following SSDLC tools,\n\n# Contrast Assess (IAST tool to be integrated in your Pre-Production (QA or Dev or E2E) Environment only)\n# Nexus IQ (Software Composition Analysis)\n# Signal Science (RASP tool for Production Environment only)\n\n*+Policy Details:+* https://testcloud.sharepoint.com/WorkResources/Pages/application-security.aspx (Refer Point 2)\n\n*+How to proceed?+*\n\n# There are individual tasks assigned below for each tools\n# Please close the tasks below when on-boarding to those specific tools are completed\n# Every task contains the respective documentation for that tool\n# *_The main story should be closed only if all the sub-tasks are closed_*\n# *_In case if your service has been already onboarded to any of these SSDLC tools feel free to close those tasks alone_*\n# *_+Note: If you are not the right assignee of this ticket please help us in re-assigning it to the right SPOC to expedite the process+_*\n\n*+Here are the co-ordinates to reach us in case of any clarification or help?+*\n\n* *+Slack Channel:+* #sbg-paranoids\n\n* *+Email Address:+* Sairam@test.com, Abhimanyu@test.com, Tri@test.com, Paranoids@test.com",
                        'issuetype' : {'name' : 'Story'},
                        'components' : [{'name' : self.parsing_asset_instance.segment_value}],
                        'assignee' : {'name' : instance.search_users(self.values['Single Point of Contact'])},
                        'labels' : ['Paranoids', 'SBSEG_SSDLC_Tools_Onboarding'],
                        'priority' : {'id' : '2'},
                        'customfield_12403' : {'name' : instance.search_users(self.parsing_asset_instance.area_owner)},
                        'customfield_10302' : {'id' : '10314'},
                        'customfield_10512' : {'id' : '26124'},
                        'customfield_14106' : [{'id' : '16961'}],
                        'customfield_11712' : [{'name' : 'tr'}, {'name' : 'test1'}, {'name' : 'test1'}, {'name' : 'testastava8'}, {'name' : 'test'}, {'name' : instance.search_users(self.values['Single Point of Contact'])}]
                    }

            '''
            customfield_12403 refers to Jira field 'Area Owner' and id value must only be usernames or user alias
            customfield_10302 refers to Jira field 'Severity' and id value 10314 refers to 'Medium'
            customfield_10512 refers to Jira field 'Organization' and id value 26124 refers to 'SBG'
            customfield_14106 refers to Jira field 'Work Type' and id value 16961 refers to 'Security'
            customfield_11712 refers to Jira field 'Watchers' and here we must only add the usernames aka user alias
            '''

            self.jira_story_creation = self.jira.create_issue(fields= jira_story_field_information)
            #subtask_creation = JiraStory()
            instance.create_subtask()

    def create_subtask(self):

        print(self.keys)
        print(self.values['Asset ID'])
        print(self.values['Asset Alias'])
        self.summary_list = ['Onboard to Contrast Assess | Asset ID: {} | Asset Alias: {} | Service Name: {}'.format(self.values['Asset ID'], self.values['Asset Alias'], self.keys), 'Onboard to Nexus IQ | Asset ID: {} | Asset Alias: {} | Service Name: {}'.format(self.values['Asset ID'], self.values['Asset Alias'], self.keys), 'Onboard to Signal Science | Asset ID: {} | Asset Alias: {} | Service Name: {}'.format(self.values['Asset ID'], self.values['Asset Alias'], self.keys)]
        print(self.summary_list)
        self.description_list = ['*+What is to be done?+*\n\nOnboard to Contrast Assess\n\n*+How to onboard to Contrast Assess?+*\n\nThe following link helps in the installation procedure for onboarding to contrast and procedure is segregated for various tech-stack accordingly in the below link, choose the appropriate procedure for your tech-stack\n\nhttps://test.test.com/display/SBGSecAE/SBSEG+-+Contrast+Assess+-+Installation+Procedure\n\n*+How to check whether Contrast Assess is online?+*\n\nThere should be a green button next to your service in the Applications tab in the Contrast Assess portal\n\n*+Updated Contrast Assess Agent:+* \n\nThe link contains agents for specific languages that contrast assess supports please choose the appropriate agent for your service tech-stack\n\nhttps://artifact.test.com/artifactory/generic-local/dev/security/ssdlc/contrast/ \n\n*+Updated Contrast Assess Agent for IKS:+* \n\nIf you are in IKS environment please refer to the latest Docker Image which contains the latest contrast assess agent\n\nFROM docker.artifactory.a.test.com/small-business/tools/e2e/e2e_oicp_base_jdk8:jenkins-dev-deploy-e2e_oicp_base_jdk8-e2e_oicp_base_jdk8-master-29-fdc057f\n\n*+How to proceed?+*\n\n# Leverage the Installation Procedure for Contrast Assess Onboarding\n# Incase if your service tech stack does not support Contrast Assess, *PLEASE GO AHEAD AND UPDATE THE LABEL SECTION BY ADDING THIS LABEL "SBSEG_SSDLC_Tools_Onboarding_ContrastAssess_OutofScope"* also mention what tech stack your service leverages in the COMMENTS SECTION\n# If your onboarding is successful, *PLEASE PASTE THE SERVICE LINK FROM CONTRAST ASSESS IN THE COMMENTS SECTION BELOW* and close the task with proper resolution\n# If your onboarding is going to be at a later date please update the committed date or resolution date directly or in the comments section\n\n*+Here are the co-ordinates to reach us in case of any clarification or help?+*\n\n* *+Slack Channel:+* [#sbseg-contrast-assess|https://test-teams.slack.com/messages/C7RGX7BQD] \n\n* *+Email Address:+* Sairam@test.com \n\n *_+Note:+_* \n* _+If you are not the right assignee of this ticket please help us in re-assigning it to the right SPOC to expedite the process+_\n* _+In case if this service has been already onboarded to Contrast Assess please feel free to close this task with a comment under the comments section as this service is already onboarded to Contrast Assess+_', '*+What is to be done?+*\n\nOnboard to Nexus IQ\n\n*+How to onboard to Nexus IQ?+*\n\nThe following link helps in the installation procedure for Onboarding to Nexus IQ\n\nhttps://test.test.com/display/CTODevSecurity/IQ+Server\n\n*+How to proceed?+*\n\n# Leverage the Installation Procedure for Nexus IQ Onboarding\n# Incase your service is not in either of the Jenkins mentioned in the Onboarding test, *PLEASE GO AHEAD AND UPDATE THE LABEL SECTION BY ADDING THIS LABEL "SBSEG_SSDLC_Tools_Onboarding_NexusIQ_OutofScope"* also mention what type of build process is leveraged in the COMMENTS SECTION\n# If your onboarding is successful, *PLEASE PASTE THE SERVICE LINK REPORT FROM NEXUS IQ OR FROM JENKINS CONSOLE IN THE COMMENTS SECTION BELOW* and close the task with proper resolution\n# If your onboarding is going to be at a later date please update the committed date or resolution date directly or in the comments section\n\n*+Here are the co-ordinates to reach us in case of any clarification or help?+*\n\n* *+Slack Channel:+* [#sbseg-nexus-iq|https://test-teams.slack.com/messages/CGS7HTVAB] \n\n* *+Email Address:+* Sairam@test.com \n\n*_+Note:+_*\n* _+If you are not the right assignee of this ticket please help us in re-assigning it to the right SPOC to expedite the process+_ \n* _+In case if this service has been already onboarded to Nexus IQ please feel free to close this task with a comment in the comments section that this service is already onboarded to Nexus IQ+_', '*+What is to be done?+*\n\nOnboard to Signal Science\n\n*+How to onboard to Signal Science?+*\n\nFollow Step 1A and 1B in the below link,\n\nhttps://github.test.com/test/modern-saas-docs/blob/master/docs/developer/security.md#sigsci_step1 \n\n*+_(Note: Please onboard your service first and then go about with your integration to your service)_+* \n\n*+How to integrate Signal Science to your service?+* \n\nThe following link helps in the installation procedure for Onboarding to Nexus IQ \n\n* *IKS Environment:* https://github.test.com/kubernetes/modern-saas-docs/blob/master/docs/developer/security.md#configure-signal-sciences \n* *Non-IKS Environment:* https://github.test.com/Paranoids/Signal-Sciences-Installation \n\n*+How to proceed?+* \n\n# Leverage the Installation Procedure for Signal Science Onboarding\n# Incase your service is not in either of the Jenkins mentioned in the Onboarding test, *PLEASE GO AHEAD AND UPDATE THE LABEL SECTION BY ADDING THIS LABEL "SBSEG_SSDLC_Tools_Onboarding_SigSci_OutofScope"* also mention what type of tech-stack your service leverages in the COMMENTS SECTION\n# If your onboarding is successful, *PLEASE ATTACH A SCREENSHOT OF AGENT STATUS FROM SIGNAL SCIENCE DASHBOARD* and close the task with proper resolution\n# If your onboarding is going to be at a later date please update the committed date or resolution date directly or in the comments section\n\n*+Here are the co-ordinates to reach us in case of any clarification or help?+*\n\n* *+Slack Channel:+* [#sbseg-signal-sciences|https://test-teams.slack.com/messages/CAU73GYB0] \n\n* *+Email Address:+* Karthik@test.com & Sairam_Murali@test.com \n\n*_+Note:+_* \n* _+If you are not the right assignee of this ticket please help us in re-assigning it to the right SPOC to expedite the process+_ \n* _+In case if this service has been already onboarded to Signal Science please feel free to close this task with a comment in the comments section that this service is already onboarded to Signal Science+_']
        self.labels_list = ['SBSEG_SSDLC_Tools_Onboarding_ContrastAssess', 'SBSEG_SSDLC_Tools_Onboarding_NexusIQ', 'SBSEG_SSDLC_Tools_Onboarding_SignalScience']
        self.onboard_environment = ['30734', '30734', '30733']

        '''
        ID 30734 refers to Non-Production Environment
        ID 30733 refers to Production Environment
        '''

        for index in range(3):
            self.jira_subtask_field_information = {
                    'project' : {'key' : 'SBGSEC'},
                    'parent' : {'key' : self.jira_story_creation.key},
                    'summary' : self.summary_list[index],
                    'description' : self.description_list[index],
                    'issuetype' : {'name' : 'Sub-task'},
                    'components' : [{'name' : self.parsing_asset_instance.segment_value}],
                    'labels' : ['Paranoids', self.labels_list[index]],
                    'assignee' : {'name' : instance.search_users(self.values['Single Point of Contact'])},
                    'priority' : {'id' : '2'},
                    'customfield_10302' : {'id' : '10314'},
                    'customfield_10512' : {'id' : '26124'},
                    'customfield_10207' : [{'id' : self.onboard_environment[index]}],
                    'customfield_11712' : [{'name' : 'test'}, {'name' : 'test1'}, {'name' : 'test1'}, {'name' : 'testastava8'}, {'name' : 'test'}, {'name' : instance.search_users(self.values['Single Point of Contact'])}]
                }
            self.jira_subtask_creation = self.jira.create_issue(fields= self.jira_subtask_field_information)

        '''
        customfield_10302 refers to Jira field 'Severity' and id value 10314 refers to 'Medium'
        customfield_10512 refers to Jira field 'Organization' and id value 26124 refers to 'SBG'
        customfield_10207 refers to Jira field 'Environments' and id value 30734 and 30733 refers to Non-production and Production Environment respectively
        customfield_11712 refers to Jira field 'Watchers' and here we must only add the username aka user alias
        '''

      def search_users(self, email_address):
          self.email_address = email_address
          #print(self.values['Single Point of Contact'])
          try:
              for value in self.email_address:
                  if value == False:
                      return self.email_address
                  else:
                      e_address = str(self.jira.search_users(self.email_address))
                      email_to_string = e_address.replace('[<JIRA User: ', '').replace('displayName=', '').replace('name=', '').replace('>]', '').replace(' ', '').replace('\'', '')
                      user_indexing = email_to_string.index('key')
                      user_alias = (email_to_string[user_indexing+4:].split(','))
                      return user_alias[0]
          except ValueError as err:
              raise err


if __name__ == '__main__':
    instance = JiraStory()
    instance.create_story()
