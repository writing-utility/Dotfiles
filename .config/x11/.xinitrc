#!/bin/sh

[ -f ~/.xprofile ] && . ~/.xprofile
[ -f ~/.config/autostart ] && . ~/.config/autostart
exec dwm
