#!/bin/bash
# Dominik Matijaca 0036524568

if uname -o | grep -q "Msys"; then
	python3="py"
else
	python3="python3"
fi

exec()
{
    echo $ $@
    $@
}

echo
echo "# FER SRS Lab1 demonstration"
echo
exec rm -rf data.bin
exec $python3 tajnik.py get mAsterPasswrd www.fer.hr
echo
exec $python3 tajnik.py init mAsterPasswrd
echo
exec $python3 tajnik.py put mAsterPasswrd www.fer.hr neprobojnAsifrA
echo
exec $python3 tajnik.py get mAsterPasswrd www.fer.hr
echo
exec $python3 tajnik.py get wrongPasswrd www.fer.hr
