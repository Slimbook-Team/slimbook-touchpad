import os
from os.path import expanduser
if (os.path.isfile("/usr/share/man/man4/libinput.4.gz") or os.path.isfile("/usr/share/man/man4/libinput.5.gz")):
	os.system("python /usr/share/slimbooktouchpad/preferences2")
else:
	os.system("python /usr/share/slimbooktouchpad/preferences")
