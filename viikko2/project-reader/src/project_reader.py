from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # tiedoston parseroitu sisältö
        parsed_content = toml.loads(content)
        #print(parsed_content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])


        return Project(parsed_content["tool"]["poetry"]["name"], parsed_content["tool"]["poetry"]["description"], parsed_content["tool"]["poetry"]["dependencies"], parsed_content["tool"]["poetry"]["dev-dependencies"])
