# .bashrc

# Apply the completion function to the edit-in-kitty command

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
	PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi
unset rc

#Add script folder to path
export PATH="/home/angel/scripts:$PATH"
export EDITOR="/usr/bin/nvim"

eval "$(oh-my-posh init bash --config /home/angel/.config/ohmyposh/theme.json)"

alias ssh="kitty +kitten ssh"
alias rssh="ssh"

alias rssh="/usr/bin/ssh"

alias kvim="kitten edit-in-kitten"

alias nvim="sudo -e vim"
