#! /usr/bin/env python3
import foldlog as fl

actions = {"abc": print}

fl.open("grep.log").do(actions)
