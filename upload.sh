
echo changed version?

read

python -m build

twine upload dist/*

