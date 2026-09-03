
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
				  image("imgs/assassino-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/assassino-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/caduto-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/caduto-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/cavaliere-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/cavaliere-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/elementale-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/elementale-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/gorgone-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/gorgone-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/scatola-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/scatola-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/serpente-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/serpente-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			
				#couple(
				  image("imgs/teschio-alpha.png", height: 7cm, fit: "contain"),
				  image("imgs/teschio-back.png", height: 7cm, fit: "contain"),
				)

				#v(1.5cm)
			