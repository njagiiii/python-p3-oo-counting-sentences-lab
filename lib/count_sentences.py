#!/usr/bin/env python3
import re
from collections import Counter

class MyString:
    def __init__(self, value= ''):
        self._value =value
   
    def get_value(self):
        return self._value
    
    def set_value(self,new_value):
        if(type(new_value) == str):
            self._value = new_value

        else:
            print("Value must be a string")

    value = property(get_value, set_value)
    @property        
    def is_sentence(self):
        if  self._value.endswith("."):
            return True
        else:
            return False
    @property    
    def is_question(self):
         if  self._value.endswith("?"):
            return True
         else:
            return False
    @property     
    def is_exclamation(self):
         if  self._value.endswith("!"):
            return True
         else:
            return False   
    @property    
    def count_sentences(self):
        if self.value == '':
            return 0
            
        return len(re.split(r'[!\?\.](?= )', self.value))
my_string = MyString("This is a sentence. This is another sentence! Is this a question?")
sentence_count = my_string.count_sentences()
print("Number of sentences:", sentence_count)