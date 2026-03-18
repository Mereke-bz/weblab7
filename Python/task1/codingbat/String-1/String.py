#hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make_abba
def make_abba(a, b):
  return a + b +b + a

#make_out_word
def make_out_word(out, word):
  return out[0]+ out[1] + word+ out[2] + out[3]

#first_two
def first_two(str):
  return str[:2] if len(str) >2 else str

#first_half
def first_half(str):
  return str[:len(str) / 2]


#without end
def without_end(str):
  return str[1:len(str) -1]


#combo_String
def combo_string(a, b):
  return a + b + a if len(a) <len(b) else b + a +b

#non_start
def non_start(a, b):
  return a[1:] + b[1:]



