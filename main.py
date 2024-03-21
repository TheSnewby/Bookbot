def main():
  with open("books/frankenstein.txt") as f:
   file_contents = f.read()
   #word_count=countWords(file_contents)
   #print(f'There are {word_count} words in Frankenstein.')
   #num_letters=countLetters(file_contents)  
   #print(f'These are the number of each letter in Frankenstein {num_letters}')
   print(f'--- Report of Frankenstein.txt ---')
   report_list=book_report(file_contents)
   print(*report_list, sep="\n")

def countWords(passed_book):
   count =0
   words=passed_book.split()
   for word in words:
     count+=1
   return count

def countLetters(passed_book):
  lowered_book=passed_book.lower()
  discovered_letters={}
  for letter in lowered_book:
    if letter not in discovered_letters and letter.isalpha():
      discovered_letters[letter]=1
    elif letter in discovered_letters and letter.isalpha():
      discovered_letters[letter]+=1
  return discovered_letters

def sort_on(dict): #sorts on the number of letters
  return dict["num"]

def book_report(passed_book):
  word_count=countWords(passed_book)
  num_letters=countLetters(passed_book) #dictionary
 
  report=[]
  report.append(f'There are {word_count} words in Frankenstein.')
  
  temp_list=[] #converts the Letter Count dictionary to a list of dicts
  for dic in num_letters: 
    temp_list.append({"letter":dic,"num":num_letters[dic]})
  temp_list.sort(key=sort_on, reverse=True) #sorts by values
  

  for letter in temp_list:#appends the letter count information to the report
    a=letter["num"]
    b=letter["letter"]
    report.append(f'There are {a} instances of the letter \'{b}\' in Frankenstein.')
  return report
      

if __name__ == '__main__':
   main()