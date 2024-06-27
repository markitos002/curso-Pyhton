"""There are several steps in Data Engineering process.

Extract - Data extraction is getting data from multiple sources. Ex. Data extraction from a website using Web scraping or gathering information from the data that are stored in different formats(JSON, CSV, XLSX etc.).

Transform - Transforming the data means removing the data that we don't need for further analysis and converting the data in the format that all the data from the multiple sources is in the same format.

Load - Loading the data inside a data warehouse. Data warehouse essentially contains large volumes of data that are accessed to gather insights.

"""

import pandas as pd
import json
from pyodide.http import pyfetch


json_data = pyfetch('https://jsonplaceholder.typicode.com/posts')