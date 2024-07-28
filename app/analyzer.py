from flask import Flask, render_template, request
from web_scraper import fetch_website_html, extract_elements
from report_generator import generate_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            html = fetch_website_html(url)
            meta_tags, images, links = extract_elements(html)
            report = generate_report(meta_tags, images, links)
            return render_template('report.html', report=report)
        except Exception as e:
            return str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)