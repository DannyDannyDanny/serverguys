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

<!--
>6. Make python environment `virtualenv envname`
>7. Install module dependencies `envname/bin/pip install firebase-admin`
 -->

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
