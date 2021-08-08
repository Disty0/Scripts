#!/bin/bash

#ffmpeg-metaflac Artist Albume Date Photo

mkdir Flac

for file in *.wav
do

ffmpeg -i "$file" -n "${file/.wav}.flac"

TITLE=${file/.wav}
TITLE=${TITLE:3}

echo "TITLE=$TITLE
ARTIST=$1
DATE=$3
COMMENT=Converted from WAV to FLAC using FFmpeg
ALBUM=$2
TRACKNUMBER=${file: 0: 2}" > "${file/.wav}.meta"

metaflac --import-picture-from=$4 --import-tags-from="${file/.wav}.meta" "${file/.wav}.flac"

rm "${file/.wav}.meta"

mv "${file/.wav}.flac" Flac/ 
done 
