import os
import base64


def shift( data: str, amt: int ) -> str:
    return "".join( [ chr( ord( c ) + amt ) for c in data ] )


def decrypt( data: bytes, key: bytes ) -> bytes:
    return bytes( d ^ key[ i % len( key ) ] for i, d in enumerate( data ) )


def load_data( raw_folder: str ) -> dict[ str, bytes ]:
    order = {
        1: "register",
        2: "register(1)",
        3: "login",
        4: "login(1)",
        5: "media%3furl=https%3A%2F%2Fi.redd.it%ryuwmzmdhheclmc.png",
        6: "media%3furl=https%3A%2F%2Fi.redd.it%zwxsdehkjftpmfk.png",
        7: "media%3furl=https%3A%2F%2Fi.redd.it%lazehucvurciccg.png",
        8: "media%3furl=https%3A%2F%2Fi.redd.it%bjuslddkpcbbjbn.png",
        9: "media%3furl=https%3A%2F%2Fi.redd.it%ozywkwxdqvszrun.png",
        10: "jquery-3.3.1.slim.min.js",
        11: "jquery-3.3.1.slim.min(1).js",
    }

    data = {}
    for file_name in os.listdir( raw_folder ):
        for order_num, order_name in order.items():
            if order_name == file_name:
                with open( os.path.join( raw_folder, file_name ), "rb" ) as f:
                    data[ order_num ] = f.read()

    return data


if __name__ == "__main__":
    data = load_data( "./raw" )
    SHIFT = 9

    print( f"[-] Decoding packet 11..." )
    dec = shift( base64.b64decode( data[ 11 ].split( b"||" )[ -1 ] ).decode(), -SHIFT )
    print( f"[+] Decoded packet 11: {dec}" )

    print( f"[+] Found key: {dec.split('|')[1]}" )
    key = dec.split( '|' )[ 1 ]  # zzmP9zzmP9

    # if u wanna test, move the flag.txt.enc to ../dist
    with open( "../dist/flag.txt.enc", "rb" ) as f:
        enc = f.read()
        flag = decrypt( enc, key.encode() )
        print( f"[+] Decrypted flag: {flag.decode()}" )

# LNC24{mOnKeY_sEe_M0nkey_7w0_7f7ad80dafbd28f2401ae37a8e0684a9}
