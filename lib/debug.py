#!/usr/bin/env python3
import ipdb

# Adjust the import path as needed
from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()

    # Create Authors and Magazines for debugging
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    # Adding articles to test the code
    author1.add_article(magazine1, "The Future of AI")
    author1.add_article(magazine2, "Living Well with Stress")
    author2.add_article(magazine1, "AI and the Workforce")

    # Now you can debug and interact with the variables
    # For example, you can inspect and evaluate the state of objects
    print("Articles by Author 1:", [article.title for article in author1.articles()])
    print("Contributors to Tech Today:", [author.name for author in magazine1.contributors()])
    print("Magazine Titles for Tech Today:", magazine1.article_titles())


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
