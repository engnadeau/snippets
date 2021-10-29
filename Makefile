profile:
	\cp -f ~/.profile $@

zshrc:
	\cp -f ~/.zshrc $@

.PHONY: sync
sync: profile zshrc

.PHONY: apply
apply:
	\cp -f profile ~/.profile
	\cp -f zshrc ~/.zshrc
