all: build/v46.pdf

build/v46.pdf: v46.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v46.tex
	lualatex  --output-directory=build v46.tex
	biber build/v46.bcf
	lualatex  --output-directory=build v46.tex

build/BFeld.pdf: BFeld.txt BFeld.py | build
	python BFeld.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
