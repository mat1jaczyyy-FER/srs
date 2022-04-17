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
exec $python3 usermgmt.py add sgros --test <<< $'test\ntesz\n'
echo
exec $python3 usermgmt.py add sgros --test <<< $'test\ntest\n'
echo
exec $python3 login.py sgros --test <<< $'test\n'
echo
exec $python3 usermgmt.py passwd sgros --test <<< $'sifra\nsifrq\n'
echo
exec $python3 usermgmt.py passwd sgros --test <<< $'sifra\nsifra\n'
echo
exec $python3 login.py sgros --test <<< $'sifra\n'
echo
exec $python3 usermgmt.py forcepass sgros --test
echo
exec $python3 login.py sgros --test <<< $'sifra\nnova\nnova\n'
echo
exec $python3 usermgmt.py del sgros --test
echo
exec $python3 login.py sgros --test
