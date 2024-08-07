# **LexiFuzz NER: Named Entity Recognition Based on Dictionary and Fuzzy Matching**

![Image](https://github.com/hanifabd/lexifuzz-ner/blob/master/assets/lexifuzz-mascot.png)

## **About**
LexiFuzz NER is a Named Entity Recognition (NER) package designed to identify and extract named entities from unstructured text data. Leveraging a combination of dictionary-based and fuzzy matching techniques, LexiFuzz NER offers state-of-the-art accuracy in recognizing named entities in various domains, making it an invaluable tool for information extraction, natural language understanding, and text analytics.

## **Requirements**
- Python 3.7 or Higher
- NLTK
- TheFuzz

## **Key Features**

1. **Dictionary-Based Recognition**: LexiFuzz NER utilizes a comprehensive dictionary of named entities, encompassing a wide range of entities such as person names, organizations, locations, dates, and more. This dictionary is continuously updated to ensure high precision in entity recognition.

2. **Fuzzy Matching**: The package employs advanced fuzzy matching algorithms to identify named entities even in cases of typographical errors, misspellings, or variations in naming conventions. This ensures robustness in recognizing entities with varying textual representations.

3. **Customization**: LexiFuzz NER allows users to easily customize and expand the entity dictionary to suit specific domain or application requirements. This flexibility makes it adaptable to a wide array of use cases.

## Usage
### Manual Installation via Github
1. Clone Repository
    ```
    git clone https://github.com/hanifabd/lexifuzz-ner.git
    ```
2. Installation
    ```
    cd lexifuzz-ner && pip install .
    ```
### Installation Using Pip
1. Installation
    ```sh
    pip install lexifuzz-ner
    ```
### Inference
1. Usage
    ```py
    from lexifuzz_ner.ner import find_entity

    dictionary = {
        'individual_product' : ['tahapan', 'xpresi', 'gold', 'berjangka'],
        'brand' : ["bca", "bank central asia"]
    }

    text = "i wanna ask about bca tahapn savings product"
    entities = find_entity(text, dictionary, 90)
    print(entities)
    ```

3. Result
    ```md
    {
        "entities": [
            {
                "id": "fa8d7946-436e-4114-baf2-7d248d193755",
                "entity": "bca",
                "similar_with": "bca",
                "category": "brand",
                "score": 100,
                "index": {
                    "start": 18,
                    "end": 20
                }
            },
            {
                "id": "a65184bd-46d0-4202-ad25-57ababd00f44",
                "entity": "tahapn",
                "similar_with": "tahapan",
                "category": "individual_product",
                "score": 92,
                "index": {
                    "start": 22,
                    "end": 27
                }
            }
        ],
        "text": "i wanna ask about bca tahapn savings product",
        "text_annotated": "i wanna ask about [bca]{fa8d7946-436e-4114-baf2-7d248d193755} [tahapn]{a65184bd-46d0-4202-ad25-57ababd00f44} savings product"
    }
    ```
