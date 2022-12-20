# Table of Contents

<!-- vim-markdown-toc GFM -->

* [Basics of LaTeX](#basics-of-latex)
* [Mathematics](#mathematics)
	* [Fractions](#fractions)
	* [Greek letters](#greek-letters)
	* [Bar](#bar)
	* [Roots](#roots)

<!-- vim-markdown-toc -->

# Basics of LaTeX

first example
```
\documentclass{article}
\begin{document}
something
\end{document}
``` 

preamble of document
```
\documentclass[10pt, a4paper]{article}
\usepackage{some_package}
```

title, author, date
```
\title{some title}
\author{somebody}
\date{a_month in_a_year}
\maketitle
```

comment
```
% some comment
```

bold, italics, underlined, emphasized
```
\textbf{some \emph{bold} text}
\textit{some \textbf{italic} text}
\underline{some underlined text}
```

use image
```
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{path_to_folder_of_images}}

\begin{document}
some text
\includegraphic{an_image_file_name}
\end{document}
```

image configuration
```
\begin{figure}[h]
	\centering
	\includegraphics[width=0.9\textwidth]{image_file_name}
	\caption{some caption text}
	\label{fig:some_label}
\end{figure}
```

reference an image
```
you should see \ref{fig:some_label}
```

unordered list
```
\begin{itemize}
  \item item one
  \item item two
\end{itemize}
```

ordered list
```
\begin{enumerate}
  \item item 1
  \item item 2
\end{enumerate}
```

inline math
```
$4=2^2$
```
```
\begin{math}
4=2^2
\end{math}
```

numbered math formula
```
\begin{equation}
4=2^2
\end{equation}
```

unnumbered math formula
```
some text and a formula in new line \[ 4=2^2\] rest of the text in new line
```

section
```
\section{first section}
```

abstract in article
```
\begin{abstract}
some abstract text
\end{abstract}
```

chapters, sections, paragraphs
```
\chapter{first chapter}

\section{first section in the first chapter}
some text in this section

\paragraph{first paragraph}
some texts in this paragraph

\subsection{first subsection in the first section}
some text in this subsection

\section*{unnumbered section}
some text in this unnumbered section

\chapter{second chapter}
```

# Mathematics
## Fractions
```
\frac{numerator}{denominator}
```

## Greek letters
Uppercase sigma
```
\Sigma
```

Lowercase sigma
```
\sigma
```

## Bar
```
\bar{word}
```

## Roots
```
\sqrt{number}
```
```
\sqrt[n]{number}
```
