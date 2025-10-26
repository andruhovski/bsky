# Copilot Instructions for bsky

This codebase is a Python tutorial series demonstrating PDF manipulation using the Aspose.PDF library.

## Project Structure and Patterns

### File Naming Convention
- Daily tutorial files follow `dayXX.py` pattern (day01.py, day02.py, etc.)
- Each file demonstrates a specific PDF text manipulation technique
- Files are standalone examples that can be run independently

### Core Library Usage
- **Primary dependency**: `aspose.pdf` (imported as `ap`)
- **Document creation pattern**: Always start with `document = ap.Document()` then `page = document.pages.add()`
- **Save pattern**: All examples end with `document.save(filename)`

### Common Code Patterns

#### Text Fragment Creation
```python
text_fragment = ap.text.TextFragment("Your text here")
text_fragment.position = ap.text.Position(x, y)  # Positioning
page.paragraphs.add(text_fragment)
```

#### Text Styling
- Font: `text_fragment.text_state.font = ap.text.FontRepository.find_font("FontName")`
- Size: `text_fragment.text_state.font_size = 14`
- Color: `text_fragment.text_state.foreground_color = ap.Color.blue`
- Effects: `text_fragment.text_state.font_style = ap.text.FontStyles.BOLD`

#### Advanced Content Types
- **HTML content**: Use `ap.HtmlFragment(html_content)`
- **LaTeX math**: Use `ap.TeXFragment(latex_content)`
- **Paragraphs**: Use `ap.text.TextParagraph()` for complex text layouts

### File Organization
- `DATA_DIR` constant points to "E:\\Samples\\Text" (Windows-specific path)
- Functions use descriptive names like `add_text_simple_case()`, `add_text_with_font_styling()`
- Output files typically saved in current directory with descriptive names

### Development Guidelines
- Each day's file should be a complete, runnable example
- Include docstrings for functions explaining the PDF operation being demonstrated
- Use consistent positioning coordinates (common: x=100, y=600-800 range)
- Always test PDF generation by running the script and checking output file

### Tutorial Progression
- **day01.py**: Basic text addition
- **day02.py**: Font styling and formatting
- **day03.py**: Paragraph formatting with text wrapping
- **day04.py**: HTML content embedding
- **day05.py**: LaTeX mathematical expressions
- **day06.py**: Transparent text effects

When adding new tutorial files, follow the established pattern of demonstrating one specific Aspose.PDF feature per file.