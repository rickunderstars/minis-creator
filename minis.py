import sys
import subprocess
import shlex


args = sys.argv[1:]

safe_args = " ".join(shlex.quote(arg) for arg in args)

rmbg = f"""

function rmbg
	if test (count $argv) -eq 0
		exit 1
	end


	set -l model birefnet-general
	set -l outdir rmbg
	mkdir -p $outdir


	for img in $argv
		set -l dir (dirname $img)
		set -l base (basename $img)
		set -l name (string split -r -m1 . $base)[1]
		set -l ext (string split -r -m1 . $base)[2]

		set -l alpha $name-alpha.$ext
		set -l back $name-back.$ext

		echo "Working on '$img':"

		echo "Removing background..." &&
		rembg i -m $model $img $outdir/$alpha &&

		echo "Trimming borders..." &&
		magick $outdir/$alpha -fuzz 1% -trim +repage -bordercolor none -border 10 $outdir/$alpha &&

		echo "Generating back image..." &&
		magick $outdir/$alpha -fill black -colorize 100% -flop $outdir/$back
	end

	echo "Done."
end

rmbg {safe_args}

"""


subprocess.run(["fish", "-c", rmbg])

print("args:", args)
