df = final_df.copy()
# 2. 배송 기간이 20일 이상인 데이터만 필터링 (total_delivery_time 기준)
long_delivery_df = df[df['total_day'] != '20day+'].copy()

# 3. 예정일 대비 지연 여부 플래그 생성
# 실제 배송일이 예정일보다 늦으면 'Late', 같거나 빠르면 'On-time'
long_delivery_df['delivery_status'] = long_delivery_df.apply(
    lambda x: 'Late' if x['order_delivered_customer_date'] > x['order_estimated_delivery_date'] else 'On-time', 
    axis=1
)

# 4. 그룹별 만족도 평균 계산
analysis_result = long_delivery_df.groupby('delivery_status')['review_score'].agg(['mean', 'count', 'median'])
print("--- 20일 이상 배송 건 중 지연 여부에 따른 만족도 분석 ---")
print(analysis_result)

# 5. 시각화
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=analysis_result.reset_index(), x='delivery_status', y='mean')

# 값 라벨 표시
for i, (status, row) in enumerate(analysis_result.iterrows()):
    count = row['count']
    ax.text(i, row['mean'] + 0.05, f'n={count}', ha='center')

plt.title('Review Score (Average) with Sample Count')
plt.ylabel('Average Review Score')
plt.xlabel('Delivery Status')
plt.show()
