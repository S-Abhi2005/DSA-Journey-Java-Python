class Solution:
    def compress(self, chars: list[str]) -> int:
        final_val = ""
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                final_val += chars[i-1]
                if count > 1:
                    final_val += str(count)
                count = 1

        if chars:
            final_val += chars[-1]
            if count > 1:
                final_val += str(count)

        chars[:] = list(final_val)
        return len(chars)