import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()
  
setuptools. setup(
  name = "mylibrary",
  version = "0.1",
  author = "Ioana-Beatrice Vicol",
  author_email = "ioanavicol@yahoo.com",
  description = "Book Library",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/ioana-vicol/mylibrary",
  project_urls = {
  "Bug Tracker"; "https://github.com/ioana-vicol/mylibrary/issues",
  },
  license="MIT',
  packages= (" JSON", "Random"), 
  python_requires >= "3.8"
)
