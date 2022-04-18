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
echo "# FER SRS Lab2 demonstration"
echo
exec rm -rf data.bin
exec $python3 usermgmt.py add sgros --test <<< $'testtesttest\ntesztesttest'
echo
exec $python3 usermgmt.py add sgros --test <<< $'testtesttest\ntesttesttest'
echo
exec $python3 login.py sgros --test <<< $'testtesttest'
echo
exec $python3 usermgmt.py passwd sgros --test <<< $'sifrasifra\nsifrqsifra'
echo
exec $python3 usermgmt.py passwd sgros --test <<< $'sifrasifra\nsifrasifra'
echo
exec $python3 login.py sgros --test <<< $'testtesttest\nsifrasifra'
echo
exec $python3 usermgmt.py forcepass sgros --test
echo
exec $python3 login.py sgros --test <<< $'sifrasifra\nnovasifra'
echo
exec $python3 login.py sgros --test <<< $'sifrasifra\nnovaasifra\nnovqqsifra'
echo
exec $python3 login.py sgros --test <<< $'sifrasifra\nnovaasifra\nnovaasifra'
echo
exec $python3 login.py sgros --test <<< $'novaasifra'
echo
exec $python3 usermgmt.py del sgros --test
echo
exec $python3 login.py sgros --test <<< $'novaasifra\nsifrasifra\ntesttesttest'
