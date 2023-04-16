from tkinter import *

class TextEditor:
 
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
 
        self.text = Text(master)
        self.text.pack()
 
        self.text.bind("<Key>", self.highlight)
        self.text.bind("<KeyRelease>", self.highlight)

    
    def highlight(self, event):
        mapping = {
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
    
        cursor_pos = self.text.index("insert")

        for i in range(1, int(self.text.index("end").split(".")[0]) + 1):
            line_start = f"{i}.0"
            line_end = f"{i}.end"
            line_text = self.text.get(line_start, line_end)
            #print("Line:",line_text)
            for j, char in enumerate(line_text):
                if char.isalnum():
                    color = mapping.get(char.lower(), "black")
                    tag_name = f"color-{char}-{color}".replace(" ", "")
                    start_pos = f"{i}.{j}"
                    end_pos = f"{i}.{j+1}"
                    self.text.tag_add(tag_name, start_pos, end_pos)
                    self.text.tag_config(tag_name, foreground=color)
        self.text.mark_set("insert", self.text.index("insert"))
            
root = Tk()
text_editor = TextEditor(root)
root.mainloop()
