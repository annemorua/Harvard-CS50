import sys

from mylibrary import hello
from mylibrary import goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
