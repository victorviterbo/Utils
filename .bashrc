
# Init
if [ -f "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh" ]; then
  __GIT_PROMPT_DIR=$(brew --prefix)/opt/bash-git-prompt/share
  GIT_PROMPT_ONLY_IN_REPO=1
  source "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh"
fi

# Aliases
alias fclear='clear && printf "\033c"'
alias gittree="git log --graph --pretty=format:'%C(yellow)%h%C(reset) %C(cyan)%d%C(reset) %s %C(blue)(%cr)%C(reset)' --all"
alias git='LANG=en_GB git'
alias mm="fclear && make re"
alias cppnewclass="python3 ~/Desktop/42/Utils/CppClassGen.py"
alias valg="valgrind -v \
  --trace-children=yes \
  --track-fds=yes \
  --track-origins=yes \
  --leak-check=full \
  --show-leak-kinds=all \
  --show-reachable=yes \
  --errors-for-leak-kinds=all \
  --error-exitcode=1 \
  --log-file=valgrind_detailed.log"
alias webserv_docker="docker run -it --rm --name webserv  -v $(pwd):/workspace  -p8080:8080 -p8081:8081 -w /workspace  /bin/bash"
alias pydiffdir="python3 /Users/victorviterbo/Desktop/42/Utils/diff_dir.py"

# Git pushall command
pushall() {
    # Get the root directory of the git repo
    local git_root=$(git rev-parse --show-toplevel 2>/dev/null)
    
    if [ -z "$git_root" ]; then
        echo "Error: Not in a git repository"
        return 1
    fi
    
    # Navigate to git root and add all files
    cd "$git_root" || return 1
    git add .
    
    # Ask for commit message
    echo "Enter commit message:"
    read commit_message
    
    # Commit and push
    git commit -m "$commit_message"
    git push
}

# Make history search interactive by typing beggining of line
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'


# Append to history instead of overwriting
shopt -s histappend


# Avoid duplicate commands in history
export HISTCONTROL=ignoredups:erasedups

# Set a larger history size
export HISTSIZE=10000
export HISTFILESIZE=20000

# Timestamp commands in history
export HISTTIMEFORMAT='%F %T '
[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# Make colors
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
export GREP_COLOR='1;33'

# Set Github utils
source $(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh
GIT_PROMPT_WITH_VIRTUAL_ENV=1
GIT_PROMPT_THEME=Single_line_Solarized
GIT_PROMPT_THEME=Solarized

relative_path="~${PWD#${HOME}}"

GIT_PROMPT_START_USER="_LAST_COMMAND_INDICATOR_ ${Yellow}${relative_path}${ResetColor}"
GIT_PROMPT_START_ROOT="_LAST_COMMAND_INDICATOR_ ${GIT_PROMPT_START_USER}"

GIT_PROMPT_END="\n$ "
GIT_PROMPT_END_USER="\n$ "
GIT_PROMPT_END_ROOT="\n# "

# Function to show the current Git branch
parse_git_branch() {

    git branch 2>/dev/null | grep '^*' | sed 's/^* //' | colrm 1 2

}

export PS1='\[\033]0;$TITLEPREFIX:$PWD\007\]\n\[\033[32m\]\u@\h \[\033[35m\]\w\[\033[0m\]\n$ '


export PATH=/opt/homebrew/Cellar/llvm/21.1.2/bin/:usr/local/:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Users/victorviterbo/.local/bin:/Users/victorviterbo/.local/bin

