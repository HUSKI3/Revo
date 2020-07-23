import parser

class tokenizer:
  keywords = [
    "print",   # terminal output
    "//",      # comment 
    "stat",    # code statistics
    "const",   # create a constant variable
    "redest",  # redestribute resources 
    "contort", # clean the output logs in output.logs.rv
    "str",     # create string object
    "int",     # create integer object /  initalize new function
    "bool",    # create boolean object
    "if",      # simple if statement
    "line-end",# system reserved
    "supercoolfunction", # whatever the heck this is
    "input",   # takes string input up to 100 characters 
    "open",    # open files
    "read",    # read everything from files
    "close"    # close file
    "main",    # main function
    "re_void"  # replaces "static void" for easier use
  ]
  operators = [
    "{",
    "}"
  ]

  tokens = []

  def peak_next_char(line,word,pos):
    line = line.split(" ")
    word = line[word]
    return word[pos]

  def gentokens(code):
    print("=== Starting tokenizer ===")
    #create code split list
    lines = code.readlines()
    imp=[]
    for line in lines:
      line = line[:-1]
      for i in line.split(" "):
        imp.append(i)
      imp.append("line-end")
    #check keywords and display information about keywords
    print("------------" + (' ' * 15)  + "   " + "revoval " + "||| " + "description")
    for token in imp:
      desc=""
      #is token a valid function?
      if token in tokenizer.keywords:
        revoval = "yes"
        #check parser for information about the token
        desc = parser.parse(token,False,line)
      else:
        revoval = "no"
      print("--- > Token: " + token + (' ' * (15-len(token)))  + "<---- " + revoval + (' ' * (4-len(revoval))) + "||| " + desc)


class compiler:
  # augments can be set here
  aug = "None"

  # build base sceleton 
  def scel(code):
    print("Building C sceleton")
    with open("build/temp.c","w+") as f:
      #translate Revo to C for compilation using parser
      print("=== Starting translation ===")
      #header
      f.write("#include <stdio.h> \n")
      #create code split list
      lines = code.readlines()
      imp=[]
      i=0
      finalcode = ""
      for line in lines:
        line = line[:-1]
        for i in line.split(" "):
          imp.append(i)
        imp.append("line-end")
      #check keywords and display information about keywords
      print("------------" + (' ' * 15)  + "   " + "revoval " + "||| " + "description")
      i=0
      for token in imp:
        rev_bit=""
        #is token a valid function?
        if token in tokenizer.keywords or token in tokenizer.operators:
          revoval = "yes"
          #check parser for information about the token and if possible value
          rev_bit = parser.parse(token,True,line)
          if rev_bit == "//":
            i+=1
            f.write(str(rev_bit))
            if i == 2:
              i=0
          else:
            if token in tokenizer.operators:
              finalcode += "\n"
            if token == "line-end":
              if imp[imp.index(token)-1] in tokenizer.operators:
                finalcode += "\n"
              else:
                finalcode += ";\n"
            else:
              finalcode += " "+rev_bit+" "
        else:
          revoval = "no"
          finalcode += " "+token+" "
        print("--- > Token: " + token + (' ' * (15-len(token)))  + "<---- " + revoval + (' ' * (4-len(revoval))) + "||| " + rev_bit)
      print(finalcode)
      f.write(finalcode)
      f.write("\nreturn 0;\n}")
      f.close()