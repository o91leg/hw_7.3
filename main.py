with open('1.txt', 'r') as f1:
  file1 = f1.readlines()
  print(file1)
with open('2.txt', 'r') as f2:
  file2 = f2.readlines()
  print(file2)
with open('3.txt', 'r') as f3:
  file3 = f3.readlines()
  print(file3)
with open('sort.txt', 'w') as f_s:
  if len(file1) < len(file2) and len(file1) < len(file3):
    f_s.write('1.txt' + '\n')
    f_s.write(str(len(file1)) + '\n')
    f_s.writelines(file1)
    f_s.write('\n')
  elif len(file2) < len(file1) and len(file2) < len(file3):
    f_s.write('2.txt' + '\n')
    f_s.write(str(len(file2)) + '\n')
    f_s.writelines(file2)
    f_s.write('\n')
  elif len(file3) < len(file1) and len(file3) < len(file2):
    f_s.write('3.txt' + '\n')
    f_s.write(str(len(file3)) + '\n')
    f_s.writelines(file3)
    f_s.write('\n')
  if len(file1) < len(file2) and len(file1) > len(file3) or len(file1) > len(file2) and len(file1) < len(file3):
    f_s.write('1.txt' + '\n')
    f_s.write(str(len(file1)) + '\n')
    f_s.writelines(file1)
    f_s.write('\n')
  elif len(file2) < len(file1) and len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
    f_s.write('2.txt' + '\n')
    f_s.write(str(len(file2)) + '\n')
    f_s.writelines(file2)
    f_s.write('\n')
  elif len(file3) < len(file1) and len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
    f_s.write('3.txt' + '\n')
    f_s.write(str(len(file3)) + '\n')
    f_s.writelines(file3)
    f_s.write('\n')
  if len(file1) > len(file2) and len(file1) > len(file3):
    f_s.write('1.txt' + '\n')
    f_s.write(str(len(file1)) + '\n')
    f_s.writelines(file1)
  elif len(file2) > len(file1) and len(file2) > len(file3):
    f_s.write('2.txt' + '\n')
    f_s.write(str(len(file2)) + '\n')
    f_s.writelines(file2)
  elif len(file3) > len(file1) and len(file3) > len(file2):
    f_s.write('3.txt' + '\n')
    f_s.write(str(len(file3)) + '\n')
    f_s.writelines(file3)
