import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def main():
    st.title("Web to App Converter")

    # Get user input for the website URL
    website_url = st.text_input("Enter the website URL:")

    if website_url:
        # Fetch website content
        website_content = get_website_content(website_url)

        # Display the website content
        st.subheader("Website Content:")
        st.text(website_content.prettify())

if __name__ == "__main__":
    main()
