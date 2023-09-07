class Author:  ##Make an author class
    def __init__(self, name):  ##Define a function with name parameter
        self.name = name
        self.books = []  ##Make an empty list

    def publish(self, title):
        self.books.append(title)  ##Define a publish function that takes a title argument

    def __str__(self):
        if self.books:
            titles = ', '.join(self.books)  ##Define a str function to join the titles or
        else:  ##give an error message if no items are in the list
            titles = 'No published books'
        return self.name + ': ' + titles


def main():
    lewisCarrol = Author('Lewis Carrol')
    lewisCarrol.publish('Alice in Wonderland')  ##Define the main method and add an author
    lewisCarrol.publish('Alice in Wonderland 2: Electric Boogaloo')
    print(lewisCarrol)  ##Publish the books and print the objects

    lbwhite = Author('L. B. Huwhite')
    print(lbwhite)

    bryan = Author('Bryan')
    bryan.publish('Chasing Righteousness')
    bryan.publish('The Prince')
    bryan.publish('Chasing Righteousness')  ##Test the publishing ability and notice duplicates
    bryan.publish('Chasing Righteousness')  ##can be added to the list
    bryan.publish('Rule for Radicals')
    print()
    print(bryan)  ##Print the author object


main()  ##Call the main function
