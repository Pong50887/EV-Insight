import csv
import tkinter as tk

data = """
,Battery,Car_name,Car_name_link,Efficiency,Fast_charge,Price.DE.,Range,Top_speed,acceleration..0.100.
0,75.0,Tesla Model Y Long Range Dual Motor,https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-Dual-Motor,172,670.0,59017.0,435,217,5.0
1,57.5,Tesla Model 3,https://ev-database.org/car/1991/Tesla-Model-3,137,700.0,46220.0,420,201,6.1
2,60.5,BYD ATTO 3,https://ev-database.org/car/1782/BYD-ATTO-3,183,370.0,44625.0,330,160,7.3
"""

# Parse the CSV data
rows = [row.strip().split(',') for row in data.strip().split('\n')]

# Extract the data except the link
text_data = '\n'.join(','.join(row[1:]) for row in rows)

# Create the tkinter window
window = tk.Tk()

# Create and place the text box
text_box = tk.Text(window, width=80, height=10)
text_box.insert(tk.END, text_data)
text_box.grid(row=1, columnspan=5, padx=10, pady=10, sticky="SEW")

# Run the tkinter event loop
window.mainloop()
