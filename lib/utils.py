# Databricks notebook source
from newspaper import article
def extract_text_to_dataframe(df, url_column, output_column):
    for index, row in df.iterrows():
        url = row[url_column]
        try:
            article = newspaper.Article(url)
            article.download()
            article.parse()
            text = article.text
            df.at[index, output_column] = text
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
    df[output_column] = df[output_column].apply(lambda x: json.dumps(x))
    return df

def extract_list_from_text(text:str):
    """Extracts a list from a string."""
    start_index = text.find("[")
    end_index = text.find("]")+1
    return eval(text[start_index:end_index])