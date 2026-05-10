import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

for spacing in [0.0, -1.0, -2.0]:
    fragment = ap.text.TextFragment(f"Tighter spacing: {spacing}")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = spacing
    page.paragraphs.add(fragment)

document.save("day08.pdf")