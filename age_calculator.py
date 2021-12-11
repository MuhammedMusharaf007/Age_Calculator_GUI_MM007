from tkinter import *
from datetime import date

home = Tk()
home.geometry('500x500')
home.resizable(0, 0)
home.title('Age Calculator by MM007')
statement = Label(home)

def calculate_age():
    global statement
    statement.destroy()
    today = date.today()
    DateOfBirth = date(int(input_year.get()), int(input_month.get()), int(input_day.get()))
    age = today.year - DateOfBirth.year
    if (today.month < DateOfBirth.month) or (today.month == DateOfBirth.month and today.day <DateOfBirth.day):
        age -= 1
    statement = Label(text=f"{nameValue.get()} is having age = {age}.")
    statement.grid(row = 12, column=1, pady=30)

l_name = Label(text="Name: ")
l_name.grid(row=2, column=0)
nameValue = StringVar()
input_name = Entry(home, textvariable=nameValue)
input_name.grid(row=2, column=2, padx=20, pady=20)

l_year = Label(text="Year of Birth: ")
l_year.grid(row=4, column=0)
yearValue = StringVar()
input_year = Entry(home, textvariable=yearValue)
input_year.grid(row=4, column=2, padx=20, pady=20)

l_month = Label(text="Month of Birth (in number): ")
l_month.grid(row=6, column=0)
monthValue = StringVar()
input_month = Entry(home, textvariable=monthValue)
input_month.grid(row=6, column=2, padx=20, pady=20)

l_day = Label(text="Day of birth: ")
l_day.grid(row=8, column=0)
dayValue = StringVar()
input_day = Entry(home, textvariable=dayValue)
input_day.grid(row=8, column=2, padx=20, pady=20)

click = Button(text="Calculate Age", command=calculate_age)
click.grid(row = 10, column=1)

home.mainloop()