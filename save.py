from CLI import CLI
import sys
import re
import subprocess

CLI("copy running-config flash://last-config\nyes")
CLI("unhide foscmd\nfibranne")
CLI("unhide foscmd\nfibranne\nfoscmd bash -c \'cp /var/config/vcs/scripts/last-config /var/config/vcs/scripts/defaultconfig.novcs\'")
CLI("unhide foscmd\nfibranne\nfoscmd bash -c \'cp /var/config/vcs/scripts/last-config /var/config/vcs/scripts/defaultconfig.vcs\'")
