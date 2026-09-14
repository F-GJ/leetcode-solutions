#read_ptr = where we're reading
#write_ptr = where we're writing
#current_char = character whose group we're processing
#count = how many consecutive copies we've found


class Solution:
    def compress(self, chars: list[str]) -> int:

        if not chars:
            return 0
        else:
            write_ptr = 0
            read_ptr = 0

        while read_ptr < len(chars):
            current_char = chars[read_ptr]
            count = 0

            while read_ptr < len(chars) and chars[read_ptr] == current_char:
                read_ptr += 1
                count += 1

            chars[write_ptr] = current_char
            write_ptr += 1

            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1

        #del chars[write_ptr:]
        return write_ptr

