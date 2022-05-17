books ={"Margaret Atwood" : "The Handmaiden's Tale", "J.R.R. Tolkien" : "The Hobbit", "Roald Dahl" : "Charlie and the Cholate Factory" }
print(books["Margaret Atwood"])
print(sorted(books))

# Problem: create a dictionary associating authors to lists of books, and write 
# search functionality to take an author name from the user and print the books by
# that author.
# Strech goals: display the books in alphabetical order, and implement add functionality.

books = {
    "margaret atwood" : ["the handmaiden's tale", "the blind assassin"], 
      "roald dahl" : ["charlie and the cholate factory", "matilda", "james and the giant"],
     "j.r.r. tolkien" : ["the hobbit", "the lord of the rings", "the silmarillion"]
}
while True:
    author_name = input("Enter author name (ctrl+c to quit)): ").lower()
    mode = input("[A]dd or [s]earch? ").upper()
    if mode == 'S':
        book_results = books.get(author_name, ["None"])
        print(f"Books by {author_name}: ",  '. '.join(sorted(book_results)))
    elif mode == 'A':
        title = input("Enter title to add: ").lower()
        if author_name in books:
            books[author_name].append(title)
        else: 
            books[author_name]
    else: 
        print("Invalid mode")




    