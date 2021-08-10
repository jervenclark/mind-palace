from __future__ import absolute_import
import tkinter as tk


def main():
    window = tk.Tk()
    greeting = tk.Label(text="Zettelkasten")
    greeting.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
