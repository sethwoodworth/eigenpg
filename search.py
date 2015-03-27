#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

from login import auth


def append(gen, target):
    target.append(gen.next())

def main():

    g = auth()
    s = g.search_code("language:html user:GITenberg")
    # get the first 30 html files
    # TODO: do this via limiting search_code
    ss = []
    [append(s, ss) for _ in xrange(30)]
    # get a html file
    h = ss[20]

    html_file = h.repository.file_contents(h.path).content
    print html_file

main()
