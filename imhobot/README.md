`

<h1>Install and Start</h1>
<h2>How to install?</h2>


- Termux

```
pkg update -y && pkg install python3 wget -y && termux-wake-lock && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- APT (Debian based)


```
apt update -y && sudo apt install python3 python3-pip wget -y && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- Astra Linux (if python < 3.7, else go to "Debian based")

```
apt update -y && sudo apt install curl wget -y && sh <(curl -sSL https://raw.githubusercontent.com/FoxUserbot/FoxUserbot/main/HowToGetPython3_8.sh) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- YUM (RHEL based)

```
yum -y update && sudo yum install wget python3 curl -y && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- PACMAN (Arch based)

```
sudo pacman -Sy python3 wget curl && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- EMERGE (Gentoo)
```
sudo emerge python wget net-misc/curl && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 main.py)
```

- MacOS

```
xcode-select --install ; /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python3 && pip3 install --upgrade pip && pip3 install wheel && brew install wget && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm foxub.$$ && cd FoxUserbot-main && python3 main.py)
```




Thank you all!
