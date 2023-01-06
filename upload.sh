
echo changed version?

read

rm -rf build
rm -rf dist
rm -rf flagser.egg-info


python -m build

twine upload dist/*

