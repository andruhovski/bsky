# bsky

PDF with Python series built around Aspose.PDF.

This repository is a small tutorial set of simple standalone Python examples that show how to create and manipulate PDF content with `aspose.pdf`.

## Prerequisites

- Python 3.x
- Aspose.PDF for Python installed in your environment

## Install

```bash
pip install aspose-pdf
```

## Run An Example

Each file is directly runnable:

```bash
python day03.py
```

Each script creates one PDF named after the file, such as `day03.pdf`.

## Tutorial Index

| File | Topic |
| --- | --- |
| `day01.py` | Create a PDF and add a simple positioned text fragment |
| `day02.py` | Apply basic font styling such as font family, size, color, bold, and underline |
| `day03.py` | Build paragraph text with indentation, layout rectangle, and word wrapping |
| `day04.py` | Insert HTML content into a PDF with `HtmlFragment` |
| `day05.py` | Render LaTeX-style math content with `TeXFragment` |
| `day06.py` | Add transparent text using ARGB color values |
| `day07.py` | Demonstrate wider character spacing values |
| `day08.py` | Demonstrate tighter character spacing values |
| `day09.py` | Control line spacing in a wrapped paragraph |
| `day10.py` | Control line spacing in explicit multi-line text |
| `day11.py` | Render an ordered list from LaTeX enumerate markup |
| `day12.py` | Rotate text at multiple angles and combine rotation with styling |
| `day13.py` | Search for and extract matching text fragments from a generated PDF |

## Output Files

Each tutorial writes a PDF in the working directory using the same naming pattern:

- `day01.pdf`
- `day02.pdf`
- `day03.pdf`
- `day04.pdf`
- `day05.pdf`
- `day06.pdf`
- `day07.pdf`
- `day08.pdf`
- `day09.pdf`
- `day10.pdf`
- `day11.pdf`
- `day12.pdf`
- `day13.pdf`

Generated PDFs are ignored by Git.

## Notes

- The examples are intentionally minimal and avoid external input files.
- `day13.py` creates a sample document first, then searches it for matching text.

## Purpose

The examples are organized as short, focused exercises rather than as a package or application. The intended workflow is to open one file at a time, run it, inspect the generated PDF, and adapt the snippet for your own PDF automation tasks.
