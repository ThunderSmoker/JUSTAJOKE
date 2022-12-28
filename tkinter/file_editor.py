from tkinter import *
from tkinter import filedialog

# Create the main window
master = Tk()
master.title("Text Editor")

# Create the filename entry field
filename_label = Label(master, text="Filename:")
filename_entry = Entry(master)
filename_label.pack(side="left")
filename_entry.pack(side="left")

# Create the text widget and scrollbar
text_widget = Text(master)
scrollbar = Scrollbar(master)
text_widget.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Configure the scrollbar to work with the text widget
text_widget.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=text_widget.yview)


def open_file():
    # Open a file dialog and get the selected file
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    # Open the file and read its contents
    with open(filepath, "r") as f:
        text = f.read()

    # Update the text widget with the file contents
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", text)

    # Update the filename entry field with the file path
    filename_entry.delete(0, "end")
    filename_entry.insert(0, filepath)


def save_file():
    # Get the contents of the text widget
    text = text_widget.get("1.0", "end")

    # Get the file path from the filename entry field
    filepath = filename_entry.get()

    # Write the contents to the file
    with open(filepath, "w") as f:
        f.write(text)


def new_file():
    # Clear the text widget and the filename entry field
    text_widget.delete("1.0", "end")
    filename_entry.delete(0, "end")


# Create the Open, Save, and New buttons
open_button = Button(master, text="Open", command=open_file)
save_button = Button(master, text="Save", command=save_file)
new_button = Button(master, text="New", command=new_file)
open_button.pack(side="left")
save_button.pack(side="left")
new_button.pack(side="left")


# Radiobutton(master, text="Red", fg='crimson', padx=10,
#             variable=vars, value=2).grid(row=1, column=2)
# Radiobutton(master, text="Others", fg='black', padx=15,
#             variable=vars, value=3).grid(row=1, column=2)

# Define the callback functions for the buttons

# Run the main loop
master.mainloop()