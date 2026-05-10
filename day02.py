import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text_fragment = ap.text.TextFragment("Hello, Aspose!")
text_fragment.position = ap.text.Position(100, 600)
text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
text_fragment.text_state.font_size = 14
text_fragment.text_state.foreground_color = ap.Color.blue
text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
text_fragment.text_state.underline = True

page.paragraphs.add(text_fragment)
document.save("day02.pdf")

