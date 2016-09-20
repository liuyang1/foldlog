from foldlog as fl

actions = {'addr': fl.locate("size ") | readHex}

fl.open("acc.log").do(actions)
