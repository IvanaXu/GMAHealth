
python code/run.py

git add *;echo;
git commit -m "Update $(date "+%Y%m%d%H%M%S"|md5sum)";echo;
proxychains4 git push;echo;
