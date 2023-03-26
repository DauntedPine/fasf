
finger_keys = [ ['q','a','z'], ['w','s','x'], ['e','d','c'],['r','f','v','t','g','b'], ['y','h','n','u','j','m'], ['i','k'], ['o', 'l'], ['p'] ]
finger_base = ['a','s','d','f','j','k','l',';']
in_memory_dict = {}

def generate_base_letter_mapping():
    global finger_keys, finger_base
    letter_mapping = {}
    for idx, letter_set in enumerate(finger_keys):
        for letter in letter_set:
            letter_mapping[letter] = finger_base[idx]
    return letter_mapping

def convert_data_in_memory(file_name):
    global in_memory_dict
    letter_mapping = generate_base_letter_mapping()
    with open(file_name, 'r') as f:
        while(True):
            current_word = f.readline()[:-1]
            if current_word == '':
                break
            mapped_word = ''
            for letter in current_word:
                base_letter = letter_mapping[letter]
                mapped_word += base_letter
            if mapped_word in in_memory_dict:
                in_memory_dict[mapped_word].append(current_word)
            else:
                in_memory_dict[mapped_word] = [current_word]


def decode(user_input):
    converted_text = []
    for word in user_input.split(' '):
            if word in in_memory_dict:
                converted_text.append(in_memory_dict[word])
            else:
                converted_text.append([f'? - {word}'])
    return converted_text


def get_user_input():
    global in_memory_dict
    convert_data_in_memory('common-words.txt')
    print(f'Here are the key mappings: {[(k,v) for k,v in generate_base_letter_mapping().items()]}')
    
    while(True):
        user_input = input('Enter your text with words separated by space: ')
        decoded = decode(user_input.lower())
        most_likely = ' '.join([word[0] for word in decoded])
        print('-----------')
        print(f'\n\nMost likeley : {most_likely}')
        raw = ' '.join([word[0] if len(word) == 1 else '/'.join(word) for word in decoded])
        print(f'Raw output: {raw}')
        print('-----------')
        
       
if __name__ == '__main__':
    get_user_input()
