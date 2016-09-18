#! /usr/bin/env python3
import foldlog as fl

actions = {"abc": lambda x: print(x)}

fl.open("grep.log").do(actions)
