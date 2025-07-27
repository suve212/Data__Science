import pandas as pd 
data = { 
'Name': ['Amit', 'Sana', 'Raj', 'Pooja', 'Karan'], 
'Math': [85, 72, 78, 88, 95], 
'Science': [91, 79, 69, 92, 89], 
'English': [76, 81, 74, 90, 86] 
} 
df = pd.DataFrame(data) 
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1) 
filtered_df = df[(df['Math'] > 75) & (df['Science'] > 75) & (df['English'] > 75)] 
sorted_df = filtered_df.sort_values(by='Average', ascending=False) 
sorted_df.to_csv("top_students.csv", index=False) 
print(sorted_df) 
