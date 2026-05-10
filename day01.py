import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text_fragment = ap.text.TextFragment("Hello, Aspose!")
text_fragment.position = ap.text.Position(100, 700)

page.paragraphs.add(text_fragment)
document.save("day01.pdf")


