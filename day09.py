import aspose.pdf as ap, os

document = ap.Document()
page = document.pages.add()

lorem_path = os.path.join("E:\\Samples\\Text", "lorem.txt")
text = (
    open(lorem_path, "r", encoding="utf-8").read()
    if os.path.exists(lorem_path)
    else "Lorem ipsum text not found."
)

fragment = ap.text.TextFragment(text)
fragment.text_state.font_size = 12
fragment.text_state.line_spacing = 16  # Custom line spacing

page.paragraphs.add(fragment)
document.save("line_spacing.pdf")
