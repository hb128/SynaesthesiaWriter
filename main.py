from tkinter import *
from tkinter import filedialog
import tkinter.font as tkfont
import json

class TextEditor:
 
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
 
        self.color_mapping = {
            "a": "#DE1919",
            "b": "blue",
            "c": "green",
            "d": "orange",
            "e": "purple",
            "f": "brown",
            "g": "grey",
            "h": "pink",
            "i": "cyan",
            "j": "magenta",
            "k": "yellow",
            "l": "olive",
            "m": "navy",
            "n": "teal",
            "o": "maroon",
            "p": "lime",
            "q": "silver",
            "r": "aqua",
            "s": "fuchsia",
            "t": "indigo",
            "u": "violet",
            "v": "khaki",
            "w": "turquoise",
            "x": "coral",
            "y": "gold",
            "z": "orchid",
            "0": "red",
            "1": "blue",
            "2": "green",
            "3": "orange",
            "4": "purple",
            "5": "brown",
            "6": "grey",
            "7": "pink",
            "8": "cyan",
            "9": "magenta",
        }
        self.text = Text(master)
        self.text.pack()
 
        self.text.bind("<Key>", self.highlight)
        self.text.bind("<KeyRelease>", self.highlight)
        self.setup_menu()

    def setup_menu(self):
        menu_bar = Menu(self.master)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu_bar.add_cascade(label="File", menu=file_menu)
        format_menu = Menu(menu_bar, tearoff=0)
        format_menu.add_checkbutton(label="Bold", command=self.toggle_bold)
        format_menu.add_checkbutton(label="Italic", command=self.toggle_italic)
        format_menu.add_checkbutton(label="Underline", command=self.toggle_underline)
        format_menu.add_command(label="Font", command=self.choose_font)
        menu_bar.add_cascade(label="Format", menu=format_menu)       
        config_menu = Menu(menu_bar, tearoff=0)
        config_menu.add_command(label="Load color mapping", command=self.load_color_mapping)
        config_menu.add_command(label="Save color mapping", command=self.save_color_mapping)
        menu_bar.add_cascade(label="Color mapping", menu=config_menu)
        self.master.config(menu=menu_bar)
    
    def choose_font(self):
        font_tuple = tkfont.Font(font=self.text['font']).actual()
        font_name = font_tuple['family']
        font_size = font_tuple['size']
        new_font = tkfont.families()
        new_font_window = Toplevel(self.master)
        new_font_window.title("Choose Font")
        new_font_label = Label(new_font_window, text="Choose a font:")
        new_font_label.grid(row=0, column=0, padx=5, pady=5)
        new_font_var = StringVar(value=font_name)
        new_font_listbox = Listbox(new_font_window, listvariable=new_font_var, height=8)
        new_font_listbox.grid(row=1, column=0, padx=5, pady=5)
        new_font_scrollbar = Scrollbar(new_font_window)
        new_font_scrollbar.grid(row=1, column=1, sticky='NS')
        new_font_listbox.config(yscrollcommand=new_font_scrollbar.set)
        new_font_scrollbar.config(command=new_font_listbox.yview)
        for font in new_font:
            new_font_listbox.insert(END, font)
        new_font_size_label = Label(new_font_window, text="Choose a font size:")
        new_font_size_label.grid(row=2, column=0, padx=5, pady=5)
        new_font_size_var = IntVar(value=font_size)
        new_font_size_spinbox = Spinbox(new_font_window, from_=1, to=72, textvariable=new_font_size_var, width=5)
        new_font_size_spinbox.grid(row=3, column=0, padx=5, pady=5)
        new_font_ok_button = Button(new_font_window, text="OK", command=lambda: self.change_font(new_font_listbox.get(ACTIVE), new_font_size_var.get()))
        new_font_ok_button.grid(row=4, column=0, padx=5, pady=5)

    def change_font(self, font_name, font_size):
        self.text.config(font=(font_name, font_size))
    
    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r") as file:
                self.text.delete(1.0, END)
                self.text.insert(END, file.read())
    
    def save_file(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            with open(filename, "w") as file:
                file.write(self.text.get(1.0, END))
                
    def toggle_bold(self):
        bold_tag = "bold"
        if self.text.tag_ranges(bold_tag):
            self.text.tag_remove(bold_tag, "sel.first", "sel.last")
        else:
            self.text.tag_add(bold_tag, "sel.first", "sel.last")
            self.text.tag_config(bold_tag, font=("TkDefaultFont", 12, "bold"))
    
    def toggle_italic(self):
        italic_tag = "italic"
        if self.text.tag_ranges(italic_tag):
            self.text.tag_remove(italic_tag, "sel.first", "sel.last")
        else:
            self.text.tag_add(italic_tag, "sel.first", "sel.last")
            self.text.tag_config(italic_tag, font=("TkDefaultFont", 12, "italic"))
    
    def toggle_underline(self):
        underline_tag = "underline"
        if self.text.tag_ranges(underline_tag):
            self.text.tag_remove(underline_tag, "sel.first", "sel.last")
        else:
            self.text.tag_add(underline_tag, "sel.first", "sel.last")
            self.text.tag_config(underline_tag, underline=1)
                
    def save_color_mapping(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            with open(filename, 'w') as f:
                json.dump(self.color_mapping, f)
    
    def load_color_mapping(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, 'r') as f:
                self.color_mapping = json.load(f)
            self.highlight(None)
            
    def highlight(self, event):    
        cursor_pos = self.text.index("insert")
        for i in range(1, int(self.text.index("end").split(".")[0]) + 1):
            line_start = f"{i}.0"
            line_end = f"{i}.end"
            line_text = self.text.get(line_start, line_end)
            #print("Line:",line_text)
            for j, char in enumerate(line_text):
                if char.isalnum():
                    color = self.color_mapping.get(char.lower(), "black")
                    tag_name = f"color-{char}-{color}".replace(" ", "")
                    start_pos = f"{i}.{j}"
                    end_pos = f"{i}.{j+1}"
                    self.text.tag_add(tag_name, start_pos, end_pos)
                    self.text.tag_config(tag_name, foreground=color)
        self.text.mark_set("insert", self.text.index("insert"))
            

def main():
    root = Tk()
    text_editor = TextEditor(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        # Close the window and terminate the program
        root.destroy()

if __name__ == '__main__':
    main()