# -*- coding: utf-8 -*-
import sys
import json
import os
import webbrowser
from datetime import datetime

html = '<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><link href="style.css" rel="stylesheet"></head><body><table>'
html += "<tr>"
html += "<th>バイトID</th>"
html += "<th>ステージ</th>"
html += "<th>プレイ日時</th>"
html += "<th>キケン度</th>"
html += "<th>Wave</th>"
html += "<th>潮位</th>"
html += "<th>イベント</th>"
html += "<th>赤イクラ</th>"
html += "<th>金イクラ</th>"
html += "<th>ノルマ</th>"
html += "<th>金イクラ出現数</th>"
html += "<th>味方1</th>"
html += "<th>味方2</th>"
html += "<th>味方3</th>"
html += "</tr>"

if __name__ == "__main__":
    print("Making...")
    dir = os.listdir()
    if "json" in dir:
        file_list = os.listdir("json")
        file_list.reverse()
        for file in file_list:
            if ".json" in file:
                try:
                    path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/json/" + file
                    f = open(path, "r")
                    ret = json.load(f)
                    for i in range(len(ret["wave_details"])):
                        while len(ret["other_results"]) < 3:
                            result["other_results"].append({"name": "-"})
                        dt = ret["wave_details"][i]
                        html += '<tr class="last">' if i == len(ret["wave_details"]) - 1 else "<tr>"
                        html += "<td>" + str(ret["job_id"]) + "</td>"
                        html += "<td>" + str(ret["schedule"]["stage"]["name"]) + "</td>"
                        html += "<td>" + str(datetime.fromtimestamp(ret["play_time"])) + "</td>"
                        html += "<td>" + str(ret["danger_rate"]) + "</td>"
                        html += "<td>" + str(i + 1) + "</td>"
                        html += "<td>" + str(dt["water_level"]["name"]) + "</td>"
                        html += "<td>" + str(dt["event_type"]["name"]) + "</td>"
                        html += "<td>" + str(dt["ikura_num"]) + "</td>"
                        html += "<td>" + str(dt["golden_ikura_num"]) + "</td>"
                        html += "<td>" + str(dt["quota_num"]) + "</td>"
                        html += "<td>" + str(dt["golden_ikura_pop_num"]) + "</td>"
                        html += "<td>" + str(ret["other_results"][0]["name"]) + "</td>"
                        html += "<td>" + str(ret["other_results"][1]["name"]) + "</td>"
                        html += "<td>" + str(ret["other_results"][2]["name"]) + "</td>"
                        html += "</tr>"
                    f.close()
                except Exception as e:
                    print(e)
        html += "</table></body></html>"
        path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/html/view.html"
        with open(path, mode="w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open(path)