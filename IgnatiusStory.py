import tkinter as tk
from PIL import Image, ImageTk

# List of scenes in order
scenes = [
    {
        "title": "Pamplona",
        "subtitle" : "A Wounded Knight",
        "text": "In 1521, Ignatius of Loyola was struck by a cannonball while defending Pamplona. This marked the beginning of his interior transformation."
    },
    {
        "title": "Loyola",
        "subtitle": "A Time of Recovery and Reflection",
        "text": "While recovering in Loyola, Ignatius read about the life of Christ and the saints, inspiring his desire for a deeper spiritual life."
    },
    {
        "title": "Montserrat and Manresa",
        "subtitle": "A Pilgrim’s Journey",
        "text": "Ignatius surrendered his sword at Montserrat and spent months in deep prayer and spiritual struggle in the caves of Manresa, where he began developing the Spiritual Exercises."
    },
    {
        "title": "Jerusalem",
        "subtitle": "A Heart Set on Pilgrimage",
        "text": "Ignatius traveled to the Holy Land hoping to remain there, but was asked to return. His desire to follow Christ grew stronger."
    },
    {
        "title": "Paris",
        "subtitle": "Brotherhood and Formation",
        "text": "In Paris, Ignatius studied theology and gathered companions who would later become the Society of Jesus. It was here that the mission became clearer: to serve Christ wherever the need was greatest."
    },
    {
        "title": "Rome",
        "subtitle": "Mission and Foundation",
        "text": "Ignatius and his companions offered themselves to the Pope. In 1540, the Society of Jesus was formally approved, beginning a new chapter of mission, education, and service."
    },
    {
        "title": "The Final Chapter of St. Ignatius' Life",
        "subtitle": "A Quiet Passing, A Lasting Fire",
        "text": "On July 31, 1556, Ignatius died quietly in Rome. He left behind no earthly treasures—just a burning desire to help souls and a community ready to carry on the mission."
    },
    {
        "title": "The Society of Jesus After His Death",
        "subtitle": "The Flame Spreads Across the World",
        "text": "Under Fr. Diego Laínez, the Society expanded globally. Even after suppression in 1773 and restoration in 1814, Jesuits like Fr. Matteo Ricci and Fr. Pedro Arrupe carried the Ignatian flame into new frontiers."
    },
    {
        "title": "Ignatian Spirituality and the Jesuits Today",
        "subtitle": "A Mission That Lives On",
        "text": "The Society now serves in 100+ countries through education, social justice, and spiritual retreats. Its values reach beyond Jesuits—teaching all to find God in all things, live for the MAGIS, and be persons for others."
    },
    {
        "title": "An Invitation Today",
        "subtitle": "Your Turn to Walk the Path",
        "text": "You don’t have to be a Jesuit to walk the Ignatian path. Like Ignatius, ask: 'What more can I do for Christ?' Let us continue the journey—together."
    }
]

class VisualNovelApp(tk.Tk):
    def __init__(self, scenes):
        super().__init__()
        self.title("Walking in the Footsteps of St. Ignatius")
        self.attributes('-fullscreen', True)
        self.configure(bg="white")
        self.minsize(800, 600)
        self.resizable(True, True)
        self.scenes = scenes
        self.index = 0

        # Load and set background image
        self.setup_background()

        # Create a frame for the bottom content with fixed height (increased height)
        self.bottom_frame = tk.Frame(self, bg="#f0f0f0", relief="flat", height=320)
        self.bottom_frame.pack_propagate(False)  # Prevent frame from shrinking to fit content
        
        # Create a top border line that spans the full width
        self.top_border = tk.Frame(self.bottom_frame, bg="black", height=1)
        self.top_border.pack(fill="x", side="top")
        
        self.title_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 26, "bold"), wraplength=600, bg="#f0f0f0", fg="black")
        self.subtitle_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 18, "italic"), wraplength=600, bg="#f0f0f0", fg="black")
        self.text_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 16), wraplength=600, justify="left", bg="#f0f0f0", fg="black")
        self.next_button = tk.Button(self.bottom_frame, text="Next", command=self.next_scene, font=("Arial", 12, "bold"))

        # Position the bottom frame at the very bottom of the screen
        self.bottom_frame.pack(side="bottom", fill="x")
        
        # Pack elements in order: title, subtitle, text
        self.title_label.pack(pady=(25, 0))
        self.subtitle_label.pack(pady=(0, 30))
        self.text_label.pack(padx=30, pady=(0, 20))
        
        # Position the button absolutely in the bottom right corner
        self.next_button.place(relx=0.95, rely=0.85, anchor="se")

        # Bind Escape key to exit fullscreen
        self.bind('<Escape>', lambda e: self.quit())

        self.show_scene()

    def setup_background(self):
        """Load and display the background image"""
        try:
            # Load the image
            image = Image.open("image.png")
            
            # Get screen dimensions
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            
            # Resize image to fit screen while maintaining aspect ratio
            image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.bg_image = ImageTk.PhotoImage(image)
            
            # Create background label
            self.bg_label = tk.Label(self, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
        except Exception as e:
            print(f"Could not load background image: {e}")
            # Continue without background if image fails to load

    def show_scene(self):
        scene = self.scenes[self.index]
        self.title_label.config(text=scene["title"])
        self.subtitle_label.config(text=scene["subtitle"])
        self.text_label.config(text=scene["text"])
        if self.index == len(self.scenes) - 1:
            self.next_button.config(text="Finish", command=self.quit)

    def next_scene(self):
        if self.index < len(self.scenes) - 1:
            self.index += 1
            self.show_scene()
        else:
            self.quit()

# Run the app
if __name__ == "__main__":
    app = VisualNovelApp(scenes)
    app.mainloop()
