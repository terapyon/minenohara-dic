import json
import eel


@eel.expose
def return_hello():
    return "Hello!!"

@eel.expose
def get_candidates(word):
    result = [
        {"word": word,
         "candidate": "candidate",
         "translate": "translate"
         },
        {"word": word,
         "candidate": "candidate2",
         "translate": "translate2"
         }
    ]
    return json.dumps(result)

def start_gui():
    eel.init("front/dist")
    eel.start("index.html")


if __name__ == "__main__":
    start_gui()
