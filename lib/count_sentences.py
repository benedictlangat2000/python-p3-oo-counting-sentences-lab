#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Split the string using punctuation as separators
        sentences = self.value.split(".") + self.value.split("?") + self.value.split("!")
        
        # Remove empty strings from the list
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return len(sentences)
