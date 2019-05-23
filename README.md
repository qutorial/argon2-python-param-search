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


