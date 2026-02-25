# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 09:48:16 2026

@author: Anagh-dot and Claud.ai
"""

# -*- coding: utf-8 -*-
"""
Grade 3 Math Worksheet Generator
Generates randomised arithmetic worksheets as LaTeX files for each student.
"""

import random
from typing import List, Tuple
import pandas as pd

# Student list - add or modify names as needed
STUDENT_LIST = [
    "Abra","Ka","Dabra"
    ]


class WorksheetGenerator:

    def __init__(self, student_name: str):
        self.student_name = student_name

    # -------------------------------------------------------------------------
    # Sequence generators
    # -------------------------------------------------------------------------

    def generate_sequence_by_1(self) -> List[List[int]]:
        sequences = []

        for direction in ["forward", "backward"]:
            hundreds = random.randint(1, 9)
            tens     = random.randint(0, 9)
            ones     = random.randint(0, 9)
            start    = hundreds * 100 + tens * 10 + ones

            if direction == "forward":
                seq = list(range(start, start + 10)) if start <= 990 else list(range(start - 9, start + 1))
            else:
                seq = list(range(start, start - 10, -1)) if start >= 109 else list(range(start, start + 10))

            sequences.append(seq)

        return sequences

    def generate_sequence_by_10(self) -> List[List[int]]:
        sequences = []

        for direction in ["forward", "backward"]:
            start = random.randint(100, 999)

            if direction == "forward":
                steps = min(9, (999 - start) // 10)
                seq   = [start + 10 * j for j in range(steps + 1)]
            else:
                steps = min(9, (start - 100) // 10)
                seq   = [start - 10 * j for j in range(steps + 1)]

            sequences.append(seq)   # FIX 1: indented inside loop

        return sequences
    
# =============================================================================
#     def generate_sequence_by_100(self) -> List[List[int]]:
#         sequences = []
# 
#         for direction in ["forward", "backward"]:
#             start = random.randint(100, 999)
# 
#             if direction == "forward":
#                 steps = min(9, (999 - start) // 100)
#                 seq   = [start + 100 * j for j in range(steps + 1)]
#             else:
#                 steps = min(9, (start - 100) // 100)
#                 seq   = [start - 100 * j for j in range(steps + 1)]
# 
#             sequences.append(seq)   # FIX 2: indented inside loop
# 
#         return sequences
#         
# =============================================================================
    
    # -------------------------------------------------------------------------
    # Arithmetic generators
    # -------------------------------------------------------------------------

    def generate_2digit_addition_no_regrouping(self, count: int) -> pd.DataFrame:
        """Generate 2-digit addition problems without regrouping"""
        problems = []
        while len(problems) < count:
            t1 = random.randint(0, 4); o1 = random.randint(0, 4)
            t2 = random.randint(0, 5 - t1); o2 = random.randint(0, 5 - o1)
            op1 = t1 * 10 + o1
            op2 = t2 * 10 + o2
            if (o1 + o2 < 10) and (t1 + t2 < 10) and (op1 + op2 < 100):
                problems.append({'operand1': op1, 'operand2': op2, 'result': op1 + op2})
        return pd.DataFrame(problems)

    def generate_2digit_subtraction_no_regrouping(self, count: int) -> pd.DataFrame:
        """Generate 2-digit subtraction problems without regrouping"""
        problems = []
        while len(problems) < count:
            t1 = random.randint(1, 9); o1 = random.randint(1, 9)
            t2 = random.randint(0, t1); o2 = random.randint(0, o1)
            op1 = t1 * 10 + o1
            op2 = t2 * 10 + o2
            if (o1 >= o2) and (t1 >= t2) and (op1 > op2):
                problems.append({'operand1': op1, 'operand2': op2, 'result': op1 - op2})
        return pd.DataFrame(problems)

    def generate_2digit_addition_with_regrouping(self, count: int) -> pd.DataFrame:
        """Generate 2-digit addition problems with regrouping"""
        problems = []
        while len(problems) < count:
            t1 = random.randint(1, 7); o1 = random.randint(1, 9)
            t2 = random.randint(1, 8 - t1); o2 = random.randint(0, 9)
            op1 = t1 * 10 + o1
            op2 = t2 * 10 + o2
            if (o1 + o2 >= 10) and (op1 + op2 < 100):
                problems.append({'operand1': op1, 'operand2': op2, 'result': op1 + op2})
        return pd.DataFrame(problems)

    def generate_2digit_subtraction_borrowing(self, count: int) -> pd.DataFrame:
        """Generate 2-digit subtraction problems with borrowing"""
        problems = []
        while len(problems) < count:
            t1 = random.randint(2, 9); o1 = random.randint(0, 8)
            t2 = random.randint(1, t1 - 1); o2 = random.randint(o1 + 1, 9)
            op1 = t1 * 10 + o1
            op2 = t2 * 10 + o2
            if (o1 < o2) and (t1 >= t2) and (op1 > op2):
                problems.append({'operand1': op1, 'operand2': op2, 'result': op1 - op2})
        return pd.DataFrame(problems)

    def generate_multiplication_tables(self, count: int) -> pd.DataFrame:
        """Generate multiplication problems using times tables up to 10"""
        problems = []
        while len(problems) < count:
            op1 = random.randint(2, 10)
            op2 = random.randint(2, 10)
            problems.append({'operand1': op1, 'operand2': op2, 'result': op1 * op2})
        return pd.DataFrame(problems)


    # -------------------------------------------------------------------------
    # Word problem generators
    # -------------------------------------------------------------------------

    # Each template is a tuple: (template_string, op)
    # Placeholders: {a} = operand1, {b} = operand2, {ans} = result
    # op: 'add', 'sub', 'mul'

    WORD_PROBLEM_TEMPLATES = {
        'add': [
            "A library had {a} books. {b} more books were bought. How many books does the library have now?",
            "A farmer harvested {a} mangoes on Monday and {b} mangoes on Tuesday. How many mangoes did he harvest in all?",
            "There are {a} students in Indus School and {b} students in Azim Premji School. How many students are there in both schools together?",
            "A shopkeeper sold {a} kg of rice in the morning and {b} kg in the evening. How many kg did he sell in total?",
            "A factory made {a} toys on Saturday and {b} toys on Sunday. What is the total number of toys made?",
        ],
        'sub': [
            "A baker baked {a} biscuits. He sold {b} of them. How many biscuits are left?",
            "A school collected {a} rupees for a trip. They spent {b} rupees on transport. How much money is left?",
            "A grocery shop had {a} boxes. {b} boxes were moved to another shop. How many boxes remain in the grocery shop?",
            "A pond had {a} litres of water. {b} litres dried in summer. How many litres of water are left?",
        ],
        'mul': [
            "A box holds {a} apples. How many apples will {b} such boxes hold?",
            "A classroom has {a} rows of desks with {b} desks in each row. How many desks are there in all?",
            "A packet has {a} pencils. How many pencils are there in {b} such packets?",
            "Each child plants {a} saplings. If {b} children take part, how many saplings are planted in total?",
            "A bus can carry {a} passengers. How many passengers can {b} such buses carry?",
        ],
    }

    def generate_word_problems(self) -> List[dict]:
        """
        Generate 2 addition, 2 subtraction, 2 multiplication word problems.
        Numbers are randomised; results stay in [1, 999].
        Returns a list of dicts with keys: text, answer.
        """
        problems = []

        # --- 2 addition problems ---
        for _ in range(2):
            while True:
                op1 = random.randint(10, 70)
                op2 = random.randint(10, 99 - op1)
                result = op1 + op2
                if 1 <= result <= 99:
                    tmpl = random.choice(self.WORD_PROBLEM_TEMPLATES['add'])
                    problems.append({
                        'text':   tmpl.format(a=op1, b=op2, ans=result),
                        'answer': result,
                    })
                    break

        # --- 2 subtraction problems ---
        for _ in range(2):
            while True:
                op1 = random.randint(20, 99)
                op2 = random.randint(10, op1 - 1)
                result = op1 - op2
                if 1 <= result <= 99:
                    tmpl = random.choice(self.WORD_PROBLEM_TEMPLATES['sub'])
                    problems.append({
                        'text':   tmpl.format(a=op1, b=op2, ans=result),
                        'answer': result,
                    })
                    break

        # --- 2 multiplication problems ---
        for _ in range(2):
            while True:
                op1 = random.randint(2, 10)
                op2 = random.randint(2, min(10, 99 // op1))
                result = op1 * op2
                if 1 <= result <= 99:
                    tmpl = random.choice(self.WORD_PROBLEM_TEMPLATES['mul'])
                    problems.append({
                        'text':   tmpl.format(a=op1, b=op2, ans=result),
                        'answer': result,
                    })
                    break

        return problems

    # -------------------------------------------------------------------------
    # LaTeX helpers
    # -------------------------------------------------------------------------

    def _vertical_problem(self, op: str, op1: int, op2: int) -> str:
        """Return a LaTeX tabular block for a vertical arithmetic problem."""
        return (
            r'\begin{tabular}{lr}' + '\n'
            r'&$' + str(op1) + r'$ \\' + '\n'
            r'$' + op + r'$ & $' + str(op2) + r'$ \\' + '\n'
            r'\midrule' + '\n'
            r'& \\' + '\n'
            r'\bottomrule' + '\n'
            r'\end{tabular}\par' + '\n'  # \par ensures multicols treats each problem as its own column item
        )

    # Running counter so sub-labels are consecutive across all three sequence blocks in Q1
    _seq_label_counter = 0

    def _sequence_rows_block(self, sequences):
        latex = ""

        for seq in sequences:
            visible = seq[:10]

            blank_positions = random.sample(
                range(1, len(visible)),
                min(3, len(visible) - 1)
            )

            cells = []
            for idx, val in enumerate(visible):
                if idx in blank_positions:
                    cells.append(r'\underline{\hspace{1cm}}')
                else:
                    cells.append(str(val))

            row_str = ' & '.join(cells) + r' \\'
            cols = len(visible)
            label = chr(ord('a') + self._seq_label_counter)
            self._seq_label_counter += 1

            latex += (
                r'(' + label + r') \begin{tabular}{' + 'c' * cols + '}\n'
                + row_str + '\n'
                + r'\end{tabular}' + '\n'
                + r'\vspace{0.3cm}\\' + '\n'
            )

        return latex

    def _multicol_block(self, problems: pd.DataFrame, op_symbol: str,
                         start: int, end: int) -> str:
        """Emit a multicols{6} block for rows [start, end) of a DataFrame."""
        cols = end - start
        latex  = r'\begin{multicols}{' + str(cols) + '}\n'
        for i in range(start, min(end, len(problems))):
            row = problems.iloc[i]
            latex += self._vertical_problem(op_symbol, int(row['operand1']), int(row['operand2']))
        latex += r'\end{multicols}' + '\n'
        return latex

    def _question_block_arithmetic(self, problems: pd.DataFrame, op_symbol: str,
                                    label: str = "Solve the following:") -> str:
        """Emit a full \\question with two rows of 6 problems each."""
        latex  = r'\question ' + label + '\n\n'
        latex += self._multicol_block(problems, op_symbol, 0, 6)
        latex += r'\vspace{0.2cm}' + '\n'
        latex += self._multicol_block(problems, op_symbol, 6, 12)
        latex += '\n'
        return latex

    def _question_block_mixed(self, problems: pd.DataFrame,
                               label: str = "Solve the following:") -> str:
        # FIX 3: infer_op was a nested function that swallowed the entire method body.
        # Moved infer_op logic inline and de-nested the latex-building code.
        def infer_op(row):
            return '+' if int(row['operand1']) + int(row['operand2']) == int(row['result']) else '-'

        latex = r'\question ' + label + '\n\n'
        for start, end in [(0, 6), (6, 12)]:
            cols = min(end, len(problems)) - start
            if cols <= 0:
                break
            latex += r'\begin{multicols}{' + str(cols) + '}\n'
            for i in range(start, min(end, len(problems))):
                row = problems.iloc[i]
                latex += self._vertical_problem(
                    infer_op(row),
                    int(row['operand1']),
                    int(row['operand2'])
                )
            latex += r'\end{multicols}' + '\n'
            if start == 0:
                latex += r'\vspace{0.2cm}' + '\n'
        latex += '\n'
        return latex

    def _question_block_word_problems(self, problems: List[dict],
                                       label: str = "Solve the following word problems. Show your working:") -> str:
        """Emit a \\question block with word problems and answer lines."""
        latex = r'\question ' + label + '\n\n'
        for i, prob in enumerate(problems, 1):
            latex += (
                r'\textbf{' + str(i) + r'.} ' + prob['text'] + '\n\n'
                + r'\vspace{0.1cm}' + '\n'
                + r'Answer: \underline{\hspace{3cm}}' + '\n\n'
                + r'\vspace{0.2cm}' + '\n\n'
            )
        return latex

    def _question_block_sequences(self, sequences: List[Tuple[int, List[int]]],
                                   step_label: str,
                                   label: str = None) -> str:
        """Emit a \\question block for number sequences with blanks."""
        if label is None:
            label = f"Fill in the blanks (counting by {step_label}):"
        latex = r'\question ' + label + '\n\n'
        for _, seq in sequences:
            visible = seq[:10]  # show at most 10 numbers
            blank_positions = random.sample(range(1, len(visible)),
                                            min(3, len(visible) - 1))
            cells = []
            for idx, val in enumerate(visible):
                if idx in blank_positions:
                    cells.append(r'\underline{\hspace{1cm}}')
                else:
                    cells.append(str(val))
            row_str = ' & '.join(cells) + r' \\'
            cols = len(visible)
            latex += (
                r'\begin{tabular}{' + 'c' * cols + '}\n'
                + row_str + '\n'
                + r'\end{tabular}' + '\n'
                + r'\vspace{0.3cm}\\' + '\n'
            )
        latex += '\n'
        return latex

    # -------------------------------------------------------------------------
    # Top-level LaTeX generation
    # -------------------------------------------------------------------------

    def generate_latex(self) -> str:
        """Generate the complete LaTeX document for one student."""

        # --- Generate all problem sets ---
        seq_by_1   = self.generate_sequence_by_1()
        seq_by_10  = self.generate_sequence_by_10()

        add_2digit_regroup   = self.generate_2digit_addition_with_regrouping(4)
        add_2digit_noregroup = self.generate_2digit_addition_no_regrouping(2)
        sub_2digit_borrow    = self.generate_2digit_subtraction_borrowing(4)
        sub_2digit_nogroup   = self.generate_2digit_subtraction_no_regrouping(2)
        mult = self.generate_multiplication_tables(12)
        word_problems = self.generate_word_problems()

        # Mixed addition/subtraction pool
        mixed_pool = (
            pd.concat([add_2digit_regroup, add_2digit_noregroup, sub_2digit_borrow, sub_2digit_nogroup])
            .sample(frac=1)
            .head(12)
            .reset_index(drop=True)
        )

        return self._build_latex_content(
            seq_by_1, seq_by_10,
            mixed_pool,
            mult,
            word_problems
        )

    def _build_latex_content(self,
                              seq_by_1, seq_by_10,
                              mixed_pool,
                              mult,
                              word_problems) -> str:
        """Assemble the complete LaTeX document string."""

        # ---------- Document preamble ----------
        latex = r'''\documentclass[13pt]{exam}
\usepackage[bottom=2cm,top=1cm,left=1cm,right=1cm]{geometry}
\usepackage{multicol}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage[fontsize=13pt]{fontsize}
\usepackage{pgf}
\usetikzlibrary{shapes.geometric, arrows, automata, positioning, patterns}
\usepackage{pgfplots}
\usepackage{array}

\selectcolormodel{gray}
\PassOptionsToPackage{monochrome}{xcolor}

\makeatletter
\newcount\my@repeat@count
\newcommand{\myrepeat}[2]{%
  \begingroup
  \my@repeat@count=\z@
  \@whilenum\my@repeat@count<#1\do{#2\advance\my@repeat@count\@ne}%
  \endgroup
}
\makeatother

\title{\vspace{-2cm} Grade 2 -- Revision Worksheet - 2}
\date{\vspace{-1cm} February, 2026}

\pagestyle{headandfoot}
\firstpagefooter{''' + self.student_name + r'''}{Grade 2 - Revision Worksheet, February, 2026}{\thepage}
\runningfooter{''' + self.student_name + r'''}{Grade 2 - Revision Worksheet, February, 2026}{\thepage}
\firstpageheader{}{}{}
\runningheader{}{}{}

\begin{document}

\vspace{-3cm}

\maketitle

\vspace{-1cm}

\begin{center}
Student : {\large \textbf{''' + self.student_name + r'''}}
\end{center}

\thispagestyle{headandfoot}

\begin{questions}

'''

        # Reset sequence label counter so each student starts at (a)
        self._seq_label_counter = 0

        # ---------- Q1: All sequences under one question (no labels) ----------  # FIX 4: restored correct 8-space indent
        latex += r'\question Fill in the missing numbers:' + '\n\n'
        
        latex += self._sequence_rows_block(seq_by_1)
        latex += self._sequence_rows_block(seq_by_10)
        
        latex += '\n'

        # ---------- Q2: Mixed addition and subtraction — single question, 2 rows of 6 ----------
        latex += self._question_block_mixed(
            mixed_pool,
            label="Solve the following:"
        )

        # ---------- Q4: Multiplication ----------
        latex += self._question_block_arithmetic(
            mult, r'\times',
            label="Solve the following:"
        )


        # ---------- Q6: Word problems ----------
        latex += self._question_block_word_problems(word_problems)

        # ---------- Footer ----------
        latex += r'''\vspace{0.25cm}

\end{questions}

\begin{center}
Rough work.
\end{center}

\end{document}
'''
        return latex


# =============================================================================
# File generation
# =============================================================================

def generate_all_worksheets(
        student_list: List[str] = None,
        output_dir: str = "."
) -> None:
    """
    Generate LaTeX worksheets for every student and save to output_dir.

    Args:
        student_list : list of student names; defaults to STUDENT_LIST
        output_dir   : folder to write .tex files into
    """
    if student_list is None:
        student_list = STUDENT_LIST

    import os
    os.makedirs(output_dir, exist_ok=True)

    for student_name in student_list:
        print(f"Generating worksheet for {student_name}...")
        generator     = WorksheetGenerator(student_name)
        latex_content = generator.generate_latex()

        safe_name   = student_name.lower().replace(' ', '_')
        output_file = os.path.join(output_dir, f"grade2_revision2_{safe_name}.tex")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)

        print(f"  ✓ Saved: {output_file}")

    print(f"\nGenerated {len(student_list)} worksheets successfully!")


if __name__ == "__main__":
    print("=" * 60)
    print("Grade 2 Revision 2 — Worksheet Generator")
    print("=" * 60)
    print(f"\nGenerating worksheets for {len(STUDENT_LIST)} students:")
    for i, name in enumerate(STUDENT_LIST, 1):
        print(f"  {i}. {name}")
    print()

    # ── Change this path to your OneDrive / local folder ──────────────────────
    OUTPUT_DIR = (
        "."
        )
    generate_all_worksheets(output_dir=OUTPUT_DIR)

    print("\nTo compile all PDFs, run from that folder:")
    for name in STUDENT_LIST:
        safe = name.lower().replace(' ', '_')
        print(f"  pdflatex grade2_revision_{safe}.tex")# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 06:38:14 2026

@author: AnaghPurandare
"""

import random
from typing import List, Tuple
import pandas as pd

# Student list - add or modify names as needed
STUDENT_LIST = [
    "Abra","Ka","Dabra"
    ]

class WorksheetGenerator:
    
    def __init__(self, student_name: str):
        self.student_name = student_name

    def generate_sequence_by_1(self, count: int = 4) -> List[Tuple[int, List[int]]]:
        """Generate 3-digit sequences counting by 1 (forward or backward)"""

        sequences = []

        for i in range(count):
            hundreds = random.randint(1, 9)
            tens = random.randint(0, 9)
            ones = random.randint(0, 9)

            start = hundreds * 100 + tens * 10 + ones

            direction = random.choice(["forward", "backward"])

            if direction == "forward":
                if start <= 990:
                    seq = list(range(start, start + 10))
                else:
                    seq = list(range(start - 9, start + 1))
            else:
                if start >= 109:
                    seq = list(range(start, start - 10, -1))
                else:
                    seq = list(range(start, start + 10))

            sequences.append((i, seq))

        return sequences

    def generate_sequence_by_10(self, count: int = 4) -> List[Tuple[int, List[int]]]:
        """Generate 3-digit sequences counting by 10 (forward or backward)"""

        sequences = []

        for i in range(count):
            start = random.randint(100, 999)
            direction = random.choice(["forward", "backward"])

            if direction == "forward":
                max_steps = (999 - start) // 10
                steps = min(9, max_steps)
                seq = [start + 10*j for j in range(steps + 1)]

            else:
                max_steps = (start - 100) // 10
                steps = min(9, max_steps)
                seq = [start - 10*j for j in range(steps + 1)]

            sequences.append((i, seq))

        return sequences

    def generate_sequence_by_100(self, count: int = 4) -> List[Tuple[int, List[int]]]:
        """Generate 3-digit sequences counting by 100 (forward or backward)"""

        sequences = []

        for i in range(count):
            start = random.randint(100, 999)
            direction = random.choice(["forward", "backward"])

            if direction == "forward":
                max_steps = (999 - start) // 100
                steps = min(9, max_steps)
                seq = [start + 100*j for j in range(steps + 1)]

            else:
                max_steps = (start - 100) // 100
                steps = min(9, max_steps)
                seq = [start - 100*j for j in range(steps + 1)]

            sequences.append((i, seq))

        return sequences

    def generate_3digit_addition_no_regrouping(self, count: int) -> pd.DataFrame:
        """Generate 3-digit addition problems without regrouping"""
        problems = []
        while len(problems) < count:
            hundreds1 = random.randint(1, 4)
            tens1 = random.randint(0, 4)
            ones1 = random.randint(0, 4)

            hundreds2 = random.randint(1, 5 - hundreds1)
            tens2 = random.randint(0, 5 - tens1)
            ones2 = random.randint(0, 5 - ones1)

            operand1 = hundreds1 * 100 + tens1 * 10 + ones1
            operand2 = hundreds2 * 100 + tens2 * 10 + ones2

            if (ones1 + ones2 < 10) and (tens1 + tens2 < 10) and (operand1 + operand2 < 1000):
                problems.append({
                    'operand1': operand1,
                    'operand2': operand2,
                    'result': operand1 + operand2
                })
        return pd.DataFrame(problems)

    def generate_multiplication_tables(self, count: int) -> pd.DataFrame:
        """Generate multiplication problems using numbers from times tables up to 10"""
        problems = []
        while len(problems) < count:
            operand1 = random.randint(2, 10)
            operand2 = random.randint(2, 10)

            problems.append({
                'operand1': operand1,
                'operand2': operand2,
                'result': operand1 * operand2
            })
        return pd.DataFrame(problems)

    def generate_division_tables(self, count: int) -> pd.DataFrame:
        """Generate division problems using numbers from times tables up to 10 (no remainders)"""
        problems = []
        while len(problems) < count:
            operand2 = random.randint(2, 10)
            multiplier = random.randint(2, 10)
            operand1 = operand2 * multiplier

            problems.append({
                'operand1': operand1,
                'operand2': operand2,
                'result': operand1 // operand2
            })

        return pd.DataFrame(problems)
