# 2024-8-14
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        if len(s) == 1:
            return s

        orderTable = {order[i]: i for i in range(len(order))}

        sTable = defaultdict(list)

        for ch in s:
            if ch in orderTable:
                sTable[orderTable[ch]].append(ch)
            else:
                sTable[len(order)].append(ch)

        sTable = dict(sorted(sTable.items(), key=lambda x: x[0]))

        result = []
        for li in sTable.values():
            result.extend(li)

        return ''.join(result)