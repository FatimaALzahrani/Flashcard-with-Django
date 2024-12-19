from django.shortcuts import render

def flashcards_list(request):
    flashcards = [
        {"question": "Python is a high-level programming language. (True/False)", "answer": "True"},
        {"question": "Who created Python?", "answer": "Guido van Rossum"},
        {"question": "Python was developed in 1995. (True/False)", "answer": "False, it was developed in 1989"},
        {"question": "Python is used for web development, artificial intelligence, and data analysis. (True/False)", "answer": "True"},
        {"question": "What is the main goal of Python?", "answer": "To be a simple and readable programming language for easy learning"},
        {"question": "What type of license does Python have?", "answer": "Open source"},
        {"question": "The first official release of Python was in 1991. (True/False)", "answer": "True"},
        {"question": "Python is a text-based language. (True/False)", "answer": "True"},
        {"question": "Python is only used for complex software development. (True/False)", "answer": "False, it is also used for simple applications"},
        {"question": "Python is supported by a global community. (True/False)", "answer": "True"},
        {"question": "What is the key feature of Python that makes it popular among developers?", "answer": "Its simplicity and readability"},
        {"question": "What programming language is named after a planet?", "answer": "None, this question is misleading"},
        {"question": "Python supports exception handling. (True/False)", "answer": "True"},
        {"question": "Python is a dynamic language. (True/False)", "answer": "True"},
        {"question": "In which year did Python start being developed?", "answer": "1989"},
        {"question": "Python is used in artificial intelligence. (True/False)", "answer": "True"},
        {"question": "Python is a fast programming language that works on all systems. (True/False)", "answer": "True"},
        {"question": "Why was Python created?", "answer": "To design a simple, readable language addressing flaws in ABC while keeping its strengths."},
        {"question": "Python's first official release was in February of which year?", "answer": "1991"},
        {"question": "Who is the creator of Python, and where was it created?", "answer": "Guido van Rossum, created at Centrum Wiskunde & Informatica (CWI) in the Netherlands."},
        {"question": "What was the main aim of Python's creation?", "answer": "To create a simple and readable language for easy learning and to support exception handling and dynamic typing."},
        {"question": "Is Python open-source?", "answer": "Yes"},
        {"question": "Which fields use Python widely?", "answer": "Artificial intelligence, data science, web development, automation, and more."},
        {"question": "What is the Python community's role?", "answer": "It is global and continuously contributes to Python's growth and evolution."},
        {"question": "Python's development started in which decade?", "answer": "Late 1980s"},
    ]
    return render(request, 'flashcards_list.html', {'flashcards': flashcards})
