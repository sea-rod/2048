from start_2048 import start

if __name__ == "__main__":
    game = start()

    swtch = {'a':game.left,
            'd':game.right,
            'w':game.up,
            's':game.down
            }

    while True:
        try:
            print("'w' for up\n'a' for left\n'd' for right\n's' for down")
            ch = input("Enter your choice:")
            if ch == 'q':
                exit()
            game.iszero = False
            swtch[ch]()
            game.random_ch()
            game.print_a()
            state = game.status()
            print(state)
            if state == 'won':
                print("you won!!!!!!!!!")
                break
            if state == 'lost':
                print("you lost!!!")
                break
        except KeyError:
            print("Try again invalid choice")