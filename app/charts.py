import matplotlib.pyplot as plt
def run():
    def generate_bar_chart(name,labels, values):
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        plt.savefig(f'./images_bar/{name}.png')
        plt.close()

    def generate_pie_chart(labels, values):
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels)
        ax.axis('equal')
        plt.savefig('pie.png')
        plt.close()

if __name__ == '__main__':
    run()