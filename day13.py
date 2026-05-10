import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

page.paragraphs.add(ap.text.TextFragment("An elephant is the largest land animal."))
page.paragraphs.add(ap.text.TextFragment("This example searches for the word elephant."))

absorber = ap.text.TextFragmentAbsorber(
    "elephant",
    ap.text.TextSearchOptions(ap.Rectangle(0, 0, 595, 842, True)),
)

document.pages[1].accept(absorber)

document.save("day13.pdf")

for fragment in absorber.text_fragments:
    print("Text:", fragment.text)
    print("Position:", fragment.position)