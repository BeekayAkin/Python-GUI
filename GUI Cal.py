import tkinter as tk
import math

root=tk.Tk()
root.title("Simple Calculator")

entry1=tk.Entry(root)
entry1.grid(row=0,column=0,padx=5,pady=5)

entry2=tk.Entry(root)
entry2.grid(row=1,column=0,padx=5,pady=5)
def cle():
    entry1.delete(0)
    entry2.delete(0)
clear_button=tk.Button(root,text="Clear",command=cle)
clear_button.grid(row=4,column=2,padx=5,pady=5)
def exi():
    root.destroy()
exit=tk.Button(root, command=exi,text="Exit",)
exit.grid(row=5, column=2, padx=5,pady=5)

operations=[
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Square Root",
    "Power",
    "Logarithm"
]
row_val= 2
for operation in operations:
    operation_button = tk.Button(root, text=operation, command=lambda op=operation: calculator(op))
    operation_button.grid(row=row_val, column=0, columnspan=2, padx=5,pady=5)
    row_val +=1


result_label=tk.Label(root)
result_label.grid(row=row_val,column=0, columnspan=2)
def calculator(operation):
    try:
        if operation == "Add":
            result= float(entry1.get())+float(entry2.get())
        elif operation == "Subtract":
            result= float(entry1.get())-float(entry2.get())
        elif operation =="Multiply":
            result=float(entry1.get())*float(entry2.get())
        elif operation == "Divide":
            num2=float(entry2.get())
            if num2 == 0:
                result= "Can not divide by zero!"
            else:
                result=float(entry1.get())/num2
        elif operation == "Square Root":
            result= math.sqrt(float(entry1.get()))
        elif operation == "Power":
            result=(float(entry1.get())) ** float(entry2.get())
        elif operation == "Logarithm":
            result=math.log(float(entry1.get()))
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid Input")
root.mainloop()