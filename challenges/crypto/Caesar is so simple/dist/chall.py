from secret import FLAG
from random import SystemRandom

CHAR_SET = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ """
CHAR_TABLE = [
    str.maketrans(CHAR_SET, CHAR_SET[i:]+CHAR_SET[:i])
    for i in range(len(CHAR_SET))
]
P = [
    0, 4, 8, 12,
    1, 5, 9, 13,
    2, 6, 10, 14,
    3, 7, 11, 15
]


class CaesarCipher:#?
    """ Caesar cipher? """    

    def __init__(self):
        self.__key = self._gen_rand_bytes(32)

    def encrypt(self, message: str):
        """ Encrypts a message using Ceasar cipher? """
        _iv = iv = self._gen_rand_bytes(16)
        message = self._pad(message, 16)

        encrypted = []
        for block in self._chunks(message, 16):

            # Initialise using IV
            block = self._caesar_encrypt(block, _iv)

            # Performs 32 rounds of encryption using sub keys
            for sub_key in self._get_round_keys():
                block = self._caesar_transform(block)
                block = self._shuffle(block)
                block = self._caesar_encrypt(block, sub_key)

            encrypted.append(block)
            _iv = block.encode()  # Update IV (CBC-mode)

        encrypted = "".join(encrypted)
        return encrypted, iv

    def _caesar_encrypt(self, block: str, key: bytes):
        """ Encrypts a block with key using caesar cipher """
        return "".join(self._caesar(m, k) for m, k in zip(block, key, strict=True))

    def _caesar_transform(self, block: str):
        """ Transform a block of message using caesar cipher """

        # Transform rows
        block = list(self._chunks(block, 4))
        block[0] = self._caesar(block[0], 13)
        block[1] = self._caesar(block[1], 198)
        block[2] = self._caesar(block[2], 87)
        block[3] = self._caesar(block[3], 42)

        # Transform columns
        block = list(map("".join, zip(*block)))
        block[0] = self._caesar(block[0], 28)
        block[1] = self._caesar(block[1], 34)
        block[2] = self._caesar(block[2], 61)
        block[3] = self._caesar(block[3], 7)

        block = "".join(map("".join, zip(*block)))
        return block

    def _get_round_keys(self):
        """ Yield sub keys used for each round """
        key = self.__key
        for _ in range(32):
            yield key[:16]
            key = bytes([*key[1:], key[0]])

    @staticmethod
    def _shuffle(block: str):
        """ Shuffles a block using the P box """
        return "".join(block[i] for i in P)

    @staticmethod
    def _chunks(array, n):
        """ Yields successive n-sized chunks from array """
        for i in range(0, len(array), n):
            yield array[i:i + n]

    @staticmethod
    def _caesar(message: str, key: int):
        """ Caesar cipher with a custom character set """
        return message.translate(CHAR_TABLE[key % len(CHAR_SET)])

    @staticmethod
    def _gen_rand_bytes(n):
        """ Generate random bytes of n-size """
        return SystemRandom().randbytes(n)

    @staticmethod
    def _pad(message: str, block_size: int):
        """ Pads message according to block size """
        padding_len = block_size - len(message)%block_size
        padding = CHAR_SET[padding_len]*padding_len
        return message + padding

    @staticmethod
    def _unpad(message: str, block_size: int):
        """ Unpads message according to block size """
        pdata_len = len(message)
        if pdata_len % block_size:
            raise ValueError("Message is not padded.")

        padding_len = CHAR_SET.find(message[-1])

        if padding_len < 1 or padding_len > min(block_size, pdata_len):
            raise ValueError("Padding is incorrect.")
        if message[-padding_len:] != CHAR_SET[padding_len]*padding_len:
            raise ValueError("Padding is incorrect.")

        return message[:-padding_len]


MSG = "So I heard that caesar cipher is too simple and decided to make it more complex! :)"

cipher = CaesarCipher()#?

msg_enc, msg_iv = cipher.encrypt(MSG)
flag_enc, flag_iv = cipher.encrypt(FLAG)

print(f"{msg_enc=}")
print(f"{msg_iv=}")
print(f"{flag_enc=}")
print(f"{flag_iv=}")
