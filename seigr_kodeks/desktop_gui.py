import tkinter as tk
from tkinter import scrolledtext
from seigr_kodeks.parsers.format_detector import detect_format
from markdown import markdown
from tkinter import messagebox

def convert_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to convert.")
        return
    
    detected_format, converted_text = detect_format(input_text)
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.INSERT, converted_text)
    output_text.config(state=tk.DISABLED)
    
    status_label.config(text=f"Converted from {detected_format}", fg="green")

# Create the main application window
root = tk.Tk()
root.title("SeigrKodeks - Markdown Converter")
root.geometry("800x600")

# Input Text Area
label_input = tk.Label(root, text="Enter MediaWiki or Markdown:")
label_input.pack()
text_input = scrolledtext.ScrolledText(root, height=10)
text_input.pack(fill=tk.BOTH, expand=True)

# Convert Button
convert_button = tk.Button(root, text="Convert to Markdown", command=convert_text)
convert_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# Output Text Area
label_output = tk.Label(root, text="Converted Markdown:")
label_output.pack()
output_text = scrolledtext.ScrolledText(root, height=10, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True)

# Run the GUI loop
root.mainloop()
