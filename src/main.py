import internal_funcs as funcs
import sys

class Dalai:
    def generate_request(self, prompt, model, id='0', n_predict=128, repeat_last_n=64, repeat_penalty=1.3, seed=-1, temp=0.5, threads=8, top_k=40, top_p=0.9):
        request = {'debug': False, 'id':id, 'model':model, 'models':[model], 'n_predict':n_predict, 'prompt':prompt, 'repeat_last_n':repeat_last_n, 'repeat_penalty':repeat_penalty, 'seed':seed, 'temp':temp, 'threads':threads, 'top_k':top_k, 'top_p':top_p}
        return request
    
    def request(self, prompt, prettify=True):
        if prettify == False:
            return funcs.generate(prompt)

        else:
            response = funcs.generate(prompt)['response']
            response = response.replace("\n", "")
            response = response.replace("\r", "")
            response = response.replace("<end>", "")
            if not response.endswith(".") :
                response += "."
            return response

