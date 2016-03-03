:: cleanup
rm -r dist
mkdir dist

:: make python executable in dist folder
pyinstaller src/poe_filter_finder.py

:: move non-code files in to dist directory
cp LICENSE dist/poe_filter_finder/LICENSE
cp README.md dist/poe_filter_finder/README.md

:: Requires 7zip, zips the file for distribution
7za a dist/poe_filter_finder dist/poe_filter_finder/ -tzip -mx9
