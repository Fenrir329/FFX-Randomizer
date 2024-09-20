


file_path = "./template_standard.txt"
with open(file_path, 'r') as file:
    lines = file.read()  # Read all lines into a list
    byte_pairs_standard = [int(lines[i:i+2],16) for i in range(0, len(lines), 2)]
print(byte_pairs_standard)
        
        
file_path = "./template_expert.txt"
with open(file_path, 'r') as file:
    lines = file.read()  # Read all lines into a list
    byte_pairs_expert = [int(lines[i:i+2],16) for i in range(0, len(lines), 2)]
print(byte_pairs_expert)



file_path = "./ffx_050"
with open(file_path, 'rb') as file:
    lines = file.read()  # Read all lines into a list
    byte_pairs_save_file = [int.from_bytes(lines[i:i+1]) for i in range(0, len(lines), 1)]
print(byte_pairs_save_file)




output_string_standard = str(byte_pairs_standard)

output_string_expert = str(byte_pairs_expert)

output_string_save_file = str(byte_pairs_save_file)

output_file_path = "./standard.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(output_string_standard)
    
output_file_path = "./expert.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(output_string_expert)
    
    
output_file_path = "./save_file.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(output_string_save_file)