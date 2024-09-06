import base64
import io
import threading
import matplotlib.font_manager as fm
from flask import Flask, request, jsonify, render_template
import folium
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')


@app.route('/select_map', methods=['POST'])
def select_map():
    # CSV 파일 읽기
    df = pd.read_csv(r"C:/Users/yjk23/sf6-data/data_csv/전체_지역구별_업종별_결과.csv", encoding="utf-8-sig", low_memory=False)
    df_gender = pd.read_csv(r"C:/Users/yjk23/sf6-data/data_csv/전체_지역구별_남성_여성.csv", encoding="utf-8-sig", low_memory=False)

    # JSON 데이터 가져오기
    data = request.get_json()
    year_id = data.get('year_id')  # 예: 20241
    select_gu_id = data.get('select_gu_id')  # 예: '강남구'

    # 원하는 업종 리스트
    desired_industries = ['서비스업', '판매업', '요식업']

    # year_id를 문자열로 변환
    year_column = str(year_id)

    # 조건에 맞는 데이터 필터링
    filtered_df = df[
        (df['지역구'] == select_gu_id) &  # 지역구 조건
        (df['업종'].isin(desired_industries))  # 업종 조건
    ]
    filtered_gender_df = df_gender[
        (df_gender['지역구'] == select_gu_id) &  # 지역구 조건
        (df_gender['업종'].isin(desired_industries))  # 업종 조건
    ]

    result_values = filtered_df[year_column].tolist()
    result_gender_man_values = filtered_gender_df[year_column + '남자_건수'].tolist()
    result_gender_woman_values = filtered_gender_df[year_column + '여자_건수'].tolist()

    # 결과가 없을 경우 처리
    if filtered_df.empty:
        return jsonify({"message": "해당 데이터가 없습니다."}), 404

    industries = ['요식업', '서비스업', '판매업']  # 업종 이름

    # 전체 그래프 공간 만들기 (1행 3열의 서브플롯)
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))  # 세 개의 서브플롯 생성
    plt.rc('font', family='Malgun Gothic')  # 한글 폰트 설정
    # font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 경우
    # fontprop = fm.FontProperties(fname=font_path, size=12)
    # plt.title('제목', fontproperties=fontprop)
    # 첫 번째 파이 그래프
    ax[0].pie(result_values, labels=industries, autopct='%.1f%%', startangle=90)
    ax[0].set_title('업종별 매출 비율')  # 제목 설정
    # ax[0].set_title('업종별 매출 비율', fontproperties=fontprop)  # 제목 설정
    ax[0].set_ylabel('')  # y축 라벨 제거

    # 두 번째 파이 그래프
    ax[1].pie(result_gender_man_values, labels=industries, autopct='%.1f%%', startangle=90)
    ax[1].set_title('남성 매출 건수')  # 제목 설정
    # ax[1].set_title('남성 매출 건수', fontproperties=fontprop)  # 제목 설정
    ax[1].set_ylabel('')

    # 세 번째 파이 그래프
    ax[2].pie(result_gender_woman_values, labels=industries, autopct='%.1f%%', startangle=90)
    ax[2].set_title('여성 매출 건수')  # 제목 설정
    # ax[2].set_title('여성 매출 건수', fontproperties=fontprop)  # 제목 설정
    ax[2].set_ylabel('')

    # 그래프를 메모리 버퍼에 저장
    buf = io.BytesIO()
    plt.tight_layout()  # 레이아웃 자동 조정
    plt.savefig(buf, format='png')
    plt.close(fig)  # 그래프 닫기
    buf.seek(0)  # 버퍼 위치를 처음으로 이동

    # 버퍼에서 이미지를 base64로 인코딩
    img = base64.b64encode(buf.getvalue()).decode('utf-8')
    img_tag = f"data:image/png;base64,{img}"

    # 성공적으로 데이터 처리됨
    return jsonify({"img_tag": img_tag})

@app.route('/generate_map', methods=['POST'])
def generate_map():
    # 요청에서 필요한 데이터를 추출
    # 지도 객체 생성
    data = request.get_json()
    button_id = data.get('button_id')
    year_key = int(button_id)
    seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=11, tiles='CartoDB Positron')

    # 데이터 불러오기
    df = pd.read_csv(r"C:/Users/yjk23/sf6-data/data_csv/all_year_seoul_salay.csv", encoding="utf-8-sig", low_memory=False)
    df_gu_gubun = pd.read_csv(r"C:/Users/yjk23/sf6-data/data_csv/2024분기_지역구_총매출.csv", encoding="utf-8-sig",
                              low_memory=False)
    geojson_path = r'C:/Users/yjk23/sf6-data/geojson_map/seoul_map.geojson'

    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    # 분기 및 지역구 목록
    quarters = [20231, 20232, 20233, 20234]
    quarters_2024 = [20241, 20242, 20243, 20244]
    seoul_map_gubun = [
        '금천구', '중랑구', '관악구', '구로구', '용산구', '노원구', '동작구', '영등포구', '동대문구', '종로구', '성북구',
        '서대문구', '서초구', '은평구', '송파구', '성동구', '강북구', '강서구', '도봉구', '광진구', '마포구', '강동구', '강남구',
        '양천구', '중구'
    ]

    # 매출 데이터 계산
    sales_data = []
    sales_data2 = []
    for q1, q2 in zip(quarters, quarters_2024):
        quarter_data = {'기준_년분기_코드': q1}
        quarter_data2 = {'기준_년분기_코드': q2}

        for seoul in seoul_map_gubun:
            filtered_df = df[(df['기준_년분기_코드'] == q1)]
            filtered_df2 = df_gu_gubun[(df_gu_gubun['기준_년분기_코드'] == q2)]

            total_sales = filtered_df[seoul].sum()
            total_sales2 = filtered_df2[seoul].sum()

            quarter_data[seoul] = total_sales
            quarter_data2[seoul] = total_sales2

        sales_data.append(quarter_data)
        sales_data2.append(quarter_data2)

    # 매출 차이 계산 (퍼센트로 변환)
    difference_data = []
    for q_2023, q_2024 in zip(sales_data, sales_data2):
        diff = {'기준_년분기_코드': q_2024['기준_년분기_코드']}
        for region in q_2023:
            if region != '기준_년분기_코드':
                # 2023년 매출 값
                sales_2023 = q_2023[region]
                # 2024년과 2023년의 매출 차이
                sales_difference = q_2024[region] - sales_2023
                # 퍼센트 계산 (2023년 매출 대비 차이 비율)
                if sales_2023 != 0:
                    percent_change = (sales_difference / sales_2023) * 100
                else:
                    percent_change = 0  # 2023년 매출이 0일 경우 퍼센트 변화는 0으로 처리

                # 결과를 diff에 저장
                diff[region] = percent_change

        difference_data.append(diff)

    # 데이터프레임 생성
    real_df = pd.DataFrame(difference_data)
    print(real_df)
    # 순위 매기는 로직
    real_df_melted = pd.DataFrame(real_df)

    melted_df = real_df_melted.melt(id_vars='기준_년분기_코드', var_name='지역구', value_name='금액')

    sorted_df = melted_df[melted_df['기준_년분기_코드'] == year_key].sort_values(by='금액', ascending=False)

    top_10_sorted_df = sorted_df.head(10).copy()

    top_10_sorted_df.rename(columns={'기준_년분기_코드': '순위'}, inplace=True)

    # '순위' 열에 1부터 10까지의 값을 할당
    top_10_sorted_df['순위'] = range(1, 11)

    # print(top_10_sorted_df)

    # Display the sorted DataFrame for the quarter 20241
    def categorize_dataframe(real_df):
        categorized_df = real_df.copy()

        # 모든 열에 대해 양수/음수 값을 수집
        all_positive_values = categorized_df.iloc[:, 1:][categorized_df.iloc[:, 1:] > 0].stack()
        all_negative_values = categorized_df.iloc[:, 1:][categorized_df.iloc[:, 1:] < 0].stack()

        # 양수(%) 구간 설정
        if not all_positive_values.empty:
            max_positive = all_positive_values.max()
            min_positive = all_positive_values.min()
            q1_pos = min_positive + (max_positive - min_positive) * 0.25
            q2_pos = min_positive + (max_positive - min_positive) * 0.5
            q3_pos = min_positive + (max_positive - min_positive) * 0.75
        else:
            q1_pos = q2_pos = q3_pos = 0  # 양수 값이 없을 경우

        # 음수(%) 구간 설정
        if not all_negative_values.empty:
            max_negative = all_negative_values.max()
            min_negative = all_negative_values.min()
            q1_neg = min_negative + (max_negative - min_negative) * 0.25
            q2_neg = min_negative + (max_negative - min_negative) * 0.5
            q3_neg = min_negative + (max_negative - min_negative) * 0.75
        else:
            q1_neg = q2_neg = q3_neg = 0  # 음수 값이 없을 경우

        # 각 열에 대해 동일한 기준으로 구간화 적용
        for column in categorized_df.columns[1:]:
            def categorize_data(value):
                if value > 0:
                    if value <= q1_pos:
                        return 'blue,0.25'
                    elif value <= q2_pos:
                        return 'blue,0.5'
                    elif value <= q3_pos:
                        return 'blue,0.75'
                    else:
                        return 'blue,1'
                elif value < 0:
                    if value >= q1_neg:
                        return 'red,0.25'
                    elif value >= q2_neg:
                        return 'red,0.5'
                    elif value >= q3_neg:
                        return 'red,0.75'
                    else:
                        return 'red,1'
                else:
                    return 0

            categorized_df[column] = categorized_df[column].apply(categorize_data)

        return categorized_df

    # 단계 구분된 데이터프레임 생성
    categorized_df = categorize_dataframe(real_df)
    # print(categorized_df)

    # 특정 키와 구에 대한 색상과 투명도를 가져오는 함수
    def get_color_for_key(key, gugun):
        row = categorized_df[categorized_df['기준_년분기_코드'] == key]
        if not row.empty:
            color_data = row[gugun].values[0]
            colors = color_data.split(',')
            return colors[0]
        return 'gray'

    def get_opacity_for_key(key, gugun):
        row = categorized_df[categorized_df['기준_년분기_코드'] == key]
        if not row.empty:
            opacity_data = row[gugun].values[0]
            opacitys = opacity_data.split(',')
            return float(opacitys[1])
        return 1

    # GeoJson 추가 및 스타일 설정
    for feature in geojson_data['features']:
        district_name = feature['properties']['SIG_KOR_NM']

        if district_name in seoul_map_gubun:  # Check if the district is in seoul_map_gubun
            fill_color = get_color_for_key(year_key, district_name)  # Get color for the district
            fill_opacity = get_opacity_for_key(year_key, district_name)  # Get opacity for the district

            folium.GeoJson(
                feature,
                name=district_name,
                id=f"{district_name}",
                tooltip=folium.GeoJsonTooltip(fields=['SIG_KOR_NM'], aliases=['구 이름:']),
                style_function=lambda x, color=fill_color, opacity=fill_opacity: {
                    # Use `color` and `opacity` in the lambda
                    'fillColor': color,
                    'fillOpacity': opacity,
                    'weight': 1,
                    'color': 'black',
                    'dashArray': '5, 5',
                    'data-id': district_name
                },
                highlight_function=lambda x: {
                    'fillOpacity': 0.8,
                    'weight': 3,
                },

            ).add_to(seoul_map)
    # 구 이름을 중앙에 표시
    for feature in geojson_data['features']:
        district_name = feature['properties']['SIG_KOR_NM']
        coords = feature['geometry']['coordinates']

        if feature['geometry']['type'] == 'Polygon':
            center = [sum(coord[1] for coord in coords[0]) / len(coords[0]),
                      sum(coord[0] for coord in coords[0]) / len(coords[0])]
        else:
            center = [sum(coord[1] for sublist in coords for coord in sublist[0]) / sum(
                len(sublist[0]) for sublist in coords),
                      sum(coord[0] for sublist in coords for coord in sublist[0]) / sum(
                          len(sublist[0]) for sublist in coords)]

        folium.Marker(
            location=center,
            icon=folium.DivIcon(
                html=f'<div id="{district_name}" style="font-size: 12pt; color: black; font-weight: bold; text-align: center; white-space: nowrap; padding: 0px; margin: 0px; writing-mode: horizontal-tb;">{district_name}</div>',
            )
        ).add_to(seoul_map)

    # 생성된 지도를 HTML로 변환
    map_html = seoul_map._repr_html_()
    sorted_df_json = top_10_sorted_df.to_dict(orient='records')

    return jsonify({'map_html': map_html, 'sorted_df': sorted_df_json})
def run_flask():
    app.run(debug=True, use_reloader=False)
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()