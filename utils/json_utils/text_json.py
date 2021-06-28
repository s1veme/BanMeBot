import json

def get_words() -> dict:
    with open('data/blacklist-words.json') as file:
        data = json.loads(file.read())
    return data

def write_words(data: dict) -> None:
    print(data)
    with open('data/blacklist-words.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

def add_word(text: str) -> list:
    data = get_words()        
    data['words'].append(text)
    write_words(data)
        
    return data

# Можно объеденить в одну функцию
def remove_word(words: list) -> list:
    data = get_words()
    data['words'] = words
    write_words(data)
    
    return words
    

        
