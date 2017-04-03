from tkinter import *
#Author: Pomo

class RegisterAthlete(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		#Frame.pack()
		self.name = ""
		self.surname = ""
		self.birth = ""
		self.gender = ""
		
			#nome
		self.name_frame = Frame(self)
		self.name_frame.pack()
		self.name_label = Label(self.name_frame, text = "Name")
		self.name_label.pack(side = LEFT)
		self.name_input = Text(self.name_frame)
		self.name_input["height"] = 1
		#self.name_input["width"] = 40
		self.name_input.config(highlightbackground="black")
		self.name_input.pack(side = LEFT)
			#cognome
		self.sur_frame = Frame(self)
		self.sur_frame.pack()
		self.sur_label = Label(self.sur_frame, text = "Surname")
		self.sur_label.pack(side = LEFT)
		self.sur_input = Text(self.sur_frame)
		self.sur_input["height"] = 1
		#self.sur_input["width"] = 40
		self.sur_input.config(highlightbackground="black")
		self.sur_input.pack(side = LEFT)
			#data di nascita
		self.date_frame = Frame(self)
		self.date_frame.pack()
		self.date_label = Label(self.date_frame, text = "Birthday")
		self.date_label.pack(side = LEFT)
		self.date_input = Text(self.date_frame)
		self.date_input["height"] = 1
		#self.date_input["width"] = 10
		self.date_input.config(highlightbackground="black")
		self.date_input.pack(side = LEFT)
			#gender
		self.gender_frame = Frame(self)
		self.gender_frame.pack()
		self.gender_label = Label(self.gender_frame, text = "Gender")
		self.gender_label.pack(side = LEFT)
		self.gender_type = StringVar()
		self.gender_type.set("Male")
		self.gender_choice = OptionMenu(self.gender_frame, self.gender_type, "Female")
		self.gender_choice.pack(side = LEFT)
			#errors
		self.error_label = Label(self)
		self.error_label["height"] = 3
		self.error_label.pack()
			#button
		self.confirm_button = Button(self)
		self.confirm_button["text"] = "Confirm"
		self.confirm_button.bind("<Button-1>", self.conferma)
		self.confirm_button.pack()

	def conferma(self, event):
		error = ""
		self.name = self.name_input.get("1.0","end-1c")
		self.surname = self.sur_input.get("1.0","end-1c")
		self.birth = self.date_input.get("1.0","end-1c")
		self.gender = self.gender_type.get()
		if self.name is "":
			error += "Name is missing\n"
		if self.surname is "":
			error += "Surname is missing\n"
		if self.birth is "":
			error += "Date of birth is missing"
		self.error_label.config(text = error)


#Just to debug
main = Tk()
start = RegisterAthlete(main)
start.pack()
main.mainloop()
