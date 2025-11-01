import aspose.pdf as ap
from aspose.pdf.text import TextFragment, FontRepository

doc = ap.Document()
page = doc.pages.add()

for spacing in [2.0, 1.0, 0.75]:
    fragment = TextFragment("Sample Text with character spacing")
    fragment.text_state.font = FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = spacing
    page.paragraphs.add(fragment)

doc.save("character_spacing.pdf")