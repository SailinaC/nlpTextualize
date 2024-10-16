# 💫 nlpTextualize

**nlpTextualize** is a Natural Language Processing (NLP) application built using Streamlit. It provides a variety of text processing functionalities such as summarization, sentiment analysis, named entity recognition, question answering, and text completion, leveraging advanced NLP models from the `transformers` library and `spaCy`.
You can access the live web app [here](https://nlptextualize-jzbcsdoavesmwfibfrtuam.streamlit.app/).

## Key Features

- **Advanced Text Summarization**: Generate succinct summaries from extensive text documents.
- **Text Completion**: Automatically complete sentences or paragraphs seamlessly.
- **Sentiment Analysis**: Assess and interpret the sentiment conveyed in written content.
- **Named Entity Recognition (NER)**: Identify and classify entities within the text.
- **Question Answering**: Provide contextual information and answer specific queries.

## How It Works

The application uses various NLP models from the `transformers` library and `spaCy` to perform different tasks based on the user's choice from the sidebar menu:

1. **Text Summarization**: Uses a summarization pipeline to condense the input text.
2. **Named Entity Recognition (NER)**: Utilizes `spaCy` to extract and display entities from the input text.
3. **Sentiment Analysis**: Applies a sentiment analysis pipeline to classify the input text's sentiment.
4. **Question Answering**: Uses a question-answering pipeline to provide answers based on the given context and question.
5. **Text Completion**: Uses a text generation pipeline to complete a given input sentence or paragraph.

## Code Explanation

1. **Imports and Setup**

   The app imports necessary libraries such as `streamlit`, `spacy`, `transformers`, and others. It also ensures that the `en_core_web_sm` model is installed before running NLP tasks.

2. **Sidebar Menu**

   The sidebar contains the app's title and a dropdown menu that allows users to select an NLP task.

3. **Main Functionality**

   Based on the selected feature, the app performs different NLP tasks and displays the results on the main page.

4. **Progress Indication**

   The `stqdm` library is used to show progress bars during processing to improve user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
