import fresh_tomatoes
#imports functions, HTML and CSS from fresh tomatoes
#and allows movies to open
import media
#imports class movie and all methods from media.py
toy_story = media.Movie("Toy Story",
                        "A story of toys that come to life",
                        ("http://img.lum.dolimg.com/v1/images/open-uri20150422-" + \
                         "20810-m8zzyx_5670999f.jpeg?region=0,0,300,450"),
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                        



avatar = media.Movie("Avatar",
                    "A marine on alien planet",
                    ("http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5" + \
"                     BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg"),
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                     


revenant = media.Movie("Revenant",
                       "Leo kills everyone",
                       ("https://upload.wikimedia.org/wikipedia/en/b/b6/" + \
"                       The_Revenant_2015_film_poster.jpg"),
                       "https://www.youtube.com/watch?v=LoebZZ8K5N0")
                       


                       
oceans_eleven = media.Movie("Oceans Eleven",
                            "Dudes rob a bank",
                            ("http://resizing.flixster.com/Why8RA9gMc5Xps9QW4Ulc7ty" + \
                             "Ilc=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/2" + \
                             "7/11172746_ori.jpg"),
                            "https://www.youtube.com/watch?v=imm6OR605UI")
                            
                            

good_dinosaur = media.Movie("Good Dinosaur",
                            "Dinosaur Adventure Time Man",
                            ("http://vignette2.wikia.nocookie.net/pixar/images/7/73/" + \
                            "The_Good_Dinosaur_Promo_Art_03.jpg/revision/latest?cb=" + \
                             "20150908153903"),
                            "https://www.youtube.com/watch?v=O-RgquKVTPE")
                            

interstellar = media.Movie("Interstellar",
                           "Inside a blakc hole",
                           ("http://ia.media-imdb.com/images/M/MV5BMjIxNTU4Mz" + \
                           "Y4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg"),
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")
                           

independance_day = media.Movie("Independance Day",
                    "Will smith saves us from aliens",
                    ("http://dl9fvu4r30qs1.cloudfront.net/6e/95e110ab5d" + \
                        "11e1bcc4123138165f92/file/independence-day-image.jpg"),
                    "https://www.youtube.com/watch?v=kA2WzBi2grE")
                    

                           
                            
                            




movies = [toy_story, avatar, revenant, oceans_eleven, good_dinosaur, interstellar, independance_day]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
