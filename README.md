# Nick's Snippets and System Settings

## Workstation Setup

- [Install WSL2 and Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- Set `Campbell` colour scheme

### SSH Key & GitHub CLI

Use the GH CLI to generate a new SSH key and add it to your GitHub account.

- [Install GH CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- `gh auth login`
- [Add SSH key as signing key](https://github.com/settings/keys)
- Sign using SSH keys: `git config --global gpg.format ssh`
- Set signing key: `git config --global user.signingkey ~/.ssh/examplekey`
- Sign by default: `git config --global commit.gpgsign true`

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

### npm and nvm

- [Install nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
- `source ~/.zshrc`
- Install node: `nvm install node`

### Commitizen CLI

[Install the global CLI](https://github.com/commitizen/cz-cli#conventional-commit-messages-as-a-global-utility):

```bash
npm install -g commitizen
npm install -g cz-conventional-changelog
echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc
```

### Other Apps

- https://github.com/mifi/lossless-cut
