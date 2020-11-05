# web-design-challenge
## Background
Create a website using html and the data from the file `cities.csv` with the following pages:

  - A landing page containing:
    - An explanation of the project.
    - Links to each visualizations page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.

  - Four visualization pages, each with:
    - A descriptive title and heading tag.
    - The plot/visualization itself for the selected comparison.
    - A paragraph describing the plot and its significance.

  - A "Comparisons" page that:
    - Contains all of the visualizations on the same page so we can easily visually compare them.
    - Uses a Bootstrap grid for the visualizations.
    - The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

  - A "Data" page that:
    - Displays a responsive table containing the data used in the visualizations.
    - The table must be a bootstrap table component. 

## WebVisualizations
This directory contains the files for the above listed webpages:
- landing page `landing.html` 
- visualization pages `cloudiness.html`, `humidity.html`, `temp.html` , and `windspeed.html` 
- comparison's page `comparison.html`
- data page `data.html` along with python code `data.py`
- Resources folder containing an `images` directory and raw data `cities.csv`
