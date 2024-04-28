**Tennis Trivia**

Tennis Trivia is a data visualization dashboard app built using Dash, a Python framework for building analytical web applications. This dashboard provides insights into performance of Tennis Greats spanning across different eras including grand slam winners, head-to-head matchups, surface statistics and recent events in the world of tennis.
The eras are divided as:
1. Era 1 : 1974 - 1990
2. Era 2 : 1985 - 2003
3. Era 3 : 2003 - 2023

**Features**

- Surface Statistics: Visualize a player's performance on different surfaces with interactive pie charts.
- Grand Slam Winners: Explore the winners of each Grand Slam tournament for a selected year. View player images and full names along with the tournament titles.
- Player Head-to-Head: Compare two players' head-to-head performance across different surfaces.
- Line Chart: Track the number of Grand Slam titles won by selected players over the years.
- Serve Statistics: Analyze serve statistics for players with a horizontal bar chart.
- Tennis News: Recent events in the world of tennis using GNews API.

**Data Sources**

The dashboard utilizes data from various CSVfiles, including player rankings, Grand Slam winners, head-to-head records, and surface statistics. These files are stored in the 'data' directory and are loaded dynamically to provide real-time insights.

The dashboard also uses pictures of tennis players extracted from the internet.

*NONE OF THESE CSV-FILES ARE AVAILABLE ON THE INTERNET. ALL OF THEM ARE CURATED BY THE CONTRIBUTORS BY TAKING CUES FROM DIFFERENT SOURCES ON THE INTERNET.*

**Getting Started**

To run the Tennis Analytics Dashboard locally,follow these steps:

1. Clone this repository to your local machine.
1. Install the required dependencies listed in the requirements.txt file.

pip install -r requirements.txt

3. Run the app.py script to start the Dash application.

python app.py

4. Open a web browser and navigate to http://localhost:8050 to access the dashboard.
4. Set the zoom settings of your browser to 50% (for a 14-inch screen) and 67% (for a 15-inch screen) to enjoy a scroll free viewing experience.

**Dependencies**

The following Python libraries are used in this project:

- Dash: Web application framework for Python.
- Pandas: Data manipulation and analysis library.
- Plotly: Interactive visualization library.

**Contributors**

- Kulkarni Tanmay Shreevallabh (@[kulkarni.5@iitj.ac.in)](mailto:kulkarni.5@iitj.ac.in)
- Kshitij Jaiswal (@[jaiswal.8@iitj.ac.in)](mailto:jaiswal.8@iitj.ac.in)

**Github**

[Here](https://github.com/kshitij2131/tennistrivia) is the github repo for Tennis Trivia.
