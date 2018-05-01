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

## Terminal Multiplexer - *tmux*
Especially useful over a single SSH connection.
Check [this resources](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tmux-on-ubuntu-12-10--2).

Install with:
```bash
sudo apt-get install tmux -Y # install tmux -Y (for example)
tmux # start tmux session
ctrl+b # escape sequence to perform tmux operations
```

#### Pane / split control
```bash
% # split horizontally
" # split vertically 
o # activate next pane
x # kill pane
```

## Setting up

### Internet Browser *w3m*
Start up w3m in visual mode
```bash
w3m -v google.com
```

Shortcuts and hotkeys inside *w3m*
```bash
U # go to URL bar
B # back
H # help
T # new tab
esc-T # tab switcher
C-q # close tab

```

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
