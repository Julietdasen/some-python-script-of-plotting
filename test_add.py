import matplotlib.pyplot as plt

# Data
methods = ["Random", "Consecutive", "Uniform", "VideoTree", "Frame-Aware"]
endovis_iar = [0.109, 0.1689, 0.0615, 0.0362, 0.0139]
pitvqa_iar = [0.1296, 0.1812, 0.0791, 0.0417, 0.0181]

endovis_bacc = [0.5018, 0.4549, 0.6481, 0.7490, 0.8034]
pitvqa_bacc = [0.6172, 0.5960, 0.6634, 0.8122, 0.8605]

x = range(len(methods))
width = 0.4

# Figure 1: IAR
plt.figure(figsize=(12, 8))
bars1 = plt.bar([p - width/2 for p in x], endovis_iar, width=width, label="EndoVis18-VQA", color="pink")
bars2 = plt.bar([p + width/2 for p in x], pitvqa_iar, width=width, label="PitVQA", color="aqua")

# Add value labels on bars for IAR
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    # Label for EndoVis18-VQA bars
    plt.text(bar1.get_x() + bar1.get_width()/2, bar1.get_height() + 0.0025, 
             f'{endovis_iar[i]:.4f}', ha='center', va='bottom', fontsize=17)
    # Label for PitVQA bars
    plt.text(bar2.get_x() + bar2.get_width()/2, bar2.get_height() + 0.0025, 
             f'{pitvqa_iar[i]:.4f}', ha='center', va='bottom', fontsize=17)

plt.xticks(x, methods, fontsize=25)
plt.ylabel("IAR", fontsize=28)
plt.legend(fontsize=20)
plt.tight_layout()
plt.show()

# Figure 2: B.Acc
plt.figure(figsize=(12, 8))
bars3 = plt.bar([p - width/2 for p in x], endovis_bacc, width=width, label="EndoVis18-VQA", color="gold")
bars4 = plt.bar([p + width/2 for p in x], pitvqa_bacc, width=width, label="PitVQA", color="palegreen")

# Add value labels on bars for B.Acc
for i, (bar3, bar4) in enumerate(zip(bars3, bars4)):
    # Label for EndoVis18-VQA bars
    plt.text(bar3.get_x() + bar3.get_width()/2, bar3.get_height() + 0.01, 
             f'{endovis_bacc[i]:.4f}', ha='center', va='bottom', fontsize=17)
    # Label for PitVQA bars
    plt.text(bar4.get_x() + bar4.get_width()/2, bar4.get_height() + 0.01, 
             f'{pitvqa_bacc[i]:.4f}', ha='center', va='bottom', fontsize=17)

plt.xticks(x, methods, fontsize=25)
plt.ylabel("B.Acc", fontsize=28)
plt.legend(fontsize=20)
plt.tight_layout()
plt.show()