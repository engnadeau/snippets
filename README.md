# Nick's Snippets

> Succinct scripts and examples

## Workstation Setup

### Backup

- VM images
- ssh keys
- Documents

### <3 Apps

- [LosslessCut](https://github.com/mifi/lossless-cut)
- [fstl](https://github.com/mkeeter/fstl)
- [pandoc](https://github.com/jgm/pandoc/releases/latest)
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
- [code-settings-sync](https://github.com/shanalikhan/code-settings-sync)
  - https://gist.github.com/nnadeau for settings
- -[nvm](https://github.com/nvm-sh/nvm)

### `.profile`

```bash
# NN: add python modules to path
PATH="$HOME/.local/bin:$PATH"

# NN: vscode as editor
export EDITOR='code'

# NN: add npm binaries
export PATH="/home/nicholas/node/bin:$PATH"
export PATH="/home/nicholas/.npm/bin:$PATH"

# NN: add GO binaries
export PATH="/home/nicholas/go/bin:$PATH"

# NN: add golang to path
export PATH=$PATH:/usr/local/go/bin

# NN: add ruby gems to path
export PATH=$PATH:/home/nicholas/.gem/ruby/2.5.0/bin

# NN: nvm
# https://github.com/nvm-sh/nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

### `.zshrc`

```bash
`ZSH_THEME="agnoster"`

# NN: fix username in prompt
# https://github.com/robbyrussell/oh-my-zsh/wiki/Themes#agnoster
DEFAULT_USER=$USER
prompt_context(){}

# https://github.com/djui/alias-tips
# https://github.com/zsh-users/zsh-autosuggestions
plugins=(
git
common-aliases
alias-tips
zsh-autosuggestions
extract
)
```
