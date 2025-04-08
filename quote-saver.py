quotesList=open("quotes.txt", "r+")
booksList=open("books.txt", "r+")
while True:
    # Prompt the user for a quote
    print("Enter a quote and page number (or 'exit' to quit):")
    # Read the quote from the user
    book=input("Book: ")
    if booksList.read().find(book) != -1:
        print("Book already exists in the list.")
        continue
    elif book.lower() == 'exit':
        break
    else:
        booksList.write(book + "\n")
    quote = input("Quote: ")
    if quotesList.read().find(quote) != -1:
        print("Quote already exists in the list.")
        continue
    if quote.lower() == 'exit':
        break
    pageNumber = input("Enter the page number: ")
    # Write the quote to the file
    quotesList.write(book + " - " + '"' + quote + '"' + "p." + " " + pageNumber + "\n")
