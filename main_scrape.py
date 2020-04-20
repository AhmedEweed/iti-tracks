from lxml import html
import requests, re


def get_dict():
    pg = 'http://www.iti.gov.eg/Admission/PTPprogram/intake40'
    page = requests.get(pg)
    tree = html.fromstring(page.content)
    fname = 'track_list'
    tnames =[i.strip() for i in [re.sub("[\t|\r|/|\n]", '', n) for n in tree.xpath("//li[@class='track']//a[contains(@href, '/Admission')]/text()")]]
    links = ['http://www.iti.gov.eg' + n for n in tree.xpath("//li[@class='track']//a[contains(@href, '/Admission')]/@href")]
    track_dict = dict(zip(tnames, links))
    return track_dict

def get_link(name):
    tracks = get_dict()
    return tracks[name]

def get_names():

    dicts = get_dict()
    return dicts.keys()

def scrape(pg):
    page = requests.get(pg)
    tree = html.fromstring(page.content)
    subjects = []
    fname = tree.xpath("//span[@id='Main_ctrl_Name_lbl_TrackName']/text()")[0]
    for v in range(6):
        for k in range(6):
            item = tree.xpath("//span[@id='Main_ctrl_Courses_rpt_Courses_rpt_CoursesColumn_" + str(v) + "_lbl_Name_" + str(k) + "']/text()")
            subjects.append(item)
    subjects.pop()
    with open(fname + '.txt', 'w') as t:
        for item in subjects:
            if len(item) > 0:
                t.write(item[0] + '\n')