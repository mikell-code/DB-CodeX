from operations import *

# Clear data for clean tests
books.clear()
members.clear()

# Test 1: Add a book successfully
assert add_book('978-3-16-148410-0', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 5) == True, "Failed to add book"
assert '978-3-16-148410-0' in books, "Book not found in dictionary"

# Test 2: Add duplicate book fails
assert add_book('978-3-16-148410-0', 'Duplicate', 'Author', 'Fiction', 1) == False, "Added duplicate book"

# Test 3: Add member successfully
assert add_member('M001', 'John Doe', 'john@example.com') == True, "Failed to add member"
assert len(members) == 1, "Member not added to list"

# Test 4: Borrow book successfully
borrow_success = borrow_book('M001', '978-3-16-148410-0')
assert borrow_success == True, "Failed to borrow book"
assert books['978-3-16-148410-0']['available_copies'] == 4, "Available copies not updated"
assert '978-3-16-148410-0' in members[0]['borrowed_books'], "Book not added to member's borrowed list"

# Test 5: Borrow when no copies left
# Reduce available to 0
for _ in range(4):
    borrow_book('M001', '978-3-16-148410-0')
assert borrow_book('M001', '978-3-16-148410-0') == False, "Borrowed when no copies left"

# Test 6: Return book successfully
return_success = return_book('M001', '978-3-16-148410-0')
assert return_success == True, "Failed to return book"
assert books['978-3-16-148410-0']['available_copies'] == 1, "Available copies not updated after return"  # Assuming one return after multiple borrows, but adjusted

# Test 7: Delete borrowed book fails
# Borrow again
borrow_book('M001', '978-3-16-148410-0')
assert delete_book('978-3-16-148410-0') == False, "Deleted borrowed book"

print("All tests passed!")
