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

# list of trivia for each scenes
trivia = {
    "Pamplona": {
        "question": "What year was St. Ignatius struck by a cannonball in Pamplona?",
        "choices": {
            "a": "1492",
            "b": "1521",
            "c": "1572",
        },
        "correct": "b",
        "response": {
            True: "Wonderful! You're absolutely right! St. Ignatius was struck by a cannonball in 1521 in Pamplona. Great job remembering that important date!",
            False: "Good try! The correct answer is 1521. Don't worry - dates can be tricky to remember! St. Ignatius was hurt in 1521, and that's when his amazing spiritual journey began. You're doing great!"
        }
    },
    "Loyola": {
        "question": "What did Ignatius read while recovering that changed his life?",
        "choices": {
            "a": "Comic books",
            "b": "Stories about Jesus and the saints",
            "c": "Cookbooks",
        },
        "correct": "b",
        "response": {
            True: "Excellent! You got it right! Ignatius read stories about Jesus and the saints, and they inspired him to want to help others. You're learning so well!",
            False: "Nice thinking! The answer is stories about Jesus and the saints. While Ignatius was getting better, he read these inspiring stories that helped him decide to serve God. Keep up the great work!"
        }
    },
    "Montserrat and Manresa": {
        "question": "What special prayers did Ignatius create during his time in the caves?",
        "choices": {
            "a": "The Spiritual Exercises",
            "b": "Magic spells",
            "c": "Bedtime stories",
        },
        "correct": "a",
        "response": {
            True: "Amazing! You're correct! Ignatius created the Spiritual Exercises - special prayers and reflections that help people feel closer to God. You're so smart!",
            False: "Great guess! The answer is the Spiritual Exercises. These are special prayers that Ignatius wrote to help people talk to God and make good choices. You're doing wonderfully!"
        }
    },
    "Jerusalem": {
        "question": "Where did Ignatius want to stay to follow in Jesus's footsteps?",
        "choices": {
            "a": "Paris",
            "b": "Jerusalem (the Holy Land)",
            "c": "Spain",
        },
        "correct": "b",
        "response": {
            True: "Perfect! Yes, Ignatius wanted to stay in Jerusalem, the Holy Land where Jesus lived! You remembered that beautifully!",
            False: "Good thinking! The answer is Jerusalem, the Holy Land. Ignatius wanted to stay there because that's where Jesus lived and taught. You're learning so much!"
        }
    },
    "Paris": {
        "question": "What did Ignatius and his friends decide to call their group?",
        "choices": {
            "a": "The Super Friends",
            "b": "The Society of Jesus (Jesuits)",
            "c": "The Knights of the Round Table",
        },
        "correct": "b",
        "response": {
            True: "Fantastic! You're absolutely right! They called themselves the Society of Jesus, and people also call them Jesuits. You're such a good listener!",
            False: "Wonderful try! The answer is the Society of Jesus (also called Jesuits). Ignatius and his friends wanted to serve Jesus together, so they chose this special name. You're doing such a great job!"
        }
    },
    "Rome": {
        "question": "Who officially approved Ignatius's group in 1540?",
        "choices": {
            "a": "The King of Spain",
            "b": "The Pope",
            "c": "His mother",
        },
        "correct": "b",
        "response": {
            True: "Excellent work! The Pope approved their group in 1540! You have such a good memory for these important details!",
            False: "Great attempt! The Pope was the one who officially approved their group. The Pope is like the leader of the Catholic Church, and he thought Ignatius's group would do wonderful work. You're learning beautifully!"
        }
    },
    "The Final Chapter of St. Ignatius' Life": {
        "question": "What year did St. Ignatius die peacefully in Rome?",
        "choices": {
            "a": "1556",
            "b": "1600",
            "c": "1500",
        },
        "correct": "a",
        "response": {
            True: "Wonderful! You got it right! St. Ignatius died peacefully in 1556, but his good work continued through all his friends. You're so smart!",
            False: "Nice try! He died in 1556. Even though Ignatius went to heaven, all the good things he started kept helping people around the world. You're doing such a great job learning!"
        }
    },
    "The Society of Jesus After His Death": {
        "question": "What happened to the Jesuits after Ignatius died?",
        "choices": {
            "a": "They disappeared",
            "b": "They spread around the world helping people",
            "c": "They became pirates",
        },
        "correct": "b",
        "response": {
            True: "Amazing! You're absolutely right! The Jesuits spread all around the world to help people and teach them about God. You understand the story so well!",
            False: "Excellent thinking! The answer is they spread around the world helping people. The Jesuits continued Ignatius's mission of helping others and teaching about God everywhere! You're doing wonderfully!"
        }
    },
    "Ignatian Spirituality and the Jesuits Today": {
        "question": "How many countries do Jesuits serve in today?",
        "choices": {
            "a": "Only 5 countries",
            "b": "More than 100 countries",
            "c": "Just Spain",
        },
        "correct": "b",
        "response": {
            True: "Incredible! You're right! Jesuits serve in more than 100 countries today - that's almost everywhere in the world! You're such a good student!",
            False: "Great guess! The answer is more than 100 countries! That means Jesuits are helping people almost everywhere in the world, just like Ignatius wanted. You're learning so much!"
        }
    },
    "An Invitation Today": {
        "question": "What question does Ignatius want us to ask ourselves?",
        "choices": {
            "a": "What's for lunch?",
            "b": "What more can I do for Christ?",
            "c": "What time is it?",
        },
        "correct": "b",
        "response": {
            True: "Perfect! You remembered perfectly! Ignatius wants us to ask 'What more can I do for Christ?' - thinking about how we can help others and be kind. You're amazing!",
            False: "Wonderful try! The question is 'What more can I do for Christ?' This means thinking about how we can be kind, helpful, and good to others every day. You're such a thoughtful student!"
        }
    }
}

class VisualNovelApp(tk.Tk):
    def __init__(self, scenes):
        super().__init__()
        self.title("Walking in the Footsteps of St. Ignatius")
        self.attributes('-fullscreen', True)
        self.configure(bg="white")
        self.minsize(800, 600)
        self.scenes = scenes
        self.index = 0

        # Load and set background image
        self.setup_background()

        # Create Genshin Impact-style overlay frame with semi-transparency
        self.bottom_frame = tk.Frame(self, bg='#1a2538', height=270, relief="flat")
        self.bottom_frame.pack_propagate(False)  # Prevent frame from shrinking to fit content
        
        # Create elegant top border with Genshin-style gradient
        self.top_border = tk.Frame(self.bottom_frame, bg="#2c5aa0", height=3)
        self.top_border.pack(fill="x", side="top")
        
        # Create subtle inner border
        self.inner_border = tk.Frame(self.bottom_frame, bg="#243447", height=1)
        self.inner_border.pack(fill="x", side="top")
        
        # Create labels with Genshin-style semi-transparent backgrounds
        self.title_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 28, "bold"), 
                                wraplength=900, fg="#f0e6d2", bg="#1a2538", anchor="w")
        self.subtitle_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 20, "italic"), 
                                wraplength=900, fg="#c9aa71", bg="#1a2538", anchor="w")
        self.text_label = tk.Label(self.bottom_frame, text="", font=("Georgia", 17), 
                                wraplength=900, justify="left", fg="#e8dcc6", bg="#1a2538")
        self.next_button = tk.Button(self.bottom_frame, text="Next", command=self.next_scene, 
                                    font=("Arial", 14, "bold"), bg="#2c5aa0", fg="#f0e6d2",
                                    relief="raised", borderwidth=2, padx=25, pady=10,
                                    activebackground="#4a7bc8", activeforeground="white")

        # Position the bottom frame at the very bottom of the screen
        self.bottom_frame.pack(side="bottom", fill="x")
        
        # Pack elements in order: title, subtitle, text
        self.title_label.pack(pady=(25, 0))
        self.subtitle_label.pack(pady=(0, 15))
        self.text_label.pack(padx=40, pady=(0, 20))
        
        # Position the button absolutely in the bottom right corner
        self.next_button.place(relx=0.95, rely=0.85, anchor="se")

        # Bind Escape key to exit fullscreen
        self.bind('<Escape>', lambda e: self.quit())
        self.bind('<Right>', lambda e: self.next_scene())

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
            self.quit() # Should be changed in to an end screen, then it should loop back to the start.

    # def ask_scene_question():
    #     if self.scenes[self.index]["title"] in trivia:
    #         scene_question = 
    #     else:
    #         pass
            


if __name__ == "__main__":
    app = VisualNovelApp(scenes)
    app.mainloop()
