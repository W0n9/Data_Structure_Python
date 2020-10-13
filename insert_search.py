def insert_search(sorted_sequence, target, left, right):
    # 仅将折半更换为插值公式
    midpoint = left + (target - sorted_sequence[left]) // (
        sorted_sequence[right] - sorted_sequence[left]) * (right - left)
    if left <= right:
        current_item = sorted_sequence[midpoint]
        if current_item == target:
            return midpoint
        elif target < current_item:
            return insert_search(sorted_sequence, target, left, midpoint - 1)
        else:
            return insert_search(sorted_sequence, target, midpoint + 1, right)
    else:
        return None


if __name__ == "__main__":
    sorted_sequence = [i for i in range(1, 999, 2)]
    print(
        insert_search(sorted_sequence,
                      target=521,
                      left=0,
                      right=len(sorted_sequence) - 1))
