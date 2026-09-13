# CSV Data Grouping and Plotting Tool

A simple Python command-line tool for working with CSV files. The project provides
three main operations:

- Group CSV data by a selected column and optionally export the result as a CSV file.
- Create a line plot from two selected CSV columns.
- Create a bar plot from two selected CSV columns.

## Project Structure

```text
CSV_Data_Toolkit/
├── codes/
│   ├── main.py
│   ├── c1.py
│   ├── c2.py
│   └── c3.py
├── datas/
│   ├── example1.csv
│   ├── example2.csv
│   ├── example3.csv
│   └── example4.csv
├── requirements.txt
└── README.md
```

## Requirements

The project uses:

- Python
- pandas
- matplotlib

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the program from the `codes` directory:

```bash
python main.py [command] [CSV path or example name]
```

### 1. Group data

Use:

```bash
python main.py group path/to/data.csv
```

The program asks for the column name and groups the data by that column.
It sorts the group sizes from largest to smallest.

You can also use one of the built-in example datasets:

```bash
python main.py group example1
```

Available examples:

```text
example1
example2
example3
example4
```

After grouping, the program asks whether you want to export the result as
a CSV file.

### 2. Line plot

Use:

```bash
python main.py line_plot path/to/data.csv
```

Then enter the names of the X and Y columns.

For example:

```text
enter x col: column1
enter y col: column2
```

The program displays the line plot.

You can also use:

```bash
python main.py line_plot example1
```

### 3. Bar plot

Use:

```bash
python main.py bar_plot path/to/data.csv
```

Then enter the label and data column names.

For example:

```text
enter label col: category
enter value col: value
```

The program displays the bar plot.

You can also use:

```bash
python main.py bar_plot example1
```

### 4. Help

To see the available commands:

```bash
python main.py --help
```

### 5. Version

To display the current version:

```bash
python main.py --version
```

Current version:

```text
1.0.1
```

## How It Works

The `main.py` file acts as the command-line entry point and calls the
appropriate function from the other modules.

```text
main.py
 ├── group      → c1.py
 ├── line_plot  → c2.py
 └── bar_plot   → c3.py
```

`c1.py` handles grouping and optional CSV export, while `c2.py` and `c3.py`
handle line and bar plots respectively.

## CSV Input

The program expects CSV files that can be read by pandas. When using a custom
CSV file, provide its path as the command-line argument.

For the built-in examples, the program expects the CSV files to be available
inside the project's `datas` directory.

## Author

Hesam Ghoreashy

2026
