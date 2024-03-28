
# Jetbrains IntelliJ Platform UI Icons Scraper

JetBrains does not offer a way to download all of the icons shown at https://jetbrains.design/intellij/resources/icons_list/ at once. This scraper solves that problem.

Out of respect I don't commit the scraper fully set up in order to minimize the risk that people are going to hammer their server/API.


## How to set up

* Install React Developer Tools for your browser of choice
* Go to https://intellij-icons.jetbrains.design/
* Right click 'This Frame' > 'Show Only This Frame'
* Open the React developer tools and go to the components tab
* Copy `state.data` text to a file named `data.json`
* Place the JSON file in this directory
* Run the scraper
