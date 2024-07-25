
echo "BUILD START"
python3.11.9 -m pip install -r requirement.txt
python3.11.9 manage.py collectstatic --noinput --clear
exho "BUILD END"