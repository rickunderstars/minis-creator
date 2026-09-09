import sys
import subprocess
import shlex
from pathlib import Path

imgs_dir = "imgs"

args = sys.argv[1:]

creatures = []

for mini in args:
    mini_name = Path(mini).stem
    size = input(f"""
 How big is '{mini_name}'?
	1 -> small
	2 -> medium
	3 -> large
	4 -> huge

~> """)

    if 0 <= int(size) <= 4:
        creatures.append((mini_name, int(size)))
    else:
        print("Invalid size, quitting...")
        sys.exit(1)

safe_args = " ".join(shlex.quote(arg) for arg in args)

rmbg = f"""

	function rmbg

		set n_args (count $argv)

		if test $n_args -eq 0
			exit 1
		end


		set -l model birefnet-general
		set -l outdir {imgs_dir}
		mkdir -p $outdir

		set i 1
		for img in $argv
			set -l dir (dirname $img)
			set -l base (basename $img)
			set -l name (string split -r -m1 . $base)[1]
			set -l ext (string split -r -m1 . $base)[2]

			set -l alpha $name-alpha.$ext
			set -l back $name-back.$ext

			echo "[$i/$n_args] >> Working on '$img':"

			echo "	- removing background..." &&
			rembg i -m $model $img $outdir/$alpha &&

			echo "	- trimming borders..." &&
			magick $outdir/$alpha -fuzz 1% -trim +repage -bordercolor none -border 10 $outdir/$alpha &&

			echo "	- generating back image...\n" &&
			magick $outdir/$alpha -fill black -colorize 100% -flop $outdir/$back

			set i (math $i + 1)
		end

		echo "Image elaboration complete!\n\n"
	end

	rmbg {safe_args}

"""

print("\n")

subprocess.run(["fish", "-c", rmbg], check=True)

print("> Writing typst document...\n")

with open("minis.typ", "w") as file:
    file.write("""
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

""")

    for mini in creatures:
        width = 2
        match mini[1]:
            case 1:
                width = 2.5
            case 2:
                width = 3.0
            case 3:
                width = 4.5
            case 4:
                width = 6.0

        file.write(f"""
#couple(
  image("{imgs_dir}/{mini[0]}-alpha.png", width: {width}cm, fit: "contain"),
  image("{imgs_dir}/{mini[0]}-back.png", width: {width}cm, fit: "contain"),
)

#v(2cm)

""")

print("> Compiling typst document...\n")

subprocess.run(["typst", "compile", "minis.typ"], check=True)

print("Done!\n")
