import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window():

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('700x900')
        self.root.title('IOT data')
        self.create_layout()

        self.root.mainloop()

    def create_layout(self) -> None:
        self.show_temperature = tk.BooleanVar()
        temperature_checkbox = tk.Checkbutton(
            self.root, text='Temperature', variable=self.show_temperature)
        temperature_checkbox.grid(row=0, column=0)

        self.show_humidity = tk.BooleanVar()
        humidity_checkbox = tk.Checkbutton(
            self.root, text='Humidity', variable=self.show_humidity)
        humidity_checkbox.grid(row=0, column=1)

        self.show_voltage = tk.BooleanVar()
        voltage_checkbox = tk.Checkbutton(
            self.root, text='Voltage', variable=self.show_voltage)
        voltage_checkbox.grid(row=0, column=2)

        date_from_label = tk.Label(self.root, text='From')
        date_from_label.grid(row=1, column=0)
        self.date_from_entry = ttk.Entry(self.root)
        self.date_from_entry.grid(row=1, column=1)

        date_to_label = tk.Label(self.root, text='To')
        date_to_label.grid(row=1, column=2)
        self.date_to_entry = ttk.Entry(self.root)
        self.date_to_entry.grid(row=1, column=3)

        self.info_text = tk.Label(self.root)
        self.info_text.grid(row=2, column=0, columnspan=4)

        show_button = tk.Button(
            self.root, text='Wyświetl wykres', command=self.show_graph)
        show_button.grid(row=3, column=2)

    def show_graph(self):
        if not self.is_valid():
            return
        # Rysowanie wykresu
        fig, ax = plt.subplots(figsize=(6, 3), dpi=80)

        ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
        ax.set_title('Wykres 1')
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, pady=10)

        # Rysowanie wykresu
        fig2, ax2 = plt.subplots(figsize=(6, 3), dpi=80)

        ax2.plot([1, 2, 3, 4], [1, 4, 9, 16])
        ax2.set_title('Wykres 1')
        canvas2 = FigureCanvasTkAgg(fig2, master=self.root)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=5, column=0, columnspan=4, pady=10)

        fig3, ax3 = plt.subplots(figsize=(6, 3), dpi=80)

        ax3.plot([1, 2, 3, 4], [1, 4, 9, 16])
        ax3.set_title('Wykres 1')
        canvas3 = FigureCanvasTkAgg(fig3, master=self.root)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=6, column=0, columnspan=4, pady=10)

    def is_valid_date(self, date_text: str) -> bool:
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S'):
                raise ValueError
            return True
        except ValueError:
            return False

    def is_valid(self) -> bool:
        checkboxes = [self.show_humidity.get(),
                      self.show_temperature.get(), self.show_temperature.get()]

        print(checkboxes)

        if not (True in checkboxes):
            self.info_text.config(
                text="Zaznacz przynajmniej jeden typ wykresu")
            return False

        print(self.date_from_entry.get())
        if self.date_from_entry.get() != "" and not self.is_valid_date(self.date_from_entry.get()):
            self.info_text.config(
                text="Poprawny format daty: 2010-12-30 13:00:00")
            return False

        if self.date_to_entry.get() != "" and not self.is_valid_date(self.date_to_entry.get()):
            self.info_text.config(
                text="Poprawny format daty: 2010-12-30 13:00:00")
            return False

        return True


Window()
