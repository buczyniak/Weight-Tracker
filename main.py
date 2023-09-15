from tkinter import *
import pandas as pd
from datetime import datetime
from charts import show_charts


### constants
FONT_TITLE = "Times 14 bold"
FONT_SUBTITLE = "Times 12"
FONT_TEXT = "Times 10"

### calculate differences between two records
def get_difference():
    excel_file = pd.read_excel("Weight Tracker.xlsx", engine='openpyxl')
    if len(excel_file) >= 2:
        last_row = excel_file.iloc[-1]
        prev_row = excel_file.iloc[-2]
    ### calculate the differences
        weight_diff = round(last_row['Weight'] - prev_row['Weight'], 2)
        fat_diff = round(last_row['Fat'] - prev_row['Fat'], 2)
        muscle_diff = round(last_row['Muscle'] - prev_row['Muscle'], 2)
        neck_diff = round(last_row['Neck'] - prev_row['Neck'], 2)
        biceps_diff = round(last_row['Biceps'] - prev_row['Biceps'], 2)
        chest_diff = round(last_row['Chest'] - prev_row['Chest'], 2)
        waist_diff = round(last_row['Waist'] - prev_row['Waist'], 2)
        belly_diff = round(last_row['Belly'] - prev_row['Belly'], 2)
        hips_diff = round(last_row['Hips'] - prev_row['Hips'], 2)
        thighs_diff = round(last_row['Thighs'] - prev_row['Thighs'], 2)
        calves_diff = round(last_row['Calves'] - prev_row['Calves'], 2)
        visceral_diff = round(last_row['Visceral Fat'] - prev_row['Visceral Fat'], 2)


    ### update the labels
        if weight_diff > 0:
            label_weight.config(text=f"Compared to last record: +{weight_diff}", fg="red")
        else:
            label_weight.config(text=f"Compared to last record: {weight_diff}", fg="green")

        if fat_diff > 0:
            label_fat.config(text=f"Compared to last record: +{fat_diff}", fg="red")
        else:
            label_fat.config(text=f"Compared to last record: {fat_diff}", fg="green")

        if muscle_diff < 0:
            label_muscle.config(text=f"Compared to last record: {muscle_diff}", fg="red")
        else:
            label_muscle.config(text=f"Compared to last record: +{muscle_diff}", fg="green")

        if neck_diff > 0:
            label_neck.config(text=f"Compared to last record: +{neck_diff}", fg="red")
        else:
            label_neck.config(text=f"Compared to last record: {neck_diff}", fg="green")

        if biceps_diff < 0:
            label_biceps.config(text=f"Compared to last record: {biceps_diff}", fg="red")
        else:
            label_biceps.config(text=f"Compared to last record: +{biceps_diff}", fg="green")

        if chest_diff > 0:
            label_chest.config(text=f"Compared to last record: +{chest_diff}", fg="red")
        else:
            label_chest.config(text=f"Compared to last record: {chest_diff}", fg="green")

        if waist_diff > 0:
            label_waist.config(text=f"Compared to last record: +{waist_diff}", fg="red")
        else:
            label_waist.config(text=f"Compared to last record: {waist_diff}", fg="green")

        if belly_diff > 0:
            label_belly.config(text=f"Compared to last record: +{belly_diff}", fg="red")
        else:
            label_belly.config(text=f"Compared to last record: {belly_diff}", fg="green")

        if hips_diff > 0:
            label_hips.config(text=f"Compared to last record: +{hips_diff}", fg="red")
        else:
            label_hips.config(text=f"Compared to last record: {hips_diff}", fg="green")

        if thighs_diff > 0:
            label_thighs.config(text=f"Compared to last record: +{thighs_diff}", fg="red")
        else:
            label_thighs.config(text=f"Compared to last record: {thighs_diff}", fg="green")

        if calves_diff > 0:
            label_calves.config(text=f"Compared to last record: +{calves_diff}", fg="red")
        else:
            label_calves.config(text=f"Compared to last record: {calves_diff}", fg="green")

        if visceral_diff > 0:
            label_visceral.config(text=f"Compared to last record: +{visceral_diff}", fg="red")
        else:
            label_visceral.config(text=f"Compared to last record: {visceral_diff}", fg="green")


### save values to a file
def save_values():

    ### get all numbers
    num_weight = float(entry3.get())
    num_fat = float(entry4.get())
    num_muscle = float(entry5.get())
    num_neck = float(entry6.get())
    num_biceps = float(entry7.get())
    num_chest = float(entry8.get())
    num_belly = float(entry10.get())
    num_waist = float(entry9.get())
    num_hips = float(entry11.get())
    num_thighs = float(entry12.get())
    num_calves = float(entry13.get())
    num_visceral = float(entry15.get())

    ### open excel file
    try:
        excel_file = pd.read_excel("Weight Tracker.xlsx")
        data = pd.DataFrame({
            "Date": datetime.now(),
            "Weight": [num_weight],
            "Fat": [num_fat],
            "Muscle": [num_muscle],
            "Neck": [num_neck],
            "Biceps": [num_biceps],
            "Chest": [num_chest],
            "Waist": [num_waist],
            "Belly": [num_belly],
            "Hips": [num_hips],
            "Thighs": [num_thighs],
            "Calves": [num_calves],
            "Visceral Fat": [num_visceral]
        })
        data = pd.concat([excel_file, data], ignore_index=True)

    except FileNotFoundError:
        data = pd.DataFrame({
            "Date": datetime.now(),
            "Weight": [num_weight],
            "Fat": [num_fat],
            "Muscle": [num_muscle],
            "Neck": [num_neck],
            "Biceps": [num_biceps],
            "Chest": [num_chest],
            "Waist": [num_waist],
            "Belly": [num_belly],
            "Hips": [num_hips],
            "Thighs": [num_thighs],
            "Calves": [num_calves],
            "Visceral Fat": [num_visceral]
        })

    ### save data to excel
    data.to_excel("Weight Tracker.xlsx", index=False)
    label_result.config(text="Data successfully saved to the file!")
    get_difference()

    button_close = Button(text="Close window", command=window.destroy)
    button_close.grid(column=2, row=16)

    button_charts = Button(text="Show charts", command=show_charts)
    button_charts.grid(column=3, row=16)


### window settings
window = Tk()
window.title("Weight tracker")
window.config(bg="white")
window.geometry("580x390")

### add labels and entry spaces
label1 = Label(text="Welcome to Weight Tracker", font=FONT_TITLE, bg="white")
label1.grid(column=2, row=0)

label2 = Label(text="Please enter your numbers:", font=FONT_SUBTITLE, bg="white")
label2.grid(column=2, row=1)

label3 = Label(text="Weight (kg):", font=FONT_TEXT, bg="white")
label3.grid(column=1, row=2, pady=10)
entry3 = Entry()
entry3.grid(column=1, row=3, padx=10)
label_weight = Label(text="", bg="white")
label_weight.grid(column=1, row=4)

label4 = Label(text="Fat (%):", font=FONT_TEXT, bg="white")
label4.grid(column=1, row=5)
entry4 = Entry()
entry4.grid(column=1, row=6)
label_fat = Label(text="", bg="white")
label_fat.grid(column=1, row=7)

label5 = Label(text="Muscles (kg):", font=FONT_TEXT, bg="white")
label5.grid(column=1, row=8)
entry5 = Entry()
entry5.grid(column=1, row=9)
label_muscle = Label(text="", bg="white")
label_muscle.grid(column=1, row=10)

label6 = Label(text="Neck (cm):", font=FONT_TEXT, bg="white")
label6.grid(column=1, row=11)
entry6 = Entry()
entry6.grid(column=1, row=12)
label_neck = Label(text="", bg="white")
label_neck.grid(column=1, row=13)

label7 = Label(text="Biceps (cm):", font=FONT_TEXT, bg="white")
label7.grid(column=2, row=2)
entry7 = Entry()
entry7.grid(column=2, row=3)
label_biceps = Label(text="", bg="white")
label_biceps.grid(column=2, row=4)

label8 = Label(text="Chest (cm):", font=FONT_TEXT, bg="white")
label8.grid(column=2, row=5)
entry8 = Entry()
entry8.grid(column=2, row=6)
label_chest = Label(text="", bg="white")
label_chest.grid(column=2, row=7)

label9 = Label(text="Waist (cm):", font=FONT_TEXT, bg="white")
label9.grid(column=2, row=8)
entry9 = Entry()
entry9.grid(column=2, row=9)
label_waist = Label(text="", bg="white")
label_waist.grid(column=2, row=10)

label10 = Label(text="Belly (cm):", font=FONT_TEXT, bg="white")
label10.grid(column=2, row=11)
entry10 = Entry()
entry10.grid(column=2, row=12)
label_belly = Label(text="", bg="white")
label_belly.grid(column=2, row=13)

label11 = Label(text="Hips (cm):", font=FONT_TEXT, bg="white")
label11.grid(column=3, row=2)
entry11 = Entry()
entry11.grid(column=3, row=3)
label_hips = Label(text="", bg="white")
label_hips.grid(column=3, row=4)

label12 = Label(text="Thighs (cm):", font=FONT_TEXT, bg="white")
label12.grid(column=3, row=5)
entry12 = Entry()
entry12.grid(column=3, row=6)
label_thighs = Label(text="", bg="white")
label_thighs.grid(column=3, row=7)

label13 = Label(text="Calves (cm):", font=FONT_TEXT, bg="white")
label13.grid(column=3, row=8)
entry13 = Entry()
entry13.grid(column=3, row=9)
label_calves = Label(text="", bg="white")
label_calves.grid(column=3, row=10)

label15 = Label(text="Visceral Fat:", font=FONT_TEXT, bg="white")
label15.grid(column=3, row=11)
entry15 = Entry()
entry15.grid(column=3, row=12)
label_visceral = Label(text="", bg="white")
label_visceral.grid(column=3, row=13)

button1 = Button(text="Save values", command=save_values)
button1.grid(column=2, row=14)

label_result = Label(text="", bg="white")
label_result.grid(column=2, row=15)

window.mainloop()
