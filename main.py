import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not file_path:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(file_path, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {file_path}")


def save_file(window, text_edit):
    file_path = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not file_path:
        return
    
    with open(file_path, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {file_path}")

def main():
    window = tk.Tk()
    window.title("Text Editor")

    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 16")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))


    window.mainloop()

if __name__ == "__main__":
    main()