import sys

argc = len(sys.argv)
argv = sys.argv
print(f"argc: {argc}")
print(f"argv:")
for i in range(argc):
    print(f"argv[{i}]")