class Author:
    def __init__(self, name):
        self.name = name    # Like the other author class, initialize and include an empty list
        self.books = []

    def publish(self, title):
        if title in self.books:     # Unlike the other class, this function is created
            print(f'{title} IS A DUPLICATE')    # for the purpose of rejecting duplicates
        else:
            self.books.append(title)

    def __str__(self):
        if self.books:  # like the other class, just defining the str function
            titles = ', '.join(self.books)  # Join the list items to be displayed
        else:  # and what to do if there are no list items
            titles = 'No published books'
        return self.name + ': ' + titles


def main():

        lewisCarrol = Author('Lewis Carrol')    # Make author objects and add books
        lewisCarrol.publish('Alice in Wonderland')  # using the publish function
        lewisCarrol.publish('Alice in Wonderland 2: Electric Boogaloo')
        print(lewisCarrol)

        lbwhite = Author('L. B. Huwhite')
        print(lbwhite)

        bryan = Author('Bryan')
        bryan.publish('Chasing Righteousness')
        bryan.publish('Dark Night of the Soul')
        bryan.publish('Chasing Righteousness')  # THe function will fail to publish
        bryan.publish('The Hunt for Red October')   # a duplicate book and will print an error message
        print()
        print(bryan)


main()
