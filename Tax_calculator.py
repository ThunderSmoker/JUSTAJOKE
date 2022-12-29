import tkinter as tk

# Calculate tax based on income and number of dependents
def calculate_tax(income, dependents):
  tax = 0
  if dependents == 1:
    tax = income * 0.05
  elif dependents == 2:
    tax = income * 0.09
  elif dependents > 2:
    tax = income * 0.12
  return tax

# Calculate final tax based on marital status
def calculate_final_tax(tax, marital_status):
  if marital_status == "single":
    final_tax = tax + (tax * 0.15)
  elif marital_status == "double":
    final_tax = tax + (tax * 0.20)
  elif marital_status == "divorce":
    final_tax = tax + (tax * 0.10)
  return final_tax

# Create the main window
window = tk.Tk()
window.title("Tax Calculator")

# Create the income label and input
income_label = tk.Label(text="Income:")
income_label.grid(column=0, row=0)
income_entry = tk.Entry()
income_entry.grid(column=1, row=0)

# Create the dependents label and input
dependents_label = tk.Label(text="Number of Dependents:")
dependents_label.grid(column=0, row=1)
dependents_entry = tk.Entry()
dependents_entry.grid(column=1, row=1)

# Create the marital status label and input
marital_status_label = tk.Label(text="Marital Status (single, double, divorce):")
marital_status_label.grid(column=0, row=2)
marital_status_entry = tk.Entry()
marital_status_entry.grid(column=1, row=2)

# Create the calculate button and bind it to the calculate_tax function
calculate_button = tk.Button(text="Calculate", command=lambda: calculate_tax(int(income_entry.get()), int(dependents_entry.get())))
calculate_button.grid(column=0, row=3)

# Create the final tax label and output
final_tax_label = tk.Label(text="Final Tax:")
final_tax_label.grid(column=0, row=4)
final_tax_output = tk.Label(text="")
final_tax_output.grid(column=1, row=4)

# Start the main loop
window.mainloop()
