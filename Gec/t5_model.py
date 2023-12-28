import torch
from transformers import (T5ForConditionalGeneration, T5Tokenizer, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq)
from transformers import (AdamW, T5ForConditionalGeneration, T5Tokenizer, get_linear_schedule_with_warmup)
model_name = r'Path of your trained T5 model'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def t5_correct(input_text):
  batch = tokenizer([input_text], truncation=True, padding='max_length', max_length=64, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch, max_length=64, num_beams=4, temperature=1.5)
  target_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  for tg_text in target_text:
    return tg_text