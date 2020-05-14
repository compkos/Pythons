def initials(text):
    #Ο κώδικάς σας θα πρέπει να ξεκινάει εδώ
    word_list=text.split();
    text_return=''
    for word in word_list:
      text_return=text_return+word[0].upper()+'. '
    return text_return

text_input=input('Give a sentence of words : ')
print (initials(text_input))