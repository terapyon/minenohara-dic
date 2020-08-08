import json
import eel

from db.ejdic import found_word

LIMIT = 10


def words_means(word):
    out = []
    for i in range(4):
        out.extend(list(found_word(word, i)))
        if len(out) > LIMIT + 20:
            break
    return out


def results(word):
    count = 0
    text_list = set()
    out = words_means(word)
    for text, mean in out:
        if text not in text_list:
            yield text, mean
            count += 1
            text_list.add(text)
            if count > LIMIT + 1:
                break


@eel.expose
def get_candidates(word):
    result = [
        {"word": word, "candidate": text, "translate": mean}
        for text, mean in results(word)
    ]
    return json.dumps(result)


def start_gui():
    app_options = {
        "port": 18085,
    }
    eel.init("front/dist")
    eel.start("index.html", **app_options)


if __name__ == "__main__":
    start_gui()
