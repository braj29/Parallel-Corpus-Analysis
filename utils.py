import glob
import os
from collections import defaultdict
from lxml import etree

def sort_docs(path_pmb):

    gold_files = glob.glob(path_pmb+'/*/*/*.drs.xml')


    d = defaultdict(set)
    for path in gold_files:
        f_name = os.path.basename(path)
        remaining_path = path.rstrip(f_name)
        lang, ext1, ext= f_name.split('.')
        d[lang].add(remaining_path)

    return d

def get_doc_text(path_to_doc):

    #Your code here
    tree = etree.parse(path_to_doc)
    root = tree.getroot()

    all_elements = root.findall('xdrs/taggedtokens/tagtoken')
    doc = []
    for token_element in all_elements:
        tags = token_element.findall('tags/tag')
        for tag in tags:
            if 'tok' in tag.get('type'):
                token = tag.text
                doc.append(token)
    strr = ' '.join(doc)

    return strr

def get_tokens(path_to_doc):
    tree = etree.parse(path_to_doc)
    root = tree.getroot()

    all_elements = root.findall('xdrs/taggedtokens/tagtoken')
    return all_elements

def get_pairs(language_list):
    """Given a list, return a list of tuples of all element pairs."""
    pairs = []
    for l1 in language_list:
        for l2 in language_list:
            if l1 != l2:
                if (l1, l2) not in pairs and (l2, l1) not in pairs:
                    pairs.append((l1, l2))
    return pairs

def get_doc_text(path_to_doc):

    #Your code here
    tree = etree.parse(path_to_doc)
    root = tree.getroot()

    all_elements = root.findall('xdrs/taggedtokens/tagtoken')
    doc = []
    for token_element in all_elements:
        tags = token_element.findall('tags/tag')
        for tag in tags:
            if 'tok' in tag.get('type'):
                token = tag.text
                doc.append(token)
    strr = ' '.join(doc)

    return strr
