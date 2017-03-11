import commands
import os
status, output = commands.getstatusoutput("sh ping.sh %s"%('cloudgcl'))

output =output.rstrip()
print output
