#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

from login import auth


def append(gen, target):
    target.append(gen.next())

def write_html(path, content64):
    """ a path to write html to
    and some base64 content to fill it """
    print path
    print base64.b64decode(content64)
    pass

def main():

    g = auth()
    s = g.search_code("language:html user:GITenberg")
    # get the first 30 html files
    # TODO: do this via limiting search_code
    ss = []
    [append(s, ss) for _ in xrange(30)]
    # get a html file
    h = ss[20]

    file_content = h.repository.file_contents(h.path).content
    write_html(h.path, file_content)

main()
