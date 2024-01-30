challenge:
  author: Kaligula 
  category: Pwn
  description: Storing explosive chemicals in the kernel is a wonderful idea! Surely nothing can go wrong...right? 
  difficulty: Insane
  discord: kaligula_armblessed

  # note: dist files are required for this challenge
  files:
  - ./dist/bzImage
  - ./dist/cheminventory.ko
  - ./dist/config
  - ./dist/initramfs.cpio.gz
  - ./dist/run.sh
  flags:
  - flag: LNC24{1f_y0U_473_n07_P4R7_0f_Th3_501UT10N_YoU_a7E_P47T_0f_Th3_Pr3C1P1T473}
    regex: false
  hints: null
  name: Cheminventory
  requirements: null
services:
  cheminventory:
    name: cheminventory
    path: service/cheminventory
    port: '1337'
