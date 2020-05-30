from dialogue_generator import *
import file_loader
import tkinter as tk

class App:
    def __init__(self):
        # init window
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.resizable(1, 1)
        self.window['background'] = "#101010"
        self.window.title("Diagen")

        # add menubar
        self.menubar = tk.Menu(self.window)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.reset_window)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save as", command=self.save_file_as)
        self.filemenu.add_command(label="Exit", command=self.close_window)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Insert node", command=self.insert_node)
        self.editmenu.add_command(label="Delete node", command=self.delete_selected_node)
        self.editmenu.add_command(label="Copy node", command=self.copy_node)
        self.editmenu.add_command(label="Paste node", command=self.paste_node)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_command(label="Help", command=self.display_help)

        self.window.config(menu=self.menubar)

        # init nodes
        self.nodes = []

        # init other control variables
        self.filename = None
        self.selected = None

    def reset_window(self):
        for node in self.nodes:
            self.delete_node(node)
        self.filename = None

    def open_file(self):
        pass

    def save_file(self):
        if self.filename:
            file_loader.save_file(filename)
        else:
            self.save_file_as()

    def save_file_as(self):
        pass

    def close_window(self):
        self.window.quit()

    def insert_node(self):
        pass

    def delete_selected_node(self):
        if self.selected:
            self.delete_node(self.selected)

    def delete_node(self, node):
        node.destroy()
        del node

    def copy_node(self):
        pass

    def paste_node(self):
        pass

    def display_help(self):
        pass

    def select_node(self, node):
        self.selected = node

    def unselect_node(self):
        self.selected = None

def main():
    app = App()
    app.window.mainloop()

if __name__ == "__main__":
    main()
