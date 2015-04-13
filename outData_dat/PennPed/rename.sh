for f in *.dat; do mv "$f" "`echo $f | sed s/PennPed-bbox-000/ground-/`"; done
