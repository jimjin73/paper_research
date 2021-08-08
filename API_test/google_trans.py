# references
# https://pypi.org/project/googletrans/
# https://github.com/ssut/py-googletrans/issues/234#issuecomment-741800500 <- Please check a stable version

from googletrans import Translator

tr = Translator()
print(tr.translate(text="hello", src="en", dest="ja").text)