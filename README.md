# Copier exam project template

Generate a self-contained Quarto exam project (not a website) directly from GitHub:

```sh
uvx copier copy --trust gh:fs-ise/exam-template path_to_new-exam
cd path_to_new-exam
make setup
make exams
```

Alternatively, replace `gh:fs-ise/exam-template` with a local checkout of this repository.

The concise questionnaire asks you to select IT Security Management, Analytics and Big Data, Introduction to Programming, or a custom course. Programming exams also ask for the Excel or Python variant. The course name is used as both the Quarto project and document title; the programming variant is displayed separately.

Copier proposes course-specific question-count and total-point defaults, both of which remain editable. It also derives an editable semester default using a single calendar year: January through March select the current year's Summer Semester, April through September select the current year's Winter Semester, and October through December select the following year's Summer Semester (for example, `Winter Semester 2026` or `Summer Semester 2027`).

Generated exams do not ask for or print an examination date. The document metadata omits the `date` field, while the assignment profile suppresses Quarto's automatic title block.

Generation creates exactly one numbered task file for each selected question and wires every file into `exam.qmd`. Question points are allocated as integers: each question gets the quotient of total points divided by question count, and the first questions receive any remainder. The same allocation is used in the cover-page scoring table.

On initial generation, after creating the numbered task files, Copier initializes the destination as an independent Git repository on branch `main` and creates a commit named `Initialize exam from template`. It uses your existing Git name and email, does not add a remote, and leaves a destination that is already a Git repository untouched. This initialization and automatic commit are skipped by `copier update`.

The generated `.gitignore` excludes rendered PDFs, Quarto working directories, and temporary LaTeX files so that generated build artifacts are not included in the initial commit.

The `assign` extension is downloaded on `make setup`, rather than embedded in this template archive. Commit the resulting `_extensions/` in each generated exam repository. The generated Makefile retains the assignment, solution, and grading profiles.
