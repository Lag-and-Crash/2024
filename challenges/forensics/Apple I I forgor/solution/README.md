# Solution

1. Unzip the .7z file into a .img file.
2. The file is a disk image containing 3 partitions. It is a disk image of an actual Macbook SSD.
3. Install apfs-fuse as MacOS uses a proprietary filesystem known as APFS which linux can't read.
4. Install qemu-utils and follow this tutorial to mount the disk image as a linux nbd device https://gist.github.com/shamil/62935d9b456a6f9877b5
5. Use apfs-fuse to mount the nbd device at the correct offset (use fstat for that)
6. After correct APFS is mounted, switch to root then navigate to /root/private/var/db/dslocal/nodes/Default/users/player.plist (location can vary, sometimes it appears in /root/System/Preboot/~randomID~/var/db)
7. Open the plist file in the directory and find the Password Hint which is the flag
