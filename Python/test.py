ransomNote = 'aa'
magazine = 'ab'

for char in ransomNote:
    if magazine.find(char) == -1:
        print(false)
    magazine = magazine.replace(char, '', 1)
    print(ransomNote, magazine)
