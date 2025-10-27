from operations import *

# Demo script showing system usage

# Add books
add_book('978-3-16-148410-0', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 5)
add_book('978-0-596-52068-7', 'Python Crash Course', 'Eric Matthes', 'Non-Fiction', 3)
add_book('978-0-553-21311-9', '1984', 'George Orwell', 'Sci-Fi', 4)

# Add members
add_member('M001', 'John Doe', 'john@example.com')
add_member('M002', 'Jane Smith', 'jane@example.com')

# Search for a book
results = search_book('Python')
print("Search results for 'Python':")
for isbn, book in results:
    print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}")

# Borrow books
borrow_book('M001', '978-3-16-148410-0')
borrow_book('M001', '978-0-596-52068-7')
borrow_book('M002', '978-0-553-21311-9')

# Update a book
update_book('978-0-596-52068-7', total_copies=4)

# Return a book
return_book('M001', '978-3-16-148410-0')

# Delete a book (should succeed since returned)
delete_book('978-3-16-148410-0')

# Attempt to delete a borrowed book (should fail)
delete_book('978-0-553-21311-9')  # Fails because borrowed

print("\nFinal books:")
print(books)
print("\nFinal members:")
print(members)
