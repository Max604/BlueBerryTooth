# BlueBerryTooth

[![Build Status](https://travis-ci.org/Max604/BlueBerryTooth.svg?branch=master)](https://travis-ci.org/Max604/BlueBerryTooth)
[![Version 2.4](https://img.shields.io/badge/version-1.0-brightgreen.svg)](https://www.internalpositioning.com/guide/development/)
[![Github All Releases](https://img.shields.io/github/downloads/Max604/BlueBerryTooth/total.svg)](https://github.com/Max604/BlueBerryTooth/releases)
[![FIND documentation](https://img.shields.io/badge/find-documentation-blue.svg)](https://github.com/Max604/BlueBerryTooth/wiki)
![Coverage](https://img.shields.io/badge/coverage-57%25-orange.svg)
[![Donate](https://img.shields.io/badge/donate-$1-brown.svg)](https://www.paypal.me/Max604/1.00)
[![Join the chat at https://gitter.im/Max604/BlueBerryTooth](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Max604/find?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# About

**BlueBerryTooth** is a proof-of-concept of the inherent privacy concerns that accompany the use of bluetooth. This project also supports Bluetooth Low Energy devices.
The idea is set up several _Raspberry Pi Zero W_s as bluetooth device sensors and then transmit the bluetooth packet information received to the server, Raspberry Pi 3 Model B.
The server will collate the information received from each of the sensors through Wi-Fi TCP on a internet connection and insert this into a MySQL database.
Packets received will send several important pieces of information: The device's MAC address, the name (if available)

# Requirements

**GNU/Linux (Preferably Raspbian (Raspberry Pi):**

- Python 3 or more recent version
- Python distutils (comes with most Python distros)
- BlueZ libraries and header files (with the experimental BLE setting enabled)

**Mac OSX:**

As much as I would wish to test my code on Mac mac alone and then transfer the files to my Raspberry Pis for further testing Bluetooth Low Energy, which BlueBerryTooth depends on, is not available for OSX. :(
So for the meantime I must always write the code on my IDE on my Mac and then sftp it to my raspberry Pis. _sigh_

**LICENSE:**

  BlueBerryTooth is free software; you can redistribute it and/or modify it under the
  terms of the GNU General Public License as published by the Free Software
  Foundation; either version 2 of the License, or (at your option) any later
  version.

  BlueBerryTooth is distributed in the hope that it will be useful, but WITHOUT ANY
  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
  A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with
  BlueBerryTooth; if not, write to the Free Software Foundation, Inc., 51 Franklin St,
  Fifth Floor, Boston, MA  02110-1301  USA