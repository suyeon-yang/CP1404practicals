import wikipedia
user_input = input(">>>")
while user_input != "":
    try:
        title = wikipedia.page(user_input, auto_suggest=False)
        print(title.title)
        print(title.url)
        print(title.summary)
        user_input = input(">>>")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        user_input = input(">>>")





