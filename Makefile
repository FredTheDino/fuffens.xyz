APP=fuffens.py


.PHONY: serve freeze

serve:
	$(shell FLASK_APP=$(APP) FLASK_ENV=development flask run)

freeze:
	$(shell FLASK_APP=$(APP) python3 freeze.py)
	@echo "  Frozen"

clean:
	rm -rf build
	
