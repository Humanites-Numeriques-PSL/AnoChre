#modules maison
import anochre.tools as st

#modules python à télécharger
from pathlib import Path

#fonctions maison
from anochre.clean_data import clean_files #no argument, need folder raw_data and clean_data
from anochre.clean_annotation import correct_annotation #arguments: syllabed, annotated
from anochre.syllabification import divide_verse_into_syllables #argument: verse
from anochre.annotate import annotation #arg


if __name__ == "__main__":

	st.nouveau_dossier("./data/clean")
	st.nouveau_dossier("./data/annotated")
	clean_files()

	#print(divide_verse_into_syllables('quoi quel qualité quais laquais est'))

	for p in Path('./data/clean/').glob('*.txt') :
		print(p)
		filename = "./data/annotated/" + str(p)[11:len(str(p))]
		content = st.file_to_lines(str(p))
		st.new_empty_file(filename)
		for line in content:
			try:
				s_verse = divide_verse_into_syllables(line.lower())
			except:
				print(f"Erreur lors de la division en syllabes de la ligne: {line}")
			try:
				ano_verse = annotation(s_verse)
				with open(filename, 'a', encoding="utf-8") as f:
					f.write(ano_verse + '\n')
			except:
				print(f"Erreur lors de l'annotation de la ligne: {line}")
