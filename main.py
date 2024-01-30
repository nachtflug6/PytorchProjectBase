import torch
from tqdm import tqdm

print(torch.cuda.is_available())

n = 1000

result = torch.zeros((n, n, n), dtype=torch.int64).to('cuda')

for i in tqdm(range(10)):
    result += torch.randint_like(result, low=-10, high=11, dtype=torch.int64).to('cuda')
    print(torch.sum(result))