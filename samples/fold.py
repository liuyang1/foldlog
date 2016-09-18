#! /usr/bin/env python3

import foldlog as fl

locate = fl.locate("value")

q = fl.queue()

actions = {"add": locate | q.append,
           "del": locate | q.remove}

fl.open("fold.log").do(actions)
