# sewing-waste-and-agriculture-leftovers
> UDP - UNRELIABLE datagram protocol.

## About the Challenge
We were given a `pcap` file (You can get the file [here](swaal.pcap.gz))

## How to Solve?
First i extract the pcap and then import the file into `Wireshark`. And then check every packet by pressing `Ctrl + Alt + Shift + U` to follow the UDP stream

![udp_1](images/udp_1.png)

![udp_2](images/udp_2.png)

If we examine each packet, the data in each packet will form a flag but there are still many parts missing, so to solve this chall there are 2 ways combine each packet manually (Like me :D) or you can create a script to get the flag. In this case i check every packet manually and then you will get the flag

![flag](images/flag.png)

```
kalmar{if_4t_first_you_d0nt_succeed_maybe_youre_us1ng_udp}
```