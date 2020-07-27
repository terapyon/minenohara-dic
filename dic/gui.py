import eel


@eel.expose
def return_hello():
    return "Hello!!"


def start_gui():
    eel.init("front/dist")
    eel.start("index.html")


if __name__ == "__main__":
    start_gui()
