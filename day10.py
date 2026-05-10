import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text = "First line\nSecond line\nThird line\nFourth line"

fragment = ap.text.TextFragment(text)
fragment.text_state.font_size = 12
fragment.text_state.line_spacing = 20

page.paragraphs.add(fragment)
document.save("day10.pdf")
