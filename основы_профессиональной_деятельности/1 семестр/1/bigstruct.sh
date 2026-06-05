mkdir source && cd source
echo "text \ntextone0" > text0 
mkdir dir && cd dir
echo "text \ntextone1" > text1 
echo "text \ntextone2" > text2
mkdir first && cd first
echo "texttexttext" > textfirst
cd ../../../
mkdir target && cd target
echo "text \ntextwo0" > text0
echo "text" > textarget
mkdir dir && cd dir
echo "text \ntextwo1" > text1 
echo "textwo2" > text2
mkdir second && cd second
echo "texttexttext" > textsecond