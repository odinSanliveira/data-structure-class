def quicksort(list, start=0, end=None):
    if end is None:
        end = len(list)-1
    if start < end:
        p = partition(list, start, end)
        # recursivamente na sublista à esquerda (menores)
        quicksort(list, start, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(list, p+1, end)

def mergesort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if(end - start > 1):
        mid = (end + start)//2
        mergesort(list, start, mid)
        mergesort(list, mid, end)
        merge(list, start, mid, end)

def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    top_left, top_right = 0, 0
    for k in range(start, end):
        if top_left >= len(left):
            list[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            list[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            list[k] = left[top_left]
            top_left = top_left + 1
        else:
            list[k] = right[top_right]
            top_right = top_right + 1

def partition(list, start, end):
    pivot = list[end]
    i = start
    for j in range(start, end):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if list[j] <= pivot:
            list[j], list[i] = list[i], list[j]
            #aumenta o limte dos elementos menores que o pivô
            i = i + 1
        list[i], list[end] = list[end], list[i]
        return i

def bubble_sort(list):
    n = len(list)
    for j in range(n-1):
        for i in range(n-1):
            if list[i] > list[i+1]:
                # troca de elementos nas posições i e i+1
                list[i], list[i+1] = list[i+1], list[i]