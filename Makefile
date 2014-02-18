PDFLATEX := pdflatex
TEXCOUNT := texcount
GNUPLOT := gnuplot

GRAPHS := toa-model.tex toa-model-verification.tex

.PHONY: all wc clean

all: radiation.pdf

wc:
	$(TEXCOUNT) radiation.tex

clean:
	rm -f *.dat radiation.pdf

radiation.pdf: radiation.tex $(GRAPHS)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(GRAPHS): radiation.plt radiation.py one_year_toa.py
	./one_year_toa.py 51 > one_year_toa.dat
	$(GNUPLOT) -e "load '$<'"
