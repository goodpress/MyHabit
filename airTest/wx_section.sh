#!/bin/bash
echo "start kill wx..."

echo "start loop ..."
for i in {1..330}
do
#    /Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE runner "/Users/wyk/Desktop/aa/justKill.air"  --device Android://127.0.0.1:5037/SJE5T17515006720 --log "/Users/wyk/Desktop/1"
    echo "working in $i ..."
    /Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE runner "/Users/wyk/Desktop/aa/single_section.air"  --device Android://127.0.0.1:5037/SJE5T17515006720 --log "/Users/wyk/Desktop/1"
done

