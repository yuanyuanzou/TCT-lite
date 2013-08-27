#!/usr/bin/python
#
# Copyright (C) 2012 Intel Corporation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
#
# Authors:
#           Liu,chengtao <chengtaox.liu@intel.com>

""" The implementation of local host communication"""

import os
import time
import socket
import re
from shutil import copyfile

from commodule.log import LOGGER
from commodule.autoexec import shell_command, shell_command_ext


HOST_NS = "127.0.0.1"
APP_QUERY_STR = "ps aux | grep %s | grep -v grep"


class LocalHost:

    """ Implementation for transfer data
        between Host and Tizen PC
    """

    def __init__(self):
        self.deviceid = "localhost"

    def shell_cmd(self, cmd="", timeout=15):
        return shell_command(cmd, timeout)

    def check_process(self, process_name):
        exit_code, ret = shell_command(APP_QUERY_STR % process_name)
        return len(ret)

    def check_widget_process(self, wgt_name):
        return True

    def shell_cmd_ext(self,
                      cmd="",
                      timeout=None,
                      boutput=False,
                      stdout_file=None,
                      stderr_file=None):
        return shell_command_ext(cmd, timeout, boutput, stdout_file, stderr_file)

    def get_device_ids(self):
        """
            get deivce list of ids
        """
        return ['localhost']

    def get_device_info(self):
        """
            get tizen deivce inforamtion
        """
        device_info = {}
        device_info["device_id"] = self.deviceid
        device_info["resolution"] = "N/A"
        device_info["screen_size"] = "N/A"
        device_info["device_model"] = "N/A"
        device_info["device_name"] = "N/A"
        device_info["os_version"] = "N/A"
        device_info["build_id"] = "N/A"
        return device_info

    def get_server_url(self, remote_port="8000"):
        """get server url"""
        url_forward = "http://%s:%s" % (HOST_NS, remote_port)
        return url_forward

    def install_package(self, pkgpath):
        """
           install a package on tizen device
        """
        cmd = "rpm -ivh %s" % pkgpath
        exit_code, ret = shell_command(cmd)
        return ret

    def get_installed_package(self):
        """get list of installed package from device"""
        cmd = "rpm -qa | grep tct"
        exit_code, ret = shell_command(cmd)
        return ret

    def download_file(self, remote_path, local_path):
        """download file"""
        copyfile(remote_path, local_path)
        return True

    def upload_file(self, remote_path, local_path):
        """upload file"""
        copyfile(local_path, remote_path)
        return True

    def get_launcher_opt(self, test_launcher, test_suite, test_set, fuzzy_match, auto_iu):
        """get test option dict """
        test_opt = {}
        test_opt["suite_name"] = test_suite
        test_opt["launcher"] = test_launcher
        test_opt["suite_id"] = test_suite
        return test_opt


def get_target_conn():
    """ Get connection for Test Target"""
    return LocalHost()
