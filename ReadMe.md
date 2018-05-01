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

## Terminal Multiplexer - tmux
Especially useful over a single SSH connection.
Check [this resources](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tmux-on-ubuntu-12-10--2).

Install with:
```bash
sudo apt-get install tmux -Y
```
#### Session control
```bash
# start session
tmux
```
```bash
# split session horizontally
ctrl + b , %
```
```bash
# next session
ctrl + b , o
```
```bash
# split session horizontally
ctrl + b , "
```

## Setting up

### Github setup
For the serverguy follow the [Github Setup Guide](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

### Time Capsule

Not sure how this works yet
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

## Misck
Making alias shorcuts for bash
```bash
alias ic='cd ~/Library/Mobile\ Documents/com~apple~CloudDocs' # alias to mac icloud folder
```

## Further info

hmu on [Telegram](http://t.me/DannyDannyDanny)
