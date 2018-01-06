class Ostream(object):
  def __init__(self, output=None):
    print("init........")
  def __lshift__(self, thing):
    print("<<--", thing)
  def __rshift__(self, thing):
    print("-->>", thing)

o = Ostream()
o << "this is a new test"
o >> 123456

