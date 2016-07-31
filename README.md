# IOS CLI Walker
A python script to walk the Cisco IOS CLI parser chain.

This is a script that interacts with the CLI parser through the "?" help prompt, an collects all the supported commands into one single log file. Hook it up with any Cisco router running IOS or IOS-XE and you should be able to get a collection of all the possible CLIs, so that later on when you can not recall what some particular CLI looks, a simple text search on the output will leads you there in no time.

##Warnings

1. It could be slow! This is mostly due to the slowness in the telnet sesion. 
2. I would not recommand to run it in production as ios is a pretty dated single thread application, drainning CPU on CLI parse chain will impact other important businesses like route updates.

