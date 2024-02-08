# BookWormCentral

BookWormCentral is an open web service for libraries that allows readers to find, order, and borrow books for lending or reading rooms. The system is based on the Django framework and has a user-friendly interface for browsing the book catalog, interacting with readers and librarians, and tracking the status of books in the library. BookWormCentral promotes easy access to knowledge and the development of reading culture, making reading books even more enjoyable and accessible to everyone.

## Django models

1. **Books:**
   - Book title
   - Author
   - Year of publication
   - Number of copies in the library
   - Book category (fiction, science, history, etc.)

2. **Readers:**
   - Name
   - Last name
   - Address
   - Email address
   - Phone number
   - Books they have borrowed from the library (many to many relationship with the Books model)

## Django Views

1. **List of books:**
   - Displays a list of all available books with the ability to filter by category, author, etc.
   - The "Order" button that allows the reader to order the book.

2. **Book details**
   - Displays information about a particular book, including the number of available copies.
   - The "Borrow" or "Check out" button, which adds the book to the list of books borrowed by the reader.

3. **Reader profile:**
   - Displays the list of borrowed books by the reader.
   - Possibility to extend the period of using the book (if it is allowed by the library rules).

## Django paths (URLs)

- `/books/`: List of books
- `/books/<book_id>/`: Book details
- `/profile/`: Reader profile with a list of borrowed books
