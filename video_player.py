import tkinter as tk
from tkinter import font as tkfont

# Import custom font manager module
import font_manager as fonts

# Import CheckVideos class from check_videos module
from check_video import CheckVideos


class VideoPlayerApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.geometry("520x150")  # Set the window size
        self.root.title("Video Player")  # Set the window title

        # Configure custom fonts using the font_manager module
        fonts.configure()

        # Create a header label
        self.header_lbl = tk.Label(root, text="Select an option by clicking one of the buttons below")
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create a button to check videos
        self.check_videos_btn = tk.Button(root, text="Check Videos", command=self.check_videos_clicked)
        self.check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

        # Create a button to create a video list
        self.create_video_list_btn = tk.Button(root, text="Create Video List", command=self.create_video_list_clicked)
        self.create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to update videos
        self.update_videos_btn = tk.Button(root, text="Update Videos", command=self.update_videos_clicked)
        self.update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

        # Create a status label to display messages
        self.status_lbl = tk.Label(root, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def check_videos_clicked(self):
        # Update the status label when the "Check Videos" button is clicked
        self.status_lbl.configure(text="Check Videos button was clicked!")
        # Create a new instance of the CheckVideos class
        CheckVideos(tk.Toplevel(self.root))

    def create_video_list_clicked(self):
        # TO DO: implement the create video list functionality
        pass

    def update_videos_clicked(self):
        # TO DO: implement the update videos functionality
        pass


if __name__ == "__main__":
    # Create the main application window
    window = tk.Tk()
    app = VideoPlayerApp(window)
    window.mainloop()