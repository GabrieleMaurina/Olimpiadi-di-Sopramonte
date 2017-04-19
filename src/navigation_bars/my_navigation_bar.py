from navigation_bars.navigation_bar import *
from pages.header_page import *
from pages.update_athlete import *


class MyNavigationBar(NavigationBar):
    def __init__(self, parent, repo_manager):
        super().__init__(parent)

        self.repoManager = repo_manager

        self.init_acquisition()
        self.init_consultation()
        self.init_administration()

    def init_acquisition(self):
        acquisition_header = HeaderPage(self.rightFrame, name="Acquisizione Dati")
        update_athlete_page = UpdateAthlete(self.rightFrame, self.repoManager)
        register_result = Page(self.rightFrame, name="Registra risultati")
        register_relay = Page(self.rightFrame, name="Registra staffetta")

        acquisition_header.add(update_athlete_page.name, lambda:self.open(update_athlete_page))
        acquisition_header.add(register_result.name, lambda:self.open(register_result))
        acquisition_header.add(register_relay.name, lambda:self.open(register_relay))

        self.add_page(acquisition_header)
        self.add_page(update_athlete_page)
        self.add_page(register_result)
        self.add_page(register_relay)

    def init_consultation(self):
        consultation_header = HeaderPage(self.rightFrame, name="Consultazione Dati")
        self.add_page(consultation_header)

    def init_administration(self):
        administration_header = HeaderPage(self.rightFrame, name="Amministrazione")
        team_creation_page = Page(self.rightFrame, name="Creazione squadre")
        reset_db_page = Page(self.rightFrame, name="Reset Database")

        administration_header.add(team_creation_page.name, lambda:self.open(team_creation_page))
        administration_header.add(reset_db_page.name, lambda:self.open(reset_db_page))

        self.add_page(administration_header)
        self.add_page(team_creation_page)
        self.add_page(reset_db_page)