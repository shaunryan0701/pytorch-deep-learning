import torch


"""Introduction to PyTorch"""

scalar = torch.tensor(3.1415)

print(scalar.item())

vector = torch.tensor([1, 2, 3, 4, 5])

print(vector.ndim)

matrix = torch.tensor([[1, 2, 3], 
                       [4, 5, 6], 
                       [7, 8, 9]])

tensor = torch.tensor([[[1, 2, 3], 
                        [4, 5, 6]], 
                        [[7, 8, 9], 
                         [10, 11, 12]]])

random_tensor = torch.rand(size=(2, 3, 4))
print(random_tensor)

tensor_zeroes = torch.zeros(size=(2, 3, 4))
print(tensor_zeroes)

tensor_ones = torch.ones(size=(2, 3, 4))
tensor_range = torch.arange(start=0, end=1000, step=12)
print(tensor_range)

tensor_like = torch.zeros_like(input=tensor_range)
print(tensor_like)

# Get the device, shape and data type of a tensor
print(tensor_like.device)
print(tensor_like.shape)
print(tensor_like.size())
print(tensor_like.dtype)

