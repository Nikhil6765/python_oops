class movie:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print("title of the movie is : ",self.title)
        print("hero of the movie is : ",self.hero)
        print("heroine of the movie is : ",self.heroine)


list_of_movies=[]
while True:
    title=input("enter title of the movie : ")
    hero=input("enter hero of the movie : ")
    heroine=input("enter heroine of the movie : ")
    m=movie(title,hero,heroine)
    list_of_movies.append(m)
    print("movie added successfully")
    
    option=input("do you want to add more movies to the list [yes/no]")
    if option.lower()=='no':
        break


