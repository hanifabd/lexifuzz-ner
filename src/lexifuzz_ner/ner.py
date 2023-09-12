import re
from thefuzz import fuzz
from thefuzz import process

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from uuid import uuid4

def getFuzzySimilarity(token=None, dictionary=None, min_ratio=None):
    """
    This function uses the TheFuzz library to find the highest matching similary score of a token in a list of values.
    We then compare the similary score of the fuzzy match with our minimum threshold and return a match if the match > treshold.

    Source: https://medium.com/tailo-ai/fuzzy-matching-entities-in-a-custom-entity-dictionary-310158d2b60e
    """

    # Check for appropriate formats
    assert isinstance(token, str), "Tokens can be str() type only"
    assert isinstance(dictionary, dict), "Dictionary format should be provided in the dictionary parameter."
    assert isinstance(min_ratio, int), "Integer format should be provided in the minimum-ratio parameter."
    
    for key, values in dictionary.items():
        # Using the process option of FuzzyWuzzy, we can search through the entire dictionary for the best match
        match = process.extractOne(token, values, scorer = fuzz.ratio)

        # Match is a tuple with the match value and the similary score.
        if min_ratio <= match[1]:
            return (match + (key, ))

def handle_slicing(data=None):

  """
    This function takes a dictionary data as input and processes its 'entities' by sorting them based on their score in descending order.
    It then identifies entities with the highest scores, ensuring there is no overlap in their index ranges.
    The function returns the modified data dictionary with the selected high-scoring entities, effectively handling slicing and overlapping index ranges.
  """

  assert isinstance(data, dict), "Dictionary format should be provided in the dictionary parameter."

  # Sort entities by their score in descending order
  sorted_entities = sorted(data['entities'], key=lambda x: -x['score'])

  # Initialize a dictionary to keep track of which indices have been covered
  indices_covered = set()

  # Create a new list of entities with the highest score and ensure no overlap
  new_entities = []
  for entity in sorted_entities:
      start = entity['index']['start']
      end = entity['index']['end']

      # Check if the entity's indices overlap with previously covered indices
      if all(start > end_covered or end < start_covered for start_covered, end_covered in indices_covered):
          new_entities.append(entity)

          # Update the covered indices
          indices_covered.add((start, end))

  # Update the entities in the data dictionary
  data['entities'] = new_entities

  # Print the modified data
  return data

def annotate_text(entities = None):
  """
    This function is used to annotate specific substrings within a text by adding custom tags around them, making it useful for highlighting or marking specific entities or elements within the text.
  """

  assert isinstance(entities, dict), "Dictionary format should be provided in the dictionary parameter."

  text = entities['text']
  current_index = 0
  for entity in entities['entities']:
    substring = entity['entity']
    custom_start_tag = "["
    custom_end_tag = f"]{{{entity['id']}}}"

    # Find the index of the substring in the input string
    start_index = text.find(substring, current_index)
    if start_index == -1:
      start_index = 0
    end_index = start_index + len(substring)

    # Update current_index to start searching for the next occurrence after the current one
    current_index = end_index + 1

    # Check if the substring is found in the input string
    if start_index != -1:
        # Create the modified string with custom tags
        modified_string = (
            text[:start_index] + custom_start_tag +
            substring + custom_end_tag +
            text[end_index:]
        )
        text = modified_string
  return text

def find_entity(text=None, dictionary=None, min_ratio=None):
  """
    This function employs a fuzzy matching algorithm to identify entities in a given text.
    It utilizes a provided dictionary of phrases, comparing them with the text to find matches with a similarity score above a specified threshold.
    The function then returns the detected entities along with their categories, scores, and index positions.
    Additionally, it performs further processing by removing overlapping entities and annotating the original text with custom tags.
  """

  assert isinstance(text, str), "Tokens can be str() type only"
  assert isinstance(dictionary, dict), "Dictionary format should be provided in the dictionary parameter."
  assert isinstance(min_ratio, int), "Integer format should be provided in the minimum-ratio parameter."

  result_detection = {}
  result_detection['entities'] = []
  tokens = text.split()
  max_ngrams = max([max(len(phrase.split()) for phrase in phrases) for phrases in dictionary.values()])
  current_index = 0
  for n in range(1, max_ngrams+1):
    ngrams_result = list(ngrams(tokens, n))
    for result in ngrams_result:
      compared_text = ' '.join(result)
      similarity_score = getFuzzySimilarity(token = compared_text, dictionary = dictionary, min_ratio = min_ratio)
      if not similarity_score == None:
        # Find the start and end indices correctly using current_index
        start_index = text.find(compared_text, current_index)
        if start_index == -1:
          start_index = 0
        end_index = start_index + len(compared_text) - 1

        # Update current_index to start searching for the next occurrence after the current one
        current_index = end_index + 1

        result_detection['entities'].append(
            {
                "id": str(uuid4()),
                "entity": compared_text,
                "category": similarity_score[-1],
                "score": similarity_score[1],
                "index": {
                    "start": start_index,
                    "end": end_index
                }
            }
        )
  result_detection = handle_slicing(result_detection)
  result_detection['text'] = text
  result_detection['text_annotated'] = annotate_text(result_detection)
  return result_detection