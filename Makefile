.PHONY: profile
profile:
	\cp -f ~/.profile $@

.PHONY: zshrc
zshrc:
	\cp -f ~/.zshrc $@

.PHONY: sync
sync: profile zshrc

.PHONY: apply
apply:
	\cp -f profile ~/.profile
	\cp -f zshrc ~/.zshrc
