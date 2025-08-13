import matplotlib.pyplot as plt

# Data from the table
frame_length = [8, 16, 24, 32]
endovis_IAR = [0.0152, 0.0201, 0.0140, 0.0139]
endovis_BAcc = [0.7977, 0.7961, 0.8002, 0.8034]
pitvqa_IAR = [0.0194, 0.0219, 0.0175, 0.0181]
pitvqa_BAcc = [0.8584, 0.8537, 0.8591, 0.8605]

fig, ax1 = plt.subplots(figsize=(8,6))

color1 = 'tab:blue'
color2 = 'tab:red'

# IAR 数据（左 y 轴）
ax1.set_xlabel('Frame Length', fontsize=18)
ax1.set_ylabel('IAR', color='black', fontsize=18)
ax1.plot(frame_length, endovis_IAR, marker='s', color=color1, label='EndoVis18-VQA IAR')
ax1.plot(frame_length, pitvqa_IAR, marker='s', color=color2, label='PitVQA IAR')
ax1.tick_params(axis='y', labelcolor='black')

# 添加 IAR 数值标签
for i, (x, y1, y2) in enumerate(zip(frame_length, endovis_IAR, pitvqa_IAR)):
    ax1.text(x, y1 + 0.00005, f'{y1:.4f}', ha='center', va='bottom', fontsize=10, color=color1)
    ax1.text(x, y2 + 0.0001, f'{y2:.4f}', ha='center', va='bottom', fontsize=10, color=color2)

# 创建右 y 轴用于 B.Acc
ax2 = ax1.twinx()
ax2.set_ylabel('B.Acc', color='black', fontsize=18)
ax2.plot(frame_length, endovis_BAcc, marker='^', linestyle='--', color=color1, label='EndoVis18-VQA B.Acc')
ax2.plot(frame_length, pitvqa_BAcc, marker='^', linestyle='--', color=color2, label='PitVQA B.Acc')
ax2.tick_params(axis='y', labelcolor='black')

# 添加 B.Acc 数值标签
for i, (x, y1, y2) in enumerate(zip(frame_length, endovis_BAcc, pitvqa_BAcc)):
    ax2.text(x, y1 + 0.0001, f'{y1:.4f}', ha='center', va='bottom', fontsize=10, color=color1)
    ax2.text(x, y2 + 0.0001, f'{y2:.4f}', ha='center', va='bottom', fontsize=10, color=color2)

# 合并图例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, 
           loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2,
           frameon=False, fontsize=16)
# 给底部留空间
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.grid(True)
plt.show()