# hello-world
Create a repository for learning







Developer
Getting-Started-Guide



Summary:

The document gives the steps to a developer
setting up the development environment for the first time for the Agilis SLC
project.

This document is Work In progress.

Revision Information:                                                                

Document originator:                          Adriana
Gonzalez / Jun 17th
2016

Co-authoring:                                        Tomasz Kazimierz Motyl

Document
registered number:          Not
used

Current
Revision:                                  0.6d


 
  
  Rev.
  
  
  Date
  
  
  Initials
  
  
  Remark
  
 
 
  
  0.1
  
  
  Jun 17th
  2016
  
  
  AG
  
  
  Create
  the initial draft
  
 
 
  
  0.2e
  
  
  Sep 14th
  2016
  
  
  TM
  
  
  Amendments to the draft concerning SocA9
  The LCES2 sections added (Building & TFTP boot)
   Editorial
  changes
  
 
 
  
  0.3
  
  
  Sep 22nd
  2016
  
  
  TM
  
  
  The Software development section
  added – including Eclipse IDE
  
 
 
  
  0.4e
  
  
  Sep 26th
  2016
  
  
  TM
  
  
  The pre-configured Virtual Machine’s
  description
  
 
 
  
  0.5
  
  
  Sep 30th
  2016
  
  
  AJ
  
  
  Amendments to Continuous Integration
  chapter
  
 
 
  
  0.6d
  
  
  Oct 4th
  2016
  
  
  TM
  
  
  Debug environment description
  VM Workstation Pro’s Shared folders feature documented
  Typographical conventions added
  Table of Acronyms added
  Table of figures Added
  Editorial changes
  
 
 
  
  0.7
  
  
  Oct 18th
  2016
  
  
  AJ
  
  
  Added Chapter about setting up klocwork on Developers Machine
  
 
 
  
  0.8
  
  
  Oct 20th
  2016
  
  
  AJ
  
  
  Added Chapter about setting up klocwork on Jenkins Build Server
  
 
 
  
  0.9
  
  
  Oct 21st
  2016
  
  
  AJ
  
  
  Added Chapter about setting up Elixir on a Development VM
  
 


 

 




 


 Table of Contents
 LIST OF
 FIGURES. 6
 ACRONYMS. 8
 FOREWORD. 8
 1.      Quick Start Guide. 9
 1.1        Setup a Development Virtual Machine. 9
 1.2        Using the pre-configured Virtual Machine. 9
 1.2.1         Importing a VM.. 9
 1.3        Booting the LCES2 board. 11
 1.3.1         Pre-requisites: 11
 1.3.2         Minimal Software requirements: 11
 1.3.3         Steps: 11
 1.4        Cross-Compiling and running the sample ‘Hello World’
 application. 14
 1.5        Remote Debugging using
 Eclipse IDE. 17
 1.5.2         Steps: 17
 2       Eclipse IDE. 22
 2.1        Installing Eclipse for C/C++
 projects. 22
 2.2        Creating a new project (demo) 22
 2.3        Cross compilation with the
 Eclipse IDE. 22
 3       VmWare Ubuntu Virtual Machine set-up. 25
 3.1        Creation of a new VM.. 25
 3.2        OS Configuration. 26
 3.2.1         General Proxy. 26
 3.2.2         Command line proxy. 27
 3.2.3         Apt-get proxy. 27
 3.2.4         Zscaler certificate. 28
 3.3        Network Server set-up. 30
 3.3.1         Setting up TFTP server 30
 3.3.2         Setup NFS. 31
 3.4        Git/Repo Setup. 32
 3.5        Build dependencies. 32
 4       Software development environment 32
 4.1        Toolchain. 32
 4.1.1         LCES2. 32
 4.1.2         SocA9. 33
 4.1.3         Installation. 33
 NOTE: It is advised, for the sake of future
 troubleshooting, to install the toolchain at the default location i.e.: ‘/opt/poky/2.0.2/…’ 33
 4.2        Command line. 33
 4.2.1         Setting-up the environment 33
 4.2.2-        ANSI-C ‘Hello World’ example. 33
 4.2.3         Building. 33
 5       Create ECP Binaries. 34
 3.1        SoC A9. 34
 3.1.1         Building the boot-loader 34
 3.1.2         Building Linux. 35
 3.2        LCES 2. 35
 3.2.1         Building the boot-loader 35
 3.2.2         Building Linux. 35
 6       Booting the platform.. 36
 6.1        Booting from an SD card. 36
 6.1        Booting over TFTP. 37
 6.2.1         Pre-requisites: 37
 6.2.2         Minimal Software requirements: 38
 6.2.3         Steps: 38
 7       Protocol Evaluations. 42
 7.1        MQTT. 43
 8       Altera Windows SW.. 43
 9       Continuous Integration. 43
 9.1        Installation. 43
 9.2        Running. 43
 9.2.1         Default Daemon. 43
 9.2.2         Run from terminal 44
 9.3        Basic Configuration. 46
 9.4   Extra
 Configuration. 47
 9.5        Creating projects. 47
 10         Setting up Klocwork on
 Developers Machine. 49
 10.1      Introduction. 50
 10.2      Prerequisites. 50
 10.3      Installing Klocwork Plugin in Eclipse. 50
 10.4      Using Klocwork in 
 a Project 52
 10.5      Link a project with an existing Klocwork project on
 the server-side. 55
 10.5.1       Using mapping file. 55
 10.5.2       Manual setting. 57
 11         Installing Klocwork on
 Jenkins Build Server 60
 11.1      Installing Klocwork on the build server 60
 11.2      Synchronisation with Klocwork Server 61
 11.3      Running Klocwork on Jenkins. 62
 12         Elixir Setup. 64
 12.1      Installing Elixir on your VM.. 64
 12.2      Install Phoenix/Nerves. 65
 12.3      Install NodeJS. 65
 12.4      Configuration for Firewall and Network Proxies. 65
 12.5      How install Elixir Syntax Recognition in VIM (Linux)
 and Sublime-text 65
 12.5.1       VIM.. 66
 12.5.2       Sublime-text 66
 13         Bibliography. 67
 14         APPENDIX 1 – List of NMC Clearances to be requested. 69
 15         APPENDIX 2 – Eclipse IDE debug configuration. 70
 15.1      Debug vs. Release build configurations. 70
 Steps: 70
 15.2      Configuring remote debug. 75
 15.2.1       Cross compiling and installing the GDB Server for the
 ‘arm-poky-linux-gnueabi’ (cortex-7A) host 75
 15.2.2       Compiling and installing
 native GNU Debugger 76
 15.2.3       Configuring a Remote Debug
 Session in Eclipse IDE. 77
 16         ANNEX 2 – Removing Unity and switching to Gnome. 82
  


 

LIST OF
FIGURES

Figure 1 - The TFTP boot environment 10

Figure 2 - PUTTY
Configuration. 11

Figure 3 - Eclipse select
workspace. 14

Figure 4 - Eclipse build
project 14

Figure 5 - Eclipse IDE -
Selecting Build configuration. 16

Figure 6 - Eclipse IDE -
Debug configurations. 17

Figure 7 - Eclipse IDE -
pre-configured debug configuration. 18

Figure 8 - Eclipse IDE -
Debugger connection. 19

Figure 9 - Eclipse IDE -
Starting Debug. 19

Figure 10 - Eclipse IDE -
Confirm Perspective Switch. 20

Figure 11 - Eclipse IDE -
Step over 20

Figure 12 - Environment
set-up. 22

Figure 13 - Project
Settings (Includes) 23

Figure 14 - The TFTP boot environment 37

Figure 15 - VM Workstation
Pro - Shared folders. 39

Figure 16 - Eclipse IDE
-Manage build configurations. 51

Figure 17 - Eclipse IDE -
New build configuration. 52

Figure 18 - Eclipse IDE -
New build configuration. 52

Figure 19 - Newly created
Debug configuration. 53

Figure 20 - Eclipse IDE -
Setting active build configuration. 53

Figure 21 - Eclipse IDE -
Disable optimization. 54

Figure 22 - Eclipse IDE -
Debug Level 55

Figure 23 - Eclipse IDE -
Stripping from symbols. 55

Figure 24 - Eclipse IDE -
C/C++ Remote Application. 59

Figure 25 - Eclipse IDE -
Choosing project application to debug. 60

Figure 26 - Eclipse IDE -
Debug configurations - Main. 61

Figure 27 - Eclipse IDE -
Debug Configurations Debugger 61

Figure 28 - Eclipse IDE -
Debug configurations - Source Selection. 62

 




 

 ACRONYMS

 










ANSI

American National
standards Institute, 8

ECP

Embedded
Controllers Platform, 23

EDS

Embedded Design
Suite, 41

FTDI

Future Technology Devices
International, 10

GNU

GNU's Not Unix, 56, 60

IDE

Interactive
Development Environment, 8

LCES2, 6

MQTT

Message Queuing Telemetry Transport, 41

NIC

Network Interface
Card, 9

PC

Personal Computer, 9

pwd

present working directory, 29

QSPI

Quad Serial
Peripheral Interface, 9

SCM

Source Code
Management, 46

SD

Secure Digital, 34

SoC

System on Chip, 8

TBD

To Be Done, 49

TFTP

Trivial File Transfer Protocol, 9, 10, 11, 12, 28, 35, 36, 37, 39, 40

UART

Universal Asynchronous
Receiver/Transmitter, 10

Universal Serial Bus, 10

VM

Virtual Machine, 7






 

 

FOREWORD

 

The purpose of this document is to get a
developer up to speed with working with the concerned LCES2 boards, lessening the time required for one’s
ramp-up.

Throughout this document we shall present
the reader with various examples, the best-known methods and a plethora of tips
and tricks. This document is neither intended to provide one with exhaustive
information nor is meant to be comprehensive.

Please bear in mind, that sources,
referenced throughout this document, binaries, as well as the hardware are
subjected to change without prior notice.

All the examples provided, are examples
only and should be treated as such and understood as methods that worked for
the authors of this document.




 

TYPOGRAPHICAL CONVENTIONS

‘Bold Italics
between apostrophes’

are used for file-names, program names,
directory names as well as names (labels) of various controls of Graphical User
Interfaces (GUIs).

 

Courier New

is used for text to be typed literally, Bourne
shell commands, code snippets, shell scripts’ code

 

<Text
between less than and greater than signs>

To indicate the part of command, code snippet,
source code that MUST be replaced (including
the surrounding <>s)
with the content identified by the Text between <>s.

 

[Text between square brackets]

To indicate an optional argument. The content
outlined by the text MUST be
replaced (including
the [] brackets) with the content identified by the Text.

 

Small courier NewItalics

Is reserved for the console/terminal outputs.

1.     
Quick Start Guide

1.1 Setup a Development Virtual
Machine

The Virtual Machine of choice is VmWare
Workstation Pro 12. It can be downloaded from: http://www.vmware.com/products/workstation/workstation-evaluation.html
.

1.2 Using the pre-configured Virtual Machine

In order to save time using the pre-configured
Virtual Machine image has been provided. 

1.2.1       
Importing a VM

Fetch the image of the pre-configured
Virtual Machine from: ftp://sesftp:sesftp@swftp.galway.apcc.com/agilis/vm/Alternative URL: ftp://sesftp:sesftp@10.216.252.11/agilis/vm/ Using the recommended VmWare
Workstation Pro 12 Import the newly downloaded file (see [1] )









NOTE:
The Virtual Machine provided is set-up for 8GB of
RAM and 4 CPUs. Please ensure the target host PC/Laptop has sufficient
resources to accommodate this. Alternatively Amend the VM’s settings.

The default user: user

Password: user

The Virtual machine’s
image already contains:

-       SoC A9 toolchain @ /opt/poky/2.0.1

-       LCES2
toolchain @ /opt/poky/2.0.2

-       Eclipse 3.8 IDE for C/C++ projects with

         a)     Set-up sample workspace ‘lces2_sample_workspace’ @ /home/user/lces2_sample_workspace:

i)   sample ‘ANSI-C ‘Hello World’ project ‘lces2_sample_project’

ii)  Cortex 7A minimal
cross-compilation configuration ‘cortex-7a-cross-compile’

NOTE:
The contemporary revision of the Virtual Machine’s
change-log can be found @ ftp://sesftp:sesftp@swftp.galway.apcc.com/agilis/vm/ChangeLog.txt
.

The demonstration video:

On the video presented, one can see
a user rambling through the properties’ configuration options outlined in Cross compilation with the Eclipse IDE. At the end of the video (when the
sample test project is built, one can see the use of NFS server for sharing
files between the Virtual Machine and the target LCES2 board as described in
(ref. 3.3.2 Setup NFS)

Due to the
size of the video file it is kept separately from this document and can be
viewed @ https://schneider-electric.app.box.com/files/0/f/9097120389/1/f_96052556308.

1.3 Booting the LCES2 board

The
LCES2 board comes with the pre-flashed loaders. According to the User Guide [2] the supported boot
modes are either from NOR-flash over QSPI or the Trivial File Transfer Protocol (TFTP).
This section focuses on the TFTP mode and provides the reader with a sample
set-up.

1.3.1        Pre-requisites:

The Linux image containing the initial RAM file-system (initramfs)(ref.
https://schneider-electric.app.box.com/files/0/f/11455181542/quick_start_ecp_linux_images_lces2
)  copied to the /var/lib/tftpboot location
on the Virtual Machine . Virtual Machine running the
TFTP server. A sample TFTP-booted
development environment is depicted on Figure 14 - The TFTP boot environment.The pre-flashed boot-loader was
tested with NIC and NIC J21 on 1000BASE-T physical layer.






 
 

 
  
  
   
    
    
    Figure 1 - The TFTP boot
    environment
    
    
   
  
  

 
  
  
   
   
   
   
   
   
   
   
   
   
   
   
  
  
  
 
  
  
 
  
   
    
    
     
      
      
      Host
      PC (Windows 10) 
       
      
      
      
     
    
    
  
   
    
    
     
      
      
      Virtual
      Machine
      
      
     
    
    
  
   
  
  
   
   
    
     
     
     BESTLA
     board
     
     
    
   
   
 
  
   
   
    
     
     
     NIC J21 Ethernet
     
     
    
   
   
 
  
   
   
    
     
     
     LCES2
     board
     
     
    
   
   
 
  
   
   
    
     
     
     USB/UART serial
     
     
    
   
   
 
  
   
   
    
     
     
     NIC 
     
     
    
   
   
 
  
   
   
    
     
     
     USB
     
     
    
   
   
 
  
   
   
    
     
     
     NFS
     folder
     
     
    
   
   
 
  
   
   
    
     
     
     TFTP Server
     
     
    
   
   
 
  
  
   
  
  
  
   
  
  
 
  
 
  
 
  
  
  
  
  
  
   
   
    
     
     
     LAN
     10.216.251.
     
     
    
   
   
 
 
  
  
   
   
   
   
  
  
  
   
   
  
  
 
 
  
 
  
   
   
    
     
     
     PUTTY
     
     
    
   
   
 
  
 
  
 

 
 
 


NOTE: The network settings may and extremely likely
will vary from ones presented hence MUST 

1.3.2      Minimal Software
requirements:

Ubuntu Linux TFTP ServerSerial terminal i.e. PUTTY



1.3.3      Steps:

Connect the LCES2 board’s J21
(via Ethernet cable) to the Local Area Network (LAN)Connect your PC (running the Virtual Machine) to same LAN as
in step 1.Connect the LCES2’s USB/UART  to the PC’s USBInstall the FTDI Drivers: The drivers can be downloaded from here: http://www.ftdichip.com/Drivers/VCP.htm . Otherwise the executable
installer for windows is up on box at https://schneider-electric.box.com/s/cf7ygashdt2f40p1sfr3cp7vvak46da3.Launch and configure your PUTTY
session over serial e.g.:
 
















Figure 2 - PUTTY Configuration

NOTE: The serial line to connect to is
set-up specific and varies from computer to computer.

Copy your Linux image files to
the configured TFTP server’s home directory: /var/lib/tftpbootPower-up the board



The pre-flashed
boot-loader should display its prompt at the PUTTY serial console, e.g.:

version

U-Boot
2014.07_se-uboot-v1.0.0 (Mar 18 2016 - 16:28:05)

arm-linux-gnueabihf-gcc
(crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09) 4.9.2
20140904 (prerelease)

GNU ld
(crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09)
2.24.0.20140829 Linaro 2014.09

=>

NOTE:
If the boot-loader’s prompt symbol ‘=>’
is not visible press Enter key when the PUTTY console’s window is focused. If
unsuccessful, check the COM port number. COM ports’ numbers are assigned
automatically and vary from computer to computer.

From the boot-loader’s command
line set-up the network interface’s environmental variables to match the
network settings of the Local Area Network in your environment, e.g.:setenv ipaddr <IP Address>setenv gatewayip <Gateway IP Address>setenv netmask <Net-mask>







Store the variables in the non-volatile memory,
so the settings will be applied for every subsequent platform’s boot:

saveenv

Load the Linux image into memory,  e.g.:tftpboot 0x80008000 <TFTP Server’s IP address>:/uImage-initramfs-4.1-r4-rzn1-snarc-20160913140308.bin Sample serial output may be as follows: => tftpboot 0x80008000
uImage-rzn1-snarc.binUsing dwmac.44002000 deviceTFTP from server 192.168.1.1; our IP address is
192.168.1.2Filename
'uImage-rzn1-snarc.bin'.Load address: 0x80008000Loading:
*#################################################################     #################################################################     #################################################################     ##################     8.4 MiB/sdoneBytes transferred = 3117224
(2f90a8 hex) Load the corresponding .dtb image file,
e.g.:tftpboot 0x80f00000 <TFTP Server’s IP Address>:/uImage--4.1-r4-rzn1-snarc-20160913140308.dtb A sample serial output is as follows: => tftpboot 0x80f00000 uImage-rzn1-snarc.bin   dtbUsing dwmac.44002000 deviceTFTP from server 192.168.1.1; our IP address is
192.168.1.2Filename
'uImage-rzn1-snarc.dtb'.Load address: 0x80f00000Loading: *####     1.4 MiB/sdone Boot Linux from memory:

































































bootm 0x80008000 – 0x80f00000

Sample serial output:

=> bootm 0x80008000 -
0x80f00000

## Booting kernel from Legacy
Image at 80008000 ...

   Image Name:  
Linux-4.1.0

   Image Type:  
ARM Linux Kernel Image (uncompressed)

   Data Size: 
  11331264 Bytes = 10.8 MiB

   Load Address: 80008000

   Entry Point: 
80008000

   Verifying Checksum ... OK

## Flattened Device Tree blob
at 80f00000

 

   Booting using the fdt blob at 0x80f00000

   Loading Kernel Image ... OK

using: FDT

   Loading Device Tree to 8fff1000, end
8ffff09f ... OK

## Transferring control to
Linux (at address 80008000)...

 

Starting
kernel ...

 

Uncompressing Linux... done,
booting the kernel.

Booting Linux on physical CPU
0x0

...

1.4   Cross-Compiling and running the sample ‘Hello World’ application

1.4.1        Pre-requisites:

Watch the
aforementioned video
. The steps from the video are reproduced below.

1.4.2        Steps:

On The Virtual Machine:

On the Virtual Machine launch Eclipse Accept the ‘/home/user/lces2_sample_workspace’ (see Figure 3 - Eclipse select
workspace)
 






Figure
3 -
Eclipse select workspace

Right click on ‘lces2_sample_project’ and in the drop-down
menu select ‘Build Project’, i.e.:
 




Figure 4 - Eclipse build project

Copy the output
‘lces2_sample_project’ binary to the server’s ‘/home/nfsroot’ directory:sudo cp /home/user/lces2_sample_workspace/lces2_sample_project/cortex-7a-cross-compile/lces2_sample_project
/home/nfs



 

On PUTTY serial console:

Mount the served /home/nfs directory, e.g.:

mount –t nfs –o nolock <NFS server’s IP address>:/home/nfs /mnt

Run the lces2_sample_project
application:

/mnt/lces2_sample_project

The output
on the serial console should be as follows:

root@rzn1-snarc:/# !!!Hello World!!!

Un-mount the /home/nfs
directory:umount /mnt






 

1.5   Remote Debugging using Eclipse IDE

This
section concerns remote debugging a target (arm cortex 7a) application executed
by the gdbserver on hosting LCES2 board. Both
components: target-gdb and host-gdbserver have been populated onto the
Development Environment Virtual Machine (starting from version 0.4). Importing
a pre-configured Virtual Machine has been described in section 1.2.

NOTE: The exact steps of creating the
cortex-7a-cross-compile-Debug build configuration as well as setting up the
remote debugging configuration are detailed in APPENDIX 2 –
Eclipse IDE debug configuration.

1.5.1        Requirements:

The Virtual
Machine (v0.4+) containing the following:

GNU DeBugger (GDB) Server of
version 5.11.1 GNU DeBugger (GDB) of version
5.11.1



1.5.2      Steps:

On the Virtual Machine Launch
the Eclipse IDESet ‘cortex-7a-cross-compile-Debug’
as an active build configuration (seeFigure
5 - Eclipse IDE - Selecting Build
configuration)




 


Figure
5 -
Eclipse IDE - Selecting Build configuration

Build the ‘lces2_sample_project’Copy the output debug
executable to the /home/nfsroot directory – it will be needed for the gdbserver
sessionBoot the LCES2 board as per section
1.3Mount the nfsroot folder served
from the Virtual Machine, i.e:







mount –t nfs –o nolock <NFS Server’s IPv4 Address>:/home/nfsroot /mnt

On the target (LCES2) platform
launch the gdbserver i.e.:

/mnt/bin/gdbserver <IP Address>:<Port no.> /mnt/lces2_sample_project

Right-clicking on the lces2_sample_project.
Traverse to ‘Debug Configurations’ (see Error! Reference
source not found.) 
 


Figure
6 -
Eclipse IDE - Debug configurations

Select pre-configured  lces2_sample_project_cortex-7a-cross-compile-Debug
debug configuration (see Figure 7 - Eclipse IDE - pre-configured debug
configuration)
 




Figure
7 -
Eclipse IDE - pre-configured debug configuration

As depicted on Figure 8 - Eclipse IDE - Debugger connection, amend
the Debugger connection settings to match the IP Address and Port no. from the On
the target (LCES2) platform launch the gdbserver above
 




Figure
8 -
Eclipse IDE - Debugger connection

 

Sart your remote debug session
by clicking the Debug button (as seen on Figure 9 - Eclipse IDE - Starting Debug ).


 


Figure
9 -
Eclipse IDE - Starting Debug

When prompted by a ‘Confirm
Perspective Switch’ pop-up window (Figure
10 - Eclipse IDE - Confirm Perspective
Switch) select ‘Yes’. 
 


Figure
10 -
Eclipse IDE - Confirm Perspective Switch

Try to step through the code as
depicted on the Figure 11 - Eclipse IDE - Step over
 


Figure
11 -
Eclipse IDE - Step over

 

NOTE: For the comprehensive list of steps taken to
configure the remote debug configuration for cortex-7a-cross-compile build
configuration please refer to the APPENDIX 2 – Eclipse IDE debug configuration.

2       
Eclipse
IDE

2.1         Installing
Eclipse for C/C++ projects

sudo apt-get install –y
eclipse-cdt

2.2  
Creating
a new project (demo)


 


2.3  
Cross
compilation with the Eclipse IDE

This
section provides a software developer with an example of a cross-compilation
setup, sufficient to build a newly created ‘Hello
World’ Project.

Steps:

a)      
Manually
unfolding all nested environment variables,at a minimum:

CCPATH,



environment
variables from the convenience script come with the toolchain (see 4.1    Toolchain) /opt/poky/2.0.2/environment-setup-cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi  file to Project à
Properties à C/C++ Build à
Environment as depicted on Figure 12 - Environment set-up.


 


Figure
12 -
Environment set-up

b)      
In  Project à Properties à C/C++ Build à Settings à Cross  GCC Compiler à Expert settings, modify the command line pattern to: 

 

${CC} ${FLAGS} ${CFLAGS}
${OUTPUT_FLAG} ${OUTPUT_PREFIX}${OUTPUT} ${INPUTS}

c)    In Project à Properties à C/C++ Build à Settings à Cross GCC Compiler à Symbols, add the __ARM_PCS_VFP
pre-compile flag

d)     In Project à Properties à C/C++ Build à Settings à Cross GCC Compiler à Includes

Provide the
include files’ path: /opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi/usr/include as depicted on Figure 13 - Project Settings (Includes)
 


Figure
13 -
Project Settings (Includes)

e)     In Project à Properties à C/C++ Build à Settings à Cross GCC Linker à Expert settings, modify the command line pattern to: 

 

${CC} ${FLAGS} ${LDFLAGS} ${OUTPUT_FLAG}
${OUTPUT_PREFIX}${OUTPUT} ${INPUTS}

f)      In
Project
à Properties à C/C++ Build à Settings à Cross GCC Linkerà Libraries

Provide the
following libraries’ paths:

 /opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi/lib

/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi/usr/lib

/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi/usr/lib/arm-poky-linux-gnueabi/5.2.0

g)        
In Project à Properties à C/C++ Build à Settings à Cross GCC Linkerà Miscellaneous à Other objects, provide the static gcc library:

/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi/usr/lib/arm-poky-linux-gnueabi/5.2.0/libgcc

3       
VmWare Ubuntu Virtual
Machine set-up

3.1       Creation of a new VM

VM guidelines are given in ECP Development Board_User Guides_Linux User
Guide_N°4 [3], [2]  in section “1.6 System Requirements” under
Box:

ECP --> ECP
Users --> ECP User Guides.

This guide has followed ECP team’s
guidelines.

Download ‘ubuntu-14.04.4-desktop-amd64.iso’
from ‘http://releases.ubuntu.com/14.04/’
to your hard drive.

Open VmWare Workstation.

‘File - > New Virtual Machine’, select ‘Custom Installation’. (Select default option if not specified
below.)

For “Install From:” select “Installer Disk
Image file (iso)” and give path to the iso file downloaded above.

Give a name for the user you wish to use on
the Virtual Machine. If this will be a shared VM, try to use something generic.
The username should be a short version of the name, which will be used to login
to the VM.

Give a name to your VM to identify it, e.g.
“ECP Ubuntu 14.04”.

Select 2 processors with 2 cores, or
something similar to give a minimum of 4 Total CPU cores.

Give at least 8GB of RAM to the VM, i.e. 8192MB.

Configure VM to use at least 100GB disk
size, select “Split disk into multiple files” to make it more manageable.

Before pressing “Finish” review your
options under “Customize Hardware”.

Useful options to change would be:

Network Adapter: select Custom
Network connection and whichever dropdown gives you a Bridged network
connection, e.g. “VMnet0 (Bridged)”. If this option does not exist, it can be
modified later. USB Controller: select USB 3.0
from the compatibility drop-down.Close the Hardware window and click Finish
to start the Ubuntu installation.  







3.2 OS Configuration

Once the OS is up and running there are a
few things that are useful to configure.

Login to your Ubuntu VM using the
username/password you created.

 

3.2.1       
General Proxy

Go to the System setting by click on the
System Setting menu in the System menu 


 


Then select the
Network Menu icon 


 


Select Network->Network Proxy and set
the method to Automatic and enter the Configuration URL ‘http://pac.schneider-electric.com/schneider-electric.com/ie.filtering.pac’and
select to apply it system wide, see below. This URL may vary from site to site
so check out that you have the correct URL by looking at the proxy settings on
your windows desktop.


 


 

3.2.2       
Command line proxy

Click on the search button on the top left
of Ubuntu Unity side-bar, type “terminal” and select the “Terminal” from the
applications found. This will open a bash shell.

Open ‘/etc/environment’ for editing by typing:

sudo gedit /etc/environment

and add the following entries:

http_proxy=http://gateway.schneider.zscaler.net:80

https_proxy=https://gateway.schneider.zscaler.net:80

ftp_proxy=ftp://gateway.schneider.zscaler.net:80

3.2.3       
Apt-get proxy

The apt-get command allows you to install,
upgrade and remove packages form the Ubuntu repositories. It needs to know
about the proxy as well. Type:

sudo apt-get
install -y --force-yes proxy 

sudo gedit
/etc/apt/apt.conf.d/02proxy

Copy and paste these lines to the 02proxy
file:

Acquire::http::Proxy "http://gateway.schneider.zscaler.net:80";

Acquire::https::Proxy "https://gateway.schneider.zscaler.net:80";

Acquire::ftp::Proxy "ftp://gateway.schneider.zscaler.net:80";

Save and close the file. Then you should be
able to run a software update:

sudo apt-get update

3.2.4       
Zscaler certificate

In order to use the web browser on your
development system you need to install the zscaler
root certificate into you favourite browser. 

To add this to FireFox, which is the
default browser in Ubuntu, open the browser and select Preferences -> Advanced.
You can do this by typing ‘about:preferences#advanced’ in the
address bar.  Select Certificates from the
tab menu: 


 


Select View Certificates and then press the
import button to import the certificate attached to this document.


 


Once the certificate is installed you
should be able to use your browser for most of the sites. It may ask you for
your login the first time it’s used.

 

3.3   Network Server set-up

3.3.1       
Setting up TFTP server

The TFTP protocol is used to transfer files to the
board for booting, e.g. kernel or other binary image. Install the following
packages:

sudo apt-get –y –force-yes
install xinetd tftpd-hpa tftp-hpa

Create the directory for the tftp server
and modify its permissions:

sudo mkdir
/var/lib/tftpboot

sudo chmod -R
777 /var/lib/tftpboot

sudo chown -R nobody
/var/lib/tftpboot

Create and edit the configuration file for
your server:

sudo gedit
/etc/xinetd.d/tftp

In the text editor add the following to
your tftp file:

service tftp

{

    protocol        = udp

    port            = 69

    socket_type     = dgram

    wait            = yes

    user            = nobody

    server          = /usr/sbin/in.tftpd

    server_args     = -4
/var/lib/tftpboot

    disable         = no

}

 

Then restart the server:

sudo /etc/init.d/xinetd
restart

Test your setup:

touch
/var/lib/tftboot/testfile

tftp localhost

In the tftp prompt type:

get testfile

quit

In your present working directory (pwd),
execute ‘ls’ and check if the testfile was fetched from your local server.

3.3.2       
Setup NFS

The NFS server is used for using a remote
root file system when booting on the target board. The file system will exist
on the network, on an NFS server and be usable from the target board when it’s
connected to the network.

sudo apt-get –y –-force-yes
install nfs-kernel-server

A settings’ file needs to be edited to add
your rootfs location to your server:

sudo gedit /etc/exports

Add your rootfs location to the file with
some options, e.g.: 

/home/nfsroot *(rw,sync,no_subtree_check,no_root_squash)

If you wish to change any of the options,
read the nfs exports manual with:

man exports

Try using a location that will not change
over time, so you don’t need to keep modifying this file. For example, you
could use a symbolic link to your rootfs location: 

sudo ln -s
/home/user/ECPlinux/build/tmp/work/snarc_soca9-poky-linux-gnueabi/ecp-image/1.0-r0/rootfs/
/home/nfsroot

Restart the server:

sudo service
nfs-kernel-server restart

3.4  
Git/Repo Setup

Read ECP Development Board_User Guides_Global
Overview_N°1 [4] document section
2.4.1 Overview (for Firmware Factory) 

Follow the instructions at the Teamforge
links [5] and [6]to setup git client and
repository. 

If there are permissions problems using
curl to get the repo, download locally first:

curl -k https://storage.googleapis.com/git-repo-downloads/repo
> repo

You may need to change permissions to make
it executable:

sudo chmod –R 755 repo

Then move repo to the bin directory:

sudo mv repo /usr/bin/repo

3.5   Build dependencies

As part of the build instructions,
sometimes certain packages may be missing, to install them run:

sudo apt-get
install <package>

 

These will be needed for Linux bitbake:

sudo apt-get –y –-force-yes
install texinfo gawk chrpath sl

4       
Software development
environment

4.1 Toolchain

4.1.1        LCES2

For the LCES2 board the toolchain has been
compiled and archived by the Agilis team here.

In order to install the cross-compilation
toolchain for the target cortex7a:

tar -xjf
poky-glic-x86_64-meta-toolchain-cortexa7hf-vfp-vfpv4-d16-toolchain-2.0.2.sh.tbz
-C /tmp/

sudo
poky-glic-x86_64-meta-toolchain-cortexa7hf-vfp-vfpv4-d16-toolchain-2.0.2.sh

To install the same version of the
toolchain but for the target native x86_64 platform:

sudo tar -xjf toolchain_native_x86_64_gcc_5.2.0.tbz
-C /

4.1.2        SocA9

For a SocA9 board the pre-built toolchain
binaries can be found as per [3].

4.1.3      Installation

Installation of the toolchain on the Ubuntu
Linux Virtual Machine is performed by invoking the provided Bourne shell script
‘poky-glibc-x86_64-meta-toolchain-cortexa7hf-vfp-vfpv4-d16-ttolchain-2.0.2.sh’

NOTE: It is advised, for the sake of future
troubleshooting, to install the toolchain at the default location i.e.: ‘/opt/poky/2.0.2/…’

4.2 Command line

4.2.1      Setting-up the
environment

In order to successfully compile for the Cortex
A7 (LCES2) platform on the x86_64 host, one is required to set-up the toolchain
environment. In order to achieve this one MUST
run the Bourne-shell script delivered
along with the toolchain:

source
/opt/poky/2.0.2/environment-setup-cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi

4.2.2-    ANSI-C ‘Hello World’
example

<fetch from git repo TBD>

4.2.3      Building

Command line approach is fairly
straightforward in its nature, hence in order to build one needs to invoke
couple standard commands:

cd
lces2_test

make

5       
Create ECP Binaries

If you do not use the binaries provided by
ECP team on Box, these can be built using the instructions provided. 

To start with you’ll need access to ECP
team’s documentation on Box:

https://schneider-electric.app.box.com/files/0/f/781759940/ECP

Request the access from Anders Lykke-Skov.

The Box folder contains User Guides and
toolchain and development board binaries.

Start with reading ECP Development Board_User
Guides_Global Overview_N°1 [4].

Follow instructions in that document
section 2.6 to request access to Teamforge. Teamforge links should still work
for you even before you get full user access.

For more than less comprehensive list of
vital clearances please refer to APPENDIX 1 – List
of NMC Clearances to be requested.

 

NOTE:
The User Guides as well as build processes differ for SoC A9 and LCES2. For the
comprehensive list of the prerequisite documentation please refer to Bibliography.

3.1  
SoC A9

3.1.1          
Building the boot-loader

Create a new folder for
the project bootloader e.g.: 

 

mkdir
/home/SESA1234/boot4linux

 

Follow instructions in ECP
Development Board_User Guides_Bootloader Guide (Boot4ECP)_N°3 [7] section 5.2 Source:
Teamforge project, where the repo is configured, downloaded and have the
bootloader binaries built for all the boards, i.e.

 

repo init -u ssh://teamforge.schneider-electric.com/boot4ecp_manifest

repo sync

cd
boot4ecp_u-boot_toolchain

sudo
./setup.sh

cd
../boot4ecp_u-boot

./make_all_ECP_boards.sh

 

Read the User Guide [7] for an explanation
of these steps.

3.1.2          
Building Linux

 

Create a new folder for the ECP Linux build environment. Follow
instructions in ECP Development Board_User Guides_Linux User Guide_N°4 [3], sections: 3.2.2
Getting Source Code and 3.2.3 Regenerate LINUX4ECP image, i.e.

 

repo init –u ssh://teamforge.schneider-electric.com:29418/yocto_manifest
–repo-url=ssh://teamforge.schneider-electric.com:29418/repo

repo sync -c

source
sources/poky/oe-init-build-env

bitbake ecp-imageRead the User Guide [3]for an explanation of
these steps.

3.2   LCES 2

This section covers the creation of binary
images from sources for the pre-loader, boot-loader as well as Yocto Linux  OS for the LCES 2 boards.

3.2.1          
Building the boot-loader

Create a new folder for the ECP bootloader
build environment. Follow instructions as per [8] i.e.:

repo init –u
ssh://teamforge.schneider-electric.com/boot4ecp_manifest –b rzn1-eval-r2 [--repo-url=ssh://teamforge.schneider-electric.com:29418/repo]

repo sync

                                                         

To build the the u-boot bootloader type in the
terminal:

cd
boot4ecp_u-boot_toolchain

sudo sh
setup.sh

cd  ../boot4ecp_u-boot

sudo sh make_rzn1.sh

3.2.2          
Building Linux

Create a new folder for the ECP Linux build
environment. Follow instructions as per [2] i.e.:

repo
init -u ssh://teamforge.schneider-electric.com/yocto_manifest -b rzn1d
--repo-url=ssh://teamforge.schneider-electric.com:29418/repo



repo sync –c

NOTE:
--repo-url=ssh://teamforge.schneider-electric.com:29418/repo is
optional – for mirroring purposes when google repositories are not accessible.

To build the source one may create the
directory then, from inside, execute the following sample Bourne shell script:

#!/bin/sh

REPO_DIR=`pwd`

echo
"REPO_DIR = $REPO_DIR"

 

cd $REPO_DIR

source
$REPO_DIR/sources/poky/oe-init-build-env

#building the linux
kernel and the rootfs

bitbake
core-image-minimal

 

##building the linux
kernel only

#bitbake
linux-rnz1

cd;

 

To
build the toolchain ‘bitbake’ another target:

 

bitbake meta-toolchain

 

To
install toolchain:

 

cd <Repo
directory>/tmp/deploy/sdk

sudo sh
poky-glibc-x86_64-meta-toolchain-cortexa7hf-vfp-vfpv4-d16-toolchain-2.0.2.sh

6       
Booting the platform

6.1    Booting from an SD card

The SD card needs
to contain at a minimum a preloader and a bootloader (u-boot.img) files. Follow
instructions in ECP Development Board_User Guides_Bootloader Guide
(Boot4ECP)_N°3 [7] section “3.2 Script generate_sd.sh” to flash the preloader to the SD
card. The images can be taken from the build described in 5. Create
ECP Binaries or a downloaded binary as described in [7] and [3]. The bootloader can be
copied directly to the SD card, as long as correct partitioning is already done
using the generate_sd.sh script. Using the generate_sd.sh script

In order to generate the bootable SD card
one can create and execute the following example script:

#!/bin/sh

SD_DEV=/dev/sdb

BOOT_BUILD=./boot4ecp_u-boot/ECP_RELEASE_FOLDER/

PRELOADER_PATH=$BOOT_BUILD/preloader-snarc-soca9-bestla-sdram-micron512-sdcard

BOOTLOADER_PATH=$BOOT_BUILD/u-boot-snarc-soca9-bestla-sdram-micron512-sdcard

FPGA_IMAGE_PATH=/home/src/fpga_micron_sdram512.rbf

 

LINUX_IMAGES=./yocto/build/tmp/deploy/images/snarc-soca9/


LINUX_KERNEL=$LINUX_IMAGES/zImage--3.14+git0+7d779b22d6-r0-snarc-soca9-20160912103015.bin

#LINUX_DEV_TREE=$LINUX_IMAGES/zImage-snarc_soca9_qspi_micronN25Q_bestla_512m.dtb

LINUX_DEV_TREE=$LINUX_IMAGES/zImage--3.14+git0+7d779b22d6-r0-socfpga_cyclone5_socdk-20160912103015.dtb

LINUX_ROOTFS=$LINUX_IMAGES/ecp-image-snarc-soca9-20160912103015.rootfs.tar.gz

 

sudo  ./boot4ecp/boot4ecp_u-boot/generate_sd.sh
$SD_DEV $PRELOADER_PATH $BOOTLOADER_PATH $FPGA_IMAGE_PATH $LINUX_KERNEL
$LINUX_DEV_TREE $LINUX_ROOTFS

 

ASSUMPTIONS:  

The respective directories’
names of repositories for boot4ecp and linux4ecp, as described in, Create ECP Binaries are:
boot4ecp and yoctoThe sources were built as
per 5. Create ECP Binaries



 

6.1   Booting over TFTP

The LCES2 board comes with the pre-flashed
pre- and boot- loaders. According to the User Guide [2] the supported boot
modes are either from NOR-flash over QSPI or the Trivial File Transfer Protocol
(TFTP). This section focuses on the second mode listed and provides the
reader with a sample set-up.

6.2.1       
Pre-requisites:

The Linux image containing the initial RAM file-system (initramfs),
built as per section 3.2.2, copied to the folder shared between the host and Virtual Machine.
Alternatively, one might use the pre-built binaries.Virtual Machine running the
TFTP server. It may be the same
machine that hosts the Virtual Machine being used for building the Linux
binaries. A sample TFTP-booted
development environment is depicted on Figure 14 - The TFTP boot environment.Network settings of the set-up
presented on Figure 14 - The TFTP boot environment LAN: 10.216.251.0NIC: 1000BASE-T; IPv4: 10.216.251.65NIC J21: 1000BASE-T; IPv4: 10.216.251.99Gateway: IPv4: 10.216.251.1
















 
  
  
   
    
    
    Figure 14 -
    The TFTP boot environment
    
    
   
  
  

 
  
  
 
  
   
    
    
     
      
      
      Host
      PC (Windows 10) 
       
      
      
      
     
    
    
  
   
    
    
     
      
      
      Virtual
      Machine
      
      
     
    
    
  
   
  
  
   
   
    
     
     
     BESTLA
     board
     
     
    
   
   
 
  
   
   
    
     
     
     NIC J21 Ethernet
     
     
    
   
   
 
  
   
   
    
     
     
     LCES2
     board
     
     
    
   
   
 
  
   
   
    
     
     
     USB/UART serial
     
     
    
   
   
 
  
   
   
    
     
     
     NIC 
     
     
    
   
   
 
  
   
   
    
     
     
     USB
     
     
    
   
   
 
  
   
   
    
     
     
     NFS
     folder
     
     
    
   
   
 
  
   
   
    
     
     
     TFTP Server
     
     
    
   
   
 
  
 
  
 
  
  
  
  
  
  
   
   
    
     
     
     LAN
     10.216.251.
     
     
    
   
   
 
 
 
  
 
  
   
   
    
     
     
     PUTTY
     
     
    
   
   
 
  
 
  
 

 
 
 


NOTE:
The network settings may and extremely likely will vary from ones presented
hence MUST be adjusted in accordance to your on-the-site eco-system.

6.2.2       
Minimal Software requirements:

Ubuntu Linux TFTP ServerSerial terminal i.e. PUTTY



6.2.3       
Steps:

Connect the LCES2 board’s J21
(via Ethernet cable) to the PC’s NIC Connect the LCES2’s
USB/UART  to the PC’s USBLaunch and configure your PUTTY
session over serial e.g.:
 
 Install, set-up  and launch the TFTP Server on the host PC’s VM machine (see 3.3.1)Copy your Linux image files to
the configured to the TFTP server’s home directory, i.e. /var/lib/tftpboot .











On of ways of
doing that is to use the shared folders’ mechanism, with which the VM
Workstation Pro  is providing us by
default.

16a.    Create the folder ‘C:\shared’ .

16b.    In the VM Settings
enable shared folders’ feature (see Figure 15 - VM Workstation Pro - Shared folders)
 


Figure
15 - VM
Workstation Pro - Shared folders

16c.    In
the VM’s terminal run the following command:

sudo vmware-config-tools.pl -d

16d.    The shared folder should become visible and
accessibl;e @ ‘/mnt/hgfs/shared’

16e.    Download your Linux image files to ‘C:\shared’
folder.

16e.    Copy the Linux image files from ‘/mnt/hgfs/shared’
to to the ‘/var/lib/tftpboot’ i.e.:

sudo cp -fv
/mnt/hgfs/shared/uImage-initramfs-4.1-r4-rzn1-snarc-20160913140308.bin
/var/lib/tftpboot/

sudo cp -fv
/mnt/hgfs/shared/uImage--4.1-r4-rzn1-snarc-20160913140308.dtb
/var/lib/tftpboot/

sudo chmod 777 /var/lib/tftpboot/*

Power-up the board

The pre-flashed
boot-loader should display its prompt at the PUTTY serial console i.e.:

version

U-Boot
2014.07_se-uboot-v1.0.0 (Mar 18 2016 - 16:28:05)

arm-linux-gnueabihf-gcc
(crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09) 4.9.2
20140904 (prerelease)

GNU ld
(crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09)
2.24.0.20140829 Linaro 2014.09

=>

From the boot-loader’s command
line set-up the network interface’s environmental variables to match the
network settings of the Local Area Network in your environment e.g.:setenv ipaddr 10.216.251.99setenv gatewayip 10.216.251.1setenv netmask 255.255.255.128







Optionally one may want to set up TFTP Server’s IP address (literally the IPv4
address that NIC on the Virtual Machine had obtained over DHCP):

setenv serverip 10.216.251.65

One may want to store the variables in the
non-volatile memory, so the settings will be applied for every subsequent
platform’s boot:

saveenv

Load the Linux image into memory as
e.g.:tftpboot 0x80008000
10.216.251.65:/uImage-initramfs-rzn1-snarc.bin Sample serial output may be as follows: => tftpboot 0x80008000
uImage-rzn1-snarc.binUsing dwmac.44002000 deviceTFTP from server 192.168.1.1; our IP address is
192.168.1.2Filename
'uImage-rzn1-snarc.bin'.Load address: 0x80008000Loading:
*#################################################################     #################################################################     #################################################################     ##################     8.4 MiB/sdoneBytes transferred = 3117224
(2f90a8 hex) Load the corresponding .dtb image file
e.g.:tftpboot 0x80f00000
10.216.251.65:/uImage-rzn1-snarc.dtb Sample serial output may be as follows: => tftpboot 0x80f00000
uImage-rzn1-snarc.bin   dtbUsing dwmac.44002000 deviceTFTP from server 192.168.1.1; our IP address is
192.168.1.2Filename
'uImage-rzn1-snarc.dtb'.Load address: 0x80f00000Loading: *####     1.4 MiB/sdone Boot the Linux from memory:

































































bootm 0x80008000 – 0x80f00000

Sample serial output:

=> bootm 0x80008000 -
0x80f00000

## Booting kernel from Legacy
Image at 80008000 ...

   Image Name:  
Linux-4.1.0

   Image Type:  
ARM Linux Kernel Image (uncompressed)

   Data Size:   
11331264 Bytes = 10.8 MiB

   Load Address: 80008000

   Entry Point: 
80008000

   Verifying Checksum ... OK

## Flattened Device Tree blob
at 80f00000

 

   Booting using the fdt blob at 0x80f00000

   Loading Kernel Image ... OK

using: FDT

   Loading Device Tree to 8fff1000, end 8ffff09f
... OK

## Transferring control to
Linux (at address 80008000)...

 

Starting
kernel ...

 

Uncompressing Linux... done,
booting the kernel.

Booting Linux on physical CPU
0x0

...

7       
Protocol Evaluations

There are a number of protocols being
considered for inter-board communications, i.e. SLC to UC, etc… This describes
installation for testing of some of the possible protocols.

7.1  
MQTT

Installing MQTT to your development system run
the following commands from the terminal window:

sudo [–E]
apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

sudo apt-get
update

sudo apt-get
install mosquitto

sudo apt-get
install libmosquitto-dev

sudo apt-get
install mosquito-clients

8       
Altera
Windows SW

Download the following from Altera website:

The Altera Software downloads will require you
to create an Altera account.

SoC EDS (Embedded Design Suite) Lite Edition [9]

After launching the installer it may take
several minutes for it to actually open.

If not already installed above, download
Quartus Prime Lite [10].

These tools will
be used to write directly to the board flash using USB-Blaster II.


 9       
 Continuous
 Integration
 The Continuous Integration (CI) tool used
 is Jenkins.
 9.1   Installation
 To
 initially install on Linux on you need to open a terminal and type the
 following:
 wget
 --no-check-certificate –q –O – https://pkg.jenkins.io/debian/jenkins-ci.org.key
 | sudo apt-key add -
 sudo sh –c
 ‘echo deb http://pkg/jenkins.io/debian-stable binary/ >
 /etc/apt/sources.list.d/jenkins.list’
 sudo apt-get
 update
 sudo apt-get
 install Jenkins
 All of the
 instructions above can also be found here.
 9.2   Running 
 There are
 2 ways in which to run Jenkins
 1.     
 Use
 default daemon
 2.     
 Run
 from terminal
 9.2.1       
 Default
 Daemon
 After
 installation (and from start up), Jenkins will be running as a daemon, on port
 8080. All information related to the installation will be stored in the
 following location: ‘/var/lib/jenkins’.
 Information
 includes, jobs, workspace and user accounts. 
 NOTE
 Using
 Jenkins from this method can cause complications with ssh keys (needed for
 contacting git repositories) as Jenkins may not be able to read them,
 depending on where they are placed in the file system due to permissions
 errors. Because by default Jenkins is installed to /var/lib/Jenkins, it is
 expecting to read ssh keys out of a directory called /var/lib/ssh or
 /var/lib/.ssh. However, unless the daemon has been run as root user, your
 Linux system will not allow Jenkins to simply read from this directory. 
  
 
  
 
 The latter
 method of running Jenkins avoids this problem as it is installed in
 /home/<user>/.jenkins directory.
 9.2.2       
 Run
 from terminal
 Jenkins
 can also now be run in a terminal with the following command: 
 java –jar /usr/share/jenkins/jenkins.war
 –httpPort=portNo &
 We use the
 ampersand (&) to indicate that we want to demonise the process. Also, port
 8080 will NOT be available to you
 because 8080 is the default port assigned to the default Jenkins daemon.
 Using this
 method, all Jenkins information will be stored in ~/.jenkins. This option is
 better because there are never any issues with permissions.
 Users can
 also demonise the running of Jenkins from another port. The advantage of this
 is that if your machine which is running Jenkins is shutdown at any point,
 Jenkins will be restarted again automatically when the machine reboots. To do
 this, follow the steps below.
 1.     
 Create
 a script called ‘run_jenkins.sh’ (or any name you want, just put .sh at the
 end!) and save it in a location where it will not be moved (e.g
 /home/<user>/run_jenkins.sh)
 2.     
 Open
 the script in an editor, put the command from above into the first line and
 save it. 
  
 
 3.     
 Run
 the following command so that your script can be made executable 
  
 
 4.     
 Then
 we have to edit the crontab file with the following command 
  
       
 5.     
 This
 will bring you to an editor (you may have to select an edit when opening this
 file, if so select whatever number corresponds to “nano”). Add “@reboot
 <path/to/run_jenkins/script>” to the end of this file and save it 
  
 
 6.     
 Now
 upon the machine’s start up, the script will run and launch Jenkins on your
 specified port.
  
 9.3    Basic Configuration
 1.     
 After
 installation, go to an internet browser and type in the IP address of the
 server where Jenkins will be running, followed by the port number. E.g.
 “127.0.0.1:8081”
 2.     
 Follow
 the onscreen instructions until asked to configure proxy. Click into configure
 proxy and add the following details
 Server: wf1-ch.pac.schneider-electric.com
 Port: 80
 
  
 
 3.     
 Next
 you will then be asked to install plugins. Select install default plugins
 using options available
 4.     
 Next
 you will be asked to setup user credentials, so enter as you see fit.
  
 9.4   Extra Configuration
 First we
 need to install some extra plugins that will be used as well.
 1.     
 On
 the Jenkins home screen (assuming you’re logged in), select ‘Manage
 Jenkins’ -> “Manage Plugins”, and click the ‘Available’ tab
 2.     
 Search
 for the plugin called ‘Email Extension Plugin’. This
 plugin will be used to email members in the project about the results of
 builds. To install, check the box next to the plugin on the list, and then
 click ‘Install without restart’ or ‘Download no and install after
 restart’. This plugin also requires further configuration once it has
 been installed.
 a.     
 Go
 back to Jenkins home screen  ‘-Manage
 Jenkins’ -> ‘-Configure
 System’
 b.     
 Scroll
 down that page to the ‘Extended Email Notification’. Here
 there will be many fields which are to be left to their default values. The
 fields that I edited were
                                                    
 i.     SMTP Server: add you  SMPT Server (e.g
 mail.<region>.apcc.com)
                                                   
 ii.     SMPT Port (Click ’Advanced’):
 25
                                                  
 iii.    
 Default   Recipients: enter in the email addresses of
 the recipients required
                                                  
 iv.     Click ‘Save’
 
  
 
  
  
  
 9.5 Creating projects
 1.     
 Go
 to Jenkins home screen and select ‘New Item’
 2.     
 Fill
 in a name (recommended name is the name of the module you are building for)
 into ‘Enter an item name’ and select ‘Freestyle Project’, and
 then ‘OK’.
 3.     
 Now
 you should see menu like below 
  
 
 4.     
 Scroll
 down to ‘Source Code Management’ and select the Git radio button, and
 fill in your repository URL, as shown below 
  
 
 5.     
 Scroll
 down to ‘Build Triggers’, and tick ‘Poll SCM‘, and type into the box ‘*/10 * * * *’. This
 means poll every 10 minutes, where each star is ‘MINUTES HOURS DAYS MONTHS YEAR’
 6.     
 Scroll
 down to ‘Build’, and click ‘Add build step’ and select ‘Execute
 shell’. In the ‘Command’ box, enter the command
 you would like to use to build/test with as if it were a terminal. 
  
 
 Note that for this step, the ‘Command’ box above is essentially
 just a terminal on the machine itself, so any command to be executed must be
 known/installed on the system. For instance, ‘gcc’ must be installed
 on the server itself in order for the command above to work.
  
 7.     
 Scroll
 down to ‘Post-build Actions’ and click ‘Add post-build action’, and
 select ‘Editable Email Notification’. This option will email selected
 members about build failures and successes. Leave all as default, except ‘Attach
 Build Log’ option, and select ‘Attach Build Log’ from the
 dropdown menu. Also, click ‘Advanced’ and scroll down to
 triggers, and then configure as follows                  
  
 
 10  Setting up Klocwork on Developers
 Machine
 10.1      Introduction 
 The
 following is a guide to installing klocwork in eclipse on your Ubuntu
 development machine. All of these instructions can also be found here, however the method of installing
 the klocwork plugin into eclipse is different. The reason that I chose the
 method below is because it is difficult to reach the plugin download site via
 eclipse plugin manager
 10.2      Prerequisites
 Install
 eclipse using the Ubuntu Software Center 
  
 
 10.3      Installing Klocwork Plugin in Eclipse
 1.     
 Go
 to the following url: http://pfrwrdk1.eur.gad.schneider-electric.com/KW-Eclipse-update-site/plugins/
 2.     
 This
 will bring you to the following page 
  
 
 3.     
 Download
 and save all of the above files to your
 <eclipse_installation_dir>/dropins/sdk/plugins directory (this directory
 is usually in /usr/lib/). You may need to root user rights to complete this.
 In that case, do the following steps.
 i.      
 Create
 a folder on your systems that does not require root access (e.g Desktop) and
 call it kw_plugin. 
 ii.     
 Download
 the jar files to that directory 
  
 
 iii.    
 
  
   
   
    
     
     
     sudo cp -v /home/alan/Desktop/kw_plugin/*.jar /usr/lib/eclipse/dropins/sdk/plugins/
     
     
    
   
   
 Open a terminal and
 type the following, replacing “/home/alan/Desktop” and “/usr/lib/” with your
 own file paths
  
  
  
 4.     
 Restart/open
 eclipse
 5.     
 Go
 to ‘Window
 – Preferences – Klocwork – Settings’ and enter the following
 information:
 License Server: PFRWFLM3.eur.gad.schneider-electric.com
 Port = 27002
 
  
 
 6.     
 Click
 “OK”
 7.     
 Klocwork
 should now be successfully installed in eclipse.
  
 10.4      Using Klocwork in  a Project
  
 
  Open a project in your environment, right click it and select
      Properties.
      
       
      
 
 
  Go to CCS Build > Builder and uncheck 'use default build command'.
      Then add this line at the begining of the 'build command' field: 
      WARNING: leave a space between the two commands
 
 ·        kwinject -u -o "${ProjDirPath}/kwinject.out" 
 
 
  
 
 
  Run a clean
      build of your project.
  Go to Project
      > properties > Klocwork > Klocwork Build settings.
  Enable 'Use Build specification file' and fill this path to
      the 'kwinject.out' file (created during the previous build step).
 
 ·        ${project_loc}\kwinject.out
 
  Validate with OK button.
      
       
      
 
 Now Klocwork
 will automatically monitor the build process.
 10.5      Link a project with an existing Klocwork project on the
 server-side
 There are two solutions to link your projects in your IDE
 (Eclipse for example) and Klocwork project.
 First one is to automatically map project names between Eclipse and Klocwork.
 The other one is a manual setting.
 Note: This is only possible if a full analysis (build) was
 previously run from the command line.
 See wiki to start with.
 10.5.1      Using mapping file
 
  Open
      a project in your environment and select Menu > Window > Preference
      
       
      
 
 
  Browse
      to Klocwork > Settings and click Import
      map option.
      
       
      
 
 
  Select
      your mapping file and validate with OK button.
  Your
      projects will now be synchronized. You should see (after few seconds) the
      green synchronized icon.
      
       
      
 
 
  Example
      of Klocwork mapping file
  This
      configuration is saved in the current Workspace, so changing / deleting
      the workspace will remove the settings.
 
 10.5.2      Manual setting
 
  Open
      a project in your environment, right click it and select Properties
      
       
      
 
 
  In
      Klocwork menu, select 'enable project specific settings'.
      Then fill the Klocwork server details in the synchronization tab.
      Hit Refresh
      when done.
 
 ·        Host = pfrwrdk1.eur.gad.schneider-electric.com·        Port = 8080
 
 
  
 
 
  To
      connect the server, Klocwork need your credential (same as your network
      account - when you login your computer).
      
       
      
 
 
  Select
      the project in the dropdown list and click OK
      
       
      
 
 
  To
      open the Klocwork perspective, click Open Perspective button 
      
       
      
 
 
  ...
      and select Klocwork. You will have the Klocwork specific view
      
       
      
 
  
  
  
  
 11  Installing Klocwork on Jenkins Build
 Server
 11.1      Installing Klocwork on the build server
 Please
 note that all instructions for Klocwork installation and synchronisation can
 be found here. Also, the “man” page for all
 klocwork commands can be found here
 1.     
 Download
 the klocwork installation script from \\rd-luge.eur.gad.schneider-electric.com\FileServer\Shared
 - Commun\Outils\common\_Software Development\_Quality\_Code
 Analyser\Klocwork\v11.2 the one that you want is called “kw-server-installer.11.2.0.402.linux64.sh”.
 Note that the link above is a link to a file on a windows network drive, so it
 will not be accessible through the web.
 2.     
 
  
   
   
    
     
     
     sudo chmod a+x kw-server-installer.11.2.0.402.linux64.sh
     
     
    
   
   
 Cd into the
 directory where you downloaded the script to, and run the following command to
 allow execution of the script.
  
 3.     
 Then,
 run the following command to install klocwork on your system
 
  
   
   
    
     
     
     ./kw-server-installer.11.2.0.402.linux64.sh --agree --license-server
     PFRWFLM3.eur.gad.schneider-electric.com:27002 -i $HOME/.klocwork BuildTools
     
     
    
   
   
  
  
  
 
 4.     
 
  
   
   
    
     
     
     KW_HOME=$HOME/.klocwork
     
     
    
   
   
 After the install
 create the KW_HOME environment variable. Do this by  adding the following line to the
 /etc/environment file
  
  
 5.     
 Then,
 update the PATH to include the klocwork bin directory
 
  
   
   
    
     
     
     PATH=$KW_HOME/bin:$PATH
     
     
    
   
   
  
  
 
 6.     
 Restart
 your machine with Klocwork Server
 11.2      Synchronisation with Klocwork Server
 Next we
 need to synchronise with the Klocwork Server
 1.     
 
  
   
   
    
     
     
     kwauth --url http://pfrwrdk1.eur.gad.schneider-electric.com:8080/
     
     
    
   
   
 Open a terminal and
 type the following 
  
 2.     
 This
 should prompt you to log in. Do so using your windows credentials
  
 3.     
 If
 login is successful, run the following command
  
 
  
   
   
    
     
     
     kwdeploy sync --url http://pfrwrdk1.eur.gad.schneider-electric.com:8080/
     
     
    
   
   
  
  
 
 4.     
 This
 should produce the following result 
 
  
 
  
  
  
 11.3      Running Klocwork on Jenkins
 
  
   
   
    
     
     
     $JENKINS_HOME/klocwork.sh  <job_name> <url> <project_name> <build_command>
     
     
    
   
   
 The easiest way to
 run the klocwork commands is to either create a script to run the command line
 executables or use the sample found here. If you plan on using the sample
 script, the usage is as follows. Also, the sample script needs to be placed in
 the JENKINS_HOME directory to run correctly.
     
 Where:
 
  
   
   job_name
   
   
   Name of
   Jenkins job (project)
   
  
  
   
   url
   
   
   Url of
   Klocwork server (note often has :portNo appended to it
   
  
  
   
   project_name
   
   
   Name of
   the klocwork project on the klocwork server
   
  
  
   
   build_command
   
   
   The
   normal build command you would use to build your project. E.g. make
   
  
 
  
 To run on
 Jenkins, follow the steps below.
 1.     
 In
 your Jenkins project configuration, got to ‘Build’ 
 2.     
 Click
 ‘Add
 build step’
 3.     
 Select
 ‘Execute
 Shell’
 4.     
 Enter
 a command similar to the following to run the script
 
  
 
 5.     
 Save
 the project.
 6.     
 The
 project should now be setup to use the Klocwork Analysis tools. After running,
 you should have an output similar to the one below.
 
  
  
  
 
  
  
  
 12  Elixir Setup
 12.1      Installing Elixir on your VM
 
  
   
   
    
     
     
     wget --no-check-certificate
     https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
     dpkg -i
     erlang-solutions_1.0_all.deb
     apt-get update
     apt-get install -y esl-erlang elixir
     
     
    
   
   
 Open a terminal and
 enter the following commands
  
  
  
 12.2      Install Phoenix/Nerves
 
  
   
   
    
     
     
     mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez
     mix archive.install --force https://github.com/nerves-project/archives/raw/master/nerves_bootstrap.ez
     
     
    
   
   
  
  
  
 
 12.3      Install NodeJS
 
  
   
   
    
     
     
     curl -sL
     https://deb.nodesource.com/setup_6.x | sudo -E bash -
     apt-get install -y nodejs
     
     
    
   
   
  
  
  
  
 
 12.4      Configuration for Firewall and Network
 Proxies
 
  
   
   
    
     
     
     # Rebar (Erlang)
     mkdir -p ~/.config/rebar3
     echo “{ssl_verify, false}.” > ~/.config/rebar3/rebar.config
      
     # Mix (Elixir)
     mix local.hex --force
     mix hex.config unsafe_https true
     mix hex.config http_proxy $http_proxy
     mix hex.config https_proxy $https_proxy
      
     # NodeJS
     npm config set proxy $http_proxy
     npm config set https-proxy $https_proxy
     npm config set registry http://registry.npmjs.org/
     npm config set strict-ssl false
     
     
    
   
   
  
  
  
  
  
  
  
  
  
  
 
 12.5      How install Elixir Syntax Recognition in
 VIM (Linux) and Sublime-text
 Note:
 This guide assumes that both editors are
 installed on your system.
 12.5.1      VIM
 1.     
 Mkdir
 ~/.vim/autoload
 2.     
 Mkdir
 ~/.vim/bundle
 3.     
 Go
 to the following link to a file and copy the contents of the file https://tpo.pe/pathogen.vim
 4.     
 Create
 the file ~/.vim/autoload/pathogen.vim and paste the contents from step 3 into
 it, and save
 5.     
 Add
 the following to the ~/.vimrc file (create if not yet created)
 execute pathogen#infect()
 syntax on
 filetype plugin indent on
 6.     
 Cd
 into ~/.vim/bundle
 7.      Run the following to install the plugin git clone https://github.com/elixir-lang/vim-elixir.git Note: git may not be able to perform a clone due to proxy restrictions on the network, so in that case just click the url above and download the project as shown below 
  
 Finally, extract the contents of the zip into the directory specified in step 6 8.      Elixir syntax recognition should now be installed in vim 
 12.5.2      Sublime-text
 1.     
  
 a.     
 (Linux) cd
 ~/.config/sublime-text-#/Packages
 b.     
 (Windows) cd
 C:\Users\<UserName>\AppData\Roaming\Sublime^ Text^ #\Packages
 2.      git clone https://github.com/elixir-lang/elixir-tmbundle.git ElixirNote: git may not be able to perform a clone due to proxy restrictions on the network, so in that case just click the url above and download the project as shown below 
  
 Finally, extract the contents of the zip into the directory specified in step 1
 3.     
 restart sublime-text
  
  
 
  13  Bibliography
  
   
   
    
     
     [1] 
     
     
     vmware,
     "Workstation 12 Pro documentation Center," vmware, [Online].
     Available:
     https://pubs.vmware.com/workstation-12/index.jsp#com.vmware.ws.using.doc/GUID-DDCBE9C0-0EC9-4D09-8042-18436DA62F7A.html.
     [Accessed 26th September 2016].
     
    
    
     
     [2] 
     
     
     Hervé
     Roussain , "ECP_ECP Development Board_LCES2_SNARc_User N 4
     Guides," Schneider Electric, 13th July 2016. [Online]. Available:
     https://schneider-electric.app.box.com/files/0/f/8792715565/1/f_75360716786.
     [Accessed 15th September 2016].
     
    
    
     
     [3] 
     
     
     Tangi
     Colin, Nikolaj Goodger, "ECP_ECP Development Board_User Guides_Linux
     User Guide_N 4," Schneider Electric, 28 April 2016. [Online].
     Available:
     https://schneider-electric.app.box.com/files/0/f/8792715681/1/f_53362615213.
     [Accessed 15th September 2016].
     
    
    
     
     [4] 
     
     
     ASTIER,
     Remy, "ECP_ECP Development Board _User Guides_Global Overview_N
     1," Schneider Electric, 14 03 2016. [Online]. Available:
     https://schneider-electric.app.box.com/files/0/f/6555163905/1/f_53362552721.
     [Accessed 15th September 2016].
     
    
    
     
     [5] 
     
     
     “Embedded Firmware
     Factory/Wiki/Eff.git_client_installation_with_ssh_configuration/View Wiki
     Page,” Schneider Electric, [Online]. Available:
     https://teamforge.schneider-electric.com/sf/wiki/do/viewPage/projects.esf/wiki/Eff.git_client_installation_with_ssh_configuration.
     [Accessed 15th September 2016].
     
    
    
     
     [6] 
     
     
     “Embedded Firmware
     Factory/Wiki/Eff.google_repo_installation/View Wiki Page,” Schneider
     Electric, [Online]. Available:
     https://teamforge.schneider-electric.com/sf/wiki/do/viewPage/projects.esf/wiki/Eff.google_repo_installation.
     [Accessed 15th September 2016].
     
    
    
     
     [7] 
     
     
     COLIN,
     Tangi; Goodger, Nikolaj, "ECP_ECP Development Board_User
     Guides_Bootloader Guide (Boot4ECP)_N 3," Schneider Electric, 18 92
     2016. [Online]. Available: https://schneider-electric.app.box.com/files/0/f/8792716957/1/f_53362592509.
     [Accessed 15th September 2016].
     
    
    
     
     [8] 
     
     
     Sebastien
     Banon, Jean-Christophe Gillet, Nikolaj Goodger, "ECP Development
     Board_LCES SNARc_User Guides_Bootloader Guide N°3_v0.6.docx," 25th
     May 2016. [Online]. Available:
     https://schneider-electric.app.box.com/files/0/f/8792719345/1/f_72259562397.
     [Accessed 12th October 2016].
     
    
    
     
     [9] 
     
     
     Altera
     SoC EDS Lite, Altera, [Online]. Available:
     https://www.altera.com/products/design-software/embedded-software-developers/soc-eds/getting-started.html.
     [Accessed 5th September 2016].
     
    
    
     
     [10] 
     
     
     Altera,
     "Quartus Prime Lite," Altera, [Online]. Available:
     https://www.altera.com/products/design-software/fpga-design/quartus-prime/download.html.
     [Accessed 5th September 2016].
     
    
    
     
     [11] 
     
     
     "PuTTY
     Download Page," [Online]. Available:
     http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html. [Accessed
     28th September 2016].
     
    
    
     
     [12] 
     [13]
     
     
     t. G.
     Developers, "the GNU Project Debugger," 2016. [Online].
     Available: https://www.gnu.org/software/gdb/download/. [Accessed 7th
     October 2016].
     "Install Klocwork client"
     [Online]. Available: http://rd-luge.eur.gad.schneider-electric.com:8080/redmine/projects/klocwork/wiki/Install_Klocwork_client
     . [Accessed 18th October 2016].
     
    
   
    
    
  

14  APPENDIX 1 – List of NMC Clearances to be requested

 

<TBD>




 

15  APPENDIX 2 – Eclipse IDE debug configuration

15.1   Debug
vs. Release build configurations

In order to
be able to debug an application, one will be required to create a Debug build
configuration. 

Steps:

Right
click on ‘lces2_sample_project’ and (as depicted on) choose Build
configurations à Manage
 


Figure 16 - Eclipse IDE -Manage
build configurations

In the pop-up window, depicted
on , click  ‘New’ button:
 


Figure 17 - Eclipse IDE - New build
configuration

In the New-configuration pop-up
window please specify the Name, provide description and copy settings from the
existing ‘cortex-7a-cross-compile’ build configuration. The sample set-up
has been depicted on Figure 18 - Eclipse IDE - New build configuration.
 




Figure
18 -
Eclipse IDE - New build configuration

After clicking ‘OK’button
the new config should be listed as illustrated on Figure 19 - Newly created Debug configuration
 


Figure
19 -
Newly created Debug configuration

Now set the
‘cortex-7a-cross-compile-Debug’ build configuration as ‘Active’ one (see Figure 20 - Eclipse IDE - Setting active build configuration)
 


Figure
20 -
Eclipse IDE - Setting active build configuration

6.     Right click on ‘lces2_sample project’ and
chose ‘Properties’ (see ).

7.     As presented on Figure 21 - Eclipse IDE - Disable , in Project
properties à Settings à Cross GCC Compiler à
Optimization disable optimization.
 


Figure
21 -
Eclipse IDE - Disable optimization

Having the cross-compiler’s optimization
enabled (especially in its higher levels e.g. -O3 or -O4, stepping through the
code may, in certain cases, be impacted.

In Project properties à Settings à Cross GCC Compiler à Debugging switch the Debug Level to ‘–g3’ (see Figure 22 - Eclipse IDE - Debug Level ).
 


Figure
22 -
Eclipse IDE - Debug Level

In Project properties à Settings à Cross GCC Linker à General
de-select omitting symbol information (-s) as illustrated on Figure 23 - Eclipse IDE -
Stripping from symbols
 


Figure
23 -
Eclipse IDE - Stripping from symbols

Please note that with the linker’s ‘–s ‘
one will be able to, at best, step through the dis-assmbly code,
whereas the debuggin ‘-g’ option provides information for
both: gdbserver and gdb.

It is recommended that the Release flavour
of the build configuration would have:

 the Debug Level disabled (‘-g’ option un-set)the symbols stripped (option ‘–s’
selected)optimization set to at least ‘–O2’
level with either size or performance chosen a priority





15.2Configuring remote debug

The VM’s image
of version 0.4 includes the pre-configured debug configuration along with the
required GDB server and client. This section outlines the steps necessary to
reproduce the pre-configured VM’s environment from section 1.5.

 

1.    
 

2.    
 

3.    
 

4.    
 

5.    
 

6.    
 

7.    
 

8.    
 

9.    
 

10.    
 

11.    
 

12.    
 

12.1.    
 

12.2.    
 

15.2.1     Cross compiling and installing the GDB Server for the ‘arm-poky-linux-gnueabi’
(cortex-7A) host

a)        Fetch the source-code of gdb. The
recommended version is 7.11.1 from here.

b)        Un-tar
the archive into ‘/home/src/gdb-7.11.server’ directory, i.e.:

mkdir –p
/home/src

tar –xzf
./gdb-7.11.tar.gz –C /home/src

mv /home/src/gdb-7.11 /home/src/gdb-7.11.server

In a clean terminal session:sudo cd /home/src/gdb-7.11.serverchmod –R 777 .sudo mv /home/src/gdb-7.11 /home/src/gdb-7.11.server Configure the
build for the cortex-7A host by running following Bourne-shell script:#!/bin/shexport CC=arm-poky-linux-gnueabi-gcc export PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbinexport CFLAGS=-march\=armv7-a\
-marm\ -mthumb-interwork\ -mfloat-abi\=hard\
-mtune\=cortex-a7\ --sysroot\=/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabi./configure --host=arm-poky-linux-gnueabi --prefix=/home/nfsroot/ Cross-compile
the source code according to the above configuration:#!/bin/shexport CC=arm-poky-linux-gnueabi-gcc export PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbinexport CFLAGS=-march\=armv7-a\
-marm\ -mthumb-interwork\ -mfloat-abi\=hard\
-mtune\=cortex-a7\ --sysroot\=/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabimakeInstall the
GDB Server:#!/bin/shexport CC=arm-poky-linux-gnueabi-gcc export PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbinexport CFLAGS=-march\=armv7-a\
-marm\ -mthumb-interwork\ -mfloat-abi\=hard\
-mtune\=cortex-a7\ --sysroot\=/opt/poky/2.0.2/sysroots/cortexa7hf-vfp-vfpv4-d16-poky-linux-gnueabimake install

















































15.2.2      Compiling and installing native GNU Debugger

Un-tar
the GDB source code fetched in the 12.2.1 a) to the ‘/home/src/gdb-7.11.client’ directory
i.e.:mkdir –p /home/src/tar –xzf ./gdb-7.11.tar.gz –C /home/src/mv /home/src/gdb-7.11 /home/src/gdb-7.11.clientcd /home/src/gdb-7.11.clientOpen
a clean terminal sessionConfigure
the build GNU system, e.g.:#!/bin/shexport PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbin./configure --target=arm-poky-linux-gnueabi --prefix=/opt/native_x86_64/Build the GNU
Debugger, e.g.:#!/bin/shexport PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbinmakeInstall the
GNU Debugger, e.g.:#!/bin/shexport PATH=/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/../x86_64-pokysdk-linux/bin:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-uclibc:/opt/poky/2.0.2/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-musl:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/pkg/bin:/usr/pkg/sbinmake install



































15.2.3    
Configuring
a Remote Debug Session in Eclipse IDE

1.     Right click on ‘lces2_sample_project’ choose ‘Debug
Asà Debug Configurations’ as
seen on Figure 6 - Eclipse IDE - Debug configurations.

2.     
In ‘Debug configurations’ select ‘C/C++ Remote Application’ (see Figure 24 -
Eclipse IDE - C/C++ Remote Application)
 


Figure
24 -
Eclipse IDE - C/C++ Remote Application

3.It will ask one to point out which
application to debug (as depicted on Figure
25 - Eclipse IDE - Choosing project
application to debug). Select the lces2_sample_project.


 


Figure
25 -
Eclipse IDE - Choosing project application to debug

4             In
‘Debug
Configurations à C/C++ Remote Application à
lces2_sample_project cortex7a-cross-compile-Debug à Main’ set (as illustrated on Figure 26 - Eclipse IDE - Debug configurations - Main):

‘C/C++ Application’ tocortex-7a-cross-compile-Debug/lces2_sample_project‘Project’ to lces2_sample_project




 


Figure
26 -
Eclipse IDE - Debug configurations - Main

5.     In
‘Debug Configurations à C/C++ Remote Application à
lces2_sample_project cortex7a-cross-compile-Debug à
Debugger’, as depicted onFigure
27 - Eclipse IDE - Debug Configurations  , point out the
native x86_64 debugger built for arm-poky-linux gnueabi target built and
installed as per section 12.2.2        Compiling and installing native GNU Debugger.
 


Figure
27 -
Eclipse IDE - Debug Configurations Debugger

6                In
‘Debug Configurations à C/C++ Remote Application à lces2_sample_project
cortex7a-cross-compile-Debug à Source’ point to the source-code of our ‘lces2_sample_project’ (see Figure 28
- Eclipse IDE - Debug configurations - Source Selection)


 


Figure
28 -
Eclipse IDE - Debug configurations - Source Selection




 

 

16   
 ANNEX 2 – Removing
Unity and switching to Gnome

 

Some people prefer to use the gnome desktop
rather than the default Unity one that come as default on Ubuntu. To do this
type in the terminal window:

sudo apt-get
update

sudo apt-get
install gnome-session-fallback

 

When the system has finished installing the
packages, log-out and select the gnome symbol beside your logon name i.e.:


 
 

 

Select the windowing system you want to use
and login i.e.:

 


 


 

 

