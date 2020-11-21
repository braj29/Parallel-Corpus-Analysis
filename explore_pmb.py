from utils import sort_docs, get_tokens, get_pairs, get_doc_text
import glob
import os

path_pmb = '../Data/pmb/pmb-2.1.0/data/gold'
language_doc_dict = sort_docs(path_pmb)

languages = language_doc_dict.keys()

for language in languages:
    n_docs = len(language_doc_dict[language])
    docs = language_doc_dict[language]
     #your code here
    tokens_n = []

    for doc in docs:
        path_to_doc = f'{doc}/{language}.drs.xml'
        tokens = get_tokens(path_to_doc)
        length = len(tokens)
        tokens_n.append(length)
    n_tokens = sum(tokens_n)
    print(f'{language}: num docs: {n_docs}, num tokens: {n_tokens}')

pairs = get_pairs(languages)
print(pairs)

for lang1, lang2 in pairs:
    docs_lang1 = language_doc_dict[lang1]
    docs_lang2 = language_doc_dict[lang2]
    #print(len(docs_lang1))
    #print(len(docs_lang2))
    number_of_docs = len(docs_lang1.intersection(docs_lang2))
    #print(len(docs_in_two))
    print(f'Coverage for parallel data in {lang1} and {lang2}: {number_of_docs}')

v1 = input("Please enter the first language for comparison(for eg. en, it, de, nl): ")
v2 = input("Please enter the second language for comparison(for eg. en, it, de, nl): ")

documents1 = language_doc_dict[v1]
documents2 = language_doc_dict[v2]
docs3 = documents1.intersection(documents2)

for docu in docs3:
    name = docu.replace('\\','/')
    paths = glob.glob(f'{name}/*.xml')



    for path in paths:
        #print(path)
        file = get_doc_text(path)

        print(file)
        ask = input("One more file?(yes/no):")
    if ask == "no":
        break
    
