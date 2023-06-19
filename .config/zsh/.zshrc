

# Run X11 in tty1
[ "$(tty)" = "/dev/tty1"  ] && ! pgrep -x Xorg >/dev/null && exec startx --nocursor vt1 &> /dev/null

# Apperance
autoload -U colors && colors
PS1=" %B%F{8}%~%f%b "
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null

# History setting
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

# lf
lf () {
	LF_TEMPDIR="$(mktemp -d -t lf-tempdir-XXXXXX)"
	LF_TEMPDIR="$LF_TEMPDIR" lf-run -last-dir-path="$LF_TEMPDIR/lastdir" "$@"
	if [ "$(cat "$LF_TEMPDIR/cdtolastdir" 2>/dev/null)" = "1" ]; then
		cd "$(cat "$LF_TEMPDIR/lastdir")"
	fi
	rm -r "$LF_TEMPDIR"
	unset LF_TEMPDIR
}

# Alias 
alias sudo='doas'
alias ls='ls --sort=time --color=auto --reverse'
alias la='ls --sort=time --color=auto -a --reverse'
alias ll='ls --sort=time --color=auto -l -a -h --reverse'
alias grep='grep --color=auto'
alias ..='cd ..'
alias v='nvim'
alias open='xdg-open'
alias pac='doas pacman'
alias install='doas xbps-install'
alias query='doas xbps-query'
alias remove='doas xbps-remove'

# Vim mode
bindkey -v
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd  ]] || [[ $1 = 'block'  ]]
	then
	  echo -ne '\e[1 q'
	elif [[ ${KEYMAP} == main  ]] || [[ ${KEYMAP} == viins  ]] || [[ ${KEYMAP} = ''  ]] || [[ $1 = 'beam'  ]]
	then
		 echo -ne '\e[5 q'
	fi
}
zle -N zle-keymap-select
zle-line-init() {
	zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
	echo -ne "\e[5 q"
}
zle -N zle-line-init
echo -ne '\e[5 q' # Use beam shape cursor on startup.
preexec() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.
