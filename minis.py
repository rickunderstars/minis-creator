import sys
import subprocess
import shlex
from pathlib import Path

imgs_dir = "imgs"

args = sys.argv[1:]

safe_args = " ".join(shlex.quote(arg) for arg in args)

rmbg = f"""

	function rmbg
		if test (count $argv) -eq 0
			exit 1
		end


		set -l model birefnet-general
		set -l outdir {imgs_dir}
		mkdir -p $outdir


		for img in $argv
			set -l dir (dirname $img)
			set -l base (basename $img)
			set -l name (string split -r -m1 . $base)[1]
			set -l ext (string split -r -m1 . $base)[2]

			set -l alpha $name-alpha.$ext
			set -l back $name-back.$ext

			echo "> Working on '$img':"

			echo "	- removing background..." &&
			rembg i -m $model $img $outdir/$alpha &&

			echo "	- trimming borders..." &&
			magick $outdir/$alpha -fuzz 1% -trim +repage -bordercolor none -border 10 $outdir/$alpha &&

			echo "	- generating back image...\n" &&
			magick $outdir/$alpha -fill black -colorize 100% -flop $outdir/$back
		end

		echo "Image elaboration complete!\n\n"
	end

	rmbg {safe_args}

"""

subprocess.run(["fish", "-c", rmbg])

print("> Writing typst document...\n")

with open("minis.typ", "w") as file:
    file.write(
        """
#set page(paper: "a4", flipped: true, margin: 1cm, columns: 2)

#let couple(lft, rgt) = {
	grid(
		columns: (1fr, 1fr),
		column-gutter: 16pt,
		align: (right, left),
		lft, rgt,
	)
}

"""
    )

    for mini in args:
        mini_name = Path(mini).stem
        file.write(
            f"""

#v(1cm)

#couple(
  image("{imgs_dir}/{mini_name}-alpha.png", width: 3cm, fit: "contain"),
  image("{imgs_dir}/{mini_name}-back.png", width: 3cm, fit: "contain"),
)

#v(1cm)

"""
        )

print("Done!\n")
