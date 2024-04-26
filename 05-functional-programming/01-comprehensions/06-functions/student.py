def movie_count(movies, director):
    return len([movie.title for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any([genre in movie.genres and director == movie.director for movie in movies])

def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2

def is_increasing(ns):
    return all(x <= y for x,y in zip(ns, ns[1:]))

