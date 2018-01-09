#update system
sudo yum -y update && upgrade

#install git python and devtools
sudo yum -y install git-all centos-relese-SCL python-setuptools python-setuptools-devel python-devel
sudo yum -y groupinstall "Development Tools"

sudo easy_install pip

git clone https://github.com/SSilvering/SCE-2018-Elections
cd SCE-2018-Elections

sudo pip install -r requirements.txt

sudo yum install git-all -y
sudo yum install wget -y

python db_create.py

sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000

nohup python run.py > ../log.txt 2>&1 </dev/null &
echo ok