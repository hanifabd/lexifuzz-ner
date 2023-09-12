# **LexiFuzz NER: Named Entity Recognition Based on Dictionary and Fuzzy Matching**

## **About**
LexiFuzz NER is a Named Entity Recognition (NER) package designed to identify and extract named entities from unstructured text data. Leveraging a combination of dictionary-based and fuzzy matching techniques, LexiFuzz NER offers state-of-the-art accuracy in recognizing named entities in various domains, making it an invaluable tool for information extraction, natural language understanding, and text analytics.

## **Key Features**

1. **Dictionary-Based Recognition**: LexiFuzz NER utilizes a comprehensive dictionary of named entities, encompassing a wide range of entities such as person names, organizations, locations, dates, and more. This dictionary is continuously updated to ensure high precision in entity recognition.

2. **Fuzzy Matching**: The package employs advanced fuzzy matching algorithms to identify named entities even in cases of typographical errors, misspellings, or variations in naming conventions. This ensures robustness in recognizing entities with varying textual representations.

3. **Customization**: LexiFuzz NER allows users to easily customize and expand the entity dictionary to suit specific domain or application requirements. This flexibility makes it adaptable to a wide array of use cases.

## Usage
1. Installation
    ```sh
    pip install lexifuzz-ner
    ```
2. Inference
    ```py
    import lexifuzz_ner

    dictionary = {
        'individual_product' : ['tahapan', 'xpresi', 'gold'],
        'brand' : ["bca", "bank central asia"]
    }

    # text = "mau nanya soal tabungan tahapan bnak central asia dong"
    # text = "Bank Central Asia has individual savings product such as Tahapan, Tahapan Xpresi, Tahapan Gold"

    text = "i wanna ask about bca tahapan savings product"

    entities = find_entity(text, dictionary, 90)
    entities
    ```