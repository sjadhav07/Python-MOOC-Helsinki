# Write your solution here:
class Series:
    def __init__(self, title: str, num_season: int, lst_genre: list):
        self.title = title
        self.num_season = num_season
        self.lst_genre = lst_genre
        self.lst = []

    def rate(self, rating: int):
        self.lst.append(rating)

    def __str__(self):
        ab = ", ".join(self.lst_genre)
        if len(self.lst) != 0:
            return f"{self.title} ({self.num_season} seasons)\ngenres: {ab}\n{len(self.lst)} ratings, average {(sum(self.lst)/len(self.lst)):.1f} points"
        else:
            return f"{self.title} ({self.num_season} seasons)\ngenres: {ab}\nno ratings"
    
def minimum_grade(grade: float, series_list: list):
    new_lst = []
    for item in series_list:
        for ra in item.lst:
            if ra >= grade:
                new_lst.append(item)
    return new_lst

def includes_genre(genre: str, series_list: list):
    new_lst = []
    for item in series_list:
        if genre in item.lst_genre:
            new_lst.append(item)
    return new_lst
            