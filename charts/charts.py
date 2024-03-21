import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['html','js','css']
    values = [60,80,120]
    
    gif, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
    
    