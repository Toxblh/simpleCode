#!/bin/sh
echo $1
filename=$(basename "$1")
extension="${filename##*.}"
filename="${filename%.*}"

ffmpeg -i $1 -vcodec h264 -acodec aac -strict -2 $filename.mp4 -loglevel panic
