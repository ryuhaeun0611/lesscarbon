import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

st.set_page_config(page_title="탄소 발자국 계산기", layout="centered")
st.title("🌱 나의 탄소 발자국 계산기")
st.markdown("생활 패턴을 입력하면 연간 탄소 배출량을 계산하고, 탄소 발자국을 시각화합니다.")

# 사용자 입력
st.header("1. 생활 패턴 입력")

# 교통
transport = st.selectbox("평소 주로 이용하는 교통수단은?", ["자가용", "대중교통", "자전거/도보"])
if transport == "자가용":
    transport_emission = 2.4  # tCO2/년 (평균)
elif transport == "대중교통":
    transport_emission = 0.8
else:
    transport_emission = 0.1

# 식습관
diet = st.selectbox("식습관은 어떤가요?", ["육식 위주", "잡식", "채식 위주"])
if diet == "육식 위주":
    diet_emission = 2.5
elif diet == "잡식":
    diet_emission = 1.7
else:
    diet_emission = 1.0

# 전기 사용량
electricity_kwh = st.slider("월 평균 전기 사용량(kWh)", 100, 1000, 350)
electricity_emission = electricity_kwh * 12 * 0.00042  # tCO2/년, 0.00042톤/kWh

# 총 배출량 계산
total_emission = transport_emission + diet_emission + electricity_emission

st.header("2. 결과: 연간 탄소 배출량")
st.metric(label="연간 배출량 (톤 CO₂)", value=f"{total_emission:.2f} 톤")

# 발자국 시각화
st.header("3. 탄소 발자국 시각화")
footprint_img = Image.open("footprint_green.png")  # 녹색 발자국 이미지 필요
footprint = np.array(footprint_img)

fig, ax = plt.subplots(figsize=(3, 3))
ax.imshow(footprint)
ax.axis('off')
ax.set_title(f"탄소 발자국: {total_emission:.2f} tCO₂")
st.pyplot(fig)

# 감축 팁
st.header("4. 탄소 감축을 위한 팁")
tips = []
if transport == "자가용":
    tips.append("🚋 대중교통이나 자전거를 더 자주 이용해 보세요.")
if diet == "육식 위주":
    tips.append("🥗 주 1회 채식 데이를 시도해보세요.")
if electricity_kwh > 500:
    tips.append("💡 고효율 LED 조명 및 에너지 절약형 가전을 사용하세요.")

if not tips:
    st.success("좋은 생활 습관을 유지하고 계시네요! 🌎")
else:
    for tip in tips:
        st.info(tip)

st.markdown("---")
st.caption("본 계산기는 평균적인 수치를 기반으로 한 간단한 모델입니다.")
