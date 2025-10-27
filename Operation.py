# Global data structures
books = {}  # Dictionary: ISBN -> {'title': str, 'author': str, 'genre': str, 'total_copies': int, 'available_copies': int}
members = []  # List of dictionaries: {'member_id': str, 'name': str, 'email': str, 'borrowed_books': list of ISBNs}
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography")  # Tuple of valid genres

def add_book(isbn, title, author, genre, total_copies):
    """
    Add a book if ISBN is unique and genre is valid.
    """
    if isbn in books:
        return False
    if genre not in genres:
        return False
    books[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'total_copies': total_copies,
        'available_copies': total_copies
    }
    return True

def add_member(member_id, name, email):
    """
    Add a member if member_id is unique.
    """
    for member in members:
        if member['member_id'] == member_id:
            return False
    members.append({
        'member_id': member_id,
        'name': name,
        'email': email,
        'borrowed_books': []
    })
    return True

def search_book(query):
    """
    Search books by title or author.
    Returns list of (isbn, book_details) tuples.
    """
    results = []
    for isbn, book in books.items():
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
            results.append((isbn, book))
    return results

def update_book(isbn, **kwargs):
    """
    Update book details. Accepts title, author, genre, total_copies.
    """
    if isbn not in books:
        return False
    for key, value in kwargs.items():
        if key in ['title', 'author', 'genre', 'total_copies']:
            if key == 'genre' and value not in genres:
                return False
            if key == 'total_copies':
                borrowed = books[isbn]['total_copies'] - books[isbn]['available_copies']
                if value < borrowed:
                    return False
                books[isbn]['available_copies'] = value - borrowed
            books[isbn][key] = value
    return True

def delete_book(isbn):
    """
    Delete book only if no copies are borrowed.
    """
    if isbn not in books:
        return False
    if books[isbn]['available_copies'] < books[isbn]['total_copies']:
        return False
    del books[isbn]
    return True

def borrow_book(member_id, isbn):
    """
    Member borrows a book if available, not exceeding 3 borrowed books.
    """
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member:
        return False
    if len(member['borrowed_books']) >= 3:
        return False
    if isbn not in books or books[isbn]['available_copies'] <= 0:
        return False
    member['borrowed_books'].append(isbn)
    books[isbn]['available_copies'] -= 1
    return True

def return_book(member_id, isbn):
    """
    Return a borrowed book.
    """
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member or isbn not in member['borrowed_books']:
        return False
    if isbn not in books:
        return False
    member['borrowed_books'].remove(isbn)
    books[isbn]['available_copies'] += 1
    return True
