class Morse:
    message = ""
    final_message = ""
    codes = [("A", "·-"), ("B", "-···"), ("C", "-·-·"), ("D", "-··"), ("E", "·"), ("F", "··-·"), ("G", "--·"),
             ("H", "····"), ("I", "··"), ("J", "·---"), ("K", "-·-"), ("L", "·-··"), ("M", "--"), ("N", "-·"),
             ("O", "---"), ("P", "·--·"), ("Q", "--·-"), ("R", "·-·"), ("S", "···"), ("T", "-"), ("U", "··-"),
             ("V", "···-"), ("W", "·--"), ("X", "-··-"), ("Y", "-·--"), ("Z", "--··"), ("0", "-----"), ("1", "·----"),
             ("2", "··---"), ("3", "···--"), ("4", "····-"), ("5", "·····"), ("6", "-····"), ("7", "--···"),
             ("8", "---··"), ("9", "----·"), ("?", "··--··"), ("!", "-·-·--"), (".", "·-·-·-"), (",", "--··--"),
             (";", "-·-·-·"), (":", "---···"), (" ", " ")]

    def __init__(self, message: str):
        self.message = message

    def to_morse(self):
        self.message = self.message.upper()
        for i in range(len(self.message)):
            not_found = True
            for j in range(len(self.codes)):
                if self.message[i] == self.codes[j][0]:
                    self.final_message = self.final_message + self.codes[j][1] + " "
                    not_found = False
            if not_found:
                raise Exception("Invalid character")

    def get_final_message(self):
        return self.final_message

    def decode(self):
        pass


if __name__ == "__main__":
    test = Morse("Message goes here")
    test.to_morse()
    morse2 = test.get_final_message()
    print(morse2)
