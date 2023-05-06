# import glob

# path = 'src/src_*/'  # 해당 경로의 모든 폴더 내의 txt 파일을 가져오기 위한 경로

# # 하나로 합칠 파일명 지정
# output_filename = 'merged.txt'

# # 파일을 읽어와서 하나의 파일로 합치기
# with open(output_filename, 'w') as outfile:
#     for filename in glob.glob(path + '*.txt'):
#         with open(filename, 'r') as infile:
#             outfile.write(infile.read())

# with open('merged.txt', 'r') as f:
#     lines = f.readlines()

# new_lines = []
# for line in lines:
#     new_line = line[3:].rstrip()  # 앞 3글자와 개행 문자 없애기
#     new_lines.append(new_line)

# with open('new.txt', 'w') as f:
#     f.write('\n'.join(new_lines))  # 리스트를 문자열로 변환하여 파일에 쓰기

with open('new.txt', 'r') as f:
    text = f.read().replace('\n', '')

with open('data.txt', 'w') as f:
    f.write(text)
