# Copier exam project template

Generate a self-contained Quarto exam project (not a website):

```sh
uvx copier copy path/to/exam-copier-template path/to/new-exam
cd path/to/new-exam
make setup
make exams
```

Copier asks for the exam/project title, course, semester, date, question count, total points, and duration. The title is propagated to `_quarto.yml` and `exam.qmd`. See the generated README for authoring and build instructions.

The `assign` extension is downloaded on `make setup`, rather than embedded in this template archive. Commit the resulting `_extensions/` in each generated exam repository.
