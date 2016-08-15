import fresh_tomatoes
import media

Divergent = media.Movie("Divergent","Action, Adventure, Thriller, Science Fiction, Mystery","A world divided by factions based on virtues, Tris learns she's Divergent and won't fit in.","https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg","https://www.youtube.com/watch?v=sutgWjz10sM")
# self is always skipped
Angry_Bird = media.Movie("The Angry Bird","Animation, Comedy, Action, Family, Adventure","Find out why the birds are so angry.","https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/The_Angry_Birds_Movie_poster.png/220px-The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=e4sdQBmqnuA")

Avengers = media.Movie("The Avengers","Action, Adventure, Fantacy, Science Fiction, Superhero","Earth's mightiest heroes must come together and learn to fight as a team.","https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")

FaultInStars = media.Movie("The Fault In Our Stars","Youth adult fiction","Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.","https://upload.wikimedia.org/wikipedia/en/thumb/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png/220px-The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png","https://www.youtube.com/watch?v=9ItBvH5J6ss")

Thor = media.Movie("Thor","Action, Adventure, Fantacy","Thor battles his villainous brother Loki to save the universe from his evil plans.","http://ia.media-imdb.com/images/M/MV5BMTYxMjA5NDMzNV5BMl5BanBnXkFtZTcwOTk2Mjk3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=JOddp-nlNvQ")

Titanic = media.Movie("Titanic","Romance, Disaster, Historical, Epic, Drama","A seventeen-year-old aristocrat falls in love with a kind but poor artist","https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg","https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

movies = [Divergent, Angry_Bird, Avengers, FaultInStars, Thor, Titanic]
fresh_tomatoes.open_movies_page(movies)
#print Divergent.storyline
#print Thor.storyline
#Divergent.show_trailer()
