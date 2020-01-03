from bs4 import BeautifulSoup
import random
import requests

class UserAgents:
    ua_url = "https://deviceatlas.com/blog/list-of-user-agent-strings#desktop"

    def __init__(self):
        self.user_agents = self.get_user_agents()
        length_ua = len(self.user_agents)
        print(f"{length_ua} user agents found")

    def get_user_agents(self, source=ua_url):
        r = requests.get(source)
        soup = BeautifulSoup(r.content, "html.parser")
        tables = soup.find_all('table')
        return [table.find('td').text for table in tables]

    def pick_agent(self):
        return random.choice(self.user_agents)

if __name__ == "__main__":
    agents_handler = UserAgents()
    print(agents_handler.pick_agent())
