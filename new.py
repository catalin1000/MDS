import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class budgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Applicatie de budgetare")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e1e")

        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.pack(pady=10)

        self.plot()

    def plot(self):
        data = [1, 2, 3, 4]
        labels = ['A', 'B', 'C', 'D']

        fig, ax = plt.subplots()
        ax.bar(labels, data, color='darkorange')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    app = budgetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()