# 必要な環境変数:
# PYPI_TOKEN https://pypi.org/manage/account/token/で作る


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
	poetry publish --username=__token__ --password=$(PYPI_TOKEN)


.PHONY: test
test:
	python -m unittest -v tests
