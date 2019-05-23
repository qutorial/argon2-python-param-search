# Playing with argon2_cffi python parameters

Run install.sh to install it,
then test.py is runnable.

After that you go like this:

1) How many cores does your system reliably
and inexpensively can provide? => parallelism parameter

2) How much memory the algorithm can reliably and inexpensively
reserve? => memory parameter

3) Now, tune the time parameter t, so that it matches your 
time requirements, for instance 0,5 seconds.

Example:
```
$argon2id$v=19$m=30720,t=20,p=1$L0u4wN9Rs7FYmxhnUGq9ercQdqjoP+V5zC19G9ip6snl5M6qZ7Of3wTVeyJGiS0/lke7YFvn2rmWHvUB029r3A$mMPa22xBDehRLg6W4S3eS4pYxPEW93k82/lOUDq/146Ht56XhM0gMB7M3/Ad1GtgQOMxXf/tiPaJWdw7Syd5kQ
205
time:  0.41727
```

Means that the run take 0,41 seconds and that 205 characters are needed
to save the result.


