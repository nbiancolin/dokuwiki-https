import requests
from requests.auth import HTTPBasicAuth

class DokuWiki:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.cookies = None
    
    def login(self):
        session = requests.Session()
        login_url = self.url + f"/doku.php" #TODO do you need an ID here?
        login_data = {
            "u": self.username,
            "p": self.password,
        }
        login_response = session.post(login_url, data=login_data)
        if login_response.status_code == 200:
            self.cookies = login_response.cookies
        else:
            print("DokuWiki Login failed.")
            exit()
        
    def getPage(self, pageName):
        full_url = f"{self.url}/doku.php?id={pageName}&do=export_raw"
        try:
            response = requests.get(full_url, cookies=self.cookies)
            if response.status_code == 200:
                #print("Wiki Successfully accessed: Current page content: \n" + response.text)
                return response.text
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        
    def editPage(self, pageName, new_content, summary = "Updated via Python dokuwiki-https"):
        edit_url = f"{self.url}/doku.php?id{pageName}&do=edit"
        try:
            # Retrieve the edit token
            print("Attempting to send content to url: " + edit_url)
            response = requests.get(edit_url, cookies=self.cookies)
            if response.status_code == 200:
                edit_token = response.text.split('name="sectok" value="', 1)[1].split('"', 1)[0]
                rev = response.text.split('name="rev" value="', 1)[1].split('"', 1)[0]
                dokuDate = response.text.split('name="date" value="', 1)[1].split('"', 1)[0]
                prefix = response.text.split('name="prefix" value="', 1)[1].split('"', 1)[0]
                suffix = response.text.split('name="suffix" value="', 1)[1].split('"', 1)[0]
                changecheck = response.text.split('name="changecheck" value="', 1)[1].split('"', 1)[0]
                target = response.text.split('name="target" value="', 1)[1].split('"', 1)[0]
                # Prepare data for the POST request
                data = {
                    "sectok": edit_token,
                    "id": pageName,
                    "rev": rev,
                    "date": dokuDate,
                    "prefix": prefix,
                    "suffix": suffix,
                    "changecheck": changecheck,
                    "target": target,
                    "wikitext": new_content,
                    "do[save]": "1",
                    "summary": summary
                }
                # Send POST request to update the page
                response = requests.post(edit_url, data=data, cookies=self.cookies)
                if response.status_code == 200:
                    return True
                else:
                    print(f"Failed to update content. Status code: {response.status_code}")
                    return False
            else:
                print(f"Failed to retrieve edit token. Status code: {response.status_code}")
                return False
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False