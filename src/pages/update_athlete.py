from pages.page import *
from domain.athlete import *
from domain.category import *
from domain.team import *
from tkinter.messagebox import *
from datetime import *

class UpdateAthlete(Page):
    def __init__(self, parent, repo_manager):
        super().__init__(parent, name="Modifica Atleti")

        self.repoManager = repo_manager
        self.categories = self.repoManager.categoryRepository.get(Category())
        self.teams = self.repoManager.teamRepository.get(Team())

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



        self.athletes = []
        self.selectedAthlete = -1

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

        self.updateLabel = Label(self, text="Modifica", font=(None, 10))
        self.updateLabel.pack(anchor=NW)

        self.updateFrame = Frame(self, relief=RIDGE, borderwidth=2)
        self.updateFrame.pack(anchor=NW, pady=(0, 10))
        for i in range(8):
            self.updateFrame.grid_columnconfigure(i, minsize=60)

        self.updateName = Label(self.updateFrame, text="Nome", font=(None, 10))
        self.updateName.grid(row=0, column=0, sticky=W)
        self.updateInputName = Entry(self.updateFrame, font=(None, 10), width=10)
        self.updateInputName.grid(row=0, column=1, padx=(0, 10), sticky=W)

        self.updateSurname = Label(self.updateFrame, text="Cognome", font=(None, 10))
        self.updateSurname.grid(row=0, column=2, sticky=W)
        self.updateInputSurname = Entry(self.updateFrame, font=(None, 10), width=10)
        self.updateInputSurname.grid(row=0, column=3, padx=(0, 10), sticky=W)

        self.updateDateOfBirth = Label(self.updateFrame, text="Data di nascita", font=(None, 10))
        self.updateDateOfBirth.grid(row=0, column=4, sticky=W)
        self.updateInputDateOfBirth = Entry(self.updateFrame, font=(None, 10), width=10)
        self.updateInputDateOfBirth.grid(row=0, column=5, padx=(0, 10), sticky=W)

        self.updateGender = Label(self.updateFrame, text="Genere", font=(None, 10))
        self.updateGender.grid(row=0, column=6, sticky=W)
        self.updateInputGender = Entry(self.updateFrame, font=(None, 10), width=10)
        self.updateInputGender.grid(row=0, column=7, sticky=W)

        self.updateCompNum = Label(self.updateFrame, text="Pettorina", font=(None, 10))
        self.updateCompNum.grid(row=1, column=0, sticky=W)
        self.updateInputCompNum = Entry(self.updateFrame, font=(None, 10), width=10)
        self.updateInputCompNum.grid(row=1, column=1, padx=(0, 10), sticky=W)

        self.updateCategory = Label(self.updateFrame, text="Categoria", font=(None, 10))
        self.updateCategory.grid(row=1, column=2, sticky=W)
        self.updateInputCategory = ttk.Combobox(self.updateFrame, font=(None, 10), width=10, values=[category.name for category in self.categories])
        self.updateInputCategory.grid(row=1, column=3, padx=(0, 10), sticky=W)

        self.updateTeam = Label(self.updateFrame, text="Squadra", font=(None, 10))
        self.updateTeam.grid(row=1, column=4, sticky=W)
        self.updateInputTeam = ttk.Combobox(self.updateFrame, font=(None, 10), width=10, values=[team.name for team in self.teams])
        self.updateInputTeam.grid(row=1, column=5, padx=(0, 10), sticky=W)

        self.updateButton = Button(self.updateFrame, text="Salva", font=(None, 10), command=self.save)
        self.updateButton.grid(row=1, column=6, padx=(0, 10), sticky=W)

        self.deleteButton = Button(self.updateFrame, text="Elimina", font=(None, 10), command=self.delete)
        self.deleteButton.grid(row=1, column=7, sticky=W)

    def update_list(self):
        self.athletes = self.repoManager.athleteRepository.get(Athlete(name=self.findInputName.get(), surname=self.findInputSurname.get(), comp_num=self.findInputCompNum.get()))
        self.listListbox.delete(0, END)
        for athlete in self.athletes:
            line = []
            if athlete.name:
                line.append(str(athlete.name))
            if athlete.surname:
                line.append(str(athlete.surname))
            if athlete.dateOfBirth:
                line.append(datetime.strptime(str(athlete.dateOfBirth), "%Y-%m-%d").strftime("%d/%m/%Y"))
            if athlete.gender:
                line.append("M" if str(athlete.gender) == "MALE" else "F")
            if athlete.compNum:
                line.append(str(athlete.compNum))

            category = [category.name for category in self.categories if athlete.categoryId == category.categoryId]
            team = [team.name for team in self.teams if athlete.teamId == team.teamId]

            category = category[0] if len(category) else None
            team = team[0] if len(team) else None

            if category:
                line.append(str(category))
            if team:
                line.append(str(team))

            a = "  ".join(line)

            self.listListbox.insert(END, a)

    def update_update(self, event=None):
        self.updateInputName.delete(0, END)
        self.updateInputSurname.delete(0, END)
        self.updateInputDateOfBirth.delete(0, END)
        self.updateInputGender.delete(0, END)
        self.updateInputCompNum.delete(0, END)
        self.updateInputCategory.delete(0, END)
        self.updateInputTeam.delete(0, END)

        if len(self.listListbox.curselection()):
            self.selectedAthlete = self.listListbox.curselection()[0]

            name = self.athletes[self.selectedAthlete].name
            surname = self.athletes[self.selectedAthlete].surname
            date_of_birth = str(self.athletes[self.selectedAthlete].dateOfBirth)
            gender = self.athletes[self.selectedAthlete].gender
            comp_num = str(self.athletes[self.selectedAthlete].compNum)
            category = [category.name for category in self.categories if self.athletes[self.selectedAthlete].categoryId == category.categoryId]
            team = [team.name for team in self.teams if self.athletes[self.selectedAthlete].teamId == team.teamId]

            category = category[0] if len(category) else None
            team = team[0] if len(team) else None

            if name != "None":
                self.updateInputName.insert(0, name)
            if surname != "None":
                self.updateInputSurname.insert(0, surname)
            if date_of_birth != "None":
                self.updateInputDateOfBirth.insert(0, datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%d/%m/%Y"))
            if gender != "None":
                self.updateInputGender.insert(0, "M" if gender == "MALE" else "F")
            if comp_num != "None":
                self.updateInputCompNum.insert(0, comp_num)
            if category:
                self.updateInputCategory.set(category)
            if team:
                self.updateInputTeam.set(team)

    def save(self):
        if self.selectedAthlete > -1:

            gender = self.updateInputGender.get()
            if gender:
                if gender[0].lower() == "m":
                    gender = "MALE"
                elif gender[0].lower() == "f":
                    gender = "FEMALE"
                else:
                    gender=None

            date_of_birth = ""
            try:
                date_of_birth = datetime.strptime(self.updateInputDateOfBirth.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            except:
                pass

            athlete = Athlete(athlete_id=self.athletes[self.selectedAthlete].athleteId,
                              name=self.updateInputName.get(),
                              surname=self.updateInputSurname.get(),
                              date_of_birth=date_of_birth,
                              gender=gender,
                              comp_num=self.updateInputCompNum.get(),
                              category_id=self.categories[self.updateInputCategory.current()].categoryId,
                              team_id=self.teams[self.updateInputTeam.current()].teamId)

            self.repoManager.athleteRepository.update(athlete)
            self.update_list()

    def delete(self):
        if self.selectedAthlete > -1:
            answer = askquestion("Cancella", "Sei sicuro di volerlo cancellare?", icon='warning')
            if answer == 'yes':
                athlete = Athlete(athlete_id=self.athletes[self.selectedAthlete].athleteId)
                self.repoManager.athleteRepository.remove(athlete)
                self.update_list()
                self.update_update()