#!/bin/sh

pid=$$
cp ./initramfs.cpio.gz "./${pid}chem.cpio.gz"

qemu-system-x86_64 \
    -kernel ./bzImage \
    -cpu qemu64,+smep,+smap \
    -m 4G \
    -smp 4 \
    -initrd "./${pid}chem.cpio.gz" \
    -append "console=ttyS0 quiet loglevel=3 kaslr kpti=1" \
    -monitor /dev/null \
    -nographic \
    -no-reboot \

rm "./${pid}chem.cpio.gz"
