def say_hello():
    print("Hello")

say_hello()

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    for row in picture:
        for column in row:
            if column == 0:
                print(" ", end="")
            elif column == 1:
                print("*", end="")
        print("\n", end="")

show_tree()
show_tree()
show_tree()
show_tree()