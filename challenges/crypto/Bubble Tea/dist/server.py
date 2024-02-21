import time
from random import SystemRandom
from secret import FLAG

rand = SystemRandom()

luck = rand.sample(range(64), 32)
spillage = [i in luck for i in range(64)]


def bytes_to_num(data: bytes):
    return int(data.hex(), 16)


def bubble():
    return rand.getrandbits(512 // 2)


def tea():
    return rand.getrandbits(512 // 2)


def bubble_tea():
    return bubble() * tea()


def generate_shares(secret: bytes, n: int):
    pn = bytes_to_num(secret)

    shares = []
    for _ in range(n-1):
        p = rand.getrandbits(512)
        pn ^= p
        shares.append(p)
    shares.append(pn)

    return shares


def serve(shares: list[int]):
    print("Preparing your order...", flush=True)
    time.sleep(1.5)
    print("Here are the shares you have ordered.")
    print("Oops, I've spilled some bubble tea over it!")
    for oops in spillage:
        if oops:
            print(bubble_tea())
        else:
            print(shares.pop())


def menu():
    print(
        "Welcome to the shares store, here is our menu:\n"
        "[1] Flag shares (limited edition, 1 per pax!)\n"
        "[2] Custom shares\n"
        "[3] Bubble Tea"
    )


polite = True
received_flag = False
while polite:
    menu()
    choice = input("What would you like to have: ")
    match choice:
        case "1":
            if received_flag:
                print("Flag share is limited to only 1 per person!")
                continue
            shares = generate_shares(FLAG, 32)
            serve(shares)
            received_flag = True
        case "2":
            message = input("Enter the message to share: ")
            try:
                message = message.encode()
                shares = generate_shares(message, 32)
            except:
                polite = False
                break
            serve(shares)
        case "3":
            drink = bubble_tea()
            print("Here's your bubble tea:")
            print(drink)
        case _:
            polite = False

if not polite:
    print("So rude, we don't welcome customers that speak gibberish!")
    print("You have been kicked out of the store.")
