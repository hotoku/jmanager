define release
$1:
	bump2version $$@
	git push --tag
	git push
endef


$(foreach part,patch minor major,$(eval $(call release,$(part))))


.PHONY: build
build:
	poetry build


.PHONY: publish
publish: build
	poetry publish -u hotoku -p $(myps -P 158)


.PHONY: test
test:
	python -m unittest -v tests
