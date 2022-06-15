from flask import Flask, render_template, jsonify, request
import string

import string

def lexical_analyzer(input_string):
    return_string = ""
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 
    'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 
    'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34 ', 'q35', 
    'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43']
    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state,'#')] = 'error'
        transition_table[(state,' ')] = 'error'
    
    transition_table[('q0', ' ')] = 'q0'

    transition_table[('q0', 'a')] = 'q1'
    transition_table[('q1', 'n')] = 'q17'
    transition_table[('q17', 'a')] = 'q42'
    transition_table[('q42', ' ')] = 'q43'
    transition_table[('q42', '#')] = 'accept'
    transition_table[('q43', ' ')] = 'q43'
    transition_table[('q43', '#')] = 'accept'

    transition_table[('q0', 'a')] = 'q1'
    transition_table[('q1', 'b')] = 'q3'
    transition_table[('q3', 'i')] = 'q42'
    
    transition_table[('q0', 'u')] = 'q2'
    transition_table[('q2', 'm')] = 'q3'
    transition_table[('q3', 'i')] = 'q42'

    transition_table[('q0', 'b')] = 'q4'
    transition_table[('q4', 'a')] = 'q5'
    transition_table[('q5', 'e')] = 'q42'

    transition_table[('q0', 't')] = 'q6'
    transition_table[('q6', 'a')] = 'q7'
    transition_table[('q7', 'j')] = 'q8'
    transition_table[('q8', 'i')] = 'q9'
    transition_table[('q9', 'r')] = 'q42'

    transition_table[('q0', 'y')] = 'q10'
    transition_table[('q10', 'u')] = 'q11'
    transition_table[('q11', 's')] = 'q12'
    transition_table[('q12', 'h')] = 'q13'
    transition_table[('q13', 't')] = 'q14'
    transition_table[('q14', 'a')] = 'q15'
    transition_table[('q15', 'r')] = 'q16'
    transition_table[('q16', 'a')] = 'q17'
    transition_table[('q17', 'a')] = 'q42'

    transition_table[('q0', 'g')] = 'q18'
    transition_table[('q18', 'h')] = 'q19'
    transition_table[('q19', 'a')] = 'q20'
    transition_table[('q20', 's')] = 'q21'
    transition_table[('q21', 'l')] = 'q42'
    
    transition_table[('q0', 'd')] = 'q22'
    transition_table[('q22', 'a')] = 'q23'
    transition_table[('q23', 'r')] = 'q24'
    transition_table[('q24', 'a')] = 'q25'
    transition_table[('q25', 'a')] = 'q26'
    transition_table[('q26', 'j')] = 'q17'
    transition_table[('q17', 'a')] = 'q42'

    transition_table[('q0', 'u')] = 'q2'
    transition_table[('q2', 'w')] = 'q28'    
    transition_table[('q28', 't')] = 'q29'
    transition_table[('q29', 'u')] = 'q30'
    transition_table[('q30', 'b')] = 'q31'
    transition_table[('q31', 'i')] = 'q32'
    transition_table[('q32', 's')] = 'q42'

    transition_table[('q0', 's')] = 'q33'
    transition_table[('q33', 'a')] = 'q34'
    transition_table[('q34', 'y')] = 'q35'
    transition_table[('q35', 'y')] = 'q36'
    transition_table[('q36', 'a')] = 'q37'
    transition_table[('q37', 'r')] = 'q38'
    transition_table[('q38', 'o')] = 'q39'
    transition_table[('q39', 't')] = 'q40'
    transition_table[('q40', 'u')] = 'q41'
    transition_table[('q41', 'n')] = 'q42'

    transition_table[('q43','a')] = 'q1'
    transition_table[('q43','u')] = 'q2'
    transition_table[('q43','b')] = 'q4'
    transition_table[('q43','t')] = 'q6'
    transition_table[('q43','y')] = 'q10'
    transition_table[('q43','g')] = 'q18'
    transition_table[('q43','d')] = 'q22'
    #transition_table[('q43','u')] = 'q27'
    transition_table[('q43','s')] = 'q33'



    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state =='q41':
            return_string += 'Current Token: '+current_token+', Valid <br/>'
            current_token = ''
        if state == 'error':
            return_string += 'Error <br/>'
            break;
        idx_char = idx_char + 1
    
    return_string += "______________________<br/>"

    if state == 'accept':
        return True, return_string
    else:
        return False, return_string
    
def parse_table(input_string):
    tokens = input_string
    non_terminals = ['S', 'NN', 'VB']
    terminals = ['ana', 'umi','abi','daraaja','uwtubis','sayyarotun','yushtaraa','bae','tajir','ghasl']

    parse_table = {}

    return_string = ""

    parse_table[('S','ana')] = ['NN', 'VB', 'NN']
    parse_table[('S','umi')] = ['NN', 'VB', 'NN']
    parse_table[('S','abi')] = ['NN', 'VB', 'NN']
    parse_table[('S','daraaja')] = ['NN', 'VB', 'NN']
    parse_table[('S','uwtubis')] = ['NN', 'VB', 'NN']
    parse_table[('S','sayyarotun')] = ['NN', 'VB', 'NN']
    parse_table[('S','Yushtaraa')] = ['error']
    parse_table[('S','bae')] = ['error']
    parse_table[('S','tajir')] = ['error']
    parse_table[('S','ghasl')] = ['error']
    parse_table[('S','EOS')] = ['error']

    parse_table[('NN','ana')] = ['ana']
    parse_table[('NN','umi')] = ['umi']
    parse_table[('NN','abi')] = ['abi']
    parse_table[('NN','daraaja')] = ['daraaja']
    parse_table[('NN','uwtubis')] = ['uwtubis']
    parse_table[('NN','sayyarotun')] = ['sayyarotun']
    parse_table[('NN','Yushtaraa')] = ['error']
    parse_table[('NN','bae')] = ['error']
    parse_table[('NN','tajir')] = ['error']
    parse_table[('NN','ghasl')] = ['error']
    parse_table[('NN','EOS')] = ['error']

    parse_table[('VB','ana')] = ['error']
    parse_table[('VB','umi')] = ['error']
    parse_table[('VB','abi')] = ['error']
    parse_table[('VB','daraaja')] = ['error']
    parse_table[('VB','uwtubis')] = ['error']
    parse_table[('VB','sayyarotun')] = ['error']
    parse_table[('VB','Yushtaraa')] = ['Yushtaraa']
    parse_table[('VB','bae')] = ['bae']
    parse_table[('VB','tajir')] = ['tajir']
    parse_table[('VB','ghasl')] = ['ghasl']
    parse_table[('VB','EOS')] = ['error']

    stack = []
    stack.append('#')
    stack.append('S')

    idx_token = 0
    symbol = tokens[idx_token]

    while (len(stack) > 0):
        top = stack[len(stack)-1]
        return_string += 'top = '+top+"<br/>"
        return_string += 'symbol = '+symbol+"<br/>"
        if top in terminals:
            return_string += 'top adalah simbol terminal'
            if top == symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    mystack = ""
                    for isi in stack:
                        mystack += isi +' '
                    mystack += "<br/>"
                    return_string += 'isi stack: ' + str(mystack) +"<br/>"
                    stack.pop()
            else:
                return_string += 'error'
                break;
        elif top in non_terminals:
            return_string += 'Top adalah simbol non-terminal' + "<br/>"
            if parse_table[(top, symbol)] [0] != 'error':
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range (len(symbols_to_be_pushed)-1,-1,-1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                return_string += 'error' + "<br/>"
                break;
        else:
            return_string += 'error' + "<br/>"
            break;
        mystack = ""
        for isi in stack:
            mystack += isi +' '
        mystack += "<br/>"
        return_string += "isi stack: " + str(mystack) + "<br/><br/>"
    
    return_string += "<br/>"
    if symbol =='EOS' and len(stack)==0:
        return True, return_string
    else:
        return False, return_string
''' 
sentence = input()
output = ""
input_string = sentence.lower()+'#'
tokens = sentence.lower().split()
tokens.append('EOS')

result_lexical, output = lexical_analyzer(input_string)

if (result_lexical):
    result_parser, r_parse = parse_table(tokens)
    output += r_parse
    output += 'Kesimpulan <br/>' 
    if (result_parser):
        output += "Lexical analyzer: Valid <br/>"  
        output += "Parser: Valid <br/>"  
        output += 'input String: ' + sentence + ', sudah sesuai grammar <br/>'
    else:
        output += "Lexical analyzer: Valid <br/>"  
        output += "Parser: Tidak Valid <br/>"   
        output += 'Error, input String: '+ sentence+', tidak sesuai grammar <br/>'
else:
    output += "Kesimpulan: <br/>"
    output += "Lexical analyzer: Tidak Valid <br/>"
    output += 'Error, input String: ' + sentence + ', tidak sesuai grammar <br/>'


print(output)
'''


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def submit():
    sentence = request.form.get("kalimat")
    output = ""
    input_string = sentence.lower()+'#'
    tokens = sentence.lower().split()
    tokens.append('EOS')

    result_lexical, output = lexical_analyzer(input_string)

    if (result_lexical):
        result_parser, r_parse = parse_table(tokens)
        output += r_parse
        output += 'Kesimpulan :<br/>' 
        if (result_parser):
            output += '<div class="alert alert-success" role="alert">Lexical analyzer: Valid </div>'
            output += '<div class="alert alert-success" role="alert">Parser: Valid </div>'
            output += '<div class="alert alert-success" role="alert">input String: ' + sentence + ', sudah sesuai grammar </div>'
        else:
            output += '<div class="alert alert-success" role="alert">Lexical analyzer: Valid </div>'
            output += '<div class="alert alert-danger" role="alert">Parser: Tidak Valid </div>'   
            output += '<div class="alert alert-danger" role="alert">Error, input String: '+ sentence+', tidak sesuai grammar </div>'
    else:
        output += "Kesimpulan : <br/>"
        output += '<div class="alert alert-danger" role="alert">Lexical analyzer: Tidak Valid </div>'
        output += '<div class="alert alert-danger" role="alert">Error, input String: ' + sentence + ', tidak sesuai grammar </div>'


    return render_template("output.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)