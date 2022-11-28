# create 2 objects {'Sounds of music', 1965} and 'God Father', 1972. Add ratings between 0 and 10.
# When get rating called, average out the rating for each movie and print name + avg rating

class Movie:
    total_movies = 0

    def __init__(self, name, year, rating=None):
        if rating is None:
            rating = []
        self.name = name
        self.rating = rating
        self.year = year
        Movie.total_movies += 1

    def rate(self, set_rating):
        if set_rating < 0 or set_rating > 10:
            print('Wrong argument')
        else:
            self.rating.append(set_rating)

    def get_rating(self):
        total = 0
        for score in self.rating:
            total += score
        avg = total / len(self.rating)
        return avg


sound = Movie('Sounds of music', 1965)
gf = Movie('God Father', 1972)
sound.rate(7.9)
sound.rate(8.3)
gf.rate(9.2)
print(sound.rating)
print(gf.rating)
print(f"{sound.name}, rating {sound.get_rating():.2f}")
print(f"{gf.name}, rating {gf.get_rating():.2f}")

