#!/bin/bash
#./.sh dir filename1 filename2 ...

# 检查传入的参数是否足够
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 directory file1 [file2 ...]"
  exit 1
fi

# 获取传入的目录
directory=$1
shift  # 移除第一个参数（目录），后面的参数是文件名

# 创建一个不存在文件的列表
missing_files=()

# 遍历传入的文件名
for filename in "$@"; do
  # 使用 find 命令在指定目录递归查找文件
  if ! find "$directory" -type f -name "$filename" -print -quit | grep -q .; then
    missing_files+=("$filename")  # 如果找不到，添加到 missing_files 列表
  fi
done

# 如果 missing_files 不为空，输出不存在的文件名列表
if [ "${#missing_files[@]}" -ne 0 ]; then
  echo "The following files were not found in $directory:"
  for file in "${missing_files[@]}"; do
    echo "$file"
  done
else
  # 如果所有文件都存在，返回空
  echo ""
fi
