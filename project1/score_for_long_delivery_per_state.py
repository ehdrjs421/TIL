# 1. 남동부(SE) 지역 정의
se_states = ['SP', 'RJ', 'ES', 'MG']
final_df['region_group'] = final_df['customer_state'].apply(lambda x: 'South-East' if x in se_states else 'Others')

# 2. 20일 이상 여부 플래그 생성
final_df['is_over_20days'] = final_df['total_day'] == '20day+'

# 3. 배송 기간 구간 설정 (5일 단위)
bins = [0, 5, 10, 15, 20, 30, 50, 100]
labels = ['0-5d', '5-10d', '10-15d', '15-20d', '20-30d', '30-50d', '50d+']
final_df['delivery_range'] = pd.cut(final_df['total_delivery_time'].dt.days, bins=bins, labels=labels)

# 지역별/배송기간구간별 평균 별점 계산
region_score_analysis = final_df.groupby(['region_group', 'delivery_range'])['review_score'].mean().unstack()

# 시각화: 지역별 배송 기간에 따른 별점 하락 추이
plt.figure(figsize=(12, 6))
sns.lineplot(data=final_df, x='delivery_range', y='review_score', hue='region_group', marker='o')
plt.axvline(x='15-20d', color='red', linestyle='--', label='20 Days Threshold')
plt.title('Review Score Drop: South-East vs Others')
plt.ylabel('Average Review Score')
plt.xlabel('Total Delivery Time (Days)')
plt.legend()
plt.show()



#######################3
# 지역별 20일 이상 지연시 품목과 유류비 

# 남동부 지역이면서 20일 이상 걸린 주문만 추출
se_delayed_orders = final_df[(final_df['region_group'] == 'South-East') & (final_df['is_over_20days'] == True)]
# se_delayed_orders.groupby('product_category_name')['order_id'].count()
# 이들의 주요 카테고리나 물류비 확인
se_delay_summary = se_delayed_orders.groupby('product_category_name').agg({
    'review_score': 'mean',
    'order_id': 'count',
    'freight_value': 'mean'
}).sort_values(by='order_id', ascending=False).head(10)

print("남동부 20일 이상 지연 건의 주요 카테고리 TOP 10:")
se_delay_summary