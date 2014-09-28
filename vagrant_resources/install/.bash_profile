# bashrc 

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim'
alias grep='grep --color'
alias c='clear'
alias ..='cd ..'
alias tm='ps -ef | grep'
alias lf='ls -Gl | grep ^d'
alias l='ll -Ah'
alias la="ls -a"
alias logs='cd /Applications/MAMP/logs/ ; ls;'
alias alogs='tail -f /Applications/MAMP/logs/apache_access.log'
alias plogs='tail -f /Applications/MAMP/logs/php_error.log'
alias www='cd www'
alias flushdns='dscacheutil -flushcache;sudo killall -HUP mDNSResponder'
alias listdotsvn="find . -name .svn -exec ls {} \;"
alias deletedotsvn="find . -name .svn -exec rm -rf {} \;"
alias purge="sudo purge"
alias svnremovedeleted="svn status | grep '!' | sed 's/^.* /svn rm /' | bash"
alias svnaddnew="svn status | grep '?' | sed 's/^.* /svn add /' | bash"

export HISTSIZE=10000
export HISTCONTROL=erasedups
export EDITOR=vim

export PATH=/Users/rajesh/pear/bin:$PATH
export PATH=/Applications/VirtualBox.app/Contents/MacOS/:$PATH

function mcd() {
  mkdir -p "$1" && cd "$1";
}

function authme() {
  ssh "$1" 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' \
    < ~/.ssh/idrdsa.pub
}


findreplace(){
    printf "Search: ${1}\n"
    printf "Replace: ${2}\n"
    printf "In: ${3}\n\n"
 
    find . -name "*${3}" -type f | xargs perl -pi -e 's/${1}/${2}/g'
}

# Define a few Colours
BLACK='\e[7;49m'
BLUE='\e[7;49m'
GREEN='\e[0;32m'
CYAN='\e[0;36m'
RED='\e[0;31m'
PURPLE='\e[0;35m'
BROWN='\e[0;33m'
LIGHTGRAY='\e[0;37m'
DARKGRAY='\e[1;30m'
LIGHTBLUE='\e[1;34m'
LIGHTGREEN='\e[1;32m'
LIGHTCYAN='\e[1;36m'
LIGHTRED='\e[1;31m'
LIGHTPURPLE='\e[1;35m'
YELLOW='\e[1;33m'
WHITE='\e[1;37m'
NC='\e[0m'              # No Color

D=$'\e[37;40m'
PINK=$'\e[35;40m'
GREEN=$'\e[32;40m'
ORANGE=$'\e[33;40m'

#export PATH=/opt/subversion/bin:$PATH

export PS1='${PINK}\u ${D}at ${ORANGE}${HOSTNAME} ${D}in ${GREEN}\w\
${D}\n$ '

export WORKON_HOME="$HOME/.virtualenvs"
source /usr/local/bin/virtualenvwrapper.sh