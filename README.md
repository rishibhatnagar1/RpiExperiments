# RpiExperiments

Before starting with anything, I have installed the OS from RasPi website.
Connected LAN cable to the Pi and connected it to my router.

Oh and your Rpi is not running until your see ACT,PWR,FDK,LNK and 100 LEDS all blinking. I used a crappy cable to power it up and did not see them. Just changing the cable in my case solved the problem. In your case it could be because of some error in the SD card. You can google how to troubleshoot that. Also, do not power on Pi without an SD card in it, you could burn it (Apparently). I am not going to try to verify that one (Duh-uh!).

Now this part is important. I use Ubuntu 14.04 fulltime at home and Mac OSx at work.So I have access to a kickass terminal one command away. But if you are still using a windows system, first of all don't, switch to Linux, you are going to love it. Eitherways, on Windows system, you will have to use Putty or something similar to get into your RasPi.

On Linux/Mac, you will have to log in to RasPi using SSH (its a cool cryptographic protocol). Now if you have installed any of the OSes from 
RaPi website, you will have a username:Pi and Password: raspberry (this could be different.Do look in the documentation of your OS file). Hence, 
you cannot use:

ssh root@IPaddressofPi

if you use this, you will be prompted for a password, which you won't know since you are not root.
You will have to use:

ssh username@IPaddressofPi

If your username is not Pi, use the username that has been given by the OS in place of Pi.

IP address of Pi can be found out using 'ifconfig'. Or going to the router page through your browser and checking the client list there.
Please change your password using 'passwd' command inside the Pi.

Since I wanted to work with Node, I did the following :
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install nodejs npm 

This blog is good: https://www.npmjs.com/package/raspberry

Next I wanted to install a few python modules. Requests specifically. There are two ways of installing requests. 
First way is to do a 'pip install requests' in your terminal. In my case pip was not installed. Pip is the python package manager.

'sudo apt-get install python-pip' will install pip in your Pi.

Next 'pip install requests' did it for me.

Other way of installing any python packages is to build it from source.There is a small hack to get around package manager not available problems. This was the same case with Yun and Intel Edison I am working with. So here is how you do it.
1.wget https://github.com/kennethreitz/requests/tarball/master  -- This is going to download the .tar.gz file.
2.tar -xzf nameofthefolder>
3.cd folder
4. python setup.py install 
and Viola, you are done!

######### Connect Rpi to your laptop/Mac directly with Ethernet Cable and login using SSH 

For this particular case, when you want to log in to Rpi through SSH from your system itslef, without connecting Rpi to the modem, do the following:
1. Without connecting your Rpi, go to network settings and find out the ethernet connection DHCP address, in my case it was of the form 169.145.X.230. Now plug in the Rpi bootable SD card into the SD card slot.
You will find a file there called cmdline.txt  . Open the file and in the same line add the "ip: 169.145.X.210" , remember, you have to add it in the same line without the quotes. X has to be in the same subnet as the network setting you saw before. The 210 can be any number between 0 to 255. Remember this ip address because you will be using this to login to the pi now.
2. login to pi:
	ssh pi@169.145.X.210 
	--You will see a question on RSA, press 'yes'
	password : -- entry raspberry and you should be in, for furthur details on the same you can look at this blog: https://pihw.wordpress.com/guides/direct-network-connection/
	


#All the programs that use GPIOs will require you to run as sudo.


