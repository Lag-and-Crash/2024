# Solution
Using pstree, we see that WINWORD.exe is a process of Microsoft word, this is definitely an application used to write reports.
```bash
$ vol3.py -f MEMORY.DMP windows.pstree
Volatility 3 Framework 2.5.1
Progress:  100.00               PDB scanning finished
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime

4       0       System  0x8a066ba62040  137     -       N/A     False   2024-01-18 13:29:17.000000      N/A
* 1792  4       MemCompression  0x8a066f613080  38      -       N/A     False   2024-01-18 13:29:20.000000      N/A
* 108   4       Registry        0x8a066bae6080  4       -       N/A     False   2024-01-18 13:29:11.000000      N/A
* 324   4       smss.exe        0x8a066d891040  2       -       N/A     False   2024-01-18 13:29:17.000000      N/A
440     428     csrss.exe       0x8a066d75c080  11      -       0       False   2024-01-18 13:29:18.000000      N/A
520     428     wininit.exe     0x8a066e53c080  1       -       0       False   2024-01-18 13:29:19.000000      N/A
* 696   520     lsass.exe       0x8a066e5ca080  12      -       0       False   2024-01-18 13:29:19.000000      N/A
* 676   520     services.exe    0x8a066e5c80c0  5       -       0       False   2024-01-18 13:29:19.000000      N/A
** 2692 676     VGAuthService.  0x8a066bb80080  2       -       0       False   2024-01-18 13:29:21.000000      N/A
** 2184 676     svchost.exe     0x8a066f893300  14      -       0       False   2024-01-18 13:29:21.000000      N/A
** 5772 676     svchost.exe     0x8a0672146080  8       -       0       False   2024-01-18 13:31:22.000000      N/A
** 1808 676     svchost.exe     0x8a066f7c1240  5       -       0       False   2024-01-18 13:29:21.000000      N/A
** 2192 676     svchost.exe     0x8a066f895300  13      -       0       False   2024-01-18 13:29:21.000000      N/A
** 1948 676     svchost.exe     0x8a066f6bc300  3       -       0       False   2024-01-18 13:29:20.000000      N/A
** 2720 676     vmtoolsd.exe    0x8a066f914080  13      -       0       False   2024-01-18 13:29:21.000000      N/A
** 2596 676     svchost.exe     0x8a066bbb7080  9       -       0       False   2024-01-18 13:29:21.000000      N/A
** 936  676     svchost.exe     0x8a066ef74240  77      -       0       False   2024-01-18 13:29:20.000000      N/A
*** 3520        936     sihost.exe      0x8a066fdcb0c0  12      -       1       False   2024-01-18 13:29:23.000000     N/A
*** 3664        936     taskhostw.exe   0x8a066fded080  13      -       1       False   2024-01-18 13:29:23.000000     N/A
*** 3684        936     MicrosoftEdgeU  0x8a066fe10340  3       -       0       True    2024-01-18 13:29:23.000000     N/A
**** 5108       3684    MicrosoftEdgeU  0x8a0672598080  5       -       0       True    2024-01-18 13:29:28.000000     N/A
*** 3728        936     BraveUpdate.ex  0x8a066fe36300  4       -       0       True    2024-01-18 13:29:23.000000     N/A
** 6440 676     svchost.exe     0x8a066f50b280  5       -       0       False   2024-01-18 13:31:22.000000      N/A
** 940  676     svchost.exe     0x8a066ee0d300  13      -       0       False   2024-01-18 13:29:19.000000      N/A
** 1196 676     svchost.exe     0x8a066efb8280  19      -       0       False   2024-01-18 13:29:20.000000      N/A
*** 3868        1196    ctfmon.exe      0x8a066fe9d080  12      -       1       False   2024-01-18 13:29:23.000000     N/A
** 1964 676     svchost.exe     0x8a066f6f2300  12      -       0       False   2024-01-18 13:29:20.000000      N/A
*** 5352        1964    audiodg.exe     0x8a06733d7340  4       -       0       False   2024-01-18 13:33:23.000000     N/A
** 824  676     svchost.exe     0x8a066edae280  19      -       0       False   2024-01-18 13:29:19.000000      N/A
*** 6408        824     UserOOBEBroker  0x8a06730d8340  1       -       1       False   2024-01-18 13:30:30.000000     N/A
*** 1164        824     WmiPrvSE.exe    0x8a066fc142c0  11      -       0       False   2024-01-18 13:29:22.000000     N/A
*** 7828        824     WinStore.App.e  0x8a0672e752c0  11      -       1       False   2024-01-18 13:30:12.000000     N/A
*** 2040        824     RuntimeBroker.  0x8a06726aa080  7       -       1       False   2024-01-18 13:29:30.000000     N/A
*** 5788        824     SkypeApp.exe    0x8a06729ba240  14      -       1       False   2024-01-18 13:29:31.000000     N/A
*** 5916        824     RuntimeBroker.  0x8a0672a42080  5       -       1       False   2024-01-18 13:29:31.000000     N/A
*** 5148        824     RuntimeBroker.  0x8a0672e97080  3       -       1       False   2024-01-18 13:33:23.000000     N/A
*** 7980        824     RuntimeBroker.  0x8a067269e080  1       -       1       False   2024-01-18 13:30:13.000000     N/A
*** 6320        824     RuntimeBroker.  0x8a0672cb5080  4       -       1       False   2024-01-18 13:29:33.000000     N/A
*** 5428        824     RuntimeBroker.  0x8a06727c0080  14      -       1       False   2024-01-18 13:29:31.000000     N/A
*** 4916        824     SppExtComObj.E  0x8a0672e43080  4       -       0       False   2024-01-18 13:32:54.000000     N/A
*** 5176        824     SearchApp.exe   0x8a06726a9080  58      -       1       False   2024-01-18 13:29:30.000000     N/A
*** 4800        824     SystemSettings  0x8a0672f42080  16      -       1       False   2024-01-18 13:30:30.000000     N/A
*** 7240        824     smartscreen.ex  0x8a06735e90c0  11      -       1       False   2024-01-18 13:36:23.000000     N/A
*** 7120        824     ShellExperienc  0x8a066fb4d300  12      -       1       False   2024-01-18 13:33:22.000000     N/A
*** 5072        824     dllhost.exe     0x8a066fdc8080  12      -       1       False   2024-01-18 13:35:58.000000     N/A
*** 6100        824     RuntimeBroker.  0x8a0672a43080  3       -       1       False   2024-01-18 13:29:32.000000     N/A
*** 6748        824     WmiPrvSE.exe    0x8a06724ea2c0  7       -       0       False   2024-01-18 13:29:42.000000     N/A
*** 4960        824     StartMenuExper  0x8a06725a60c0  10      -       1       False   2024-01-18 13:29:30.000000     N/A
*** 5988        824     LockApp.exe     0x8a0672b08080  12      -       1       False   2024-01-18 13:29:32.000000     N/A
*** 7532        824     TextInputHost.  0x8a06726a3080  11      -       1       False   2024-01-18 13:30:57.000000     N/A
*** 7800        824     ApplicationFra  0x8a0672b33080  6       -       1       False   2024-01-18 13:30:12.000000     N/A
*** 5756        824     SkypeBackgroun  0x8a06729b3080  4       -       1       False   2024-01-18 13:29:31.000000     N/A
** 2236 676     spoolsv.exe     0x8a066f898240  7       -       0       False   2024-01-18 13:29:21.000000      N/A
** 3388 676     msdtc.exe       0x8a066fd622c0  12      -       0       False   2024-01-18 13:29:23.000000      N/A
** 6652 676     SecurityHealth  0x8a0672c4d280  11      -       0       False   2024-01-18 13:29:41.000000      N/A
** 1088 676     svchost.exe     0x8a066efa8300  8       -       0       False   2024-01-18 13:29:20.000000      N/A
** 1600 676     svchost.exe     0x8a066f7bc300  4       -       0       False   2024-01-18 13:29:21.000000      N/A
** 1092 676     svchost.exe     0x8a066efac300  13      -       0       False   2024-01-18 13:29:20.000000      N/A
** 4424 676     SearchIndexer.  0x8a066fa17080  32      -       0       False   2024-01-18 13:29:24.000000      N/A
** 6856 676     svchost.exe     0x8a0672a50300  6       -       0       False   2024-01-18 13:29:42.000000      N/A
** 3148 676     svchost.exe     0x8a066fc70240  27      -       0       False   2024-01-18 13:29:22.000000      N/A
** 1104 676     svchost.exe     0x8a066efaa300  24      -       0       False   2024-01-18 13:29:20.000000      N/A
** 1876 676     svchost.exe     0x8a066f647240  4       -       0       False   2024-01-18 13:29:20.000000      N/A
** 2136 676     svchost.exe     0x8a066f821280  4       -       0       False   2024-01-18 13:29:21.000000      N/A
** 8024 676     SgrmBroker.exe  0x8a06733cc080  7       -       0       False   2024-01-18 13:31:22.000000      N/A
** 7516 676     MicrosoftEdgeU  0x8a06730b82c0  9       -       0       True    2024-01-18 13:29:57.000000      N/A
** 3548 676     sppsvc.exe      0x8a067358d0c0  3       -       0       False   2024-01-18 13:31:10.000000      N/A
** 3552 676     svchost.exe     0x8a066fde40c0  12      -       1       False   2024-01-18 13:29:23.000000      N/A
** 996  676     svchost.exe     0x8a066ef72300  25      -       0       False   2024-01-18 13:29:20.000000      N/A
** 1388 676     svchost.exe     0x8a066f484300  16      -       0       False   2024-01-18 13:29:20.000000      N/A
** 2668 676     dllhost.exe     0x8a066fc120c0  14      -       0       False   2024-01-18 13:29:22.000000      N/A
** 1520 676     svchost.exe     0x8a066f507300  18      -       0       False   2024-01-18 13:29:20.000000      N/A
** 4976 676     svchost.exe     0x8a06723a1080  9       -       1       False   2024-01-18 13:29:26.000000      N/A
** 2548 676     svchost.exe     0x8a066bbb9080  3       -       0       False   2024-01-18 13:29:21.000000      N/A
** 2684 676     vm3dservice.ex  0x8a066f91c1c0  2       -       0       False   2024-01-18 13:29:21.000000      N/A
*** 2860        2684    vm3dservice.ex  0x8a066fa5d240  2       -       1       False   2024-01-18 13:29:21.000000     N/A
* 860   520     fontdrvhost.ex  0x8a066edb7180  5       -       0       False   2024-01-18 13:29:19.000000      N/A
528     508     csrss.exe       0x8a066e541140  13      -       1       False   2024-01-18 13:29:19.000000      N/A
592     508     winlogon.exe    0x8a066e5810c0  3       -       1       False   2024-01-18 13:29:19.000000      N/A
* 380   592     LogonUI.exe     0x8a066eec20c0  0       -       1       False   2024-01-18 13:29:20.000000      2024-01-18 13:30:12.000000
* 852   592     fontdrvhost.ex  0x8a066edb5180  5       -       1       False   2024-01-18 13:29:19.000000      N/A
* 392   592     dwm.exe 0x8a066eec3080  14      -       1       False   2024-01-18 13:29:20.000000      N/A
* 4108  592     userinit.exe    0x8a066ff5a080  0       -       1       False   2024-01-18 13:29:23.000000      2024-01-18 13:29:53.000000
** 4128 4108    explorer.exe    0x8a066ff5b080  80      -       1       False   2024-01-18 13:29:23.000000      N/A
*** 4512        4128    runonce.exe     0x8a067216e080  4       -       1       False   2024-01-18 13:29:24.000000     N/A
**** 4696       4512    BingChatInstal  0x8a06721ef300  3       -       1       True    2024-01-18 13:29:25.000000     N/A
*** 608 4128    msedge.exe      0x8a0672e5f080  37      -       1       False   2024-01-18 13:30:57.000000      N/A
**** 6272       608     msedge.exe      0x8a06730c8340  7       -       1       False   2024-01-18 13:30:57.000000     N/A
**** 868        608     msedge.exe      0x8a06728d9080  9       -       1       False   2024-01-18 13:31:57.000000     N/A
**** 6568       608     msedge.exe      0x8a067338d080  17      -       1       False   2024-01-18 13:31:01.000000     N/A
**** 6712       608     msedge.exe      0x8a06733be080  15      -       1       False   2024-01-18 13:30:58.000000     N/A
**** 7308       608     msedge.exe      0x8a06731f1340  8       -       1       False   2024-01-18 13:30:57.000000     N/A
**** 876        608     msedge.exe      0x8a06729340c0  12      -       1       False   2024-01-18 13:31:09.000000     N/A
**** 2004       608     msedge.exe      0x8a06731df340  14      -       1       False   2024-01-18 13:30:57.000000     N/A
**** 7700       608     msedge.exe      0x8a06730e8080  15      -       1       False   2024-01-18 13:31:01.000000     N/A
**** 3128       608     msedge.exe      0x8a06731e8340  13      -       1       False   2024-01-18 13:30:57.000000     N/A
*** 6788        4128    vmtoolsd.exe    0x8a0672cbe080  8       -       1       False   2024-01-18 13:29:42.000000     N/A
*** 6924        4128    OneDrive.exe    0x8a0672d8e2c0  21      -       1       False   2024-01-18 13:29:43.000000     N/A
**** 6444       6924    msedgewebview2  0x8a0672cfa080  0       -       1       False   2024-01-18 13:29:50.000000     2024-01-18 13:29:57.000000
*** 6616        4128    SecurityHealth  0x8a067226f2c0  3       -       1       False   2024-01-18 13:29:41.000000     N/A
*** 7740        4128    WINWORD.EXE     0x8a06736ce080  13      -       1       False   2024-01-18 13:31:04.000000     N/A
**** 4476       7740    FIRSTRUN.EXE    0x8a06735eb080  0       -       1       False   2024-01-18 13:32:54.000000     2024-01-18 13:33:39.000000
```

Try to dump pid with id 7740 and use strings can't help anything. 

I tried to use handles on that pid but also there is no luck

```
$ vol3.py -f MEMORY.DMP windows.handles --pid 7740
Volatility 3 Framework 2.5.1
Progress:  100.00               PDB scanning finished
PID     Process Offset  HandleValue     Type    GrantedAccess   Name

7740    WINWORD.EXE     0x8a067356a060  0x4     Event   0x1f0003
7740    WINWORD.EXE     0x8a067356b060  0x8     Event   0x1f0003
7740    WINWORD.EXE     0x8a067316cbc0  0xc     WaitCompletionPacket    0x1
7740    WINWORD.EXE     0x8a067370af40  0x10    IoCompletion    0x1f0003
7740    WINWORD.EXE     0x8a0673620d20  0x14    TpWorkerFactory 0xf00ff
7740    WINWORD.EXE     0x8a0673638200  0x18    IRTimer 0x100002
.....
7740    WINWORD.EXE     0x8a0672f53980  0x18d4  File    0x12019f        \Device\HarddiskVolume3\Users\IEUser\AppData\Local\Microsoft\Windows\Explorer\iconcache_32.db
7740    WINWORD.EXE     0x8a0672426150  0x18e4  Mutant  0x1f0001
7740    WINWORD.EXE     0x8a067371ab30  0x18f0  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a066fe1b6e0  0x1908  Semaphore       0x1f0003
7740    WINWORD.EXE     0x8a067371c490  0x1910  EtwRegistration 0x804
7740    WINWORD.EXE     0x9b089f614890  0x1914  Section 0xf0007
7740    WINWORD.EXE     0x8a067371acf0  0x1928  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a067371c110  0x1934  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a067371ac10  0x1938  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a067371c3b0  0x1940  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a066fe25360  0x1954  Event   0x1f0003
7740    WINWORD.EXE     0x8a0672f5a3c0  0x1958  File    0x12019f        \Device\HarddiskVolume3\Users\IEUser\AppData\Local\Microsoft\Windows\Explorer\iconcache_16.db
7740    WINWORD.EXE     0x8a0672f5ab90  0x19a0  File    0x12019f        \Device\HarddiskVolume3\Users\IEUser\AppData\Local\Microsoft\Windows\Explorer\iconcache_idx.db
7740    WINWORD.EXE     0x8a067371b230  0x19b4  EtwRegistration 0x804
7740    WINWORD.EXE     0x8a067371b070  0x19bc  EtwRegistration 0x804
7740    WINWORD.EXE     0x9b0894b48e10  0x19f8  Key     0x20006 USER\S-1-5-21-1281496067-1440983016-2272511217-1000_CLASSES\LOCAL SETTINGS\SOFTWARE\MICROSOFT\WINDOWS\SHELL\BAGS\15\COMDLG\{B3690E58-E961-423B-B687-386EBFD83239}
7740    WINWORD.EXE     0x8a06731ab930  0x1a04  EtwRegistration 0x804
```


I had to seek help from google. Finally I found [this document](https://learn.microsoft.com/en-us/office/troubleshoot/word/recover-lost-unsaved-corrupted-document) from Microsoft

Using filescan to find .asd autorecovery file

```
$ vol3.py -f MEMORY.DMP windows.filescan | grep asd
0x8a06722ade70.0\Users\IEUser\AppData\Roaming\Microsoft\Word\AutoRecovery save of Document1.asd 216
```

But when i fail to open it

![image.png](https://images.viblo.asia/2d2cece2-5eb2-42fd-830f-fba939947e9e.png)

So i need to move it to original location `C:\Users\<UserName>\AppData\Roaming\Microsoft\Word` and open it 

![image.png](https://images.viblo.asia/1b9be258-71c0-4996-9bce-163f3656c028.png)

Edit to show all tables

![image.png](https://images.viblo.asia/1d982fae-3504-45c5-8984-7dc8f0d8a4a6.png)

delete all "O" we can see the qr code. scan to get flag

![image.png](https://images.viblo.asia/87c1fa46-9dcf-40fc-850a-ef17f72a5efd.png)