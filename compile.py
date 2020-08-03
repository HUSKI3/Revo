from tokens import tokenizer, compiler
import os
import sys
#open file
class RevoMain:
  def __init__(self, filename):
    self.f = open(filename,"r")
  def main(self):
    tokenizer.gentokens(self.f)
  def build(self):
    compiler.scel(self.f)

    


if __name__ == "__main__":
  p = RevoMain("test.rv")
  p.build()
  print("=== Output ===")
  os.system("gcc build/temp.c ")
  os.system("./a.out")

p = RevoMain(str(sys.argv[1]))
p.build()
print("=== Output ===")
os.system("gcc build/temp.c -o revobin")
os.system("./revobin")
