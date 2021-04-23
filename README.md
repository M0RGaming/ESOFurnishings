[Visit the webpage!](https://M0RGaming.github.io/ESOFurnishings)

# How to use ttcParse.py:
ttcParse.py provides a way to download pricing data from Tamriel Trade Center and use it to autofill most prices. Simply go to your TTC addon folder or download [this zip](https://us.tamrieltradecentre.com/download/PriceTable) and copy the `PriceTable.lua` and `ItemLookUpTable_EN.lua` into this directory. Run the `ttcParse.py` Python 3 file, and a `prices.json` file will be produced.

Included in this git repository is a precompiled `prices.json` which you can also use, but it may be a bit out of date.

Finally, take this `prices.json` file, and under the `Price Import/Export` box on the website, select the file then press import. Prices should be automatically updated.
