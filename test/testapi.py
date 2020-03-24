import os
import requests as req
from unittest import TestCase


class Test(TestCase):
    def test_api_book_list(self):
        res = req.get('http://127.0.0.1:5000/api/books')
        assert res.status_code == 200

    def test_api_author_list(self):
        res = req.get('http://127.0.0.1:5000/api/authors')
        assert res.status_code == 200

    def test_api_book_get(self):
        params = {'title': "Dear Edward"}
        res = req.get(url='http://127.0.0.1:5000/api/books', params=params)
        assert res.status_code == 200

    def test_api_author_get(self):
        params = {'name': "Brian Goetz"}
        res = req.get(url='http://127.0.0.1:5000/api/authors', params=params)
        assert res.status_code == 200

    def test_api_book_put(self):
        params = {'title': "Clean Architecture"}
        data = {'book_id': "18043011"}
        res = req.put(url='http://127.0.0.1:5000/api/books', params=params, json=data)
        assert res.status_code == 200

    def test_api_author_put(self):
        params = {'name': "Brian Goetz"}
        data = {'author_id': "73409"}
        res = req.put(url='http://127.0.0.1:5000/api/authors', params=params, json=data)
        assert res.status_code == 200

    def test_api_book_post(self):
        data = {
            "book_url": "https://www.goodreads.com/book/show/85009.Design_Patterns",
            "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
            "book_id": "85009",
            "isbn": "0201633612",
            "author_url": "https://www.goodreads.com/author/show/48622.Erich_Gamma",
            "author": "Erich Gamma",
            "rating": "4.18",
            "rating_count": "9402",
            "review_count": "327",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348027904l/85009.jpg",
            "sim_books": [
                [
                    "Refactoring: Improving the Design of Existing Code",
                    "https://www.goodreads.com/book/show/44936.Refactoring"
                ],
                [
                    "Clean Code: A Handbook of Agile Software Craftsmanship",
                    "https://www.goodreads.com/book/show/3735293-clean-code"
                ],
                [
                    "Head First Design Patterns",
                    "https://www.goodreads.com/book/show/58128.Head_First_Design_Patterns"
                ],
                [
                    "The Pragmatic Programmer: From Journeyman to Master",
                    "https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer"
                ],
                [
                    "Test Driven Development: By Example",
                    "https://www.goodreads.com/book/show/387190.Test_Driven_Development"
                ],
                [
                    "Code Complete",
                    "https://www.goodreads.com/book/show/4845.Code_Complete"
                ],
                [
                    "Effective C++: 55 Specific Ways to Improve Your Programs and Designs",
                    "https://www.goodreads.com/book/show/105125.Effective_C_"
                ],
                [
                    "Patterns of Enterprise Application Architecture",
                    "https://www.goodreads.com/book/show/70156.Patterns_of_Enterprise_Application_Architecture"
                ],
                [
                    "Effective Java Programming Language Guide",
                    "https://www.goodreads.com/book/show/105099.Effective_Java_Programming_Language_Guide"
                ],
                [
                    "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                    "https://www.goodreads.com/book/show/179133.Domain_Driven_Design"
                ],
                [
                    "Working Effectively with Legacy Code",
                    "https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code"
                ],
                [
                    "Introduction to Algorithms",
                    "https://www.goodreads.com/book/show/108986.Introduction_to_Algorithms"
                ],
                [
                    "The C++ Programming Language",
                    "https://www.goodreads.com/book/show/112251.The_C_Programming_Language"
                ],
                [
                    "The C Programming Language",
                    "https://www.goodreads.com/book/show/515601.The_C_Programming_Language"
                ],
                [
                    "The Clean Coder: A Code of Conduct for Professional Programmers",
                    "https://www.goodreads.com/book/show/10284614-the-clean-coder"
                ],
                [
                    "Java Concurrency in Practice",
                    "https://www.goodreads.com/book/show/127932.Java_Concurrency_in_Practice"
                ],
                [
                    "Refactoring to Patterns",
                    "https://www.goodreads.com/book/show/85041.Refactoring_to_Patterns"
                ],
                [
                    "The Mythical Man-Month: Essays on Software Engineering",
                    "https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month"
                ]
            ]
        }
        res = req.post(url='http://127.0.0.1:5000/api/book', json=data)
        assert res.status_code == 201

    def test_api_books_post(self):
        data = [{
            "book_url": "https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer",
            "title": "The Pragmatic Programmer: From Journeyman to Master",
            "book_id": "4099",
            "isbn": "020161622X",
            "author_url": "https://www.goodreads.com/author/show/2815.Andy_Hunt",
            "author": "Andy Hunt",
            "rating": "4.31",
            "rating_count": "14336",
            "review_count": "784",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1401432508l/4099.jpg",
            "sim_books": [
                [
                    "Clean Code: A Handbook of Agile Software Craftsmanship",
                    "https://www.goodreads.com/book/show/3735293-clean-code"
                ],
                [
                    "Refactoring: Improving the Design of Existing Code",
                    "https://www.goodreads.com/book/show/44936.Refactoring"
                ],
                [
                    "Code Complete",
                    "https://www.goodreads.com/book/show/4845.Code_Complete"
                ],
                [
                    "Design Patterns: Elements of Reusable Object-Oriented Software",
                    "https://www.goodreads.com/book/show/85009.Design_Patterns"
                ],
                [
                    "The Mythical Man-Month: Essays on Software Engineering",
                    "https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month"
                ],
                [
                    "The Clean Coder: A Code of Conduct for Professional Programmers",
                    "https://www.goodreads.com/book/show/10284614-the-clean-coder"
                ],
                [
                    "Head First Design Patterns",
                    "https://www.goodreads.com/book/show/58128.Head_First_Design_Patterns"
                ],
                [
                    "Test Driven Development: By Example",
                    "https://www.goodreads.com/book/show/387190.Test_Driven_Development"
                ],
                [
                    "The Passionate Programmer",
                    "https://www.goodreads.com/book/show/6399113-the-passionate-programmer"
                ],
                [
                    "Clean Architecture",
                    "https://www.goodreads.com/book/show/18043011-clean-architecture"
                ],
                [
                    "Effective Java Programming Language Guide",
                    "https://www.goodreads.com/book/show/105099.Effective_Java_Programming_Language_Guide"
                ],
                [
                    "JavaScript: The Good Parts",
                    "https://www.goodreads.com/book/show/2998152-javascript"
                ],
                [
                    "Structure and Interpretation of Computer Programs (MIT Electrical Engineering and Computer Science)",
                    "https://www.goodreads.com/book/show/43713.Structure_and_Interpretation_of_Computer_Programs"
                ],
                [
                    "Extreme Programming Explained: Embrace Change (The XP Series)",
                    "https://www.goodreads.com/book/show/67833.Extreme_Programming_Explained"
                ],
                [
                    "Working Effectively with Legacy Code",
                    "https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code"
                ],
                [
                    "The C Programming Language",
                    "https://www.goodreads.com/book/show/515601.The_C_Programming_Language"
                ],
                [
                    "Clean Agile: Back to Basics",
                    "https://www.goodreads.com/book/show/45280021-clean-agile"
                ],
                [
                    "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                    "https://www.goodreads.com/book/show/179133.Domain_Driven_Design"
                ]
            ]
        },
        {
            "book_url": "https://www.goodreads.com/book/show/44936.Refactoring",
            "title": "Refactoring: Improving the Design of Existing Code",
            "book_id": "44936",
            "isbn": "0201485672",
            "author_url": "https://www.goodreads.com/author/show/25215.Martin_Fowler",
            "author": "Martin Fowler",
            "rating": "4.24",
            "rating_count": "6581",
            "review_count": "258",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386925632l/44936.jpg",
            "sim_books": [
                [
                    "Design Patterns: Elements of Reusable Object-Oriented Software",
                    "https://www.goodreads.com/book/show/85009.Design_Patterns"
                ],
                [
                    "Clean Code: A Handbook of Agile Software Craftsmanship",
                    "https://www.goodreads.com/book/show/3735293-clean-code"
                ],
                [
                    "Working Effectively with Legacy Code",
                    "https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code"
                ],
                [
                    "The Pragmatic Programmer: From Journeyman to Master",
                    "https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer"
                ],
                [
                    "Test Driven Development: By Example",
                    "https://www.goodreads.com/book/show/387190.Test_Driven_Development"
                ],
                [
                    "Code Complete",
                    "https://www.goodreads.com/book/show/4845.Code_Complete"
                ],
                [
                    "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                    "https://www.goodreads.com/book/show/179133.Domain_Driven_Design"
                ],
                [
                    "Head First Design Patterns",
                    "https://www.goodreads.com/book/show/58128.Head_First_Design_Patterns"
                ],
                [
                    "Growing Object-Oriented Software, Guided by Tests",
                    "https://www.goodreads.com/book/show/4268826-growing-object-oriented-software-guided-by-tests"
                ],
                [
                    "The Clean Coder: A Code of Conduct for Professional Programmers",
                    "https://www.goodreads.com/book/show/10284614-the-clean-coder"
                ],
                [
                    "Clean Architecture",
                    "https://www.goodreads.com/book/show/18043011-clean-architecture"
                ],
                [
                    "Refactoring to Patterns",
                    "https://www.goodreads.com/book/show/85041.Refactoring_to_Patterns"
                ],
                [
                    "Extreme Programming Explained: Embrace Change (The XP Series)",
                    "https://www.goodreads.com/book/show/67833.Extreme_Programming_Explained"
                ],
                [
                    "The Passionate Programmer",
                    "https://www.goodreads.com/book/show/6399113-the-passionate-programmer"
                ],
                [
                    "The Mythical Man-Month: Essays on Software Engineering",
                    "https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month"
                ],
                [
                    "Effective Java Programming Language Guide",
                    "https://www.goodreads.com/book/show/105099.Effective_Java_Programming_Language_Guide"
                ],
                [
                    "Java Concurrency in Practice",
                    "https://www.goodreads.com/book/show/127932.Java_Concurrency_in_Practice"
                ],
                [
                    "Agile Software Development, Principles, Patterns, and Practices",
                    "https://www.goodreads.com/book/show/84985.Agile_Software_Development_Principles_Patterns_and_Practices"
                ]
            ]
        }]
        res = req.post(url='http://127.0.0.1:5000/api/books', json=data)
        assert res.status_code == 201

    def test_api_author_post(self):
        data = {
            "name": "Erich Gamma",
            "author_url": "https://www.goodreads.com/author/show/48622.Erich_Gamma",
            "author_id": "48622",
            "rating": "4.19",
            "rating_count": "15535",
            "review_count": "550",
            "image_url": "https://images.gr-assets.com/authors/1488278705p5/48622.jpg",
            "related_authors": [
                [
                    "Chad Fowler",
                    "https://www.goodreads.com/author/show/302.Chad_Fowler"
                ],
                [
                    "Andy Hunt",
                    "https://www.goodreads.com/author/show/2815.Andy_Hunt"
                ],
                [
                    "Steve McConnell",
                    "https://www.goodreads.com/author/show/3307.Steve_McConnell"
                ],
                [
                    "Michael C. Feathers",
                    "https://www.goodreads.com/author/show/25201.Michael_C_Feathers"
                ],
                [
                    "Kent Beck",
                    "https://www.goodreads.com/author/show/25211.Kent_Beck"
                ],
                [
                    "Martin Fowler",
                    "https://www.goodreads.com/author/show/25215.Martin_Fowler"
                ],
                [
                    "Jon L. Bentley",
                    "https://www.goodreads.com/author/show/29393.Jon_L_Bentley"
                ],
                [
                    "Eric Freeman",
                    "https://www.goodreads.com/author/show/32731.Eric_Freeman"
                ],
                [
                    "Bruce Eckel",
                    "https://www.goodreads.com/author/show/40523.Bruce_Eckel"
                ],
                [
                    "Robert C. Martin",
                    "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
                ],
                [
                    "Gregor Hohpe",
                    "https://www.goodreads.com/author/show/48627.Gregor_Hohpe"
                ],
                [
                    "Joshua Kerievsky",
                    "https://www.goodreads.com/author/show/48660.Joshua_Kerievsky"
                ],
                [
                    "Joshua Bloch",
                    "https://www.goodreads.com/author/show/60805.Joshua_Bloch"
                ],
                [
                    "Scott Meyers",
                    "https://www.goodreads.com/author/show/60832.Scott_Meyers"
                ],
                [
                    "Thomas H. Cormen",
                    "https://www.goodreads.com/author/show/60841.Thomas_H_Cormen"
                ],
                [
                    "Craig Walls",
                    "https://www.goodreads.com/author/show/61117.Craig_Walls"
                ],
                [
                    "Bjarne Stroustrup",
                    "https://www.goodreads.com/author/show/64947.Bjarne_Stroustrup"
                ],
                [
                    "Brian Goetz",
                    "https://www.goodreads.com/author/show/73409.Brian_Goetz"
                ],
                [
                    "Eric Evans",
                    "https://www.goodreads.com/author/show/104368.Eric_Evans"
                ],
                [
                    "Brian W. Kernighan",
                    "https://www.goodreads.com/author/show/153350.Brian_W_Kernighan"
                ],
                [
                    "Douglas Crockford",
                    "https://www.goodreads.com/author/show/1290380.Douglas_Crockford"
                ],
                [
                    "Roy Osherove",
                    "https://www.goodreads.com/author/show/2938301.Roy_Osherove"
                ],
                [
                    "Frederick P. Brooks Jr.",
                    "https://www.goodreads.com/author/show/3174788.Frederick_P_Brooks_Jr_"
                ],
                [
                    "Steve  Freeman",
                    "https://www.goodreads.com/author/show/9824504.Steve_Freeman"
                ]
            ],
            "author_books": [
                [
                    "Design Patterns: Elements of Reusable Object-Oriented Software",
                    "https://www.goodreads.com/book/show/85009.Design_Patterns"
                ],
                [
                    "Refactoring: Improving the Design of Existing Code",
                    "https://www.goodreads.com/book/show/44936.Refactoring"
                ],
                [
                    "Contributing to Eclipse: Principles, Patterns, and Plug-Ins",
                    "https://www.goodreads.com/book/show/310630.Contributing_to_Eclipse"
                ],
                [
                    "Objektorientierte Software Entwicklung Am Beispiel Von Et++: Design Muster, Klassenbibliothek, Werkzeuge",
                    "https://www.goodreads.com/book/show/310629.Objektorientierte_Software_Entwicklung_Am_Beispiel_Von_Et_"
                ],
                [
                    "Introduction to Object Orient Design in C++",
                    "https://www.goodreads.com/book/show/310631.Introduction_to_Object_Orient_Design_in_C_"
                ],
                [
                    "Object-Oriented Application Frameworks",
                    "https://www.goodreads.com/book/show/2825238-object-oriented-application-frameworks"
                ],
                [
                    "The Future of Software Engineering: Panel Discussions",
                    "https://www.goodreads.com/book/show/21147713-the-future-of-software-engineering"
                ]
            ]
        }
        res = req.post(url='http://127.0.0.1:5000/api/author', json=data)
        assert res.status_code == 201

    def test_api_authors_post(self):
        data = [{
            "name": "Eric Freeman",
            "author_url": "https://www.goodreads.com/author/show/32731.Eric_Freeman",
            "author_id": "32731",
            "rating": "4.23",
            "rating_count": "9487",
            "review_count": "632",
            "image_url": "https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png",
            "related_authors": [
                [
                    "Sun Tzu",
                    "https://www.goodreads.com/author/show/1771.Sun_Tzu"
                ],
                [
                    "Andy Hunt",
                    "https://www.goodreads.com/author/show/2815.Andy_Hunt"
                ],
                [
                    "Steve McConnell",
                    "https://www.goodreads.com/author/show/3307.Steve_McConnell"
                ],
                [
                    "Walter Isaacson",
                    "https://www.goodreads.com/author/show/7111.Walter_Isaacson"
                ],
                [
                    "Yvon Chouinard",
                    "https://www.goodreads.com/author/show/12641.Yvon_Chouinard"
                ],
                [
                    "Michael C. Feathers",
                    "https://www.goodreads.com/author/show/25201.Michael_C_Feathers"
                ],
                [
                    "Kent Beck",
                    "https://www.goodreads.com/author/show/25211.Kent_Beck"
                ],
                [
                    "Martin Fowler",
                    "https://www.goodreads.com/author/show/25215.Martin_Fowler"
                ],
                [
                    "Kathy Sierra",
                    "https://www.goodreads.com/author/show/32733.Kathy_Sierra"
                ],
                [
                    "Bruce Eckel",
                    "https://www.goodreads.com/author/show/40523.Bruce_Eckel"
                ],
                [
                    "Robert C. Martin",
                    "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
                ],
                [
                    "Erich Gamma",
                    "https://www.goodreads.com/author/show/48622.Erich_Gamma"
                ],
                [
                    "Joshua Bloch",
                    "https://www.goodreads.com/author/show/60805.Joshua_Bloch"
                ],
                [
                    "Scott Meyers",
                    "https://www.goodreads.com/author/show/60832.Scott_Meyers"
                ],
                [
                    "Thomas H. Cormen",
                    "https://www.goodreads.com/author/show/60841.Thomas_H_Cormen"
                ],
                [
                    "Craig Walls",
                    "https://www.goodreads.com/author/show/61117.Craig_Walls"
                ],
                [
                    "Brian Goetz",
                    "https://www.goodreads.com/author/show/73409.Brian_Goetz"
                ],
                [
                    "Eric Evans",
                    "https://www.goodreads.com/author/show/104368.Eric_Evans"
                ],
                [
                    "Douglas Crockford",
                    "https://www.goodreads.com/author/show/1290380.Douglas_Crockford"
                ],
                [
                    "Jez Humble",
                    "https://www.goodreads.com/author/show/4149510.Jez_Humble"
                ],
                [
                    "\u0411\u043e\u0440\u0438\u0441 \u0414\u0440\u0430\u043d\u0433\u043e\u0432",
                    "https://www.goodreads.com/author/show/4840713._"
                ],
                [
                    "Zlatan Ibrahimovi\u0107",
                    "https://www.goodreads.com/author/show/5324300.Zlatan_Ibrahimovi_"
                ],
                [
                    "\u0421\u0442\u0435\u0444\u0430\u043d \u0421\u0442\u0430\u043c\u0431\u043e\u043b\u043e\u0432",
                    "https://www.goodreads.com/author/show/5820526._"
                ],
                [
                    "\u0421\u0442\u043e\u044f\u043d \u0421\u0442\u043e\u044f\u043d\u043e\u0432",
                    "https://www.goodreads.com/author/show/6570999._"
                ],
                [
                    "Ilya Grigorik",
                    "https://www.goodreads.com/author/show/6889482.Ilya_Grigorik"
                ],
                [
                    "Steve  Freeman",
                    "https://www.goodreads.com/author/show/9824504.Steve_Freeman"
                ],
                [
                    "\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440 \u0412\u0430\u0437\u043e\u0432",
                    "https://www.goodreads.com/author/show/17901359._"
                ]
            ],
            "author_books": [
                [
                    "Head First Design Patterns",
                    "https://www.goodreads.com/book/show/58128.Head_First_Design_Patterns"
                ],
                [
                    "Head First HTML with CSS & XHTML",
                    "https://www.goodreads.com/book/show/564.Head_First_HTML_with_CSS_XHTML"
                ],
                [
                    "Use a Cabe\u00e7a! An\u00e1lise e Projeto Orientado ao Objeto",
                    "https://www.goodreads.com/book/show/18518240-use-a-cabe-a-an-lise-e-projeto-orientado-ao-objeto"
                ],
                [
                    "Head First HTML and CSS",
                    "https://www.goodreads.com/book/show/13355960-head-first-html-and-css"
                ],
                [
                    "Head First HTML5 Programming",
                    "https://www.goodreads.com/book/show/10896369-head-first-html5-programming"
                ],
                [
                    "Head First JavaScript Programming",
                    "https://www.goodreads.com/book/show/17912853-head-first-javascript-programming"
                ],
                [
                    "Head Rush Ajax",
                    "https://www.goodreads.com/book/show/45578.Head_Rush_Ajax"
                ],
                [
                    "Head First Design Patterns Poster",
                    "https://www.goodreads.com/book/show/7705818-head-first-design-patterns-poster"
                ],
                [
                    "An Engineering Manager's Guide to Design Patterns",
                    "https://www.goodreads.com/book/show/25739573-an-engineering-manager-s-guide-to-design-patterns"
                ],
                [
                    "Javaspaces Principles, Patterns, and Practice",
                    "https://www.goodreads.com/book/show/651977.Javaspaces_Principles_Patterns_and_Practice"
                ],
                [
                    "Head First Learn to Code: A Learner's Guide to Coding and Computational Thinking",
                    "https://www.goodreads.com/book/show/35355002-head-first-learn-to-code"
                ],
                [
                    "iPad Programming",
                    "https://www.goodreads.com/book/show/7848922-ipad-programming"
                ],
                [
                    "Mixed Messages: When Praise & Slander Collide",
                    "https://www.goodreads.com/book/show/17834812-mixed-messages"
                ],
                [
                    "Grey's Anatomy: Season 5",
                    "https://www.goodreads.com/book/show/28803443-grey-s-anatomy"
                ],
                [
                    "Eric Freeman",
                    "https://www.goodreads.com/book/show/8946333-eric-freeman"
                ],
                [
                    "The Sin Of Unbelief: A Believer's Guide To Rightousness In The Eyes Of God",
                    "https://www.goodreads.com/book/show/25505027-the-sin-of-unbelief"
                ],
                [
                    "The Rising",
                    "https://www.goodreads.com/book/show/20613953-the-rising"
                ]
            ]
        },
        {
            "name": "Joshua Bloch",
            "author_url": "https://www.goodreads.com/author/show/60805.Joshua_Bloch",
            "author_id": "60805",
            "rating": "4.47",
            "rating_count": "9073",
            "review_count": "473",
            "image_url": "https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png",
            "related_authors": [
                [
                    "Andy Hunt",
                    "https://www.goodreads.com/author/show/2815.Andy_Hunt"
                ],
                [
                    "Steve McConnell",
                    "https://www.goodreads.com/author/show/3307.Steve_McConnell"
                ],
                [
                    "Michael C. Feathers",
                    "https://www.goodreads.com/author/show/25201.Michael_C_Feathers"
                ],
                [
                    "Kent Beck",
                    "https://www.goodreads.com/author/show/25211.Kent_Beck"
                ],
                [
                    "Martin Fowler",
                    "https://www.goodreads.com/author/show/25215.Martin_Fowler"
                ],
                [
                    "Eric Freeman",
                    "https://www.goodreads.com/author/show/32731.Eric_Freeman"
                ],
                [
                    "Kathy Sierra",
                    "https://www.goodreads.com/author/show/32733.Kathy_Sierra"
                ],
                [
                    "Bruce Eckel",
                    "https://www.goodreads.com/author/show/40523.Bruce_Eckel"
                ],
                [
                    "Robert C. Martin",
                    "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
                ],
                [
                    "Erich Gamma",
                    "https://www.goodreads.com/author/show/48622.Erich_Gamma"
                ],
                [
                    "Scott Meyers",
                    "https://www.goodreads.com/author/show/60832.Scott_Meyers"
                ],
                [
                    "Craig Walls",
                    "https://www.goodreads.com/author/show/61117.Craig_Walls"
                ],
                [
                    "Brian Goetz",
                    "https://www.goodreads.com/author/show/73409.Brian_Goetz"
                ],
                [
                    "Jeffrey E.F. Friedl",
                    "https://www.goodreads.com/author/show/404200.Jeffrey_E_F_Friedl"
                ],
                [
                    "Douglas Crockford",
                    "https://www.goodreads.com/author/show/1290380.Douglas_Crockford"
                ],
                [
                    "Sam Newman",
                    "https://www.goodreads.com/author/show/3362774.Sam_Newman"
                ],
                [
                    "Martin Kleppmann",
                    "https://www.goodreads.com/author/show/7969625.Martin_Kleppmann"
                ],
                [
                    "Aditya Y. Bhargava",
                    "https://www.goodreads.com/author/show/8423673.Aditya_Y_Bhargava"
                ],
                [
                    "Dmitry Jemerov",
                    "https://www.goodreads.com/author/show/15018113.Dmitry_Jemerov"
                ]
            ],
            "author_books": []
        },
        {
            "name": "Brian Goetz",
            "author_url": "https://www.goodreads.com/author/show/73409.Brian_Goetz",
            "author_id": "73409",
            "rating": "4.44",
            "rating_count": "2362",
            "review_count": "118",
            "image_url": "https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png",
            "related_authors": [
                [
                    "Andy Hunt",
                    "https://www.goodreads.com/author/show/2815.Andy_Hunt"
                ],
                [
                    "Steve McConnell",
                    "https://www.goodreads.com/author/show/3307.Steve_McConnell"
                ],
                [
                    "Michael T. Nygard",
                    "https://www.goodreads.com/author/show/6089.Michael_T_Nygard"
                ],
                [
                    "Michael C. Feathers",
                    "https://www.goodreads.com/author/show/25201.Michael_C_Feathers"
                ],
                [
                    "Martin Fowler",
                    "https://www.goodreads.com/author/show/25215.Martin_Fowler"
                ],
                [
                    "Scott Oaks",
                    "https://www.goodreads.com/author/show/28723.Scott_Oaks"
                ],
                [
                    "Eric Freeman",
                    "https://www.goodreads.com/author/show/32731.Eric_Freeman"
                ],
                [
                    "Kathy Sierra",
                    "https://www.goodreads.com/author/show/32733.Kathy_Sierra"
                ],
                [
                    "Bruce Eckel",
                    "https://www.goodreads.com/author/show/40523.Bruce_Eckel"
                ],
                [
                    "Robert C. Martin",
                    "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
                ],
                [
                    "Erich Gamma",
                    "https://www.goodreads.com/author/show/48622.Erich_Gamma"
                ],
                [
                    "Joshua Bloch",
                    "https://www.goodreads.com/author/show/60805.Joshua_Bloch"
                ],
                [
                    "Scott Meyers",
                    "https://www.goodreads.com/author/show/60832.Scott_Meyers"
                ],
                [
                    "Thomas H. Cormen",
                    "https://www.goodreads.com/author/show/60841.Thomas_H_Cormen"
                ],
                [
                    "Craig Walls",
                    "https://www.goodreads.com/author/show/61117.Craig_Walls"
                ],
                [
                    "Eric Evans",
                    "https://www.goodreads.com/author/show/104368.Eric_Evans"
                ],
                [
                    "Brian W. Kernighan",
                    "https://www.goodreads.com/author/show/153350.Brian_W_Kernighan"
                ],
                [
                    "Martin Odersky",
                    "https://www.goodreads.com/author/show/666527.Martin_Odersky"
                ],
                [
                    "Douglas Crockford",
                    "https://www.goodreads.com/author/show/1290380.Douglas_Crockford"
                ],
                [
                    "Scott Chacon",
                    "https://www.goodreads.com/author/show/1846363.Scott_Chacon"
                ],
                [
                    "Frederick P. Brooks Jr.",
                    "https://www.goodreads.com/author/show/3174788.Frederick_P_Brooks_Jr_"
                ],
                [
                    "Sam Newman",
                    "https://www.goodreads.com/author/show/3362774.Sam_Newman"
                ],
                [
                    "Gayle Laakmann McDowell",
                    "https://www.goodreads.com/author/show/4692311.Gayle_Laakmann_McDowell"
                ],
                [
                    "Martin Kleppmann",
                    "https://www.goodreads.com/author/show/7969625.Martin_Kleppmann"
                ],
                [
                    "Steve  Freeman",
                    "https://www.goodreads.com/author/show/9824504.Steve_Freeman"
                ],
                [
                    "Dmitry Jemerov",
                    "https://www.goodreads.com/author/show/15018113.Dmitry_Jemerov"
                ]
            ],
            "author_books": []
        }]
        res = req.post(url='http://127.0.0.1:5000/api/authors', json=data)
        assert res.status_code == 201
