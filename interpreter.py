import sys
import re

def main():
	prompt = sys.argv[1]
	print(prompt)
	tokens = re.findall(r"\d+|[+*/()-]", prompt)
	print(tokens)

if __name__ == "__main__":
	main()