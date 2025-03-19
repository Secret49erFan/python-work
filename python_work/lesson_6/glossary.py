py_glossary = {
    'variable': 'a container of information with a specific label',
    'loop': 'an efficient way of iterating tasks on chunks of code',
    'boolean': 'a type of variable that is either true or false',
    'list': 'a construct for orginizing groups of information',
    'tuple': 'a set of information that is immutable',
    'set': 'a list of unique items',
    'method': 'a list of instructions that does something',
    'key': 'an identifier for a value in a group of items',
    'value': 'store information retrieved with a specific key',
    'dictionary': 'a group of items stored in key-value pairs',
    }

for word, meaning in py_glossary.items():
    print(f'\nTerm: {word.title()}.')
    print(f'Definition: {meaning.capitalize()}.')