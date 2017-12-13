from db import *

class System(object):
    def __init__(self):
        try:
            Base.metadata.create_all(engine)
        except:
            pass
