#!/usr/bin/env python3

import subprocess


def install_nginx():
    subprocess.Popen(['pwd'])

    subprocess.run(['wget', 'https://nginx.org/keys/nginx_signing.key'])
    subprocess.run(['apt-key', 'add', 'nginx_signing.key'])

    with open('/etc/hosts', 'a') as f:
        f.write('deb http://nginx.org/packages/ubuntu/ codename nginx')
        f.write('deb-src http://nginx.org/packages/ubuntu/ codename nginx')

    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'install', 'nginx', '-y'])


install_nginx()
