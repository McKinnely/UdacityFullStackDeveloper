import media
import fresh_tomatoes

ifWorked = "It Works..."


toy_story = media.Movie("Toy Story", "Toy Story is an awseome movie!", "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

the_internship = media.Movie("The Internship", "A movie about two regular guys getting hired at Google.", "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg", "https://www.youtube.com/watch?v=cdnoqCViqUo")

ratatouille = media.Movie("Ratatouille", "A movie about a cooking mouse.", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight In Paris", "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone.", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "A movie about survival.", "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg", "https://www.youtube.com/watch?v=4S9a5V9ODuY")



print(the_internship.storyline)

print(ifWorked)

movies = [toy_story, avatar, the_internship, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
