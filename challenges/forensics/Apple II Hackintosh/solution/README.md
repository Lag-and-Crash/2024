# Solution

1. Follow same steps as Apple I: I forgor
2. Eventually navigate to /private/var/folders/zz/~randomId~/C/locationd/consolidated.db after filtering out folders and trial and error to find an SQLite database
3. Use an SQLite viewer to find the device's serial number
4. Many possible ways to find the hypervisor used, one way is to inspect the /Library/Receipts/InstallHistory.plist and notice the Parallels Tools were installed. Thus Parallels is the Hypervisor
