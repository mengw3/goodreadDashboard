import requests
from bs4 import BeautifulSoup
from unittest import TestCase
from elements import webscraper_book
from elements import webscraper_author


class Test(TestCase):
    def test_book_title(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        title = info_book.get_title(contents)
        assert title == "Clean Code: A Handbook of Agile Software Craftsmanship"

    def test_book_id(self):
        info_book = webscraper_book.WebScraperBook()
        url = 'https://www.goodreads.com/book/show/3735293-clean-code'
        book_id = info_book.get_book_id(url)
        assert book_id == "3735293"

    def test_book_isbn(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        isbn = info_book.get_isbn(contents)
        assert isbn == "0132350882"

    def test_book_author_url(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        author_url = info_book.get_author_url(contents)
        assert author_url == "https://www.goodreads.com/author/show/45372.Robert_C_Martin"

    def test_book_author(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        author = info_book.get_author(contents)
        assert author == "Robert C. Martin"

    def test_book_rating(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        rating = info_book.get_rating(contents)
        assert rating == "4.40"

    def test_book_rating_counts(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        rating_counts = info_book.get_rating_count(contents)
        assert rating_counts == "13423"

    def test_book_review_counts(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        review_counts = info_book.get_review_count(contents)
        assert review_counts == "804"

    def test_book_image_url(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        image_url = info_book.get_image_url(contents)
        assert image_url == "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436202607l/3735293._SX318_.jpg"

    def test_book_sim_books(self):
        info_book = webscraper_book.WebScraperBook()
        page = requests.get('https://www.goodreads.com/book/show/3735293-clean-code')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="leftContainer")
        sim_books = info_book.get_sim_books(contents)
        original_list = [
            [
                'The Pragmatic Programmer: From Journeyman to Master'
                'https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer'
            ],
            [
                'Design Patterns: Elements of Reusable Object-Oriented Software'
                'https://www.goodreads.com/book/show/85009.Design_Patterns'
            ],
            [
                'Refactoring: Improving the Design of Existing Code'
                'https://www.goodreads.com/book/show/44936.Refactoring'
            ],
            [
                'Head First Design Patterns'
                'https://www.goodreads.com/book/show/58128.Head_First_Design_Patterns'
            ],
            [
                'Code Complete'
                'https://www.goodreads.com/book/show/4845.Code_Complete'
            ],
            [
                'Test Driven Development: By Example'
                'https://www.goodreads.com/book/show/387190.Test_Driven_Development'
            ],
            [
                'Effective Java Programming Language Guide'
                'https://www.goodreads.com/book/show/105099.Effective_Java_Programming_Language_Guide'
            ],
            [
                'Working Effectively with Legacy Code'
                'https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code'
            ],
            [
                'Domain-Driven Design: Tackling Complexity in the Heart of Software'
                'https://www.goodreads.com/book/show/179133.Domain_Driven_Design'
            ],
            [
                'Patterns of Enterprise Application Architecture'
                'https://www.goodreads.com/book/show/70156.Patterns_of_Enterprise_Application_Architecture'
            ],
            [
                'The Software Craftsman: Professionalism, Pragmatism, Pride'
                'https://www.goodreads.com/book/show/23215733-the-software-craftsman'
            ],
            [
                'The Art of Unit Testing: With Examples in .NET'
                'https://www.goodreads.com/book/show/6487349-the-art-of-unit-testing'
            ],
            [
                'Growing Object-Oriented Software, Guided by Tests'
                'https://www.goodreads.com/book/show/4268826-growing-object-oriented-software-guided-by-tests'
            ],
            [
                'The Mythical Man-Month: Essays on Software Engineering'
                'https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month'
            ],
            [
                'JavaScript: The Good Parts'
                'https://www.goodreads.com/book/show/2998152-javascript'
            ],
            [
                'Java Concurrency in Practice'
                'https://www.goodreads.com/book/show/127932.Java_Concurrency_in_Practice'
            ],
            [
                'The Passionate Programmer'
                'https://www.goodreads.com/book/show/6399113-the-passionate-programmer'
            ],
            [
                'Refactoring to Patterns'
                'https://www.goodreads.com/book/show/85041.Refactoring_to_Patterns'
            ]
        ]
        i = 0
        for elem in sim_books:
            self.assertListEqual(elem, original_list[i])
            i = i + 1

    def test_author_name(self):
        info_author = webscraper_author.WebScraperAuthor()
        page = requests.get('https://www.goodreads.com/author/show/45372.Robert_C_Martin')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="rightContainer")
        name = info_author.get_name(contents)
        assert name == "Robert C. Martin"

    def test_author_id(self):
        info_author = webscraper_author.WebScraperAuthor()
        url = 'https://www.goodreads.com/author/show/45372.Robert_C_Martin'
        author_id = info_author.get_author_id(url)
        assert author_id == "45372"

    def test_author_rating(self):
        info_author = webscraper_author.WebScraperAuthor()
        page = requests.get('https://www.goodreads.com/author/show/45372.Robert_C_Martin')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="rightContainer")
        rating = info_author.get_rating(contents)
        assert rating == "4.34"

    def test_author_rating_count(self):
        info_author = webscraper_author.WebScraperAuthor()
        page = requests.get('https://www.goodreads.com/author/show/45372.Robert_C_Martin')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="rightContainer")
        rating_count = info_author.get_rating_count(contents)
        assert rating_count == "23991"

    def test_author_review_count(self):
        info_author = webscraper_author.WebScraperAuthor()
        page = requests.get('https://www.goodreads.com/author/show/45372.Robert_C_Martin')
        soup = BeautifulSoup(page.content, "html.parser")
        contents = soup.find('div', class_="rightContainer")
        review_count = info_author.get_review_count(contents)
        assert review_count == "1562"

    def test_author_image_url(self):
        info_author = webscraper_author.WebScraperAuthor()
        page = requests.get('https://www.goodreads.com/author/show/45372.Robert_C_Martin')
        soup = BeautifulSoup(page.content, "html.parser")
        image_url = info_author.get_image_url(soup)
        assert image_url == "https://images.gr-assets.com/authors/1490470967p5/45372.jpg"
