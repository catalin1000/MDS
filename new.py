import customtkinter as ctk


class AplicatieBugetare(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplicatie de budgetare")
        self.geometry("600x400")

        # Create a frame to hold the chart
        self.chart_frame = ctk.CTkFrame(self, width=400, height=300)
        self.chart_frame.pack(padx=20, pady=20)

        # Single entry field for user input
        self.input_field = ctk.CTkEntry(self, width=500, placeholder_text="bar {number} {value}")
        self.input_field.pack()

        # Update button with new text
        self.update_button = ctk.CTkButton(self, text="Update Bar", command=self.update_data)
        self.update_button.pack(pady=10)

        # Label for error messages (initially hidden)
        self.error_label = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 12)
        )
        self.error_label.pack(padx=20, pady=5)

        # Ensure the label is packed initially (might be necessary in older versions)
        try:
            self.error_label.pack()  # Attempt to pack for visibility control
        except (AttributeError, ctk.TclError):  # Handle potential packing errors (older versions)
            pass

        self.error_label.pack_forget()

        # Initial data 
        self.data = [1, 2, 3, 5]

        self.draw_bars()

    def update_data(self):
        user_input = self.input_field.get().strip()

        
        try:
            parts = user_input.split(" ")
            if len(parts) != 3:
                raise ValueError
            bar_number = int(parts[1]) - 1  # Adjust for 0-based indexing
            value = int(parts[2])
        except ValueError:
            # Handle invalid input format or numbers
            self.show_error("Invalid input format! Use: bar {number} {value}")
            return

        # Check for valid bar number within data list
        if bar_number < 0 or bar_number >= len(self.data):
            self.show_error("Invalid bar number! Please enter a number between 1 and {}".format(len(self.data)))
            return

        # Update the data list
        self.data[bar_number] = value

        # Clear and redraw the chart
        self.draw_bars()

    def show_error(self, message):
        # Display the error message
        self.error_label.configure(text=message)

        # Make the label visible (show or pack depending on version)
        try:
            self.error_label.show()  # Use show if available (newer versions)
        except AttributeError:
            self.error_label.pack() # Fallback to pack for older versions

        # Optionally, hide the error message after a short delay
        self.after(2000, self.hide_error)  # Hide after 2 seconds

    def hide_error(self):
        self.error_label.configure(text="")

        
        self.error_label.pack_forget() # delete text

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

            # Create the rectangle for the bar
            canvas.create_rectangle(
                x, y, x + bar_width, 300, fill=bar_colors[i], outline="black"
            )

            # Draw the value text above the bar (optional)
            # canvas.create_text(
            #     x + bar_width // 2, y - 10, text=str(value), font=("Arial", 12)
            # )

            x += bar_width + bar_spacing

        

# Run the application
app = AplicatieBugetare()
app.mainloop()