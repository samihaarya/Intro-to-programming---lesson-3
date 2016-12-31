import fresh_tomatoes
import media

Divergent = media.Movie("Divergent","Action, Adventure, Thriller, Science Fiction, Mystery","2014","https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg","https://www.youtube.com/watch?v=sutgWjz10sM")
# self is always skipped
Angry_Bird = media.Movie("The Angry Bird","Animation, Comedy, Action, Family, Adventure","2016","https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/The_Angry_Birds_Movie_poster.png/220px-The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=e4sdQBmqnuA")

Avengers = media.Movie("The Avengers","Action, Adventure, Fantacy, Science Fiction, Superhero","2015","https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")

FaultInStars = media.Movie("The Fault In Our Stars","Youth adult fiction","2014","https://upload.wikimedia.org/wikipedia/en/thumb/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png/220px-The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png","https://www.youtube.com/watch?v=9ItBvH5J6ss")

Thor = media.Movie("Thor","Action, Adventure, Fantacy","2011","http://ia.media-imdb.com/images/M/MV5BMTYxMjA5NDMzNV5BMl5BanBnXkFtZTcwOTk2Mjk3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=JOddp-nlNvQ")

Titanic = media.Movie("Titanic","Romance, Disaster, Historical, Epic, Drama","1997","https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg","https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

Frozen = media.Movie("Frozen","Animation, Comedy, Adventure, Fantacy","2013","https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg","https://www.youtube.com/watch?v=Adpi_tMDQvA")

JungleBook = media.Movie("The Jungle Book","Animation, Comedy, Adventure, Drama","1967","https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Thejunglebook_movieposter.jpg/220px-Thejunglebook_movieposter.jpg","https://www.youtube.com/watch?v=LNVTKXIK7q8")

Furious7 = media.Movie("Furious 7","Action, Crime, Thriller","2015","https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg","https://www.youtube.com/watch?v=Skpu5HaVkOc")

IronMan3 = media.Movie("Iron Man 3","Action, Superhero, Adventure, Science Fiction","2013","https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg","https://www.youtube.com/watch?v=muIsc5lIEyQ")

Maleficent = media.Movie("Maleficent","Action, Romance, Fantacy, Adventure, Family","2014","http://ia.media-imdb.com/images/M/MV5BMTQ1NDk3NTk0MV5BMl5BanBnXkFtZTgwMTk3MDcxMzE@._V1_UY268_CR4,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=w-XO4XiRop0")

BigHero6 = media.Movie("Big Hero 6","Animation, Comedy, Science Fiction, Action, Adventure","2014","https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Big_Hero_6_%28film%29_poster.jpg/220px-Big_Hero_6_%28film%29_poster.jpg","https://www.youtube.com/watch?v=8IdMPpKMdcc")

movies = [Divergent, Angry_Bird, Avengers, FaultInStars, Thor, Titanic, Frozen, Furious7, JungleBook, Maleficent, IronMan3, BigHero6]

fresh_tomatoes.open_movies_page(movies)
