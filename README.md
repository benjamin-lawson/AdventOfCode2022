# 🎄 Advent Of Code 2022
I'm challenging myself to complete the [Advent of Code 2022](https://adventofcode.com/2022) and using this repository to store my code.

## Days
| Day | Repo Link                                                                   | Difficulty (1-5) | Part 1 | Part 2 |
|-----|-----------------------------------------------------------------------------|------------------|--------|--------|
| 1   | [Day 1](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day1) | ⭐                | ✔️      | ✔️      |
| 2   | [Day 2](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day2) | ⭐                | ✔️      | ✔️      |
| 3   | [Day 3](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day3) | ⭐                | ✔️      | ✔️      |
| 4   | [Day 4](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day4) | ⭐                | ✔️      | ✔️      |
| 5   | [Day 5](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day5) | ⭐⭐               | ✔️      | ✔️      |
| 6   | [Day 6](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day6) | ⭐                | ✔️      | ✔️      |
| 7   | [Day 7](https://github.com/benjamin-lawson/AdventOfCode2022/tree/main/Day7) | ⭐⭐⭐              | ✔️      | ✔️      |

## DayRunner
The `DayRunner` class makes it easy to run my solutions without having to manually provide the python file for the solution or the data needed to load. The `DayRunner` can be called using the following syntax:

###### Create New Day
```powershell
python ./DayRunner.py --day <NUM> --new-day
```

The above command will create a new diretory with the templated `Solver.py` and an empty `testdata.txt` and `data.txt` file. You will need to populate the `testdata.txt` and `data.txt` files with the appropriate data from the [Advent of Code 2022](https://adventofcode.com/2022) website. The newly created `Solver.py` file will contain boiler-plate code to run the data and you will need to implement the `solve_part_1()` and `solve_part_2()` functions.

###### Run Day Solver
```powershell
python ./DayRunner.py --day <NUM>
```

The above command will run the `Solver.py` file located under the `Day<NUM>` directory.

## DataLoader
The `DataLoader` was created to simplify data loading based on the day and copying the template code for new days. It is utilized by the `DayRunner` and is a static class.
