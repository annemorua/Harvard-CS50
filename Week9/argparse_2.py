import argparse_1

parser = argparse.Argument.Parser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

#Lo que me tira en la terminal son las cosas que puedo escribirle para correrlo.
