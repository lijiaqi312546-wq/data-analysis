# 大数据专业 - 基础数据分析示例代码
# 功能：读取数据、数据清洗、简单统计、绘图可视化

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 创建模拟数据（代表学生成绩数据集）
data = {
    'name': ['张三', '李四', '王五', '赵六', '孙七'],
    'math': [85, 92, 78, 90, 88],
    'english': [79, 85, 92, 86, 90],
    'computer': [95, 88, 91, 85, 93]
}

# 2. 转为DataFrame（大数据最常用格式）
df = pd.DataFrame(data)
print("===== 原始数据 =====")
print(df)

# 3. 基础统计分析
print("\n===== 数据统计 =====")
print(df.describe())

# 4. 计算总分
df['total'] = df['math'] + df['english'] + df['computer']
print("\n===== 加上总分 =====")
print(df)

# 5. 绘图可视化
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示
plt.bar(df['name'], df['total'], color='skyblue')
plt.title('学生总分统计')
plt.xlabel('姓名')
plt.ylabel('总分')
plt.savefig('result.png')  # 保存图片
plt.show()

print("\n✅ 数据分析执行完成！已生成统计图表 result.png")