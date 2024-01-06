for path in /Users/nguyenhung/Downloads/home/tests/newuser/tests/*
do
  echo "Checking: $path"
  python3 /Users/nguyenhung/Downloads/home/jafr.py /Users/nguyenhung/Downloads/home/tests/passwd < $path/test.in > $path/test.out
  #diff $path/test.out $path/test.actual
done