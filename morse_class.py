"""Python code for coding and decoding Morse code"""

import subprocess
import time
import winsound


class Morse:
    """Class that allows the codification and codification of messages in Morse"""
    message = ""
    final_message = ""
    codes = [("A", "·-"), ("B", "-···"), ("C", "-·-·"), ("D", "-··"), ("E", "·"), ("F", "··-·"),
             ("G", "--·"), ("H", "····"), ("I", "··"), ("J", "·---"), ("K", "-·-"),
             ("L", "·-··"), ("M", "--"), ("N", "-·"), ("O", "---"), ("P", "·--·"), ("Q", "--·-"),
             ("R", "·-·"), ("S", "···"), ("T", "-"), ("U", "··-"), ("V", "···-"), ("W", "·--"),
             ("X", "-··-"), ("Y", "-·--"), ("Z", "--··"), ("0", "-----"), ("1", "·----"),
             ("2", "··---"), ("3", "···--"), ("4", "····-"), ("5", "·····"), ("6", "-····"),
             ("7", "--···"), ("8", "---··"), ("9", "----·"), ("?", "··--··"), ("!", "-·-·--"),
             (".", "·-·-·-"), (",", "--··--"), (";", "-·-·-·"), (":", "---···"), (" ", " ")]

    def __init__(self, message: str):
        self.message = message

    # pylint: disable=C0200
    def to_morse(self):
        """
        Function that transforms from natural language to Morse.
        :return: void function
        """
        self.message = self.message.upper()
        for i in range(len(self.message)):
            not_found = True
            for j in range(len(self.codes)):
                if self.message[i] == self.codes[j][0]:
                    self.final_message = self.final_message + self.codes[j][1] + " "
                    not_found = False
            if not_found:
                raise ValueError("Invalid character")

    def get_final_message(self):
        """
        Getter of the message.
        :return: Final message. Can be in Morse or in natural language
        """
        return self.final_message

    def decode(self):
        """
        Depending on the number of words of the message the decoding process
        will be done in one way or another.
        :return: void function
        """
        if '  ' in self.message:  # Message with multiple words
            self.decode_multiple()
        else:  # Message with only one word
            self.decode_single()

    def decode_multiple(self):
        """
        Decoding process for a multiple-word message.
        :return: void function
        """
        words = self.message.split('  ')  # Split words
        letters = []  # Every word will be split letter by letter
        for i in range(len(words)):
            letters.append(words[i].split(' '))
        for j in range(len(letters)):
            not_found = True
            for k in range(len(letters[j])):
                for m in range(len(self.codes)):
                    if letters[j][k] == self.codes[m][1]:
                        self.final_message = self.final_message + self.codes[m][0]
                        not_found = False
                if not_found:
                    raise ValueError("Invalid morse code")
            self.final_message = self.final_message + " "

    def decode_single(self):
        """
        Decoding process for a single-word message.
        :return:  void message
        """
        str_chunks = self.message.split()
        for i in range(len(str_chunks)):
            not_found = True
            for j in range(len(self.codes)):
                if str_chunks[i] == self.codes[j][1]:
                    self.final_message = self.final_message + self.codes[j][0]
                    not_found = False
            if not_found:
                raise ValueError("Invalid morse code")

    def play_from_original(self):
        """
        Reproduces the morse code from the original message
        :return: void function
        """
        dash = 300
        dot = 100
        frequency = 1000
        letter_space = 300
        word_space = 700
        for char in self.message:
            if char == '·':
                winsound.Beep(frequency, dot)
            elif char == '-':
                winsound.Beep(frequency, dash)
            elif char == ' ':
                time.sleep(letter_space / 1000)
            time.sleep(dot / 1000)
        time.sleep(word_space / 1000)

    def play_from_final(self):
        """
        Reproduces the morse code from the final message
        :return: void function
        """
        dash = 300
        dot = 100
        frequency = 1000
        letter_space = 300
        word_space = 700
        for char in self.final_message:
            if char == '·':
                winsound.Beep(frequency, dot)
            elif char == '-':
                winsound.Beep(frequency, dash)
            elif char == ' ':
                time.sleep(letter_space / 1000)
            time.sleep(dot / 1000)
        time.sleep(word_space / 1000)


def run_pylint():
    """
    Function that runs pylint in order to know how aesthetic is the code
    :return: void function
    """
    pylint_call = subprocess.run(['pylint', 'morse_class.py'], capture_output=True, text=True,
                                 check=True)
    print(pylint_call.stdout)
    print(pylint_call.stderr)


if __name__ == "__main__":
    test = Morse("Message goes here!")
    test.to_morse()
    test.play_from_final()
    # test.decode()
    # morse2 = test.get_final_message()
    # print("The final message is: ", morse2)
    run_pylint()
