import re

import requests


def test_scores_service(url):
    response = requests.get(url)
    match = re.search(r'<div id="score">(\d+)</div>', response.text)
    print(match)
    score = int(match.group(1))
    print(score)
    if 0 < score < 1000:
        return True
    return False


def main_function():
    if test_scores_service("http://127.0.0.1:5000"):
        return 0
    return -1

main_function()