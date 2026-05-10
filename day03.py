import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text = "Lorem ipsum sample text..."
para = ap.text.TextParagraph()
para.first_line_indent = 20
para.rectangle = ap.Rectangle(80, 800, 400, 200, True)
para.formatting_options.wrap_mode = (
    ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
)

frag = ap.text.TextFragment(text)
frag.text_state.font = (
    ap.text.FontRepository.find_font("Times New Roman")
)
frag.text_state.font_size = 12

para.append_line(frag)
ap.text.TextBuilder(page).append_paragraph(para)

document.save("day03.pdf")