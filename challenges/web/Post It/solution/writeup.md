# Solution to Post It

1. Log in with the credentials `test_user:password`.
2. Click on `RSA Key` in the navbar.
3. Copy the public key.
4. Copy your JWT token.
5. Use a JWT debugger to set `admin` to `true` and `alg` to `HS256`. Sign the token with the public key using HS256.
5. Change your JWT token to the new token.
6. Refresh the page and you should be logged in as admin.
7. The `/view` endpoint is vulnerable to path traversal, but there is a filter preventing you from reading the flag.
8. Get the needed info to generate the Flask debug console PIN from the following urls:
- `http://example.com/view/..%252F..%252Fproc/net/arp (Get the network interface name)`
- `http://example.com/view/..%252F..%252Fsys/class/net/*/address ("*": network interface name, Get the MAC address)`
- `http://example.com/view/..%252F..%252Fproc/sys/kernel/random/boot_id (Get the boot ID)`
- `http://example.com/view/..%252F..%252F/proc/self/cgroup (Only take the part after the last slash in the first line)`
9. Put the 2 strings obtained into [here](./get_key.py) and run the script. The PIN will be printed.
10. Go to `http://example.com/console` and enter the PIN. Execute the following command to get the flag:
```python
print(open('/flag.txt').read())
```