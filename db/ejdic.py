import os
import sqlite3
from db.automata import Matcher, find_all_matches

dataset_dir = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(dataset_dir + "/ejdict.sqlite3")


def make_sorted_words():
    c = conn.cursor()
    # sql = '''SELECT * FROM items WHERE level > 0 ORDER BY word'''
    sql = """SELECT * FROM items ORDER BY word"""
    rows = c.execute(sql)
    return sorted((r[1], r[2]) for r in rows)


dic_words = make_sorted_words()
words = [w for w, m in dic_words]
means = [m for w, m in dic_words]


def found_word(word, k):
    m = Matcher(words, means)
    return find_all_matches(word, k, m)


if __name__ == "__main__":
    print(len(dic_words))
    print(dic_words)
