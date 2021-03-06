import media
import fresh_tomatoes
""" Creates intances of the Movie class """

the_lord_of_the_ring_movie_1 = media.Movie(
                    "The Lord of the Rings: The Fellowship of the Ring",
                    "A meek Hobbit from the Shire and eight companions set "
                    "out on a journey to destroy the powerful One Ring and "
                    "save Middle Earth from the Dark Lord Sauron.",
                    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                    "https://youtu.be/V75dMMIW2B4",
                    "2h 24min")

the_lord_of_the_ring_movie_2 = media.Movie(
                    "The Lord of the Rings: The Two Towers",
                    "While Frodo and Sam edge closer to Mordor with the help "
                    "of the shifty Gollum, the divided fellowship makes a "
                    "stand against Sauron's new ally, Saruman, and his hordes "
                    "of Isengard.",
                    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                    "https://youtu.be/LbfMDwc4azU",
                    "2h 30min")

the_lord_of_the_ring_movie_3 = media.Movie(
                    "The Lord of the Rings: The Return of the King",
                    "Gandalf and Aragorn lead the World of Men against "
                    "Sauron's army to draw his gaze from Frodo and Sam as "
                    "they approach Mount Doom with the One Ring.",
                    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                    "https://youtu.be/r5X-hFf6Bwo",
                    "2h 15min")

the_hobbit_movie_1 = media.Movie(
                    "An Unexpected Journey",
                    " A reluctant hobbit, Bilbo Baggins, sets out to the "
                    "Lonely Mountain with a spirited group of dwarves to "
                    "reclaim their mountain home, and the gold within it from "
                    "the dragon Smaug.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                    "https://youtu.be/SDnYMbYB-nU",
                    "3h")

the_hobbit_movie_2 = media.Movie(
                    "The Desolation of Smaug",
                    "The dwarves, along with Bilbo Baggins and Gandalf the "
                    "Grey, continue their quest to reclaim Erebor, their "
                    "homeland, from Smaug. Bilbo Baggins is in possession of "
                    "a mysterious and magical ring.",
                    "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
                    "https://youtu.be/fnaojlfdUbs",
                    "2h 40min")

the_hobbit_movie_3 = media.Movie(
                    "The Battle of the Five Armies",
                    "Bilbo and Company are forced to engage in a war against "
                    "an array of combatants and keep the Lonely Mountain from "
                    "falling into the hands of a rising darkness.",
                    "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                    "https://youtu.be/iVAgTiBrrDA",
                    "2h 12min")

movies = [
    the_lord_of_the_ring_movie_1, the_lord_of_the_ring_movie_2,
    the_lord_of_the_ring_movie_3, the_hobbit_movie_1, the_hobbit_movie_2,
    the_hobbit_movie_3]

fresh_tomatoes.open_movies_page(movies)
