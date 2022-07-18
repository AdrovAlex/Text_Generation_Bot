from opt_einsum.backends import torch
import numpy as np
import textwrap
import torch

model_news = torch.load(' ', map_location=torch.device('cpu'))
model_congr = torch.load(' ', map_location=torch.device('cpu'))

from transformers import GPT2Tokenizer


# Функции для генерации

def get_good(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model_congr.generate(
        input_ids=prompt,
        max_length=25,
        num_beams=15,
        do_sample=True,
        temperature=3.,
        top_k=50,
        top_p=0.7,
        no_repeat_ngram_size=2,
        num_return_sequences=7,
    ).cpu().numpy()
    return textwrap.fill(tokenizer.decode(out[0]) + '!', 120)


def get_bad(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model_news.generate(
        input_ids=prompt,
        max_length=25,
        num_beams=15,
        do_sample=True,
        temperature=3.,
        top_k=50,
        top_p=0.6,
        no_repeat_ngram_size=2,
        num_return_sequences=7,
    ).cpu().numpy()
    return textwrap.fill(tokenizer.decode(out[0]) + '...', 120)