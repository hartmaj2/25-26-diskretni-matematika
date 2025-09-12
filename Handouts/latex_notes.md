# LaTeX notes

## Document class

Each document must have `\documentclass` specified.
The format is `\documentclass[options]{class}`
- options - paper size (a5,a4), text font, single/two column, landscape etc.
- class - article, report, book (differ in sections vs chapters, different page numbering etc.)

## Preamble

Here list of all used packages:
- geometry - sets the layout of the paper (a4,a5), margins etc.
  - pro tip - use `showframe` option for debugging
- fancyhdr - used to control headers and footers with `\fancyhead[align]{content}` and `\fancyhead{content}`
  - TODO: why we need `\pagestyle{fancy}` and `\fancyhf`
- titling - allows to use metadata like title, author and date using `thetitle`, `thedate` etc.
- hyperref - enables to use the `\url` command

## Making new commands
- use syntax `\newcommand{command_sequence}{action}`

## Useful commands
- make font size of text different - `\scriptsize`,`\small` etc.