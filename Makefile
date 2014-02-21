PDFLATEX := pdflatex
BIBER := biber
TEXCOUNT := texcount
GNUPLOT := gnuplot
R := /usr/bin/R
EPSPDF := epspdf
GS = gs

GRAPHS := toa-model-annual.tex toa-model-daily.tex extended-cloud.tex

.PHONY: all wc clean

all: radiation.pdf

wc:
	$(TEXCOUNT) radiation.tex

clean:
	rm -f *.dat radiation.pdf *.bcf *.aux $(GRAPHS)

stats:
	$(R) --vanilla < statistics.r

presentation:
	$(GNUPLOT) -e "load 'presentation-cloud-sw.plt'"
	$(GNUPLOT) -e "load 'presentation-cloud-sw-with-cloud-cover.plt'"	
	$(GNUPLOT) -e "load 'presentation-longwave.plt'"	
	$(EPSPDF) presentation_cloud_sw.eps
	$(EPSPDF) presentation_cloud_sw_with_cloud_cover.eps 
	$(EPSPDF) presentation-longwave-simple.eps 
	$(EPSPDF) presentation-longwave-loridan.eps 
	$(EPSPDF) presentation-longwave-variables.eps 
	$(GS) -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=presentation.pdf presentation_cloud_sw.pdf presentation_cloud_sw_with_cloud_cover.pdf presentation-longwave-simple.pdf presentation-longwave-loridan.pdf presentation-longwave-variables.pdf

radiation.pdf: radiation.tex radiation.bib $(GRAPHS)
	$(PDFLATEX) $<
	$(BIBER) radiation
	$(PDFLATEX) $<

$(GRAPHS): radiation.plt radiation.py one_year_toa.py model_obs_merge.py
	./one_year_toa.py 51 > one_year_toa.dat
	./model_obs_merge.py London_MET_20102012.csv London_CL31_CLDW15_15min_OctDec.csv 51 > model_obs.dat 2> parse-errors.log
	$(GNUPLOT) -e "load '$<'"
