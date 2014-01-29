################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
#      Copyright (C) 2013 Lutz Fiebach (lufie@openelec.tv)
#
#  This program is dual-licensed; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC; see the file COPYING.  If not, see
#  <http://www.gnu.org/licenses/>.
#
#  Alternatively, you can license this library under a commercial license,
#  please contact OpenELEC Licensing for more information.
#
#  For more information contact:
#  OpenELEC Licensing  <license@openelec.tv>  http://www.openelec.tv
################################################################################
# -*- coding: utf-8 -*-
import os

################################################################################
# Base 
################################################################################
XBMC_USER_HOME = os.environ.get("XBMC_USER_HOME", "/root/.xbmc")
CONFIG_CACHE = os.environ.get("CONFIG_CACHE", "/root/.cache")
USER_CONFIG = os.environ.get("USER_CONFIG", "/root/.config")

################################################################################
# Connman Module
################################################################################
connman = \
    {
        "CONNMAN_DAEMON"  : "/usr/sbin/connmand",
        "WAIT_CONF_FILE"  : "%s/amlinux/network_wait" % CONFIG_CACHE,
        "VPN_PLUGINS_DIR" : "/usr/lib/connman/plugins-vpn",
        "VPN_CONF_DIR"    : "%s/vpn-config/" % USER_CONFIG,
        "ENABLED"         : lambda:(True if os.path.exists(connman["CONNMAN_DAEMON"]) else False),
    }

################################################################################
# Bluez Module
################################################################################
bluetooth = \
    {
        "BLUETOOTH_DAEMON" : "/usr/sbin/bluetoothd",
        "OBEX_DAEMON"      : "/usr/lib/bluetooth/obexd",
        "ENABLED"          : lambda:(True if os.path.exists(connman["BLUETOOTH_DAEMON"]) else False),
      #DEFAULT_VALUES
        "D_OBEXD_ROOT"     : "/root/.xbmc/downloads/"
    }

################################################################################
# Service Module
################################################################################    
services = \
    {
        "ENABLED"       : True,
                
      #SAMBA
        "KERNEL_CMD"            : "/proc/cmdline",
        "SAMBA_NMDB"            : "/usr/sbin/nmbd",
        "SAMBA_SMDB"            : "/usr/sbin/smbd",
      #DEFAULT_VALUES 
        "D_SAMBA_SECURE"        : "0",
        "D_SAMBA_USERNAME"      : "amlinux",
        "D_SAMBA_PASSWORD"      : "amlinux",
        "D_SAMBA_AUTOSHARE"     : "1",
    
      #SSH
        "SSH_DAEMON"            : "/usr/sbin/sshd",
        "OPT_SSH_NOPASSWD"      : "-o 'PasswordAuthentication no'",
      #DEFAULT_VALUES
        "D_SSH_DISABLE_PW_AUTH" : "0",
    
      #AVAHI
        "AVAHI_DAEMON"          : "/usr/sbin/avahi-daemon",
        
      #CRON
        "CRON_DAEMON"           : "/usr/sbin/crond",
        
      #LCD
        "LCD_DRIVER_DIR"        : "/usr/lib/lcdproc/",        
        
    }
    
system = \
    {
        "ENABLED"             : True,
        "KERNEL_CMD"          : "/proc/cmdline",
        
      #CLOCK
        "SET_CLOCK_CMD"       : "/sbin/hwclock --systohc --utc",

      #UPDATE
        "UPDATE_REQUEST_URL"  : "http://update.amlinux.tv/updates.php",
        "UPDATE_DOWNLOAD_URL" : "http://%s.amlinux.tv/%s",
        "LOCAL_UPDATE_DIR"    : "/root/.update/",
        "GET_CPU_FLAG"        : "cat /proc/cpuinfo | grep -q 'flags.* lm ' && echo '1' || echo '0'",
        
      #RESET
        "XBMC_RESET_FILE"     : "%s/reset_xbmc" % CONFIG_CACHE,
        "AMLINUX_RESET_FILE"  : "%s/reset_amlinux" % CONFIG_CACHE,

      #KEYBOARD
        "KEYBOARD_INFO"       : "/usr/share/X11/xkb/rules/base.xml",
        "UDEV_KEYBOARD_INFO"  : "%s/xkb/layout" % CONFIG_CACHE,
        "RPI_KEYBOARD_INFO"   : "/usr/lib/keymaps",
            
      #BACKUP / RESTORE
        "BACKUP_DIRS"         : [XBMC_USER_HOME, USER_CONFIG, CONFIG_CACHE],
        "BACKUP_DESTINATION"  : "/root/backup/",
        "RESTORE_DIR"         : "/root/.restore/",
    }
    
about = \
    {
        "ENABLED" : True
    }    
    
xdbus = \
    {
        "ENABLED" : True
    }

_services = \
    {
        "sshd"   : ["sshd.service"],
        "avahi"  : ["avahi-daemon.service"],
        "samba"  : ["nmbd.service", "smbd.service"],
        "bluez"  : ["bluetooth.service"],
        "obexd"  : ["obex.service"],
        "crond"  : ["cron.service"],
    }
