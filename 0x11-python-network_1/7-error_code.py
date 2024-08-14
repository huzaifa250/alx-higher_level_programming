#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    response = get(url)
    err_txt = 'Error code: {}'
    status = response.status_code
    print(err_txt.format(status) if (status >= 400) else response.text)
