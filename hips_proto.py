#!/usr/bin/python

# HIPSproto - Completely unnecessary and overkill use of a combination
# of GnuPG and steganography. This script creates an imgur link to an 
# image that has a PGP encypted password to another image that has been
# embedded as well. Within the embedded image is a message or small file.
#		+----------------------------+
#		|   Imgur-Posted Steg Image  |
#		| +------------------------+ |
#		| |                        | |
#		| |   Password-Protected   | |
#		| |   Embedded Steg Image  | |
#		| | +--------------------+ | |
#		| | |  Super Secret Data | | |
#		| | +--------------------+ | |
#		| +------------------------+ |
#		| +------------------------+ |
#		| | PGP Encrypted Password | |
#		| |   for Embedded Image   | |
#		| +------------------------+ |
#		+----------------------------+
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# 
# Author: DW3B, DnA Labs
# Email: dweb@dw3b.io 
# Version 0.1
# Date: 08-28-2015

import gnupg, subprocess
from settings import settings as SETTINGS

def main():
	example = "Examples: \n\n./hips_proto.py -e -s 'DW3B' -r 'M4g1k5tuff' -ri\n./hips_proto.py -d test_image.jpg"
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="HIPS Proto - Hidden In Plain Sight", epilog=example)
	required = parser.add_argument_group("Default")
	required.add_argument('-e', '--encrypt', help='Encrypt a new file/message')
	required.add_argument('-d', '--decrypt', help='Decrypt a file/message')
	required.add_argument('-s', '--sender', help='Sender username (you)')
	required.add_argument('-r', '--sender', help='Recipient username (the other person)')
	custom.add_argument('-ri', '--random-images', help='Choose random images from Imgur')
	custom.add_argument('-fi', '--first-image', help='This image will be the one posted to Imgur')
	custom.add_argument('-si', '--second-image', help='This is the embedded image')
	args = parser.parse_args()
	
	print '\n ' + '-' * 69 + '\n ' + ' HIPS Proto v0.1 by DW3B\n ' + '-' * 69 + '\n '
	
	if args.encrypt and args.decrypt:
		print "Cannot use -e and -d at the same time."
		sys.exit()
		
	
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
