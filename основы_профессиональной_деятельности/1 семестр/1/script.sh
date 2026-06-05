#!/bin/bash
# создаем заданный файл, попутно создавая все директории
function update_diff {
	local file="$1"
	local source="$2"
	local target="$3"
	local type_cat="$4"
	if [[ -e "diff${file}" ]]; then
		return
	fi
	local all_dirs=(`echo "$file" | tr "/" "\n"`)
	for (( i = 0; i < ${#all_dirs[@]} - 1; i++ )); do
		if [[ $i == 0 ]]; then
			cd "diff"; mkdir -p "${all_dirs[$i]}"
		else
			cd "${all_dirs[$i-1]}"; mkdir -p "${all_dirs[$i]}"
		fi
	done
	cd "$main_dir"
	case "$type_cat" in
		"copy" )
			cat "${source}${file}" > "diff${file}"
			;;
		"diff" )
			diff "${source}${file}" "${target}${file}" > "diff${file}"
			if [[ $? == 0 ]]; then
				rm "diff${file}"
			fi
			;;
	esac
}
# Выполняем сравнение для указанных директорий
function compare {
	local source="$1"
	local target="$2"
	for i in `find "$source" -type f | sed "s/$source//"`; do
		if [[ -e "$target$i" ]]; then
			update_diff "$i" "$source" "$target" "diff"
		else
			update_diff "$i" "$source" 0 "copy"
		fi
	done
}
source_dir="$1"
target_dir="$2"
main_dir=`pwd`
rm -rf "diff"
mkdir "diff"
compare "$source_dir" "$target_dir"
compare "$target_dir" "$source_dir"