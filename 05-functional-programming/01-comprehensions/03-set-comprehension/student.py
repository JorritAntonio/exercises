def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {same for same in xs if same in ys}