import requests
from requests.auth import HTTPBasicAuth

# JiraのURLと認証情報
jira_url = "https://ochisite.atlassian.net/rest/api/3/issue/"
jira_search_url = "https://ochisite.atlassian.net/rest/api/3/search"
jira_token = "ATATT3xFfGF0jwqxVEgJiyS6D7Lcq_UaLdbXmrl1ZpqX2czr3wD8UY8eDoRFI734l0fvyu1Cd1RXeARHXCuxZ9WmbKSU1g0rmGB9r3O7adhimFwpet5CbxA-ctmEClLu71Q4YYBc9YARPEMbrhzIoqM4saWfxJEor7pS7nWpAhkrWGkFYWGea40=203A9E93"
email = "soryuusi1@gmail.com"

def get_jira_issue(issue_id):
    try:
        response = requests.get(
            jira_url + issue_id,
            auth=HTTPBasicAuth(email, jira_token),
            headers={"Accept": "application/json"}
        )
        
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, response.status_code
    except Exception as e:
        return None, str(e)

def get_all_issues():
    try:
        response = requests.get(
            jira_search_url,
            auth=HTTPBasicAuth(email, jira_token),
            headers={"Accept": "application/json"},
            params={"jql": "", "maxResults": 50}
        )
        
        if response.status_code == 200:
            return response.json().get('issues', []), None
        else:
            return None, response.status_code
    except Exception as e:
        return None, str(e)