from distutils import text_file


dic_word = { "a": "apple", "b": "Boy"}

for key  in dic_word:
  print(key, dic_word[key])

text = "I know you well well"

text_diction = {}

for word in text.lower().split():
  if word in text_diction:
    text_diction[word] += 1
  else: 
    text_diction[word] = 1

print(text_diction)
