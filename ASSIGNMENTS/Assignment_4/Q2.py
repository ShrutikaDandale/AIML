# Create a class Book with the following attributes:
# •title
# •author
# •list of reviews
#  And add methods to:
# •add a new review
# •count reviews 
# •display all reviews

# class created
class Book:

# attributes
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

# method of add review 
    def add_review(self, review):
        self.reviews.append(review)

# method of count
    def count_reviews(self):
        print("Total reviews:", len(self.reviews))

# method to display all review
    def display_reviews(self):
        for review in self.reviews:
            print(review)


b1 = Book("Python Basics", "ABC")

b1.add_review("Good")
b1.add_review("Excellent")

b1.count_reviews()
b1.display_reviews()




    