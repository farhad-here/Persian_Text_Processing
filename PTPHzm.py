#library
from bidi.algorithm import get_display
import arabic_reshaper
import parsivar as pars
# import parsivar as pars

#open file and read
with open('./PersianText.txt','r',encoding='utf-8') as file:
       text = file.read()

#Normalizer
normal = pars.Normalizer()
normalized_text = normal.normalize(text)

#fixing display of persian text in output
reshaped_text = arabic_reshaper.reshape(normalized_text)
bidi_text = get_display(reshaped_text)
print(bidi_text)
print('====================================================================')
#tokenize
tokenizer = pars.Tokenizer()
tokenized_sent = tokenizer.tokenize_sentences(bidi_text)
print(tokenized_sent)
print('====================================================================')
tokenized_word = tokenizer.tokenize_words(bidi_text)
print(tokenized_word)

print('====================================================================')
#Stemmer
stemmer = pars.FindStems()
stem_token = [stemmer.convert_to_stem(i) for i in tokenized_word]
print(stem_token)
print('====================================================================')

word_tests = ['درختان' ,'اژدها' ,'رفتارها' ,'برقص' ,'بنواز' ,'کفار' ,'برآشفتن']
for i in word_tests:
       reshaped_test = arabic_reshaper.reshape(i)
       bidi_test = get_display(reshaped_test)
       x = stemmer.convert_to_stem(i)
       reshaped_test_s = arabic_reshaper.reshape(x)
       bidi_test_s = get_display(reshaped_test_s)
       print(bidi_test, ">>",bidi_test_s)
print('====================================================================')
#check
spell = pars.SpellCheck()
misspeled = 'صلام من به ذبان فارصی مسلت هستم'
spell_check = spell.spell_corrector(misspeled)
reshape_check = arabic_reshaper.reshape(spell_check)
bidi_check = get_display(reshape_check)
print(bidi_check)