from create_word import *
from word_generator.core.word_search import WordSearch

# D:\VSC\word-search-AI\myproject\myproject\word-search-generator

# createPuzzle function to generate word search board
def createPuzzle(course, lesson, grade):
    words = generate_related_words(course, lesson, grade)
    puzzle = WordSearch(words)
    puzzle.show(solution=True)
    puzzle.save("puzzle.pdf", solution=True)

# Eg
course = 'math'
lesson = 'plus'
grade = '5'
# test createPuzzle function
createPuzzle(course, lesson, grade)