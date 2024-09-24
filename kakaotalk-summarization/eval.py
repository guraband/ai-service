import pickle


def get_eval_data():
    with open('./resource/eval_data.pickle', 'rb') as f:
        eval_data = pickle.load(f)

    return eval_data


eval_data = get_eval_data()
for conv in eval_data:
    print(len(conv))
