import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

html_content = "<h1>Header <i>1</i></h1>"
for i in range(5):
    html_content += f"<p>Paragraph <b>{i+1}</b></p>"

html_content += "<p>a<sub>2</sub> + b<sup>3</sup></p>"
html_fragment = ap.HtmlFragment(html_content)

page.paragraphs.add(html_fragment)
document.save("day04.pdf")