set -g -x fish_greeting ''


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/presdec/anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# some conda aliases
alias tkinter='conda activate tkinter'
alias py37='conda activate py37'
alias base='conda activate base'

neofetch

alias penv='conda info --envs'

thefuck --alias | source

alias gg='cd /home/presdec/github/practice'
alias color='python /home/presdec/github/practice/Tkinter\ Tutorial/color.py'
