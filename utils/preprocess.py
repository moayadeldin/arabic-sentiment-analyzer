import re

class preprocessingText:

    def __init__(self,text):

        self.text = text


    def removeEmojis(self,text):

        emoji_pattern = re.compile(
            "(["
                "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "\U0001F300-\U0001F5FF"  # symbols & pictographs
                "\U0001F600-\U0001F64F"  # emoticons
                "\U0001F680-\U0001F6FF"  # transport & map symbols
                "\U0001F700-\U0001F77F"  # alchemical symbols
                "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                "\U0001FA00-\U0001FA6F"  # Chess Symbols
                "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                "\U00002702-\U000027B0"  # Dingbats
                "])"
            )
        return emoji_pattern.sub(r'', text)

    def removeUsernames(self,text):

        return re.sub(r'@[A-Za-z0-9_]+','',text)

    def removeEnglishwords(self,text):

        return re.sub(r'[A-Za-z]', '', text)

    def removeLinks(self,text):

        return re.sub('https?://[A-Za-z0-9./]+','',text)

    def cleanText(self):

        text = self.removeEmojis(self.text)
        text = self.removeUsernames(text)
        text = self.removeEnglishwords(text)
        text = self.removeLinks(text)

        return text