import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content): 
    text_area.delete("1.0", tk.END) # Delete existing content
    text_area.insert(1.0, content) # Enter text

class CheckVideos(): 
    def __init__(self, window):
        window.geometry("750x350") # Set the size of the window
        window.title("Check Videos") # Editing window's title

        self.list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) # Create a button which is labeled "List all video", and upon clicking it, the class containing this code's list_videos_clicked method is called
        self.list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # Editing grid appearance

        self.enter_lbl = tk.Label(window, text="Enter Video Number") # Make a label to instruct users on entering video number
        self.enter_lbl.grid(row=1, column=0, padx=10, pady=10) # Editing grid appearance

        self.input_txt = tk.Entry(window, width=3) # The area where users can input the video number
        self.input_txt.grid(row=1, column=2, padx=10, pady=10) # Editing grid appearance

        self.check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked) # Create a button which is labeled "Check Video", and upon clicking it, the class containing this code's check_video_clicked method is called
        self.check_video_btn.grid(row=0, column=3, padx=10, pady=10) # Editing grid appearance

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Make a text area which can be scrolled up and down
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="", padx=10, pady=10) # Editing grid appearance

        self.video_txt=tk.Text(window, width=24, height=4, wrap="none") # Make a window that shows text in Video format
        self.video_txt.grid(row=1, column=3, sticky="n", padx=10, pady=10) # Editing grid appearance

        self.status_lbl = tk.Label(window, text="", font="Helvetica",) # View the status of the video
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="", padx=10, pady=10) # Editing grid appearance

        self.list_videos_clicked() # Invoke the list_videos_clicked function

    def check_video_clicked(self): # A procedure for handling checking videos
        key = self.input_txt.get() # Obtain the entered video number from the input
        name = lib.get_name(key) # Retrieve the video name from lib
        if name is not None: # Gather and present the video's information if it does exist
            director = lib.get_director(key) # Display properties obtained from lib
            rating = lib.get_rating(key) # Passing the variable key as an argument when calling the get_rating method from lib. A rating is returned by the method and is subsequently kept in the rating variable
            play_count = lib.get_play_count(key) # Invoke the get_play_count method from lib and passes the variable key as an argument, the value of the play count for the item indicated by the key is returned by the method and is kept in the play_count variable
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details) # Provide video details information and show it in a window
        else: # Present the error message if video does not exist
            set_text(self.video_txt, f"Video ({key}) not found")
        self.status_lbl.configure(text="Check Video button was clicked!") # Updating the status

    def list_videos_clicked(self): # A procedure for handling listing videos
        video_list = lib.list_all() # Obtain a list of all videos from lib
        set_text(self.list_txt, video_list) 
        self.status_lbl.configure(text="List Videos button was clicked!") # After the button is clicked, update the status

if __name__ == "__main__": # only runs when this file is run as a standalone
    window = tk.Tk() # create a Tk object
    fonts.configure() # configure the fonts
    CheckVideos(window) # open the CheckVideo GUI
    window.mainloop() # run the window main loop, reacting to button presses, etc