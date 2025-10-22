import os
from pathlib import Path
from nbformat.v4 import new_notebook, new_markdown_cell
import nbformat

structure = {
    "week0-prep": [
        "day1_intro.ipynb",
        "day2_variables.ipynb",
        "day3_input_output.ipynb",
        "day4_operators.ipynb",
        "day5_conditionals.ipynb",
    ],
    "week1-loops": [
        "day6_for_loop.ipynb",
        "day7_while_loop.ipynb",
        "day8_nested_loops.ipynb",
    ],
    "week2-functions-data": [
        "day9_functions.ipynb",
        "day10_lists.ipynb",
        "day11_tuples_sets.ipynb",
        "day12_dictionaries.ipynb",
        "day13_exercises.ipynb",
    ],
    "week3-files-modules": [
        "day14_modules.ipynb",
        "day15_fileio.ipynb",
        "day16_project_calculator.ipynb",
        "day17_project_quiz.ipynb",
    ],
}

base_dir = Path.cwd()

for week, notebooks in structure.items():
    week_path = base_dir / week
    week_path.mkdir(exist_ok=True)
    for nb_name in notebooks:
        nb_path = week_path / nb_name
        if not nb_path.exists():
            nb = new_notebook()
            title = nb_name.replace(".ipynb", "").replace("_", " ").title()
            nb.cells.append(
                new_markdown_cell(f"# {title}\n\n🗓️ Date:\n\n---\n## 🎯 Learning Objectives\n- \n- \n\n## 🧠 Notes\n\n\n## 💻 Practice Code\n\n\n## ✅ Summary\n\n")
            )
            with open(nb_path, "w") as f:
                nbformat.write(nb, f)
print("✅ All week folders and notebooks created successfully!")