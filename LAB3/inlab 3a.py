def search(root, x):

    if root is None or root.val == x:
        return root


    if root.val < x:
        return search(root.right, x)

    return search(root.left, x)