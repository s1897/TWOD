"""
MS5611 driver code is placed under the BSD license.
Copyright (c) 2014, Emlid Limited, www.emlid.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
	* Redistributions of source code must retain the above copyright
	notice, this list of conditions and the following disclaimer.
	* Redistributions in binary form must reproduce the above copyright
	notice, this list of conditions and the following disclaimer in the
	documentation and/or other materials provided with the distribution.
	* Neither the name of the Emlid Limited nor the names of its contributors
	may be used to endorse or promote products derived from this software
	without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL EMLID LIMITED BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import spidev
import time
import argparse
import sys
import navio.mpu9250
import navio.lsm9ds1
import navio.util
from math import asin, degrees

navio.util.check_apm()

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Sensor selection: -i [sensor name]. Sensors names: mpu is MPU9250, lsm is LSM9DS1")

if len(sys.argv) == 1:
    print("Enter parameter")
    parser.print_help()
    sys.exit(1)
elif len(sys.argv) == 2:
    sys.exit("Enter sensor name: mpu or lsm")

args = parser.parse_args()

if args.i == 'mpu':
    print("Selected: MPU9250")
    imu = navio.mpu9250.MPU9250()
elif args.i == 'lsm':
    print("Selected: LSM9DS1")
    imu = navio.lsm9ds1.LSM9DS1()
else:
    print("Wrong sensor name. Select: mpu or lsm")
    sys.exit(1)


if imu.testConnection():
    print("Connection established: True")
else:
    sys.exit("Connection established: False")

imu.initialize()

time.sleep(1)

while True:
    # imu.read_all()
    # imu.read_gyro()
    # imu.read_acc()
    # imu.read_temp()
    # imu.read_mag()

    # print "Accelerometer: ", imu.accelerometer_data
    # print "Gyroscope:     ", imu.gyroscope_data
    # print "Temperature:   ", imu.temperature
    # print "Magnetometer:  ", imu.magnetometer_data

    # time.sleep(0.1)

    m9a, m9g, m9m = imu.getMotion9()

    # print(("Acc:" + " {:+6f} {:+6f} {:+6f} " + "Gyr:" + " {:+6f} {:+6f} {:+6f} " + "Mag:" + " {:+6f} {:+6f} {:+6f}").format(m9a[0], m9a[1], m9a[2], m9g[0], m9g[1], m9g[2], m9m[0], m9m[1], m9m[2]))

    # print("Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]))
    # print("Gyr:", "{:+8.3f}".format(m9g[0]), "{:+8.3f}".format(m9g[1]), "{:+8.3f}".format(m9g[2]))
    # print("Mag:", "{:+7.3f}".format(m9m[0]), "{:+7.3f}".format(m9m[1]), "{:+7.3f}".format(m9m[2]))

    # time.sleep(0.5)
    x = m9a[0]
    y = m9a[1]
    z = m9a[2]
    r = 1

    a = (x * x + y * y + z * z)**0.5

    if not a == 0:
        x /= a
        y /= a
        z /= a

    d = (x * x + y * y)**0.5

    if not d > 1:

        if not d == 0:
            xa = asin(x / d)
            ya = asin(y / d)
        else:
            xa = x
            ya = y

        if not r == 0:
            za = asin(z / r)
            da = asin(d / r)

        else:
            za = z
            da = d

    print(("Acc:" + " {:+6f} {:+6f} {:+6f} {:+6f} " + "Norm :" + " {:+6f} {:+6f} {:+6f} ").format(degrees(xa), degrees(ya), degrees(za), degrees(da), x, y, z))
    # a = (x * x + y * y + z * z)**0.5
    #
    # print(a)
