from fileparse import file_rows_to_list

def find_start_of_packet(message: str,length_of_string:int) -> int:
    string_end_index = length_of_string-1
    for start in range(len(message)):
        end=start+length_of_string
        potential_packet = message[start:end]
        no_double_occurance=0
        for letter in potential_packet[0:string_end_index]:
            if (potential_packet.count(letter) == 1):
                no_double_occurance+=1
        if no_double_occurance == string_end_index:
            return start + length_of_string
        
if __name__ == '__main__':
    f = file_rows_to_list("inputs\input6.txt")[0]
    print("part1: " + str(find_start_of_packet(f,4)))
    print("part2: " + str(find_start_of_packet(f,14)))