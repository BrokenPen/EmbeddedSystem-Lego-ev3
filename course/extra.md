## radiopy

An interface for mplayer aimed at listening to streaming radio.
https://pypi.python.org/pypi/radiopy/0.6


#### Install radiopy

https://pypi.python.org/pypi/radiopy/0.6

(the git from SourceForge don't work)

    pip install radiopy

#### Add rthk sources file link into radiopy radio list

    sudo nano /usr/local/lib/python2.7/dist-packages/radiopy/data/radiopy.default

you have to go this way. (/etc/radiopy (global configuration) or to ~/.radiopy (per-user).  don't work for me)

#### add the follow connect in the file

    [rthk radio2]
    home: http://www.rthk.hk/radio/radio2
    stream: http://rthkaudio2-lh.akamaihd.net/i/radio2_1@355865/master.m3u8

##### enter the command (radio.py!!)

    sudo radio.py rthk radio2

##### Error

    robot@ev3dev:~$ sudo radio.py rthk radio2
	Traceback (most recent call last):
	  File "/usr/local/bin/radio.py", line 96, in <module>
		main()
	  File "/usr/local/bin/radio.py", line 91, in main
		player.play(args._station_name, **player_options)
	  File "/usr/local/lib/python2.7/dist-packages/radiopy/__init__.py", line 96, in play
		os.execvp(execargs[0],execargs)
	  File "/usr/lib/python2.7/os.py", line 346, in execvp
		_execvpe(file, args)
	  File "/usr/lib/python2.7/os.py", line 382, in _execvpe
		func(fullname, *argrest)
	OSError: [Errno 2] No such file or directory

##### install mplayer!!

     apt-get install mplayer -y


