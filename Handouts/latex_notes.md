# LaTeX notes

## Document class

Each document must have `\documentclass` specified.
The format is `\documentclass[options]{class}`
- options - paper size (a5,a4), text font, single/two column, landscape etc.
- class - article, report, book (differ in sections vs chapters, different page numbering etc.)

## Preamble

Possible to define pagestyle using `\pagestyle{style}` command:
- style - plain, empty, headings
  - with fancyheader - fancy

Here list of all used packages:
- geometry - sets the layout of the paper (a4,a5), margins etc.
  - pro tip - use `showframe` option for debugging
- fancyhdr - used to control headers and footers with `\fancyhead[align]{content}` and `\fancyhead{content}`
  - TODO: why we need `\pagestyle{fancy}` and `\fancyhf`
- titling - allows to use metadata like title, author and date using `thetitle`, `thedate` etc.
- hyperref - enables to use the `\url` command
- amsthm (American Mathematical Society theorems) 
  - allows for command `\newtheorem{env_name}{printed_name}`
  - used with `\begin{env_name}`
  - allows to create theorem styles `\newtheoremstyle{style name}{space above}{space below}{body font}{indent amount}{head font}{head punct}{after head space}{head spec}`

## Making new commands
- use syntax `\newcommand{command_sequence}{action}`

## Useful commands
- make font size of text different - `\scriptsize`,`\small` etc.