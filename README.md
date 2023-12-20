# Minecraft Dreaming

* Extracting chunk data from a Minecraft server.
* Training various models on the chunk data.
* Insert model output back into the Minecraft server
* ????
* Profit

## Files/notebooks

### world_file.py / exact_region_files.ipynb 
- Extracts .mca region files from Minecraft server docker container

### replace_world_file.py / copy_mca_to_container.ipynb 
- Creates a backup of region file in container, then inserts source region file into Minecraft docker container

### reading_chunks.ipynb 
- Extracts Minecraft NBT chunk data from .mca files and plots the chunks as voxels, converts chunk to numpy array

### single_chunk_plot.ipynb 
- Extracts Minecraft NBT chunk data from .mca files and plots the chunk as voxels.

### nbt_to_mca_file.ipynb
- Takes Minecraft NBT chunks and compresses and stores them in .mca region format to be consumed by a Minecraft server

### chunk_dummy_default.ipynb chunk_dummy_good.ipynb
- Simple FFN model that takes an input of a NxNxN numpy array.
- Splits the NxNxN array into sub chunks. 
- Generate dataset where the input is a sub chunk and the output is the up to 6 sub chunks it shares a face with. The sub chunk is rotated such that input chunk is always facing its output chunk.
- Training the model to overfit on the dataset to get an idea of number of parameters and settings of hyperparameters.

### actual_chunk_2.ipynb 
- Training a FFN model on actual chunk data. 
- Splitting a 16x16x16 into 2x2x2 chunks. 
- Checking to see how many one-to-many relationships this causes as with sub chunks this small its very possible to have exact chunks have a large variance in adjacent chunks.

### actual_chunk_4.ipynb 
- Training a FFN model on actual chunk data. 
- Splitting a 16x16x16 into 4x4x4 chunks. 
- Increased sub chunk size reduces the number of one-to-many relationships at the cost of model size.


