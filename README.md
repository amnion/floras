# floras
Includes files useful for extracting and managing data from online floras

Data from floras such as eFloras.org, kew.org, etc., should be downloaded and in files
where each line contains a species name, the text description, and a URL or other identifier,
each separated by tabs.

searcher.py will search for given terms and extract whole sentences that contain them (context
is important), and sep_ranges.py will format the appropriate measurement values while also
standardizing units to millimeters.
