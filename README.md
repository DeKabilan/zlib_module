# __CryptoPriceBIN__

 Python module for searching books and fetching book links from Zlib

## __How this works__

 Scraps the information from the HTML of the page using `beautifulsoup4` .
 
 ## __Requirements__
 
 BeautifulSoup4   `pip install bs4`<br/>
 Requests   `pip install requests`

## __Installation__

 `pip install zlibrary_module`

## __Usage__

 ```python
 from zlibrary_module import zlib

 zlib.searchbook("The Alchemist")
 zlib.selectbook("The Alchemist", 1)

 ```

 Output

 ```python
"""
1.The Alchemist 1 The Alchemist (PDF)
2.Saint Germain: Master Alchemist
3.The Red Lion- The Elixir of Eternal Life (An Alchemist Novel) (PDF)
4.The Alchemist
5.Parusavedi, Alchemist in Telugu, పరుసవేది. (PDF)
6.Rappers best friend : an instrumental series
7.Herbal Alchemists Handbook, The: A Grimoire of Philtres. Elixirs, Oils, Incense, and Formulas for Ritual Use (PDF)
8.Alchemist Ph.C-HD LIVE Operators Manual Manual (PDF)
9.The Alchemist by Ben Jonson (PDF)
10.The Neutronium Alchemist
"""

https://zlibrary.to/pdfs/the-alchemist-1-the-alchemist-pdf
 ```
## __Disclaimer__

 I'm in no way related to that website / person behind it / the kind of information hosted on it. The author of this library isn't responsible for what you do with this library.
