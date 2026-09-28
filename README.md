# Copier exam project template

Generate a self-contained Quarto exam project (not a website) directly from GitHub:

```sh
uvx copier copy gh:fs-ise/exam-template path_to_new-exam
cd path_to_new-exam
make setup
make exams
```

Alternatively, replace `gh:fs-ise/exam-template` with a local checkout of this repository.

The concise questionnaire asks you to select IT Security Management, Analytics and Big Data, Introduction to Programming, or a custom course. Programming exams also ask for the Excel or Python variant. The course name is used as both the Quarto project and document title; the programming variant is displayed separately.

Copier proposes course-specific question-count and total-point defaults, both of which remain editable. It also derives an editable semester default using a single calendar year: January through March select the current year's Summer Semester, April through September select the current year's Winter Semester, and October through December select the following year's Summer Semester (for example, `Winter Semester 2026` or `Summer Semester 2027`).

Generated exams do not ask for or print an examination date. Their Quarto metadata explicitly sets `date: false`, preventing Quarto from inserting a date automatically in assignment, solution, or grading output.

The `assign` extension is downloaded on `make setup`, rather than embedded in this template archive. Commit the resulting `_extensions/` in each generated exam repository. The generated Makefile retains the assignment, solution, and grading profiles.
