# Copilot Instructions for bsky

This codebase is a Python tutorial series demonstrating PDF manipulation using the Aspose.PDF library.

## Project Structure and Patterns

### File Naming Convention

- Daily tutorial files follow `dayXX.py` pattern (day01.py through day10.py, etc.)
- Each file demonstrates a specific PDF text manipulation technique
- Files are standalone examples that can be run independently

### Core Library Usage

- **Primary dependency**: `aspose.pdf` (imported as `ap`)
- **Document creation pattern**: Always start with `document = ap.Document()` then `page = document.pages.add()`
- **Save pattern**: All examples end with `document.save(filename)`
- **Import variations**: Use specific imports for clarity: `from aspose.pdf.text import TextFragment, FontRepository`

### Common Code Patterns

#### Rectangle Creation

```python
rectangle = ap.Rectangle(llx, lly, urx, ury, True)
```

#### Text Fragment Creation

```python
text_fragment = ap.text.TextFragment("Your text here")
text_fragment.position = ap.text.Position(x, y)  # Positioning (optional)
page.paragraphs.add(text_fragment)
```

#### Text Styling Properties

- Font: `text_fragment.text_state.font = FontRepository.find_font("Arial")`
- Size: `text_fragment.text_state.font_size = 14`
- Color: `text_fragment.text_state.foreground_color = ap.Color.blue`
- Effects: `text_fragment.text_state.font_style = ap.text.FontStyles.BOLD`
- Spacing: `text_fragment.text_state.character_spacing = 2.0`
- Line height: `text_fragment.text_state.line_spacing = 16`

#### Advanced Content Types

- **HTML content**: Use `ap.HtmlFragment(html_content)`
- **LaTeX math**: Use `ap.TeXFragment(latex_content)`
- **Paragraphs**: Use `ap.text.TextParagraph()` for complex text layouts

### File Organization

- `DATA_DIR` constant points to "E:\\Samples\\Text" (Windows-specific path)
- External text files loaded with fallback: `open(path).read() if os.path.exists(path) else "fallback text"`
- Output PDFs saved in current directory with descriptive names
- All PDFs ignored in `.gitignore` with `*.pdf` pattern

### Development Environment

- Uses `.venv/` virtual environment (ignored in git)
- No requirements.txt - dependencies managed through pip/conda
- Standard Python .gitignore with PDF output exclusions

### Tutorial Progression

- **day01-02**: Basic text and font styling
- **day03**: Paragraph formatting with text wrapping
- **day04-05**: HTML content and LaTeX math embedding
- **day06**: Transparent text effects
- **day07-08**: Character spacing variations
- **day09-10**: Line spacing and external file integration

When adding new tutorial files, follow the established pattern of demonstrating one specific Aspose.PDF feature per file.