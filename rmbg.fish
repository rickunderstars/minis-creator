#!/usr/bin/env fish

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