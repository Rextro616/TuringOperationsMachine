class TuringMachine:
    def __init__(self, tape, initial_state='q0', final_state='q18'):
        self.tape = list(tape) + ['_'] * 100 
        self.head = 0  
        self.state = initial_state  
        self.final_state = final_state  

        self.transitions = {
            ('q0', '1'): ('q1', '1', 'R'),
            ('q0', ' '): ('q0', ' ', 'R'),
            
            ('q1', '0'): ('q2', '0', 'R'),
            ('q1', ' '): ('q1', ' ', 'R'),
            ('q1', '1'): ('q3', '1', 'R'),
            
            ('q2', ' '): ('q2', ' ', 'R'),
            ('q2', '+'): ('q4', '+', 'R'),
            
            ('q3', ' '): ('q3', ' ', 'R'),
            ('q3', '+'): ('q5', '+', 'R'),
            
            ('q4', ' '): ('q4', ' ', 'R'),
            ('q4', '1'): ('q6', '1', 'R'),
            ('q4', '0'): ('q7', '0', 'R'),
            
            ('q5', ' '): ('q5', ' ', 'R'),
            ('q5', '1'): ('q8', '1', 'R'),
            ('q5', '0'): ('q9', '0', 'R'),
            
            ('q6', ' '): ('q6', ' ', 'R'),
            ('q6', '='): ('q10', '=', 'R'),
            
            ('q7', ' '): ('q7', ' ', 'R'),
            ('q7', '='): ('q11', '=', 'R'),
            
            ('q8', ' '): ('q8', ' ', 'R'),
            ('q8', '='): ('q12', '=', 'R'),
            
            ('q9', ' '): ('q9', ' ', 'R'),
            ('q9', '='): ('q13', '=', 'R'),
            
            ('q10', ' '): ('q10', ' ', 'R'),
            ('q10', '_'): ('q14', '1', 'R'),
            
            ('q11', ' '): ('q11', ' ', 'R'),
            ('q11', '_'): ('q15', '1', 'R'),
            
            ('q12', ' '): ('q12', ' ', 'R'),
            ('q12', '_'): ('q16', '1', 'R'),
            
            ('q13', ' '): ('q13', ' ', 'R'),
            ('q13', '_'): ('q17', '1', 'R'),
            
            ('q14', '_'): ('q18', '1', 'R'),
            ('q15', '_'): ('q18', '0', 'R'),
            ('q16', '_'): ('q19', '0', 'R'),
            ('q17', '_'): ('q18', '1', 'R'),
            ('q19', '_'): ('q18', '0', 'R'),  
            ('q18', '_'): ('qa', '0', 'R')  
        }

    def step(self):
        symbol = self.tape[self.head]
        transition_key = (self.state, symbol)

        if transition_key in self.transitions:
            new_state, new_symbol, move = self.transitions[transition_key]
            self.tape[self.head] = new_symbol
            self.state = new_state

            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1
        else:
            self.state = self.final_state 

    def run(self):
        while self.state != self.final_state:
            self.step()
        return ''.join(self.tape).strip('_')
