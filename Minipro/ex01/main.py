import sys
from checkmate import checkmate

def main():
    #print("Arguments:", sys.argv)

    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        #print("Reading:", filename)
        try:
            with open(filename, "r") as f:
                board = f.read()
            checkmate(board)
        except Exception as e:
            print("Error")

if __name__ == "__main__":
    main()
