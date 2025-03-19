import tkinter as tk
from tkinter import ttk

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        if from_unit == to_unit:
            result.set(f"Same unit: {temp:.2f} {to_unit}")
            return
        
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                converted = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                converted = temp + 273.15

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                converted = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                converted = (temp - 32) * 5/9 + 273.15

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                converted = temp - 273.15
            elif to_unit == "Fahrenheit":
                converted = (temp - 273.15) * 9/5 + 32

        result.set(f"{converted:.2f} {to_unit}")
    except ValueError:
        result.set("Invalid input!")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# UI Components
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

tk.Label(root, text="Convert From:", font=("Arial", 12)).pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12))
combo_from.pack(pady=5)
combo_from.current(0)

tk.Label(root, text="Convert To:", font=("Arial", 12)).pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12))
combo_to.pack(pady=5)
combo_to.current(1)

btn_convert = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature)
btn_convert.pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14, "bold")).pack(pady=5)

# Run the app
root.mainloop()
