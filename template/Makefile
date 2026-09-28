QUARTO ?= quarto
.PHONY: setup exams exams-assign exams-solution exams-grading exams-assign-tex clean

setup:
	$(QUARTO) add coatless-quarto/assign

exams: exams-assign exams-solution exams-grading

exams-assign:
	$(QUARTO) render exam.qmd --profile assign

exams-solution:
	$(QUARTO) render exam.qmd --profile solution

exams-grading:
	$(QUARTO) render exam.qmd --profile rubric

exams-assign-tex:
	$(QUARTO) render exam.qmd --profile assign --to latex

clean:
	rm -rf _output/ .quarto/
