from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

def get_ipa(word):
	word = parser.fetch(word, "English")
	pron = word[0]["pronunciations"]["text"]
	pron = pron[0].split("/")[1]
	return pron

def is_const(letter):
	return letter in ('t', 'k', 'p', 'b', 'k', 'g', 
                          's', 'z', 'f', 'v',
                          'r', 'l', 'w', 'j', 'h',
                          'n', 'm', '\u014B', 
                          '\u02a7', '\u02A4',
                          '\u0288', '\u0292',
                          '\u03b8', '\u00f0')

def is_vowel(letter):
	return not is_const(letter)

def last_syllable_end(word):
	end = ""
	while len(word) and is_const(word[-1]):
		end = word[-1] + end
		word = word[:-1]
	while len(word) and is_vowel(word[-1]):
		end = word[-1] + end
		word = word[:-1]

	print(word, end)

	return end			

def ipa_rhymes(a, b):
	return last_syllable_end(a) == last_syllable_end(b)

def rhymes(a, b):
	return ipa_rhymes(get_ipa(a), get_ipa(b))
