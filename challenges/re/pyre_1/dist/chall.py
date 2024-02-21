from base64 import urlsafe_b64decode

strings = ['dOpl3PA4RINDiQQr.OKQm7sRDNNo34TRFK5gAipVKceoNzltCB7UW7K9VEcAr1jdKB9sArq9MDLct1mYaGt4XtcVLOQ==', 
           'jqAaS7XzO5uy7ukY.wu5ZeYGIS8LGhtl20dJ_HdCBDvL8qbZx_f9pe-qebtjasdp5_ZF_OeqHc6_csYsp4JRoIoCARg==', 
           'JAhRxb8R5PSjnTn8.aEYS94tqlK3X9QmSe3o0k9pj0Z3t2maVV1ci9eB8sbfLwgqdVzk0t-BlrMDNwlvNSjwjrIpimQ==']


def pyre_1(msg:bytes, key:bytes) -> bytes:
    ptr = 0
    result = []
    while ptr < len(msg):
        msg_val = msg[ptr]
        key_val = key[ptr % len(key)]
        res_val = msg_val ^ key_val
        result.append(res_val)
        ptr += 1
    result = bytes(result)
    return result


def test_flag(flag:bytes, test_str:str) -> bool:
    key, ct = test_str.split('.')
    key = urlsafe_b64decode(key)
    ct = urlsafe_b64decode(ct)

    if pyre_1(flag, key) == ct:
        return True
    else:
        return False


def main():
    is_correct = True
    flag = open("flag.txt", "rb").read()
    for i in range(10):
        test_str = strings[i]
        if test_flag(flag, test_str) == False:
            is_correct = False
            break

    if is_correct:
        print("Correct!")
    else:
        print("Wrong!")


if __name__ == "__main__":
    main()