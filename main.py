from tkinter import *
from tkinter import messagebox
from datetime import datetime

window = Tk()
window.title("Days Counter for My Lovely Rose")
window.config(width=1024, height=800, padx=50, pady=50)


# ---------------------------- Button Function ------------------------------- #
def calculate_days():
    try:
        date_start = entry_start.get()
        date_end = entry_end.get()

        date_start_parsed = datetime.strptime(date_start, "%m%d%y")
        date_end_parsed = datetime.strptime(date_end, "%m%d%y")
    except ValueError:
        messagebox.showinfo(title="Date format", message="Date format must be in MMDDYY Your birthday is 083180")
    else:
        days_calculated = date_end_parsed - date_start_parsed
        days_calculated_int = days_calculated.days + 1

        if checkbutton_start_checked_state.get() == 0:
            days_calculated_int += -1
        if checkbutton_end_checked_state.get() == 0:
            days_calculated_int += -1

        label_days.config(text=f"{days_calculated_int:,} day(s)")


# Checkbutton function
def checkbutton_used():
    calculate_days()
    # Prints 1 if On button checked, otherwise 0
    # print(checkbutton_start_checked_state.get())
    # print(checkbutton_end_checked_state.get())


# ---------------------------- UI SETUP ------------------------------- #
label_days = Label(text="00 day(s)", pady=20, font=("arial", 50, "bold"))
label_start = Label(text="START DATE")
label_end = Label(text="END DATE")

entry_start = Entry(width=30, justify=RIGHT)
entry_start.config(width=10)
entry_start.focus()
entry_end = Entry(width=30, justify=RIGHT)
entry_end.config(width=10)
# entry_start.insert(END, string="Some text to begin with.")

# variable to hold on to checked state, 0 is off, 1 is on.
checkbutton_start_checked_state = IntVar()
checkbutton_start_checked_state.set(1)
checkbutton_start = Checkbutton(text="Include?", variable=checkbutton_start_checked_state, command=checkbutton_used)
checkbutton_end_checked_state = IntVar()
checkbutton_end = Checkbutton(text="Include?", variable=checkbutton_end_checked_state, command=checkbutton_used)
checkbutton_end_checked_state.set(1)

button_calculate = Button(text="Calculate", width=20, height=2, command=calculate_days)

label_days.grid(row=0, column=0, columnspan=2)
label_start.grid(row=1, column=0)
label_end.grid(row=1, column=1)
entry_start.grid(row=2, column=0)
entry_end.grid(row=2, column=1)
checkbutton_start.grid(row=3, column=0)
checkbutton_end.grid(row=3, column=1)
button_calculate.grid(row=4, column=0, columnspan=2)
window.mainloop()
