#! /bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
clear
echo "#############################################################"
echo "# Install Shadowsocks(Python) for CentOS5.x (32bit/64bit) or CentOS6.x (32bit/64bit)"
echo "#"
echo "# Author: Teddysun <i@teddysun.com>"
echo "#"
echo "#############################################################"
echo ""

# Get IP address
IP=`ifconfig | grep 'inet addr:'| grep -v '127.0.0.*' | cut -d: -f2 | awk '{ print $1}'`;

# Install Shadowsocks
function install_shadowsocks(){
    rootness
    disable_selinux
    pre_install
    download_files
    config_shadowsocks
    iptables_set
    install
}

# Make sure only root can run our script
function rootness(){
if [[ $EUID -ne 0 ]]; then
   echo "Error:This script must be run as root!" 1>&2
   exit 1
fi
}

# Disable selinux
function disable_selinux(){
if [ -s /etc/selinux/config ] && grep 'SELINUX=enforcing' /etc/selinux/config; then
    sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
    setenforce 0
fi
}

# Pre-installation settings
function pre_install(){
    #Set shadowsocks config password
    echo "Please input password for shadowsocks:"
    read -p "(Default password: teddysun.com):" shadowsockspwd
    if [ "$shadowsockspwd" = "" ]; then
        shadowsockspwd="teddysun.com"
    fi
    echo "password:$shadowsockspwd"
    echo "####################################"
    get_char(){
        SAVEDSTTY=`stty -g`
        stty -echo
        stty cbreak
        dd if=/dev/tty bs=1 count=1 2> /dev/null
        stty -raw
        stty echo
        stty $SAVEDSTTY
    }
    echo ""
    echo "Press any key to start...or Press Ctrl+C to cancel"
    char=`get_char`
}

# Download files
function download_files(){
    if [ -s ez_setup.py ]; then
        echo "ez_setup.py [found]"
    else
        echo "ez_setup.py not found!!!download now......"
        if ! wget --no-check-certificate https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py;then
            echo "Failed to download ez_setup.py!"
            exit 1
        fi
    fi
}

# Config shadowsocks
function config_shadowsocks(){
    touch /etc/config.json
    cat >>/etc/config.json<<-EOF
{
    "server":"${IP}",
    "server_port":8989,
    "local_port":1080,
    "password":"${shadowsockspwd}",
    "timeout":600,
    "method":"aes-256-cfb"
}
EOF
}

# iptables set
function iptables_set(){
    /sbin/service iptables status 1>/dev/null 2>&1
    if [ $? -eq 0 ]; then
        /sbin/iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 8989 -j ACCEPT
        /etc/rc.d/init.d/iptables save
        /etc/init.d/iptables restart
    fi
}


# Install 
function install(){
    yum install -y wget openssl-devel gcc swig python python-devel python-setuptools autoconf libtool libevent
    yum install -y automake make curl curl-devel zlib-devel openssl-devel perl perl-devel cpio expat-devel gettext-devel
    python ez_setup.py install
    easy_install pip
    pip install shadowsocks
    pip install M2Crypto
    pip install greenlet
    pip install gevent
    nohup ssserver -c /etc/config.json > /dev/null 2>&1 &
    clear
    echo ""
    echo "Congratulations, shadowsocks install completed!"
    echo -e "Your Server IP: 33[41;37m ${IP} 33[0m"
    echo -e "Your Server Port: 33[41;37m 8989 33[0m"
    echo -e "Your Password: 33[41;37m ${shadowsockspwd} 33[0m"
    echo -e "Your Proxy Port: 33[41;37m 1080 33[0m"
    echo ""
    echo ""
    echo "Welcome to visit:http://teddysun.com/342.html"
    echo "Enjoy it! ^_^"
    echo ""
    echo ""
}

# Uninstall Shadowsocks
function uninstall_shadowsocks(){
    killall ssserver
    pip uninstall shadowsocks
}

# Initialization step
action=$1
[  -z $1 ] && action=install
case "$action" in
install)
    install_shadowsocks
    ;;
uninstall)
    uninstall_shadowsocks
    ;;
*)
    echo "Usage: `basename $0` {install|uninstall)}"
    ;;
esac