from pages.page import *
from domain.athlete import *

class UpdateAthlete(Page):
    def __init__(self, parent, repo_manager):
        super().__init__(parent, name="Modifica Atleti")

        self.repoManager = repo_manager

        self.findLabel = Label(self, text="Trova Atleta", font=(None, 10))
        self.findLabel.pack(anchor=NW)

        self.findFrame = Frame(self, relief=RIDGE, borderwidth=2)
        self.findFrame.pack(anchor=NW, pady=(0, 10))

        self.findName = Label(self.findFrame, text="Nome", font=(None, 10))
        self.findName.pack(side=LEFT)
        self.findInputName = Entry(self.findFrame, font=(None, 10), width=10)
        self.findInputName.pack(side=LEFT, padx=(0, 10))

        self.findSurname = Label(self.findFrame, text="Cognome", font=(None, 10))
        self.findSurname.pack(side=LEFT)
        self.findInputSurname = Entry(self.findFrame, font=(None, 10), width=10)
        self.findInputSurname.pack(side=LEFT, padx=(0, 10))

        self.findCompNum = Label(self.findFrame, text="Pettorina", font=(None, 10))
        self.findCompNum.pack(side=LEFT)
        self.findInputCompNum = Entry(self.findFrame, font=(None, 10), width=10)
        self.findInputCompNum.pack(side=LEFT, padx=(0, 10))

        self.findButton = Button(self.findFrame, text="Trova", font=(None, 10), command=self.update_list)
        self.findButton.pack(side=LEFT)



        self.listLabel = Label(self, text="Atleti", font=(None, 10))
        self.listLabel.pack(anchor=NW)

        self.listFrame = Frame(self)
        self.listFrame.pack(anchor=NW, fill=X, pady=(0, 10))

        self.listListbox = Listbox(self.listFrame)
        self.listListbox.pack(side=LEFT, fill=X, expand=True)

        self.listScrollbar = Scrollbar(self.listFrame)
        self.listScrollbar.pack(side=RIGHT, fill=Y)

        self.listListbox.config(yscrollcommand=self.listScrollbar.set)
        self.listScrollbar.config(command=self.listListbox.yview)

        self.listListbox.bind('<<ListboxSelect>>', self.update_update)

        self.update_list()

        self.update_label = Label(self, text="Modifica", font=(None, 10))
        self.update_label.pack(anchor=NW)

    def update_list(self):
        self.listListbox.delete(0, END)
        for athlete in self.repoManager.athleteRepository.get(Athlete(name=self.findInputName.get(), surname=self.findInputSurname.get(), comp_num=self.findInputCompNum.get())):
            self.listListbox.insert(END, athlete)

    def update_update(self, e):
        print(self.listListbox.get(self.listListbox.curselection()))