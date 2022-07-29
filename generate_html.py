from os.path import exists
from xml.etree import ElementTree as ET


def generate_html_page(div_children=1024):
    """
    :param div_children: Number of divs to be added to the body of the html page, along with the span element
    :return: None
    """

    file_name = 'static_dir/page.html'
    # Uncomment this to not overwrite the file each time
    # if exists(file_name):
    #     return

    html = ET.Element('html')
    body = ET.Element('body')
    html.append(body)

    span = ET.Element('span', attrib={'class': 'bar'})
    body.append(span)
    span.text = "Hello World"

    for idx in range(div_children):
        div = ET.Element('div', attrib={'class': f'foo{idx}'})
        body.append(div)

    with open(file_name, 'w') as f:
        ET.ElementTree(html).write(f, encoding='unicode', method='html')
