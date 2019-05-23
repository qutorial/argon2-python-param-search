#!/usr/bin/python3
import time
from argon2 import *
ph = PasswordHasher(time_cost=20,
        memory_cost=30*1024, # 30 Mega bytes
        parallelism=1, # 1 core
        hash_len= 64, # 64 bytes of hash
        salt_len= 64) # 64 is the recommended in the paper salt length for argon
t = time.clock()
hash = ph.hash("s3kr3tp4ssw0rd")
print(hash)
print(len(hash))
print("time: ", time.clock() - t)
