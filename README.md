# Nick's Snippets and System Settings

## Workstation Setup

- [Install WSL2 and Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- Set `Campbell` colour scheme

### SSH Key & GitHub CLI

Use the GH CLI to generate a new SSH key and add it to your GitHub account.

- https://github.com/cli/cli/blob/trunk/docs/install_linux.md
- `gh auth login`

### ZSH

- `sudo apt install zsh`
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

#### `.zshrc`

Search and set the following:

```zsh
ZSH_THEME="afowler"

HIST_STAMPS="yyyy-mm-dd"

plugins=(
git
common-aliases
alias-tips
zsh-autosuggestions
extract
)

# User configuration

# vscode as editor
export EDITOR='code'

# add python modules to path
export PATH=$PATH:$HOME/.local/bin
```

#### Plugin Installation

- https://github.com/djui/alias-tips#oh-my-zsh
- https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh

### Other Apps

- https://github.com/mifi/lossless-cut
- https://github.com/nvm-sh/nvm
- https://github.com/commitizen/cz-cli
