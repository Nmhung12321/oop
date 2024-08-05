# Import the tkinter library for creating the GUI
import tkinter as tk

# Define a class to create the GUI for updating videos
class UpdateVideosGUI:
    def __init__(self):
        # Create the main window for the GUI
        self.window = tk.Tk()
        self.window.title("Update Videos")

        # Create frames to organize the GUI widgets
        self.top_frame = tk.Frame(self.window)
        self.middle_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        # Create labels and entries for the video ID, title, director, and rating
        self.video_id_label = tk.Label(self.top_frame, text="Video ID:")
        self.video_id_entry = tk.Entry(self.top_frame)
        self.title_label = tk.Label(self.top_frame, text="Title:")
        self.title_entry = tk.Entry(self.top_frame)
        self.director_label = tk.Label(self.top_frame, text="Director:")
        self.director_entry = tk.Entry(self.top_frame)
        self.rating_label = tk.Label(self.top_frame, text="Rating:")
        self.rating_entry = tk.Entry(self.top_frame)

        # Create buttons to update a video and cancel the operation
        self.update_button = tk.Button(self.middle_frame, text="Update Video")
        self.cancel_button = tk.Button(self.middle_frame, text="Cancel")

        # Create a listbox to display the updated videos
        self.video_listbox = tk.Listbox(self.bottom_frame)

        # Layout the widgets in the GUI
        self.top_frame.pack()
        self.video_id_label.pack(side=tk.LEFT)
        self.video_id_entry.pack(side=tk.LEFT)
        self.title_label.pack(side=tk.LEFT)
        self.title_entry.pack(side=tk.LEFT)
        self.director_label.pack(side=tk.LEFT)
        self.director_entry.pack(side=tk.LEFT)
        self.rating_label.pack(side=tk.LEFT)
        self.rating_entry.pack(side=tk.LEFT)

        self.middle_frame.pack()
        self.update_button.pack(side=tk.LEFT)
        self.cancel_button.pack(side=tk.LEFT)

        self.bottom_frame.pack()
        self.video_listbox.pack()

    # Define a method to run the GUI event loop
    def run(self):
        self.window.mainloop()

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the GUI class and run it
    gui = UpdateVideosGUI()
    gui.run()