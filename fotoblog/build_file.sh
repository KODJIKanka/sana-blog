# build_files.sh
echo " BUILD START" 

python3 -m venv env
source env/bin/activate

pip3 install --root-user-action=ignore -r requirements.txt

echo " BUILD END"

python3 manage.py collectstatic --noinput --clear

#python manage.py makemigrations

#python manage.py migrate
#python3 manage.py collectstatic --noinput --clear 