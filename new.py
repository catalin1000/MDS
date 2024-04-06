import customtkinter as ctk


class BarChartApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bar Chart App")
        self.geometry("600x400")

        # Create a frame to hold the chart
        self.chart_frame = ctk.CTkFrame(self, width=400, height=300)
        self.chart_frame.pack(padx=20, pady=20)

        # Input field labels
        self.input_labels = ["Bar 1:", "Bar 2:", "Bar 3:", "Bar 4:"]

        # Entry widgets to store user input
        self.data_entries = []
        for label_text in self.input_labels:
            label = ctk.CTkLabel(self, text=label_text)
            label.pack()

            entry = ctk.CTkEntry(self, width=50)
            entry.pack()
            self.data_entries.append(entry)

        # Button to trigger data update
        self.update_button = ctk.CTkButton(self, text="Update Chart", command=self.update_data)
        self.update_button.pack(pady=10)

        # Initial data (replace with empty list if no default values)
        self.data = [1, 2, 3, 5]

        self.draw_bars()

    def update_data(self):
        # Get user input from entry widgets
        user_data = []
        for entry in self.data_entries:
            try:
                value = int(entry.get())
                user_data.append(value)
            except ValueError:
                # Handle empty input: use previous value or default value (0 here)
                if len(user_data) > 0:
                    user_data.append(user_data[-1])
                else:
                    user_data.append(0)

        # Update data with user input or previous values
        self.data = [user_data[i] if i < len(user_data) else self.data[i - 1] for i in range(len(self.input_labels))]

        # Clear and redraw the chart
        self.draw_bars()

    def draw_bars(self):
        # Get the canvas within the frame
        canvas = self.chart_frame._canvas

        # Clear any existing elements
        canvas.delete("all")

        # Define bar width and spacing
        bar_width = 50
        bar_spacing = 20

        # Calculate starting position for the first bar
        x = bar_spacing

        # Draw each bar with its corresponding color and height
        bar_colors = ["#2ecc71", "#3498db", "#9b59b6", "#f1c40f"]
        for i, value in enumerate(self.data):
            max_value = max(self.data)
            bar_height = (value / max_value) * 200  # Scale height based on max value
            y = 300 - bar_height

            canvas.create_rectangle(
                x, y, x + bar_width, 300, fill=bar_colors[i], outline="black"
            )

            # Add text label above the bar
            canvas.create_text(
                x + bar_width // 2, y - 10, text=str(value), font=("Arial", 12)
            )

            x += bar_width + bar_spacing


# Create the application instance
app = BarChartApp()
app.mainloop()
