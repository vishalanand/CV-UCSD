for name in FudanPed000*
do
    newname=test-"$(echo "$name" | cut -c12-)"
    mv "$name" "$newname"
done