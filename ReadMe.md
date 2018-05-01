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
## Python & pipenv
```bash
# installing pipenv
There som guide which starts with something like...
```bash
sudo apt install software-properties-common python-software-properties
```
...yeah google that to install properly

## Terminal Multiplexer - tmux
Especially useful over a single SSH connection.
Check [this resources](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tmux-on-ubuntu-12-10--2).

Install with:
```
sudo apt-get install tmux -Y # installing tmux (for example)
tmux # start tmux
C-b # tmux escape sequence
% # verical split
" # horizontal split
o # swap pane
x # kill pane
```

## Setting up

### Github setup
>Desperately needs a shortguide. I'm so trash at git. The biggest change I did to this guide got ranched because of git. I'm so mad rn.

For the serverguy follow the [Github Setup Guide](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

### Time Capsule

```
sudo apt-get install cifs-utils
```

## Torrenting
If in doubt, see [ubuntu community article](https://help.ubuntu.com/community/TransmissionHowTo)
#### Install transmission
```
sudo apt-get install transmission-cli transmission-common transmission-daemon
```
#### See torrents in actions
```
transmission-remote -n 'transmission:transmission' -l
```

```
sudo transmission-cli "magnet:?XXX"
```



## Further info

hmu on [Telegram](http://t.me/DannyDannyDanny)
