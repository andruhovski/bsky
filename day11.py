import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

latex_content = r"""
\begin{enumerate}
\item First item in the ordered list
\item Second item in the ordered list
\item Third item in the ordered list
\item Fourth item in the ordered list
\item Fifth item in the ordered list
\end{enumerate}
"""

latex_fragment = ap.TeXFragment(latex_content)

page.paragraphs.add(latex_fragment)
document.save("day11.pdf")
