import sys
import argparse

# Wyświetlenie argumentów
# print(sys.argv)

#dodanie tego co ma się wyświetlić jak nie będzie żadnych parametrów
parser = argparse.ArgumentParser(description='Testowy skrypt ( wyświetlam to co będzie jeżeli będzie -h )')
parser.add_argument('filename', help='Filename to process')
parser.add_argument('-l', '--limit', help='Length limit', type=int, default=10)
parser.add_argument('-f', '--flag', help='A boolean flag', action='store_true') # flaga nie wymagane do uruchomienia poprzez action
parser.add_argument('-L', '--list', help='A list of values', nargs='*')
args = parser.parse_args()

print(args)

#wyciągnięcie argumentu
print(f'Processing file: {args.filename}')
print(f'Applying length limit: {args.limit} {type(args.limit)}')
print(f'Flag is set to: {args.flag} {type(args.flag)}')
print(f'List of values: {args.list} {type(args.list)}')