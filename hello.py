def main():
    charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!',',',' ']
    word = ['H','e','l','l','o',',',' ','W','o','r','l','d','!']
    made_word=[]
    for num1 in range(len(word)):
        for num in range(len(charlist)):
            char=charlist[num]
            need_char=word[num1]
            if char==need_char:
                print(char)
                made_word.append(char)
    print(made_word)
    print('converting to string...')
    made_str=''
    for i in made_word:
        made_str=made_str+i
    print(made_str)
    return made_str