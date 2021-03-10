
import torch

temp = torch.tensor(list(range(9)))

print(temp)

temp.shape, temp.stride(), temp.storage_offset()

torch.cos(temp)
torch.sqrt(temp)

float_temp = temp.to(torch.float)
print(float_temp)
torch.cos(float_temp)
torch.sqrt(float_temp)

float_temp.cos_()
float_temp.sqrt_()

