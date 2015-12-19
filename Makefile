test:
	@py.test --pep8 -v --cov-report term-missing --cov=wonderful_bing/ tests/ wonderful_bing/

create:
	@python setup.py sdist bdist_wheel

upload:
	@python setup.py sdist bdist_wheel upload
