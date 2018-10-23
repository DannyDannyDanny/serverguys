# Serverguys

## Purpose

This git repo will be used for maintaining structure between my newly developed computer cluster *serverguys*.

## Structure

I have no idea how the structure will be at the moment, chances are there'll be some folders and stuff...

## General info

Installing and auto-saying yes to everything
```
sudo apt-get install [<package-name> , ...] -Y
```

* Stop transmission from running: `/etc/init.d/transmission-daemon stop`

## To do
* [X] set up `ssh` over LAN
* [X] set up `ssh` over IP
* [x] set up [transmission](Torrenting) over LAN
* [ ] set up Time Capsule connection


## Python & pipenv
```bash
# installing pipenv
There som guide which starts with something like...
```bash
sudo apt install software-properties-common python-software-properties
```
...yeah google that to install properly

## Internet Browser - w3m
```bash
# start
w3m google.com
# stopping
q,y
```

## Setup Python and pipenv

1. New git repository (w Python .gitignore)
2. Clone locally
3. `cd` to into repository
4. Make folder for sensitive data: `mkdir creds`
5. Add creds to .gitignore with: `echo "creds/" >> .gitignore`
6. Make sure `pipenv` is installed: `pip install --user pipenv`
7. Set up python environment with `firebase-admin` module: `pipenv install firebase-admin`
8. Run `pipenv run python /path/file.py` to run python scripts
> you can also `pipenv shell` to start the environment

>outside of shell do `pipenv install ipykernel`
>or within `pipenv shell` do `python3 -m ipykernel install --user`

## Ipykernel in Atom
Setup kernel:
`pipenv install ipykernel`
`pipenv shell`
`python -m ipykernel install --user --name=python-XXXXXX`
`jupyter notebook`


## Terminal Multiplexer - tmux
Especially useful over a single SSH connection.
Check [this resources](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tmux-on-ubuntu-12-10--2).

Install with:

```bash
sudo apt-get install tmux -Y # installing tmux
tmux # start tmux
```

#### tmux commands

```bash
C-b # tmux escape sequence
% # verical split
" # horizontal split
o # swap pane
x # kill pane
```

## UNIX Terminal / Ubuntu Essentials

### File system navigation

```bash
$ pwd # print current (working) directory
$ ls # list files and directories in current directory
$ cd # change directory
$ cp ./myfile.txt ./destination/ # duplicate file(s)
$ rm ./myfile.txt  # delete file(s)
$ mv ./myfile.txt ./destination/ # move file(s)
$ mv ./myfile.txt ./mytext.txt # rename file
$ -> # use tab to autocomplete
```

### SSH
gives remote terminal access to another machine on the LAN

`ssh serverguy@192.168.0.X`

### **SCP**
enables copying files across machines on the LAN. This command will move MyFile from local machine to user folder on serverguy:

  scp /Users/Me/MyFile/ serverguy@192.168.0.X:/home/serverguy
  scp /Users/Me/MyFile/ serverguy@192.168.0.X:/home/serverguy



### Github setup
>Desperately needs a shortguide. I'm so trash at git. The biggest change I did to this guide got ranched because of git. I'm so mad rn.

For the serverguy follow the [Github Setup Guide](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

### Time Capsule

1. Read [afpfs-ng](https://www.omgubuntu.co.uk/2010/11/connecting-to-your-apple-time-capsule-in-ubuntu) and download what they refer to as the ".deb file"
2. Unzip the file and follow instructions in `afpfs-ng-0.8.x/INSTALL`

You made need cifs: `sudo apt-get install cifs-utils`

Make a mount point: `mkdir ~/timecapsule`

Mount to mount point: `mount_afp 'afp://tc_usr:tc_pwd@192.168.0.x/tc_usr' ~/timecapsule`

Unmount: `afp_client unmount ~/timecapsule/`

## Further info
More stuff:
* [cli-ck.io](https://cli-ck.io)

hmu on [Telegram](http://t.me/DannyDannyDanny) ✈️
