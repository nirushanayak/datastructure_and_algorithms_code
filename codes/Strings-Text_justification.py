class Solution:
    def fullJustify(self, words, maxWidth: int):
        Result_list = []
        Str = words[0]
        for word in words[1:]:
            if (len(Str) + 1 + len(word) <= maxWidth):
                Str = Str + ' ' + word
            else:
                St = self.Justify(Str, maxWidth)
                Result_list.append(St)
                Str = word
        Result_list.append(Str + ' ' * (maxWidth - len(Str)))
        return Result_list

    def Justify(self, Str, maxWidth):
        word_list = Str.split()
        if len(word_list) == 1:
            return Str + ' ' * (maxWidth - len(Str))
        word_len = len(Str) - (len(word_list) - 1)
        spaces = maxWidth - word_len
        quo = int(spaces / (len(word_list) - 1))
        rem = spaces % (len(word_list) - 1)
        return (' ' * (quo + 1)).join(Str.split()[:rem + 1]) + ' ' * quo + (' ' * quo).join(Str.split()[rem + 1:])

