replace = { 'witnesses': 'dudes I know',
  'allegedely': 'kinda probably', 
  'new study': 'tumblr post', 
  'rebuilt': 'avenge',
  'space': 'spaace',
  'google glass': 'virtual boy',
  'smartphone': 'pokedex',
  'electric': 'atomic',
  'senator': 'elf-lord',
  'speaker': 'elf-lord',
  'car': 'cat',
  'election': 'eating contest',
  'congressional leaders': 'river spirits',
  'homeland security': 'homestar runner',
  'could not be reached for comment': 'is guilty and everyone knows it',
  'republican': 'orc',
  'democrat': 'hobbit'
}
 
news = """Senator johnson was caught stealing a smartphone on election night. 
witnesses say that he allegedly took the smartphone from a kindly old lady while she was washing her electric car. 
republican and democrat congressional leaders have vowed to hold hearings. Senator johnson could not be reached for comment."""

list_words = []
for word in news.split():
  list_words = list_words + [word]

def toString(lst):
  phrase = ''
  has_period = False
  for word in lst[:-1]:
    phrase = phrase + word + ' '
  last_word = lst[-1]
  if last_word[-1]=='.':
    has_period = True
    last_word = last_word[:-1]
  phrase = phrase + last_word
  return phrase, has_period

changed = ''
i = 0
while i in range(len(list_words)):
  word = list_words[i]
  j = i+1
  phrase, has_period = toString(list_words[i:j])

  while j<=len(list_words) and not phrase.lower() in replace:
    j+=1
    phrase, has_period = toString(list_words[i:j])

  if phrase.lower() in replace:
    if has_period:
      changed = changed + replace[phrase.lower()] + '. '
    else:
      changed = changed + replace[phrase.lower()] + ' '
    i = j
  else:
    changed = changed + word + ' '
    i+=1

with_caps = ''
k = 0
while k in range(len(changed)):
  if k==0:
    with_caps = with_caps + changed[k].upper()
  elif changed[k]=='.' and k+2<len(changed):
    with_caps = with_caps + '. ' + changed[k+2].upper()
    k = k+2
  else:
    with_caps = with_caps + changed[k]
  k+=1

print('')
print(with_caps)



