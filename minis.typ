
#set page(paper: "a4", flipped: true, margin: 1cm, columns: 2)

#let couple(lft, rgt) = context {
  let h = measure(lft).height
  grid(
    columns: (1fr, 0.7cm, 1fr),
    column-gutter: 0pt,
    align: (right, center, left),
    lft, line(stroke: 1pt + luma(222), angle: 90deg, length: h), rgt,
  )
}


#couple(
  image("imgs/assassino-alpha.png", width: 3.0cm, fit: "contain"),
  image("imgs/assassino-back.png", width: 3.0cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/caduto-alpha.png", width: 6.0cm, fit: "contain"),
  image("imgs/caduto-back.png", width: 6.0cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/cavaliere-alpha.png", width: 4.5cm, fit: "contain"),
  image("imgs/cavaliere-back.png", width: 4.5cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/gorgone-alpha.png", width: 3.0cm, fit: "contain"),
  image("imgs/gorgone-back.png", width: 3.0cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/melma-alpha.png", width: 2.5cm, fit: "contain"),
  image("imgs/melma-back.png", width: 2.5cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/oracolo-alpha.png", width: 4.5cm, fit: "contain"),
  image("imgs/oracolo-back.png", width: 4.5cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/serpente-alpha.png", width: 6.0cm, fit: "contain"),
  image("imgs/serpente-back.png", width: 6.0cm, fit: "contain"),
)

#v(2cm)


#couple(
  image("imgs/trent-alpha.png", width: 3.0cm, fit: "contain"),
  image("imgs/trent-back.png", width: 3.0cm, fit: "contain"),
)

#v(2cm)

