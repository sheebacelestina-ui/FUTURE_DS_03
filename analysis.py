import pandas as pd
cols = ['event_type', 'user_id', 'product_id', 'category_code', 'price', 'user_session']
df = pd.read_csv('Task3/Data/data.csv', usecols=cols , nrows=300000)
print(df.shape)
print(df.head())
print(df.isnull().sum())
##Category colums has a lot of missing value,that column is not need for funnel but it is needed for category analysis.
##So, make 2 dataframes one with missing values and the other without missing values
df_main = df.copy()
df_category = df.dropna(subset=['category_code'])
print(df_main.head())
print(df_category.head())
#creating funnel dataset
view_users = set(df_main[df_main['event_type'] == 'view']['user_id'])
cart_users = set(df_main[df_main['event_type'] == 'cart']['user_id'])
purchase_users = set(df_main[df_main['event_type'] == 'purchase']['user_id'])
cart_users = cart_users.intersection(view_users)
purchase_users = purchase_users.intersection(cart_users)
views = len(view_users)
carts = len(cart_users)
purchases = len(purchase_users)
print("Views:", views)
print("Carts:", carts)
print("Purchases:", purchases)
view_drop = views - carts
cart_drop = carts - purchases
print("Drop from View → Cart:", view_drop)
print("Drop from Cart → Purchase:", cart_drop)
view_df=df_category[df_category['event_type']=='view'].groupby('category_code')['user_id'].nunique().reset_index(name='views')
purchase_df=df_category[df_category['event_type']=='purchase'].groupby('category_code')['user_id'].nunique().reset_index(name='purchases')
category_group=view_df.merge(purchase_df,on='category_code')
category_group['conversion']=category_group['purchases']/category_group['views']
category_group=category_group.sort_values('conversion',ascending=False)
print(category_group.head(10))
funnel_df = pd.DataFrame({
    'Stage': ['View', 'Cart', 'Purchase'],
    'Users': [views, carts, purchases]
})

drop_df = pd.DataFrame({
    'Stage': ['View→Cart', 'Cart→Purchase'],
    'Drop_Users': [view_drop, cart_drop]
})

category_group = category_group[category_group['views'] > 100]
# export files
funnel_df.to_csv('Task3/funnel.csv', index=False)
drop_df.to_csv('Task3/dropoff.csv', index=False)
category_group.to_csv('Task3/category_analysis.csv', index=False)