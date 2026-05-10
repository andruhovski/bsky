import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text = ap.text.TextFragment(
    "This is transparent text. "
    "This is transparent text. "
    "This is transparent text."
)
text.text_state.foreground_color = ap.Color.from_argb(0, 0, 255, 0)

page.paragraphs.add(text)

document.save("day06.pdf")
