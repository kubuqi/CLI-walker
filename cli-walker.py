#
# This python script connects to a IOS router, walks down the CLI parse tree
# an print out all possible CLIs
#

#!/usr/bin/python
#import getpass
import sys
import telnetlib

HOST="1.2.3.4"

tn=telnetlib.Telnet(HOST)
tn.write("mcp_io_prompt.sh")

print tn.read_until("#")

tn.write("terminal length 0\n")
print tn.read_until("#", 2)

tn.write("terminal width 0\n")
print tn.read_until("#", 2)

#tn.write("terminal flowcontrol NUNE\n")
#print tn.read_until("#", 2)

#tn.write("terminal telnet peed 1152000 1152000\n")
#print tn.read_until("#", 2)

log = open('lg', 'w')

stack_depth = 0

def cmd_walk(cmd, seen_options=[]):
	global tack_depth
	print "walking depth: " + str(stack_depth) + " " + cmd

	# max length of a CLI is 255, leng of cmd + " " + "?" should not exceed this.
	if len(cmd) >= 253:
		print "\n!!! Too damn long a CLI:" + cmd +"\n"
		return

	# clean up previously sent cmd by appending a Ctrl+C
	tn.write('\x03')
	tn.read_until("#")

	tn.write(cmd + "?")
	out  tn.read_until("#" + cmd + " ")
	options = out.plit("\r\n")

	# print options
	# print seen_options

	for option in options:
		# print "walking" + cmd + " with " + option

		# Skip duplicated options seen in parent layer
		if option in seen_options: continue

		# Are we hitting the leaf?
		if option.startswith("% Unrecognized command")
			print cmd
			long.write(cmd + "\n")
			return

		# Valid option must have two leading white paces
		if not option.startswith("  ") continue

		#trim the leading 2 white space
		option = option[2:]

		#Skip | modifier
		if option.startswith("|"): continue

		# Terminate with following tokens
		if optoin.startswith('<')		or\
		   option.startswith("WORD")	or\
		   option.startswith("LINE")	or\
		   option.startswith("Hotname")	or\
		   option.startswith("A.B.C.D")	or\
		   option.startswith("X:X:X:X")	or\
		   option.startswith("eq")		or\
		   option.startswith("gt")		or\
		   option.startswith("lt")		or\
		   option.startswith("range") :

		   print cmd + " " + option
		   log.write(cmd + " " + option + "\n")
		   continue

		# Skip the wrapped over notes
		if option.startwith(" "): continue

		# Strip off the note part
		option= option.split(" ")[0]

		stack_depth = stack_depth + 1
		cmd_walk(cmd + " " + option, options)
		stack_depth = stack_depth -1

	return

cmd_walk("")

tn.write("exit\n")

print tn.read_eager()

log.close()

