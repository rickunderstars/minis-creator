#set page(paper: "a4", flipped: false, margin: 1cm)

#let couple(lft, rgt) = {
  grid(
    columns: (1fr, 1fr),
    column-gutter: 0pt,
    align: (right, left),
    lft, rgt,
  )
}

#couple(
  image("rmbg/assassino-alpha.png", height: 7cm, fit: "contain"),
  image("rmbg/assassino-back.png", height: 7cm, fit: "contain"),
)

#v(1.5cm)

#couple(
  image("rmbg/gorgone-alpha.png", height: 7cm, fit: "contain"),
  image("rmbg/gorgone-back.png", height: 7cm, fit: "contain"),
)
