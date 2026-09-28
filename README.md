# Copier exam project template

Generate a self-contained Quarto exam project (not a website) directly from GitHub:

```sh
uvx copier copy gh:fs-ise/exam-template path/to/new-exam
cd path/to/new-exam
make setup
make exams
```

Alternatively, replace `gh:fs-ise/exam-template` with a local checkout of this repository.

The concise questionnaire asks you to select IT Security Management, Analytics and Big Data, Introduction to Programming, or a custom course. Programming exams also ask for the Excel or Python variant. The course name is used as both the Quarto project and document title; the programming variant is displayed separately.

Copier proposes course-specific question-count and total-point defaults, both of which remain editable. It also derives the upcoming semester when generation runs: April through September select the next Winter Semester, while October through March select the next Summer Semester. The semester and printed exam date remain editable.

The `assign` extension is downloaded on `make setup`, rather than embedded in this template archive. Commit the resulting `_extensions/` in each generated exam repository. The generated Makefile retains the assignment, solution, and grading profiles.
