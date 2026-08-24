def sort_text_file(input_filename, output_filename): 
        file = open(input_filename, "r") 
        raw_lines = file.readlines() 
        file.close() 
        clean_lines = [] 
        for line in raw_lines: 
            stripped_line = line.strip() 
            if len(stripped_line) > 0: 
                clean_lines.append(stripped_line) 
        clean_lines.sort() 
        output_file = open(output_filename, "w") 
        for line in clean_lines: 
            output_file.write(line + "\n") 
        output_file.close() 
        print(f"Sorted contents written to '{output_filename}' successfully.") 

sort_text_file("input.txt", "sorted_output.txt")   
