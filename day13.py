import aspose.pdf as ap
from aspose.pdf.text import TextFragmentAbsorber, FontRepository

input_file_path = "sample.pdf"

document = ap.Document()

absorber = ap.text.TextFragmentAbsorber(
    "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
)

document.pages[2].accept(absorber)

for fragment in absorber.text_fragments:
    print("Text:", fragment.text)
    print("Position:", fragment.position)