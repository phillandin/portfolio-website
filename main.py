from flask import Flask, render_template, request
import project

app = Flask(__name__, template_folder="templates")

skills_list = [
    {
        "id": 1,
        "heading": "Web Design & Development",
        "subheading": "Responsive sites via flask and Bootstrap.",
        "icon": "icon-screen-smartphone",
    },
    {
        "id": 2,
        "heading": "GUI Design",
        "subheading": "Made with PyQt and Tkinter.",
        "icon": "icon-screen-desktop"
    },
    {
        "id": 3,
        "heading": "Data Processing & Management",
        "subheading": "Via pandas, NumPy, matplotlib, and SQLAlchemy",
        "icon": "icon-notebook"
    },
    {
        "id": 4,
        "heading": "Data Scraping, APIs\n& More",
        "subheading": "With BeautifulSoup, Requests, pillow, smtplib, Selenium, etc.",
        "icon": "icon-options"
    }

]

project_list = [
    {
        "id": 1,
        "name": "Watermarker",
        "caption": "Image watermarking desktop app built with Pillow and PyQt6.",
        "image": "assets/img/watermarker-img-1.png",
        "url": "https://github.com/phillandin/watermarker#readme"
    },
    {
        "id": 2,
        "name": "Breakout",
        "caption": "Classic arcade game recreated with the Python turtle library.",
        "image": "assets/img/breakout-screenshot-2.png",
        "url": "https://github.com/phillandin/breakout-game#readme"
    },
    {
        "id": 3,
        "name": "Morse Code Encoder",
        "caption": "Console-based program that translates English into morse code script.",
        "image": "assets/img/morse-screenshot.png",
        "url": "https://github.com/phillandin/morse-encoder"
    },
    {
        "id": 4,
        "name": "Personal Website",
        "caption": "Source code for page, built using flask and bootstrap.",
        "image": "assets/img/website.png",
        "url": "https://github.com/phillandin/portfolio-website#readme"
    }
]

# for item in project_list:
#     project = project.PortProject(ident=item["id"], name=item["name"], caption=item["caption"], image=item["image"])
#
# portfolio_items = [{key: value for (key, value) in dictionary}]

@app.route('/')
def home():
    return render_template("index.html", projects=project_list, skills=skills_list)


if __name__ == "__main__":
    app.run(debug=True)

# former navbar background: #bd5d38