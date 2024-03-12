'''
Author: Nitzan Orr

This example program is for reading ROS 1 .bag files on Ubuntu 22.04+. 
ROS 1 does not support Ubuntu 22.04+ and so cannot be easily installed

This code depends on Ternaris's Rosbags Python library and CLI Tools
https://ternaris.gitlab.io/rosbags/

The above repo can also convert ROS 2 recordings (.db3 and .mcap file formats)
to ROS 1 .bag file format.


'''


from pathlib import Path
from rosbags.highlevel import AnyReader

path = '/home/pi/Data/nitzan/spot_rosbags/feb13/feb13_4_2.bag'
bagpath = Path(path)

with AnyReader([bagpath]) as reader:

    for connection, timestamp, rawdata in reader.messages():
        print(connection.msgtype)
        print(connection.topic)
        msg = reader.deserialize(rawdata, connection.msgtype)
        print("Message Data:", msg.data)
